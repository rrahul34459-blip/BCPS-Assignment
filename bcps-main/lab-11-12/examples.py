"""Runnable companions to the lab 11–12 pseudocode; no dependencies."""


def arithmetic(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else None


def rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("Invalid dimensions")
    return length * width, 2 * (length + width)


def average(a, b, c):
    return (a + b + c) / 3


def simple_interest(principal, rate, years):
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("Invalid input")
    interest = principal * rate * years / 100
    return interest, principal + interest


def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


def largest(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result


def grade(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Invalid marks")
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 40:
        return "D"
    return "F"


def leap_year(year):
    if year <= 0:
        raise ValueError("Invalid year")
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def demo():
    assert arithmetic(12, 4) == (16, 8, 48, 3)
    assert arithmetic(5, 0) == (5, 5, 0, None)
    assert rectangle(5, 3) == (15, 16)
    assert rectangle(0, 3) == (0, 6)
    assert average(10, 20, 30) == 20
    assert simple_interest(10000, 5, 2) == (1000, 11000)
    assert simple_interest(10000, 0, 2) == (0, 10000)
    assert [even_or_odd(n) for n in (14, 7, 0, -3)] == ["Even", "Odd", "Even", "Odd"]
    assert largest(8, 17, 12) == 17
    assert largest(9, 9, 2) == 9
    assert largest(-8, -2, -3) == -2
    assert [grade(n) for n in (0, 39, 40, 59, 60, 74, 75, 89, 90, 100)] == [
        "F", "F", "D", "D", "C", "C", "B", "B", "A", "A"
    ]
    assert [leap_year(y) for y in (2000, 1900, 2024, 2025)] == [True, False, True, False]
    for function, args in (
        (rectangle, (-1, 3)), (simple_interest, (-1, 5, 2)),
        (simple_interest, (100, -1, 2)), (simple_interest, (100, 5, -1)),
        (grade, (-1,)), (grade, (101,)), (leap_year, (0,)),
    ):
        try:
            function(*args)
        except ValueError:
            pass
        else:
            raise AssertionError(f"{function.__name__} accepted invalid input")
    print("Arithmetic:", arithmetic(12, 4))
    print("Rectangle (area, perimeter):", rectangle(5, 3))
    print("Average:", average(10, 20, 30))
    print("Simple interest (interest, amount):", simple_interest(10000, 5, 2))
    print("14 is", even_or_odd(14))
    print("Largest:", largest(8, 17, 12))
    print("Grade for 90:", grade(90))
    print("2000 is a leap year:", leap_year(2000))
    print("All algorithm checks passed.")


if __name__ == "__main__":
    demo()
