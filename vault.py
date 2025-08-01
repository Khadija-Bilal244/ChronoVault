import os
import time
from datetime import datetime
import logging

# ---------- Setup Logging ----------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("vault_access.log")
formatter = logging.Formatter('%(asctime)s → %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# ---------- Config ----------
password = "heybaby"
count = 3  # Number of allowed attempts
lock_file = "vault.lock"

# ---------- Check Lock Status ----------
if lock_file in os.listdir():
    with open(lock_file, "r") as lock:
        lock_timestamp = float(lock.read())

    current_time = time.time()
    unlock_time = lock_timestamp + 12 * 3600

    if current_time < unlock_time:
        time_remaining = unlock_time - current_time
        hours = int(time_remaining // 3600)
        minutes = int((time_remaining % 3600) // 60)
        seconds = int(time_remaining % 60)
        print(f"Vault is locked. Time remaining: {hours}h {minutes}m {seconds}s")
        logger.warning("Attempt to access locked vault. %dh %dm %ds remaining.",
                       hours, minutes, seconds)
        exit()
    else:
        os.remove(lock_file)
        print("Lock expired. You may try again.")
        logger.info("Lock expired, vault accessible again.")

# ---------- Password Check Loop ----------
while count > 0:
    user_enter = input("Enter password to unlock vault:\n")

    if user_enter == password:
        print( "Access granted.\n")
        logger.info("Access granted.")
        print("Files in this directory:\n")

        for file in os.listdir():
            if file in ["vault.py", "vault.lock", "vault_access.log"]:
                continue  # Skip internal files
            print(f" >>> {file} <<<\n")

            try:
                with open(file, 'r') as f:
                    print(f.read())
                    logger.info("Accessed file: %s", file)
            except UnicodeDecodeError:
                print("[!] Cannot display binary file:", file)
                logger.warning("Tried to read binary file: %s", file)
            except Exception as e:
                print("[!] Error opening file:", file)
                logger.error("Failed to open %s: %s", file, str(e))
        break

    else:
        count -= 1
        logger.warning("Wrong password. Attempts remaining: %d", count)
        if count == 0:
            print("Too many failed attempts. Vault is now locked for 12 hours.")
            with open(lock_file, "w") as lock:
                lock.write(str(time.time()))
            logger.warning("Vault locked due to failed attempts.")
        else:
            print(f"Wrong password. Tries remaining: {count}")

