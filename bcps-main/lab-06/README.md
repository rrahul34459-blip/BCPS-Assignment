# Lab 6 — Student marksheet

## Aim
Prepare a marksheet in LibreOffice Calc using SUM, AVERAGE, MAX and MIN.

Open `student-marksheet.ods` in LibreOffice Calc. The `.xlsx` copy is also provided. All names and marks are fictional sample data.

## Procedure
1. Enter roll numbers, student names and four subject marks in columns A–F.
2. In G2 enter `=SUM(C2:F2)` for total marks out of 400.
3. In H2 enter `=AVERAGE(C2:F2)` for average marks.
4. In I2 enter `=MAX(C2:F2)` and in J2 enter `=MIN(C2:F2)`.
5. In K2 enter `=G2/400` and apply Percentage formatting.
6. Fill the formulas down through row 6. Change an input mark and observe recalculation.

## Expected result
Student A: total **345**, average **86.25**, highest **92**, lowest **80**, percentage **86.25%**.

Each subject is marked out of 100. Input validation allows whole marks from 0 to 100.

Reference: [LibreOffice SUM documentation](https://help.libreoffice.org/latest/en-US/text/scalc/01/func_sum.html).
