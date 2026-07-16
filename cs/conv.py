# Base conversion functions

def den2bin(den):
    binary = bin(int(den))
    binary = binary.replace("0b", "")
    return binary

def den2hex(den):
    hexadecimal = hex(den)
    hexadecimal = hexadecimal.replace("0x", "")
    return hexadecimal

def den2oct(den):
    octal = oct(int(den))
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

CONVERSIONS = {
    "d2b": den2bin,
    "d2h": den2hex,
    "d2o": den2oct,
    "b2d": bin2den,
    "h2d": hex2den,
    "o2d": oct2den,
    "b2h": bin2hex,
    "b2o": bin2oct,
    "h2b": hex2bin,
    "h2o": hex2oct,
}

CONVERSION_LABELS = {
    "d2b": "Denary → Binary",
    "d2h": "Denary → Hex",
    "d2o": "Denary → Octal",
    "b2d": "Binary → Denary",
    "b2h": "Binary → Hex",
    "b2o": "Binary → Octal",
    "h2d": "Hex → Denary",
    "h2b": "Hex → Binary",
    "h2o": "Hex → Octal",
    "o2d": "Octal → Denary",
}

DISPLAY_CONVERSIONS = {
    label: CONVERSIONS[code]
    for code, label in CONVERSION_LABELS.items()
}

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
else:
    print("You have imported the cs/conv.py")