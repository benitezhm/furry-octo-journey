import hashlib
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()

def hash_block(block):
    """
    Hasehs a block and returns a strin representation of it.
    
    Arguments:
        :block: The block that should be hashed
    """
    return hash_string_256(json.dumps(block, sort_keys=True).encode())


