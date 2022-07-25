def to_sha256(s):
    import hashlib
    hash_value = hashlib.sha256(s.encode())
    print(hash_value.hexdigest())

    # Create a function that converts a given ASCII string to its hexadecimal SHA-256 hash.

to_sha256('Hello World!')