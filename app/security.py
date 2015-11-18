from os import urandom
from common import config
from common import files
from salsa20 import XSalsa20_xor

__author__ = 'bubble'


class Security:
    def __init__(self):
        key_path = config.get_registry_file()
        self.key = files.read_from_file(key_path)
        self.nonce_path = config.get_certificate_path()

    def save_nonce(self, nonce):
        files.overwrite_file(self.nonce_path, nonce)

    def get_nonce(self):
        return files.read_from_file(self.nonce_path)

    def encode_string(self, string):
        nonce = urandom(24)
        ciphertext = XSalsa20_xor(string, nonce, self.key)
        self.save_nonce(nonce)
        return ciphertext

    def decode_string(self, string):
        nonce = self.get_nonce()
        return XSalsa20_xor(string, nonce, self.key).decode().encode('utf-8')
