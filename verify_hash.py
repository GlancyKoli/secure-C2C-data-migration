import hashlib, datetime

def get_hash(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

original = "clients_info.csv"
decrypted = "clients_info_decrypted.csv"

hash1 = get_hash(original)
hash2 = get_hash(decrypted)

status = "Match" if hash1 == hash2 else "Mismatch"

with open("migration_log.txt", "a") as log:
    log.write(f"[{datetime.datetime.now()}] File: {original} -> {decrypted} | Status: {status} | Hash: {hash1}\n")

print(f"Hash Match Status: {status}")
