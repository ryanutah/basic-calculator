#!/usr/bin/env python3
"""
Basic Calculator CLI.

Usage examples:
  python BasicCalculator.py add 2 3
  python BasicCalculator.py divide 10 2
  python BasicCalculator.py --interactive

When --interactive is used, the script prompts the user for operation and inputs.
"""
import argparse
import sys
from Functions import add, subtract, multiply, divide

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}

def interactive_mode() -> int:
    print("Basic Calculator (add, subtract, multiply, divide)")
    op = input("Operation: ").strip().lower()
    if op not in OPERATIONS:
        print("Invalid operation. Choose from: add, subtract, multiply, divide")
        return 2
    try:
        a = input("First number: ").strip()
        b = input("Second number: ").strip()
        result = OPERATIONS[op](a, b)
        print("Result:", result)
        return 0
    except ZeroDivisionError as e:
        print("Error:", e)
        return 1
    except Exception as e:
        print("Error:", e)
        return 1

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Basic Calculator")
    parser.add_argument("operation", nargs="?", choices=list(OPERATIONS.keys()),
                        help="Operation to perform")
    parser.add_argument("a", nargs="?",
                        help="First operand (number or numeric string)")
    parser.add_argument("b", nargs="?",
                        help="Second operand (number or numeric string)")
    parser.add_argument("--interactive", action="store_true",
                        help="Run in interactive prompt mode")
    args = parser.parse_args(argv)

    if args.interactive:
        return interactive_mode()

    if args.operation is None or args.a is None or args.b is None:
        parser.print_help()
        return 2

    try:
        func = OPERATIONS[args.operation]
        print(func(args.a, args.b))
        return 0
    except ZeroDivisionError as e:
        print("Error:", e, file=sys.stderr)
        return 1
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
