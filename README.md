# 🎓 Student Management System Using Django

A complete web-based Student Management System built using **Django** and **SQLite/MySQL**. This project allows **superusers (admins)** to manage student data, attendance, and marks, while **normal users (students)** can view their personalized dashboard securely. It features full authentication, form validation, Bootstrap UI, and Google Charts for analytics.

---

## 🚀 Features

### ✅ Admin (Superuser) Panel
- Add/Edit/Delete Student records.
- Add Attendance and Marks for each student.
- Secure CRUD operations with permission control.
- Admin dashboard with messages & search/pagination.

### ✅ Student (Normal User) Dashboard
- Secure login system.
- View only access to:
  - Personal Info
  - Attendance (Pie Chart Visualization via Google Charts)
  - Marks (Clean tabular view)
  - Contact Info
- Auto-logout after 5 minutes of inactivity.

### ✅ Common Functionality
- Login / Logout / Registration system.
- Bootstrap-enhanced UI.
- Custom success & error messages.
- Role-based access: No unauthenticated or unauthorized access.
- Static file and media file handling.
- Fully integrated with Git and ready to deploy.

---

## 🧱 Tech Stack

| Layer              | Tech Used                         |
|--------------------|-----------------------------------|
| Backend Framework  | Django 5.x                        |
| Database           | SQLite (default) |
| Frontend           | HTML, CSS, Bootstrap              |
| Charts             | Google Charts (for Attendance)    |
| Version Control    | Git + GitHub                      |
| Authentication     | Django Auth System                |



## 📁 Project Structure

student_management_system/
├── student/ # App handling all student-related models/views
│ ├── models.py # Student, Attendance, Marks models
│ ├── views.py # Logic for admin and student operations
│ ├── forms.py # Django Forms for student data
├── templates/ # HTML templates (Bootstrap)
│ ├── dashboard.html # Student dashboard
│ ├── student_list.html # Admin dashboard
│ ├── login.html / register.html / etc.
├── static/ # Static CSS and JS
│ └── css/styles.css
├── media/ # Profile pictures and media uploads
├── learning/ # Project settings and URLs
├── manage.py


👨‍💻 Developer
Name: Harishwar Reddy Jara
