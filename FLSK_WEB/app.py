from flask import Flask, render_template, request  # Import Flask and tools
from chatbot import Chatbot  # Import your chatbot from chatbot.py

app = Flask(__name__)  # Start your Flask app

chatbot = Chatbot()  # Create your chatbot

@app.route('/', methods=['GET', 'POST'])  # When someone visits your site
def home():
    if request.method == 'POST':  # If they send a message
        user_input = request.form['message']  # Get the message
        response = chatbot.get_response(user_input)  # Get the chatbot's response
        return render_template('home_page.html', user_input=user_input, response=response)  # Show the message and response
    return render_template('home_page.html')  # Just show the page if no message


@app.route('/contact_page.html')
def contact():
    # return "hello this is the home page"
    return render_template('contact_page.html')

@app.route('/About_page.html')
def about():
    # return "hello this is the home page"
    return render_template('About_page.html')

@app.route('/application_page.html')
def application():
    # return "hello this is the home page"
    return render_template('application_page.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')  # Start the app
