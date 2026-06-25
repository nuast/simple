# Base conversion functions

def den2bin(den):
    binary = bin(den)
    binary = binary.replace("0b", "")
    return binary

def den2hex(den):
    hexadecimal = hex(den)
    hexadecimal = hexadecimal.replace("0x", "")
    return hexadecimal

def den2oct(den):
    octal = oct(den)
    octal = octal.replace("0o", "")
    return octal

def bin2den(bin):
    den = int(bin, 2)
    return den

def hex2den(hex):
    den = int(hex, 16)
    return den

def oct2den(oct):
    den = int(oct, 8)
    return den

# Function composition

def bin2hex(bin):
    den = bin2den(bin)
    hex = den2hex(den)
    return hex

def bin2oct(bin):
    den = bin2den(bin)
    oct = den2oct(den)
    return oct

def hex2bin(hex):
    den = hex2den(hex)
    bin = den2bin(den)
    return bin

def hex2oct(hex):
    den = hex2den(hex)
    oct = den2oct(den)
    return oct

if __name__ == "__main__":
    print("Testing conversion functions...")
    assert den2bin(10) == "1010"
    assert den2hex(255) == "ff"
    assert den2oct(8) == "10"
    assert bin2den("1010") == 10
    assert hex2den("ff") == 255
    assert oct2den("10") == 8
    assert bin2hex("1010") == "a"
    assert bin2oct("1010") == "12"
    assert hex2bin("a") == "1010"
    assert hex2oct("a") == "12"
    print("All tests passed!")