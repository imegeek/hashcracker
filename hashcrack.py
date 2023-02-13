import hashlib, sys, os
from time import sleep
import time

program_name = sys.argv[0]

if len(sys.argv) < 4:
    print(f"""    Usage of {program_name} :
{program_name} <hash-value> <hash-type> <path-to-password-file>

         Example of usage :
{program_name} 5d41402abc4b2a76b9719d911017c592 md5 passwd_list.txt""")
    exit()

hash_value = sys.argv[1]
hash_type = sys.argv[2]
passwd_file = sys.argv[3]

count=1

# Open the password file for reading

if not os.path.exists(passwd_file):
    print(f"Password file '{passwd_file}' not found.")
    exit()

with open(passwd_file, "r", encoding='latin-1') as file:
    # Read the list of passwords
    passwords = file.readlines()

    # Loop through the list of passwords
    for password in passwords:
        # Strip the newline character from each password
        password = password.strip()
        count += 1
        start = time.time()
        # Generate the MD5 hash of the password

        if hash_type == "md5":
            password_hash=hashlib.md5(f"{password}".encode('utf-8')).hexdigest()
        elif hash_type == "sha1":
            password_hash=hashlib.sha1(f"{password}".encode('utf-8')).hexdigest()
        elif hash_type == "sha224":
            password_hash=hashlib.sha224(f"{password}".encode('utf-8')).hexdigest()
        elif hash_type == "sha256":
            password_hash=hashlib.sha256(f"{password}".encode('utf-8')).hexdigest()
        elif hash_type == "sha512":
            password_hash=hashlib.sha512(f"{password}".encode('utf-8')).hexdigest()
        else:
            print("Unidentified hash type has selected.")
            exit()

        # Compare the hash to the hash entered by the user
        if password_hash == hash_value:
            end = time.time()
            total_time = (end - start)
            print(f"\33[92mPassword found: {password}\33[0m")
            print(f"Total time consumed: {total_time}")
            break
        else:
            print(f"\33[91m{count}. No match found: {password}\33[0m ")
            sleep(0.000100)          # wait a little to make the effect look good.

