from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create the chatbot
bot = ChatBot(
    "CollegeBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",  # Saves data locally
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation",
        },
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "I'm not sure how to answer that. Ask me about programming, math, or your project!",
            "maximum_similarity_threshold": 0.90,
        }
    ]
)

# Train with basic English + custom college-related Q&A
trainer_corpus = ChatterBotCorpusTrainer(bot)
trainer_corpus.train("chatterbot.corpus.english")

trainer_custom = ListTrainer(bot)
college_qa = [
    "What is this project about?", "It's a CLI chatbot built with Python for my college project!",
    "What can you do?", "I can answer questions about programming, math, and your project!",
    "Who created you?", "A brilliant CS student (you!) for their B.Tech project!",
    "Bye", "Goodbye! Good luck with your presentation! :)"
]
trainer_custom.train(college_qa)

# Chat interface
print("\n🤖 CollegeBot: Hi! I'm your CLI ChatBot. Type 'exit' to quit.\n")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("CollegeBot: See you later!")
            break
        response = bot.get_response(user_input)
        print(f"CollegeBot: {response}")
    except (KeyboardInterrupt, EOFError):
        break