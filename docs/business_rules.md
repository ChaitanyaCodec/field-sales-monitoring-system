# Business Rules

## Attendance Rules

### Rule 1

An employee can start work only once per day.

Reason:

Prevents duplicate attendance records.

---

### Rule 2

An employee must have ACTIVE attendance before performing any customer visit.

Reason:

Ensures visits are linked to a valid workday.

---

### Rule 3

An employee can end work only if an ACTIVE attendance record exists.

Reason:

Prevents invalid attendance completion.

---

## Visit Rules

### Rule 4

An employee can have only one active visit at a time.

Reason:

Prevents overlapping customer visits.

---

### Rule 5

A visit must be checked out before another visit can begin.

Reason:

Maintains accurate visit history.

---

### Rule 6

A visit is considered completed only after check-out.

Reason:

Ensures visit duration can be calculated.

---

## GPS Verification Rules

### Rule 7

The customer must exist in the system before a visit can be created.

Reason:

Prevents invalid customer visits.

---

### Rule 8

The employee must be within 100 meters of the customer location.

Reason:

Ensures physical presence at the customer site.

---

### Rule 9

Check-in is denied if the employee is outside the allowed distance.

Reason:

Prevents fake visit reporting.

---

## Dashboard Rules

### Rule 10

Dashboard statistics are generated from live database records.

Reason:

Provides accurate business insights.

---

### Rule 11

Employee performance is calculated using visit records.

Reason:

Measures field employee productivity.

---

## Reporting Rules

### Rule 12

Visit reports display customer visit activity.

Reason:

Allows managers to review visit history.

---

### Rule 13

Attendance reports display employee attendance activity.

Reason:

Allows managers to monitor workforce attendance.