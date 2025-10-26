import random

# ---------------------------------------------
# Title: Fake Funny Joke Generator
# Author: Pratiksha Bhagat (Example)
# Description:
# This program generates random funny one-liners
# based on the category chosen by the user.
# ---------------------------------------------

# Dictionary of categories and their joke parts
categories = {
    "sports": {
        "characters": [
            "A cricket umpire",
            "A lazy footballer",
            "A confused coach",
            "A gym trainer who hates running",
            "An overconfident chess player",
        ],
        "actions": [
            "forgets the score",
            "starts dancing instead of warming up",
            "argues with the scoreboard",
            "celebrates before scoring",
            "mistakes the ball for lunch",
        ],
        "situations": [
            "during a world cup match",
            "in front of the audience",
            "on live TV",
            "inside the stadium",
            "while giving an interview",
        ],
    },

    "school": {
        "characters": [
            "A sleepy student",
            "A strict principal",
            "A talkative teacher",
            "A confused topper",
            "A backbencher with big dreams",
        ],
        "actions": [
            "forgets their homework",
            "tries to escape during the exam",
            "writes a love letter on answer sheet",
            "calls the teacher 'mom' by mistake",
            "uses calculator in English test",
        ],
        "situations": [
            "in the morning assembly",
            "during the parent-teacher meeting",
            "while giving a presentation",
            "inside the principal's office",
            "on the first day of school",
        ],
    },

    "fun": {
        "characters": [
            "A dancing robot",
            "A talking banana",
            "A lazy panda",
            "An angry mosquito",
            "A singing potato",
        ],
        "actions": [
            "joins a yoga class",
            "starts rapping in traffic",
            "tries to open the fridge with Wi-Fi",
            "argues with Alexa",
            "starts a TikTok live in the jungle",
        ],
        "situations": [
            "during a power cut",
            "on a Zoom call",
            "at midnight",
            "inside a shopping mall",
            "while cooking noodles",
        ],
    },

    "games": {
        "characters": [
            "A gamer with no internet",
            "A PUBG champion",
            "A chess grandmaster’s cat",
            "A racing driver with motion sickness",
            "A kid with unlimited lives",
        ],
        "actions": [
            "throws the controller in anger",
            "plays hide and seek in real life",
            "tries to pause a live match",
            "calls mom for extra XP",
            "screams 'headshot' in public",
        ],
        "situations": [
            "during an online tournament",
            "inside a gaming cafe",
            "while losing connection",
            "in front of parents",
            "while wearing VR glasses",
        ],
    },
}

# ---------------------------------------------
# Main Joke Generator Loop
# ---------------------------------------------
print("😂 Welcome to the Fake Funny Joke Generator!")
print("Available categories: sports, school, fun, games")

while True:
    # Ask user for a category
    category = input("\nEnter a category (or 'exit' to quit): ").strip().lower()

    if category == "exit":
        print("\nThanks for using the Fake Funny Joke Generator! 🤣")
        break

    # Check if category exists
    if category not in categories:
        print("❌ Invalid category! Please choose from sports, school, fun, or games.")
        continue

    # Pick random parts of the joke
    character = random.choice(categories[category]["characters"])
    action = random.choice(categories[category]["actions"])
    situation = random.choice(categories[category]["situations"])

    # Generate and print the funny joke
    joke = f"😂 {character} {action} {situation}!"
    print("\n" + joke)

    # Ask if the user wants another one
    again = input("\nDo you want another joke? (yes/no): ").strip().lower()
    if again == "no":
        print("\nThanks for laughing with us! 😂")
        break
