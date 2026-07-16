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
    print("Example: python run_cli.py -'Binary → Hex' 0111")
    print(f"Conversion types: {', '.join(CONVERSIONS)}")