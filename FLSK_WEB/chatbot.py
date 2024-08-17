class Chatbot:
    def __init__(self):
        # Initialize a dictionary to map questions to responses
        self.responses = {
            "hello": "Hello! How can I help you today?",
            "What is your name?": "I am SnowyChatbot!",
            "How are you?": "I'm just a program, but I'm doing great!",
            "What can you do?": "I can answer simple questions.",
            "What is the weather like?": "I don't have access to real-time data.",
            "What is your favorite color?": "I don't have preferences, but I like all colors equally!",
            "hi": "Hello! How can I help you today?",
            "hey": "Hello! How can I help you today?",
            "who are you?": "I am Snowy, made by NISHA. I am here to help you with questions about girls' well-being.",
            "how old are you?": "I don't have an age, but I'm here to support you!",
            "what do you do?": "I'm a chatbot designed to provide information about girls' well-being.",
            "what is self-care?": "Self-care is taking care of your physical, emotional, and mental health. It's essential for maintaining a healthy lifestyle.",
            "how can girls stay healthy?": "Health is most important, if health is good, you could achieve anything. Some tips for staying healthy include getting enough sleep, eating a balanced diet, exercising regularly, and practicing self-care.",
            "why is education important for girls?": "Education empowers girls with knowledge and opportunities for the future. It helps them develop critical thinking skills, build confidence, and pursue their passions.",
            "why should girls have hobbies?": "Hobbies provide fun and help develop new skills. They also promote social connections and self-expression.",
            "goodbye": "Goodbye! Have a great day!",
            "bye": "Goodbye! Have a great day!",
            "see you": "Goodbye! Have a great day!"
        }

    def get_response(self, message):
        # Convert the message to lowercase to make the matching easier
        message = message.lower()

        # Check if the message is a question and has a corresponding response
        if message in self.responses:
            return self.responses[message]

        # Default response
        else:
            return "I'm not sure how to respond to that. Can you ask something else?"