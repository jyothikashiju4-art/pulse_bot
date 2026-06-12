import os
import smtplib
from email.mime.text import MIMEText
import requests
from datetime import date



# Pulse Daily Summary Bot
# Fetches: weather (wttr.in) + quote (ZenQuotes) + daily fact
# Runs locally and later via GitHub Actions


# 1. WEATHER
def get_weather(city="Thiruvananthapuram"):
    """Fetch today's weather as a one-line text summary."""

    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()

    except Exception as e:
        return f"Weather unavailable ({e})"


# 2. QUOTE
def get_quote():
    """Fetch a random motivational quote."""

    url = "https://zenquotes.io/api/random"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        return f"{quote} - {author}"

    except Exception as e:
        return f"Quote unavailable ({e})"


# 3. FACT
def get_date_fact():
    """Return a daily fact."""

    return "Fun fact: Consistency builds mastery 🚀"


# 4. BUILD SUMMARY
def build_summary():
    """Assemble the full daily summary."""

    today = date.today().strftime("%A, %d %B %Y")

    weather = get_weather()
    quote = get_quote()
    fact = get_date_fact()

    summary = f"""
📅 DAILY SUMMARY - PULSE BOT ({today})

🌦 WEATHER:
{weather}

💬 QUOTE OF THE DAY:
{quote}

📌 FACT:
{fact}
"""

    return summary


# 5. SEND EMAIL
def send_email(summary):
    """Send the summary to Gmail."""

    sender = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_PASSWORD"]

    msg = MIMEText(summary)
    msg["Subject"] = "📊 Your Daily Pulse Summary"
    msg["From"] = sender
    msg["To"] = sender

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("📧 Email sent successfully!")


# 6. RUN BOT
def run():
    """Main entry point."""

    summary = build_summary()

    # Show output in terminal/GitHub Actions logs
    print(summary)

    # Save output to a file
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    # Send email
    send_email(summary)

    print("✅ Pulse ran successfully!")


# Start the program
if __name__ == "__main__":
    run()