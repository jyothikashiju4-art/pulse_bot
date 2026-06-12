
# 📊 Pulse Daily Summary Bot

A Python automation bot that sends a daily summary email every morning.

## 🚀 Features
- 🌦 Live weather for Thiruvananthapuram
- 💬 Random motivational quote
- 📌 Daily fact
- 📧 Automated email delivery via Gmail
- ⚙️ Runs daily at 8 AM IST using GitHub Actions

## 🛠 Tech Stack
- Python 3.11
- GitHub Actions (CI/CD)
- wttr.in API (weather)
- ZenQuotes API (quotes)
- SMTP (email)

## 📁 Project Structure
```
pulse_bot/
├── bot.py
├── requirements.txt
└── .github/
    └── workflows/
        └── daily.yml
```

## ⚙️ Setup
1. Fork this repo
2. Add GitHub Secrets:
   - `EMAIL_ADDRESS` — your Gmail
   - `EMAIL_PASSWORD` — Gmail app password
3. Enable GitHub Actions
4. Trigger manually or wait for 8 AM IST

## 👤 Author
jyothikashiju4-art
```



