"""
Functions for basic calculator operations with type validation.

This module exports add, subtract, multiply, divide. It accepts ints/floats (or
numeric strings) and returns a float when needed. divide() raises ZeroDivisionError
for division by zero. All functions raise TypeError for non‑numeric inputs.
"""
from typing import Union

Number = Union[int, float]

def _to_number(x) -> Number:
    """Best-effort conversion of x to a number (int if possible, else float)."""
    if isinstance(x, (int, float)):
        return x
    if isinstance(x, str):
        try:
            if x.strip().isdigit() or (x.strip().startswith('-') and x.strip()[1:].isdigit()):
                return int(x)
            return float(x)
        except ValueError as e:
            raise TypeError(f"Value {x!r} is not a number") from e
    raise TypeError(f"Unsupported type {type(x).__name__}; expected number or numeric string.")

def add(a: Number, b: Number) -> Number:
    a, b = _to_number(a), _to_number(b)
    return a + b

def subtract(a: Number, b: Number) -> Number:
    a, b = _to_number(a), _to_number(b)
    return a - b

def multiply(a: Number, b: Number) -> Number:
    a, b = _to_number(a), _to_number(b)
    return a * b

def divide(a: Number, b: Number) -> float:
    a, b = _to_number(a), _to_number(b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
