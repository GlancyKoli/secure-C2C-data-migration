import hashlib

def get_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

original_hash = "cdc374304c02d2967debf17c099ed50100fc5485f0abd991d0c7377561db14cf"  # Replace with the correct hash
downloaded_hash = get_hash("clients_info.enc")

print("Integrity OK" if downloaded_hash == original_hash else "Tampered!")
