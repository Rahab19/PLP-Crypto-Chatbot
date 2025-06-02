# Chatbot Name and Tone
BOT_NAME = "CryptoBuddy"
BOT_TONE = "Hey there! I’m CryptoBuddy — your friendly crypto sidekick! Let’s find you a green and growing coin!"

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

def analyze_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"{BOT_NAME}: Invest in {recommend}! It’s eco-friendly and has long-term potential!"
   
    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"{BOT_NAME}: These coins are trending up : {', '.join(trending)}"
    
    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"{BOT_NAME}: {coin} is trending up and has a top-tier sustainability score!"
        return f"{BOT_NAME}: Hmm, nothing's a perfect match now. Try again later!"

    elif "energy" in user_query:
        low_energy = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        return f"{BOT_NAME}: These coins use low energy: {', '.join(low_energy)}"

    elif "recommend" in user_query or "should i buy" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                return f"{BOT_NAME}: {coin} is profitable right now — rising trend and strong market cap!"
        return f"{BOT_NAME}: No high-cap coin is booming right now, check back later!"

    elif "all" in user_query or "data" in user_query:
        response = f"{BOT_NAME}: Here's the current crypto snapshot:\n"
        for coin, data in crypto_db.items():
            response += f"- {coin}: Trend={data['price_trend']}, Market Cap={data['market_cap']}, Energy={data['energy_use']}, Sustainability={data['sustainability_score'] * 10:.0f}/10\n"
        return response

    else:
        return f"{BOT_NAME}: I didn’t get that Try asking about trends, sustainability, or energy use!"


def run_chat():
    print(BOT_TONE)
    print("Type 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print(f"{BOT_NAME}: See you next time! Remember — crypto is risky, always DYOR! ")
            break
        response = analyze_query(user_input)
        print(response)

if __name__ == "__main__":
    run_chat()

