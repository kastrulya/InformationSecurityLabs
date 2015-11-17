import hashlib

__author__ = 'bubble'

class Cipher:
    def __init__(self, ciphertext, nonce):
        self.ciphertext = ciphertext
        self.nonce = nonce


def get_hash_md5(string):
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()
