
# 🏪 Store Management System (Flask + HTML)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black.svg)
![Status](https://img.shields.io/badge/Status-Learning%20Project-success)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A **full-stack beginner-friendly Store Management System** built using **Python Flask**, HTML templates, and file-based storage.
This project simulates real-world store operations such as **product management, purchasing, billing, and history tracking** through a web interface.

---

## 🚀 Live Features

* 🔐 Secure admin login system (Flask-based authentication)
* 📦 Add, update, and manage products
* 📋 View complete product inventory
* 🛒 Purchase system with dynamic billing
* 🧾 Automatic bill generation & total calculation
* 📜 Purchase history stored in `bill_history.txt`
* 🌐 Clean and responsive HTML-based UI (Jinja2 templates)

---

## 🛠️ Tech Stack

| Technology     | Purpose             |
| -------------- | ------------------- |
| Python 🐍      | Core backend logic  |
| Flask 🌶️      | Web framework       |
| HTML / CSS 🎨  | Frontend UI         |
| Pandas 📊      | Data handling       |
| File System 📁 | Lightweight storage |

---

## 📁 Project Architecture

```text id="arch1"
Store-Management-System/
│
├── app.py                  # Main Flask application
├── admin.py               # Admin authentication logic
├── stock.py               # Product inventory management
├── Product_Menu.py        # Menu handling logic
├── bill_handling.py       # Billing + history system
│
├── templates/             # HTML UI templates
│   ├── dashboard.html
│   ├── add_product.html
│   ├── view_product.html
│   ├── purchase.html
│   ├── history.html
│   └── login.html
│
├── static/                # CSS, images, icons
│
├── bill_history.txt      # Stores transaction history
├── products.json/csv     # Product database (optional)
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash id="c1"
git clone <your-repo-link>
cd Store-Management-System
```

### 2️⃣ Create Virtual Environment

```bash id="c2"
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows**

```bash id="c3"
venv\Scripts\activate
```

**Mac/Linux**

```bash id="c4"
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash id="c5"
pip install flask pandas
```

### 5️⃣ Run the Application

```bash id="c6"
python app.py
```

---

## 🌐 Application Routes

| Route          | Description     |
| -------------- | --------------- |
| `/`            | Login page      |
| `/dashboard`   | Admin dashboard |
| `/add-product` | Add new product |
| `/products`    | View inventory  |
| `/purchase`    | Purchase items  |
| `/history`     | Billing history |

---

## 📌 Core Concepts Implemented

* Flask routing system (`@app.route`)
* Session-based login authentication
* HTML templating using Jinja2
* Form handling (GET & POST methods)
* File-based data persistence
* Basic OOP structure (Admin, Stock)
* Data processing using Pandas

---

## 📊 Project Highlights (Portfolio Ready)

✔ Built a complete **mini e-commerce backend system**
✔ Implemented **real-world store operations workflow**
✔ Designed **modular Python architecture (OOP + Flask)**
✔ Integrated **billing system with history tracking**
✔ Created a **clean web-based admin dashboard**

---

## 🚀 Future Improvements

* 🔄 Replace file storage with **SQLite / MySQL**
* 👥 Add **Customer + Admin roles**
* 🎨 Upgrade UI using **Bootstrap / TailwindCSS**
* 📦 Add inventory quantity control system
* 🔌 Convert into **REST API (FastAPI version)**
* ⚛️ Build React frontend version (Full Stack upgrade)
* ☁️ Deploy on Render / AWS / Railway

---

## 🧠 What I Learned

* Backend development using Flask
* Full CRUD system design
* Data handling using Python
* Web templating with Jinja2
* Building real-world project architecture
* File-based persistence systems

---

## 👨‍💻 Author

**md farhan**
💡 Python | Flask | AI/ML Enthusiast | Full Stack Learner

---

## ⭐ If you like this project

Give a ⭐ on the repository and follow for more projects!
