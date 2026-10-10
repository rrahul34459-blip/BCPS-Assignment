# Labs 11–12: Algorithms and pseudocode

## Aim

Write finite, unambiguous steps for arithmetic and logical problems, then dry-run them with sample inputs. `READ` means input, `PRINT` means output, `←` assigns a value, and `MOD` means remainder.

## Lab 11: Arithmetic

### 1. Four arithmetic operations

Algorithm: read two numbers; compute their sum, difference and product; divide only when the second number is nonzero; display the results.

```text
START
READ a, b
PRINT a + b, a - b, a * b
IF b = 0 THEN
    PRINT "Division undefined"
ELSE
    PRINT a / b
END IF
STOP
```

Dry run: `a = 12`, `b = 4` → sum `16`, difference `8`, product `48`, quotient `3`. With `b = 0`, no division is attempted.

### 2. Area and perimeter of a rectangle

Algorithm: read length and width; reject negative dimensions; calculate area and perimeter.

```text
START
READ length, width
IF length < 0 OR width < 0 THEN
    PRINT "Invalid dimensions"
ELSE
    area ← length * width
    perimeter ← 2 * (length + width)
    PRINT area, perimeter
END IF
STOP
```

Dry run: length `5`, width `3` → area `15` square units; perimeter `16` units. Zero is allowed as a degenerate rectangle.

### 3. Average of three numbers

Algorithm: read three numbers; add them; divide the total by three.

```text
START
READ a, b, c
total ← a + b + c
average ← total / 3
PRINT average
STOP
```

Dry run: `10, 20, 30` → total `60`, average `20`.

### 4. Simple interest

Algorithm: read nonnegative principal, annual percentage rate and time in years; compute interest and final amount.

```text
START
READ principal, rate, years
IF principal < 0 OR rate < 0 OR years < 0 THEN
    PRINT "Invalid input"
ELSE
    interest ← principal * rate * years / 100
    amount ← principal + interest
    PRINT interest, amount
END IF
STOP
```

Dry run: principal `10000`, annual rate `5%`, time `2` years → interest `1000`, amount `11000`. This is simple, not compound, interest.

## Lab 12: Logic and decisions

### 5. Even or odd

Algorithm: read an integer; divide by two and inspect the remainder.

```text
START
READ integer n
IF n MOD 2 = 0 THEN
    PRINT "Even"
ELSE
    PRINT "Odd"
END IF
STOP
```

Dry runs: `14` → Even; `7` → Odd; `0` → Even; `-3` → Odd.

### 6. Largest of three numbers

Algorithm: assume the first value is largest; compare the second and third in sequence; update as necessary.

```text
START
READ a, b, c
largest ← a
IF b > largest THEN
    largest ← b
END IF
IF c > largest THEN
    largest ← c
END IF
PRINT largest
STOP
```

Dry run: `8, 17, 12` → largest begins at `8`, becomes `17`, stays `17`. Ties are valid: `9, 9, 2` → `9`.

### 7. Grade calculation

Classroom rule: A ≥ 90, B ≥ 75, C ≥ 60, D ≥ 40, otherwise F. These are illustrative thresholds, not an institutional grading policy.

Algorithm: reject scores outside 0–100; test thresholds from highest to lowest.

```text
START
READ marks
IF marks < 0 OR marks > 100 THEN
    PRINT "Invalid marks"
ELSE IF marks >= 90 THEN
    PRINT "A"
ELSE IF marks >= 75 THEN
    PRINT "B"
ELSE IF marks >= 60 THEN
    PRINT "C"
ELSE IF marks >= 40 THEN
    PRINT "D"
ELSE
    PRINT "F"
END IF
STOP
```

Dry runs: `90` → A; `75` → B; `40` → D; `39` → F; `101` → Invalid marks.

### 8. Leap year

Algorithm: read a positive Gregorian year; it is a leap year if divisible by 400, or divisible by 4 but not by 100.

```text
START
READ integer year
IF year <= 0 THEN
    PRINT "Invalid year"
ELSE IF year MOD 400 = 0 OR (year MOD 4 = 0 AND year MOD 100 != 0) THEN
    PRINT "Leap year"
ELSE
    PRINT "Not a leap year"
END IF
STOP
```

Dry runs: `2000` → Leap year; `1900` → Not a leap year; `2024` → Leap year; `2025` → Not a leap year.

## Runnable verification

From the repository root run `python3 lab-11-12/examples.py`.
The Python companion demonstrates every algorithm and checks zero division, negative dimensions, tied maxima, grade boundaries and century leap-year rules using assertions. Numeric input types are assumed in the pseudocode; the companion uses fixed numeric examples rather than interactive input parsing.

## Result

Arithmetic problems use sequence; logical problems use selection. Each algorithm identifies inputs, processing and outputs and terminates after a finite number of steps.
