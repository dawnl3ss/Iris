def next_hex_value(hex, _):
    return int(hex) + _

def prev_hex_value(hex, _):
    return int(hex) - _

def hash(str, _):
    hex_array = [x for x in str]
    hex_hash = []

    for c_hex in hex_array:
        hex_hash.append(chr(next_hex_value(format(ord(c_hex), "x"), 2)))
    return hex_hash, hex_array

print(hash("test", 1))