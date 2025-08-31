def sport_to_emoji(sport: str) -> str:
    sports_emojis = {
        "football": "⚽",
        "cricket": "🏏",
        "swimming": "🏊",
        "running": "🏃",
        "cycling": "🚴",
        "badminton": "🏸"
    }
    return sports_emojis.get(sport, "Emoji not available")


user_input = input("Enter a sport name: ")
print("Emoji:", sport_to_emoji(user_input))
