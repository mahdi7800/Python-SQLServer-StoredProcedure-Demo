# Python SQL Server Stored Procedure Demo

A simple and practical Python project that demonstrates how to execute **SQL Server Stored Procedures** using **pyodbc**.

This project focuses on connecting Python to Microsoft SQL Server, validating user input, executing parameterized stored procedures, handling transactions, and managing database exceptions using a clean and modular project structure.

> **Note**
>
> This repository only contains the **Python implementation**.
> The required SQL Server database objects (such as the Stored Procedure) are assumed to already exist in your SQL Server database.

---

## 🚀 Features

* Connect to Microsoft SQL Server using **pyodbc**
* Execute Stored Procedures with parameters
* Input validation
* Transaction management (`Commit` / `Rollback`)
* Exception handling
* Clean and modular project structure
* Beginner-friendly example

---

## 🛠 Technologies

* Python 3.x
* Microsoft SQL Server
* pyodbc
* T-SQL Stored Procedures

---

## 📁 Project Structure

```text
Python-SQLServer-StoredProcedure-Demo/
│
├── db/
│   ├── __init__.py
│   └── database.py
│
├── validation.py
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.x
* Microsoft SQL Server
* Northwind Database (or your own database)
* SQL Server ODBC Driver

Install the required package:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Edit the `config.py` file and update your SQL Server connection information.

```python
DRIVER = "{SQL Server}"
SERVER = "YOUR_SERVER_NAME"
DATABASE = "Northwind"
TRUSTED_CONNECTION = "yes"
```

---

## ▶️ Run

```bash
python main.py
```

Example:

```text
Enter Customer ID: ALFKI
Enter Amount: 1000

Payment completed successfully.
```

---

## 📚 Learning Objectives

This project demonstrates:

* Connecting Python to SQL Server
* Executing Stored Procedures
* Using parameterized SQL queries
* Managing SQL transactions
* Exception handling
* Input validation
* Organizing a Python project

---

# 🇮🇷 نسخه فارسی

## معرفی

این پروژه یک نمونه عملی برای اجرای **Stored Procedure** در **Microsoft SQL Server** با استفاده از زبان **Python** و کتابخانه **pyodbc** است.

هدف پروژه، آشنایی با نحوه ارتباط Python با SQL Server، اجرای Stored Procedure، اعتبارسنجی اطلاعات ورودی، مدیریت تراکنش‌ها و پیاده‌سازی یک ساختار ماژولار برای پروژه‌های پایتون است.

> **نکته**
>
> این مخزن تنها شامل پیاده‌سازی **سمت Python** است.
> فرض بر این است که Stored Procedure و سایر اشیای پایگاه داده از قبل در SQL Server ایجاد شده‌اند.

---

## ✨ امکانات پروژه

* اتصال به Microsoft SQL Server
* اجرای Stored Procedure با پارامتر
* اعتبارسنجی اطلاعات ورودی
* مدیریت تراکنش‌ها (Commit و Rollback)
* مدیریت خطاها
* ساختار ماژولار و خوانا
* مناسب برای یادگیری ارتباط Python و SQL Server

---

## 🛠 تکنولوژی‌های استفاده شده

* Python
* Microsoft SQL Server
* pyodbc
* T-SQL

---

## 📁 ساختار پروژه

```text
Python-SQLServer-StoredProcedure-Demo/
│
├── db/
│   ├── __init__.py
│   └── database.py
│
├── validation.py
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ پیش‌نیازها

برای اجرای پروژه به موارد زیر نیاز دارید:

* Python 3
* Microsoft SQL Server
* پایگاه داده Northwind (یا هر پایگاه داده دلخواه)
* SQL Server ODBC Driver

سپس وابستگی‌های پروژه را نصب کنید:

```bash
pip install -r requirements.txt
```

---

## ⚙️ تنظیمات

اطلاعات اتصال به SQL Server را در فایل `config.py` وارد کنید.

---

## ▶️ اجرای پروژه

```bash
python main.py
```

---

## 🎯 هدف پروژه

این پروژه با هدف آموزش نحوه اجرای Stored Procedure در SQL Server با استفاده از Python توسعه داده شده است و می‌تواند به عنوان یک نمونه آموزشی برای دانشجویان، توسعه‌دهندگان و علاقه‌مندان به برنامه‌نویسی سمت پایگاه داده مورد استفاده قرار گیرد.

---

## 🔗 Related Repository

The SQL Server Stored Procedure used in this project is maintained in a separate repository.

**Stored Procedure Repository:**

[Stored-Procedure-Payment](https://github.com/mahdi7800/Stored-Procedure-Payment)

This Python project calls the Stored Procedure from the repository above to demonstrate how to execute SQL Server Stored Procedures using **pyodbc**.

---

# 🔗 مخزن مرتبط

Stored Procedure مورد استفاده در این پروژه در یک مخزن جداگانه نگهداری می‌شود.

**لینک مخزن Stored Procedure:**

[Stored-Procedure-Payment](https://github.com/mahdi7800/Stored-Procedure-Payment)

این پروژه تنها بخش **Python** را پیاده‌سازی می‌کند و برای اجرای صحیح آن، لازم است Stored Procedure موجود در مخزن بالا را در SQL Server ایجاد کنید.


---

## 👨‍💻 Author

**Mahdi Davoudi**



