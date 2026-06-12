import os
import requests
import smtplib
from email.mime.text import MIMEText

def get_weather():
    api_key = os.environ["OPENWEATHER_API_KEY"]
    city = "Thiruvananthapuram"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url, timeout=10)
    data = response.json()

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    return temp, description

def send_alert(temp, description):
    sender = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_PASSWORD"]

    msg = MIMEText(f"""
⚠️ WEATHER ALERT!

🌡 Temperature: {temp}°C
🌤 Condition: {description}

Stay safe today!
""")
    msg["Subject"] = "⚠️ Weather Alert - Pulse Bot"
    msg["From"] = sender
    msg["To"] = sender

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
    print("Alert email sent!")

def run():
    temp, description = get_weather()
    print(f"Temperature: {temp}°C, Condition: {description}")

    if temp > 35 or "rain" in description.lower():
        print("⚠️ Alert condition met!")
        send_alert(temp, description)
    else:
        print("✅ Weather is normal. No alert needed.")

if __name__ == "__main__":
    run()