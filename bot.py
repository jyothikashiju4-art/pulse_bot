import requests
from datetime import date


# 1. WEATHER FUNCTION
def get_weather(city="Thiruvananthapuram"):
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Weather unavailable ({e})"


# 2. QUOTE FUNCTION
def get_quote():
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


# 3. BUILD SUMMARY
def build_summary():
    today = date.today().strftime("%A, %d %B %Y")

    weather = get_weather()
    quote = get_quote()

    summary = f"""
📅 DAILY SUMMARY - PULSE BOT ({today})

🌦 WEATHER:
{weather}

💬 QUOTE OF THE DAY:
{quote}
"""
    return summary


# 4. RUN FUNCTION (MAIN)
def run():
    summary = build_summary()

    print(summary)

    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("\n✅ Pulse ran successfully!")


if __name__ == "__main__":
    run()