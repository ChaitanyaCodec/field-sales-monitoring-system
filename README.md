# Field Sales Monitoring & Visit Verification System

## Project Overview

The Field Sales Monitoring & Visit Verification System is a Django-based web application designed to monitor and verify field sales activities.

The system helps organizations track employee attendance, customer visits, and location-based verification to ensure that field employees actually visit assigned customers.

Managers can monitor employee activities through dashboards and reports.

---

# Problem Statement

Organizations with field sales teams often face challenges such as:

- Fake customer visit entries
- Lack of employee location verification
- Inaccurate attendance records
- Limited visibility into field operations
- Difficulty measuring employee performance

This system addresses these issues through attendance tracking, customer visit management, and GPS-based verification.

---

# Objectives

- Track employee attendance
- Record customer visits
- Verify employee location using GPS coordinates
- Prevent fake visit reporting
- Provide dashboards and reports for managers
- Improve field sales transparency

---

# Key Features

## User Management

- Custom User Model
- Employee Role
- Admin Role

## Customer Management

- Customer Registration
- Customer GPS Coordinates

## Attendance Management

- Start Work
- End Work
- Attendance Status Tracking

## Visit Management

- Customer Check-In
- Customer Check-Out
- Visit Duration Calculation
- Active Visit Validation

## GPS Verification

- Haversine Distance Formula
- Customer Location Validation
- 100 Meter Distance Rule

## Dashboard

- Total Employees
- Total Customers
- Today's Attendance
- Today's Visits
- Completed Visits
- Recent Visits
- Recent Attendance
- Employee Performance Summary

## Reports

- Visit Report
- Attendance Report

---

# Technology Stack

## Backend

- Python
- Django

## Database

- SQLite (Development)
- PostgreSQL (Production Ready)

## Frontend

- HTML
- CSS
- Bootstrap 5

## Version Control

- Git
- GitHub

---

# Project Structure

sales_monitoring/

├── accounts/

├── customers/

├── attendance/

├── visits/

├── dashboard/

├── reports/

├── templates/

├── static/

├── manage.py

└── db.sqlite3

---

# Business Workflow

Employee Login

↓

Start Work

↓

Attendance ACTIVE

↓

Visit Customer

↓

GPS Verification

↓

Check-In

↓

Check-Out

↓

Visit COMPLETED

↓

End Work

↓

Attendance COMPLETED

---

# GPS Verification Logic

The system calculates the distance between:

- Employee GPS Coordinates
- Customer GPS Coordinates

using the Haversine Formula.

Rules:

- Employee must be within 100 meters of customer location.
- Check-in is denied if the employee is outside the allowed range.

---

 

# Installation

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Clone Repository

```bash
git clone <repository-url>
cd sales_monitoring


# Future Scope

## Phase 2
- Photo Evidence Upload
- Route Tracking
- Live Employee Location
- Customer Feedback

## Phase 3
- Analytics Dashboard
- Charts and Graphs
- Performance Reports

## Phase 4
- REST APIs
- Mobile App Integration
- Cloud Deployment


# Author

Chaitanya Bhogawade
MCA Student
GH Raisoni College of Engineering & Management, Pune