# 🏥 Django Hospital Management System

A complete hospital management system built with Django — designed for healthcare facilities in Kenya.

## 🚀 Features

- **Patient Management** — Register and manage patient records
- **Doctor Management** — Add doctors and assign them to departments
- **Visit Tracking** — Record patient visits, diagnoses, and treatments
- **Department Management** — Organize hospital departments
- **Admin Interface** — Full Django admin panel for data management

## 🛠️ Tech Stack

- **Backend:** Django 6.0
- **Database:** SQLite (development), PostgreSQL (production ready)
- **Language:** Python 3.14

## 📂 Models

| Model | Purpose |
|-------|---------|
| `Patient` | Patient demographics (name, DOB, gender, phone, sub-county) |
| `Doctor` | Doctor details (name, specialty, department) |
| `Department` | Hospital departments (name, location) |
| `Visit` | Clinical visits (patient, doctor, diagnosis, treatment) |

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/LOROHK/django-hospital.git
cd django-hospital

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python3 manage.py migrate

# Create superuser
python3 manage.py createsuperuser

# Run the server
python3 manage.py runserver