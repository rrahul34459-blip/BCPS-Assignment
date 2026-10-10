# Labs 7–8 — Attendance, salary and inventory

Open `attendance-salary-inventory.ods` in LibreOffice Calc. An `.xlsx` copy is included. These are fictional classroom examples.

## Attendance
Enter `P` for present or `A` for absent using the dropdowns. Blank days are not counted.

- H2: `=COUNTIF(C2:G2;"P")`
- I2: `=COUNTIF(C2:G2;"P")+COUNTIF(C2:G2;"A")`
- J2: `=IF(I2=0;"";H2/I2)`

Format column J as a percentage. Student A attends 4 of 5 recorded days, giving **80%**. Fill the formulas down for other students.

## Salary
Enter basic salary, HRA rate, DA rate and deduction rate. Rates are editable assumptions.

- HRA: `=C2*D2`
- DA: `=C2*E2`
- Gross: `=SUM(C2;F2:G2)`
- Deduction: `=H2*I2`
- Net: `=H2-J2`

Employee A: basic INR 25,000, HRA 20%, DA 10%, gross INR **32,500**, deduction 5% of gross = INR **1,625**, net INR **30,875**. This is an arithmetic exercise, not a statutory payroll calculation.

## Inventory
Enter opening stock, receipts, issues, unit cost and reorder level.

- Closing stock: `=C2+D2-E2`
- Stock value: `=F2*G2`

Notebook: closing stock **40**, stock value INR **1,600**. Yellow closing-stock cells indicate stock below the row's reorder level. Keep quantities non-negative and do not issue more than the available stock.

## Practice
Change one input in each sheet and confirm its calculated output changes. Restore the sample value afterward. Calc commonly uses semicolons between function arguments; the stored files handle this automatically.

Reference: [LibreOffice formulas and functions](https://books.libreoffice.org/en/CG262/CG26209-FormulasAndFunctions.html).
