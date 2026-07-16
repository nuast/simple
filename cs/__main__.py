import sys
from .conv import CONVERSIONS

print("Conversion App")

if len(sys.argv) == 3:
    conversion = sys.argv[1].strip('-')
    number = sys.argv[2]

    if conversion in CONVERSIONS:
        result = CONVERSIONS[conversion](number)
        print(f"Result: {str(result).upper()}")
    else:
        print("Invalid conversion type")

else:
    print("Usage: python run_cli.py <conversion_type> <number>")
    print("Example: python run_cli.py -b2h 0111")
    print("Conversion types: d2b, d2h, d2o, b2d, h2d, o2d, b2h, b2o, h2b, h2o, o2b, o2h")