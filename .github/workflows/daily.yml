import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def get_news():
    api_key = os.environ["NEWS_API_KEY"]
    url = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=10&apiKey={api_key}"

    response = requests.get(url, timeout=10)
    data = response.json()

    articles = data["articles"]
    return articles

def build_html(articles):
    today = datetime.now().strftime("%A, %d %B %Y")

    html = f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: auto;">
        <h2 style="color: #e63946;">📰 Daily News Summary</h2>
        <p style="color: gray;">{today}</p>
        <hr>
    """

    for i, article in enumerate(articles[:10], 1):
        title = article.get("title", "No title")
        source = article["source"].get("name", "Unknown")
        url = article.get("url", "#")
        published = article.get("publishedAt", "")[:10]

        html += f"""
        <div style="margin-bottom: 20px; padding: 10px; border-left: 4px solid #e63946;">
            <h3 style="margin: 0;">
                <a href="{url}" style="color: #1d3557; text-decoration: none;">
                    {i}. {title}
                </a>
            </h3>
            <p style="color: gray; margin: 5px 0;">
                📌 {source} &nbsp;|&nbsp; 📅 {published}
            </p>
        </div>
        """

    html += """
        <hr>
        <p style="color: gray; font-size: 12px;">
            Sent by Pulse Bot 🤖
        </p>
    </body>
    </html>
    """
    return html

def send_email(html):
    sender = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_PASSWORD"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📰 Your Daily News Summary"
    msg["From"] = sender
    msg["To"] = sender

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("📧 News email sent!")

def run():
    print("Fetching news...")
    articles = get_news()
    print(f"Got {len(articles)} articles")

    html = build_html(articles)
    send_email(html)
    print("✅ News bot ran successfully!")

if __name__ == "__main__":
    run()