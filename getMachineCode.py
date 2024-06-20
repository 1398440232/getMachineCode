import uuid
import hashlib


def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(['{:02x}'.format((mac >> i) & 0xff) for i in range(0, 48, 8)])
    sha256_hash = hashlib.sha256(mac_address.encode()).hexdigest()
    return sha256_hash



a = get_mac_address()

