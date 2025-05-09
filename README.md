
# 🕒 Remind-me-later API (Django)

This is a simple backend API built using Django to support a **reminder web app**.  
It allows users to set a reminder with:
- a specific date
- time
- message
- reminder method (Email or SMS)

> ⚠️ This API does **not send messages** — it only stores reminder data for future use.

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/remind-me-later.git
cd remind-me-later
```

### 2. Set Up Virtual Environment

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

Open your browser at:  
👉 `http://127.0.0.1:8000/api/reminders/`

---

## 📮 API Endpoint

| Method | Endpoint           | Description        |
|--------|--------------------|--------------------|
| POST   | `/api/reminders/`  | Create a reminder  |

### Example POST Body (JSON)

```json
{
  "date": "2025-05-10",
  "time": "14:30:00",
  "message": "Team meeting at 2:30 PM",
  "method": "email"
}
```

---

## 🛠 Tech Stack

- Python
- Django
- SQLite (default database)

---

## 📁 Project Structure

```
remind_me_later/
├── reminders/           # App with models, views, and URLs
├── remind_me_later/     # Project settings and main URLs
├── manage.py
├── db.sqlite3
└── .gitignore
```

---

## 👤 Author

**Vasu Krishna**  
📧 vasukrishna2002@gmail.com

---

## ✅ To Do

- [ ] Add frontend integration
- [ ] Add support for actual reminder delivery via SMS/Email
- [ ] Add authentication

---

## 📄 License

This project is for assessment purposes only.
