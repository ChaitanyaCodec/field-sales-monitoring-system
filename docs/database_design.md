# Database Design

## User Model



Purpose:

Store system users.

Fields:

| Field | Type | Description |
|---------|---------|---------|
| id | Integer | Primary Key |
| username | String | Username |
| email | String | Email Address |
| role | String | EMPLOYEE / ADMIN |

## Customer Model
 

Purpose:

Store customer information.

Fields:

| Field | Type | Description |
|---------|---------|---------|
| id | Integer | Primary Key |
| name | String | Customer Name |
| address | Text | Customer Address |
| latitude | Decimal | GPS Latitude |
| longitude | Decimal | GPS Longitude |

## Attendance Model
 

Purpose:

Track employee attendance.

Fields:

| Field | Type | Description |
|---------|---------|---------|
| id | Integer | Primary Key |
| employee | ForeignKey | User |
| date | Date | Attendance Date |
| start_time | DateTime | Start Work |
| end_time | DateTime | End Work |
| start_latitude | Decimal | Start GPS |
| start_longitude | Decimal | Start GPS |
| end_latitude | Decimal | End GPS |
| end_longitude | Decimal | End GPS |
| status | String | ACTIVE / COMPLETED |

## Visit Model
 

Purpose:

Track customer visits.

Fields:

| Field | Type | Description |
|---------|---------|---------|
| id | Integer | Primary Key |
| employee | ForeignKey | User |
| attendance | ForeignKey | Attendance |
| customer | ForeignKey | Customer |
| checkin_time | DateTime | Check-In Time |
| checkout_time | DateTime | Check-Out Time |
| checkin_latitude | Decimal | Check-In GPS |
| checkin_longitude | Decimal | Check-In GPS |
| checkout_latitude | Decimal | Check-Out GPS |
| checkout_longitude | Decimal | Check-Out GPS |
| notes | Text | Visit Notes |
| status | String | CHECKED_IN / COMPLETED |

## Relationships


### Relationship Meaning

```text
USER 1 ---- M ATTENDANCE

ATTENDANCE 1 ---- M VISIT

CUSTOMER 1 ---- M VISIT
```

 
## Database Summary

 

Total Core Models:

1. User
2. Customer
3. Attendance
4. Visit

Primary Relationships:

- User → Attendance
- Attendance → Visit
- Customer → Visit