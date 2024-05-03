import sys
import base64
import random
import string
import hashlib
from concurrent.futures import ProcessPoolExecutor

info = '''
Jankie's HCoin Miner (on CPU,Python version:{})
workers: {}.
'''

def generate_random_string(length):
    charset = string.ascii_letters + string.digits + "-_"
    return ''.join(random.choice(charset) for _ in range(length))

def sha512(input):
    hash_object = hashlib.sha512(input.encode())
    return hash_object.digest()

def base64_encode(input):
    encoded_bytes = base64.b64encode(input)
    return encoded_bytes.decode()

def to_lower(input):
    return input.lower()

def find_hcoin(_):
    while True:
        random_string = generate_random_string(8)
        hashed_string = sha512(random_string)
        base64_encoded = base64_encode(hashed_string)
        base64_encoded_lower = to_lower(base64_encoded)

        if base64_encoded_lower.startswith("hcoin"):
            print("\n HCoin:", random_string, "\n")
            break

if __name__ == "__main__":
    num_processes = 20
    print(info.format(sys.version,num_processes))
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(find_hcoin, i) for i in range(num_processes)]
        for future in futures:
            future.result()
