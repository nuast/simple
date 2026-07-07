import sys
from conv import den2bin, den2hex, den2oct, bin2den, hex2den, oct2den, bin2hex, bin2oct, hex2bin, hex2oct, oct2bin, oct2hex

conversions = {
    "d2b": den2bin, "d2h": den2hex, "d2o": den2oct, "b2d": bin2den, "h2d": hex2den, "o2d": oct2den,
    "b2h": bin2hex, "b2o": bin2oct, "h2b": hex2bin, "h2o": hex2oct, "o2b": oct2bin, "o2h": oct2hex
}

print("Conversion App")

if len(sys.argv) == 3:
    conversion = sys.argv[1].strip('-')
    number = sys.argv[2]

    if conversion in conversions:
        result = conversions[conversion](number)
        print(f"Result: {str(result).upper()}")
    else:
        print("Invalid conversion type")

else:
    print("Usage: python run_cli.py <conversion_type> <number>")
    print("Example: python run_cli.py -b2h 0111")
    print("Conversion types: d2b, d2h, d2o, b2d, h2d, o2d, b2h, b2o, h2b, h2o, o2b, o2h")