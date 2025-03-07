*Flask URL Shortener*

## Project Overview##
This is a simple **Flask-based URL shortener** that allows users to convert long URLs into short, easy-to-share links. The app generates a random 6-character short code for each URL or allows users to specify their own short code.

## 🛠 Tech Stack
- *Python* (Flask framework)
- *Flask* (Web framework)
- *cURL* (for API testing)

---

## 📌 Installation & Setup
## 1️⃣ Clone the Repository
---
git clone https://github.com/Hord16/URLShortener.git
cd URLShortener
---

### 2️⃣ Create a Virtual Environment & Install Dependencies
---
python3 -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
pip install flask
---

### 3️⃣ Run the Flask Server
---
python3 app.py
---
The server will start at `http://127.0.0.1:5000`.

---

🔗 Usage
*Shorten a URL*
## Request:
---
curl -X POST http://127.0.0.1:5000/shorten -H "Content-Type: application/json" -d '{"original_url": "https://www.google.com"}'
---
## Response:
---json
{
  "short_url": "http://127.0.0.1:5000/abc123"
}
---

# *Custom Short Code (Optional but fun)*
##Request:
---
curl -X POST http://127.0.0.1:5000/shorten -H "Content-Type: application/json" -d '{"original_url": "https://www.google.com", "custom_code": "google1"}'
---

##Response:
---json
{
  "short_url": "http://127.0.0.1:5000/google1"
}
---

## *Redirect to Original URL*
#Request:
----
curl -X GET http://127.0.0.1:5000/abc123
---
This will redirect to `https://www.google.com`.

---

## 📌 Features & To-Do
✅ Shortens URLs with a randomly generated 6-character code  
✅ Allows users to choose their own short code  
⬜ Store URLs in a database instead of in-memory dictionary  
⬜ Add an expiration time for short URLs  

---

## 💡 Contribution
Feel free to fork this repository and submit pull requests for new features or bug fixes!

---

## 📜 License
This project is open-source and available under the **MIT License**.
