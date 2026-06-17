# Secure Booking System

## 1. Project Description

The Secure Booking System is a complete web application built with Django 4.2.7 (Python) that allows users to create, read, update, and delete service bookings. The system implements Role-Based Access Control (RBAC) with two user types: **Admin** and **Normal User**.

This project was developed as part of the Secure Software Development course (IKB 21503) at Universiti Kuala Lumpur (UniKL MIIT) to demonstrate OWASP-compliant secure coding practices.

**Key Features:**
- 🔐 Secure User Authentication & Registration
- 👤 Role-Based Access Control (Admin vs Normal User)
- 📝 Complete Booking CRUD Operations (Create, Read, Update, Delete)
- 📊 Audit Logging for Security Monitoring
- 🛡️ OWASP-Compliant Security Controls

---

## 2. Installation Steps

### Prerequisites
- Python 3.10 or higher
- Git
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/ariefzolkopli/secure-booking-system.git
cd secure-booking-system
```

### Step 2: Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
```bash
cp .env.example .env
```
Edit `.env` file:
```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
```

### Step 5: Run Migrations
```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

---

## 3. Security Features Summary

| OWASP Control | Implementation |
|---------------|----------------|
| **Input Validation** | Custom validators for service type, date, time, phone number, and SQL injection prevention |
| **Authentication & Session Security** | 30-minute session timeout, password complexity requirements, rate limiting (5 attempts) |
| **Access Control** | Role-Based Access Control, ownership validation, admin-only audit log |
| **Error Handling** | Custom 400/403/404/500 error pages, DEBUG=False in production |
| **Sensitive Data Protection** | Environment variables (.env), SECRET_KEY excluded from version control |
| **Configuration Security** | HttpOnly cookies, CSRF protection, security headers |
| **Logging & Monitoring** | Audit log tracking all user actions (login, logout, booking CRUD) |
| **Output Encoding** | Django template auto-escaping prevents XSS attacks |

---

## 4. How to Run the App

### Step 1: Activate Virtual Environment
```bash
source venv/Scripts/activate
```

### Step 2: Start the Development Server
```bash
python manage.py runserver
```

### Step 3: Access the Application
Open browser and go to: `http://127.0.0.1:8000`

### Step 4: Login
- **Username:** `admin`
- **Password:** Admin123!

---

## 5. Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 4.2.7 | Web framework |
| python-dotenv | 1.0.0 | Environment variable management |
| SQLite | Built-in | Database |

**requirements.txt:**
```
Django==4.2.7
python-dotenv==1.0.0
```

---

## 6. Screenshots

![Login Page](media/image6.png)
*Figure 1: User Login Page*

![Dashboard](media/image18.png)
*Figure 2: Admin Dashboard*

![Booking List](media/image13.png)
*Figure 3: Booking List*

![Audit Log](media/image19.png)
*Figure 4: Audit Log (Admin Only)*

---

## 👥 Team Members

| Name | GitHub Username | Role |
|------|-----------------|------|
| Arief Zolkopli | @ariefzolkopli | Project Lead & Backend Developer |
| Eiman Danish | @eiman31 | Secure Coding Implementation |
| Azaim Hazim | @azaim | Security Testing |
| Muhammad Izzuddin | @izzue71 | CI/CD & Version Control |

---

## 👨‍🏫 Course Lecturer

| Name | GitHub Username | Role |
|------|-----------------|------|
| **Mdm Mardiana Mahari** | @MDiana272 | Course Leader & Lecturer |

---

## 📚 Course Details

| Detail | Information |
|--------|-------------|
| **Campus** | UniKL MIIT |
| **Course Code** | IKB 21503 |
| **Course Name** | Secure Software Development |
| **Semester** | 2026/January |
| **Submission Date** | Week 15 (Wednesday) |

---

## 🔗 Repository Access

- **Repository:** [secure-booking-system](https://github.com/ariefzolkopli/secure-booking-system)
- **Access:** Private repository (Lecturer added as collaborator)

---

## 📖 References

1. [Django Documentation](https://docs.djangoproject.com/)
2. [OWASP Top 10](https://owasp.org/Top10/)
3. [OWASP ASVS](https://owasp.org/ASVS/)

---

**© 2026 - Secure Booking System Team | UniKL MIIT**