# AI Q&A Bot - Intern Assignment Project

This project was built as part of an intern assignment. The goal was to build a very simple AI-powered app. 

This is a command-line application that takes a question from the user and uses the OpenAI API to provide an answer.

## Technologies and Tools Used

**Language:** Python
**Main Library:** `openai`
**API:** OpenAI API (`gpt-3.5-turbo` model)
**Environment Management:** `venv` (Python Virtual Environment)

## Installation and How to Run
To run this project on your local machine, follow these steps:

1.  **Clone this repository:**
    git clone https://github.com/your-username/ai-qa-bot.git
    cd ai-qa-bot
    
2.  **Create and activate a virtual environment:**
    
    # Create a virtual environment named 'venv'
    python -m venv venv

    # Activate it (on Windows)
       venv\Scripts\Activate
    

3.  **Install the open ai library:**
    pip install openai

4.  **Set the OpenAI API Key:**
    *   set API key as an environment variable:
        
        $env:OPENAI_API_KEY="original openai api key "
        
    *   Replace "original openai api key" with actual API key.

5.  **Run the application:**
    python app.py
    
    The bot is now ready to answer your questions! Type exit to quit.

## My Learning Journey and Challenges

I learned a lot while building this project. Here are some of the key takeaways:

1.  **Working with APIs:** This was my third time working directly with the OpenAI API.i already worked with gemini api key before in many projects.

2.  **The Environment Variable Problem:** First i directly make .env file and save api key here but i get this error "Error: The OPENAI_API_KEY environment variable is not set.
(venv) PS D:\ai-qa-bot> python app.py
Error: The OPENAI_API_KEY environment variable is not set."================but then i take the help of chatgpt and get the solution for this and change my way i.e., use this method----$env:OPENAI_API_KEY = " original key here "

3.  **The 500 Internal Server Error:** after run i got this error but its not the coding problem this is a temporary issue on the server's side. I waited a few minutes and tried again, and it worked! =================================================
(venv) PS D:\ai-qa-bot> python app.py
AI Q&A Bot is ready! Type 'exit' to quit.
You: hello
AI Q&A Bot is ready! Type 'exit' to quit.
You: hello
You: hello
AI: An error occurred: Error code: 500 - {'error': {'message': 'Internal server error', 'type': 'internal_error', 'param': None, 'code': 'internal_error'}}
You: exit

=============================================================================================================

this was a fantastic learning experience. I not only built a functional AI bot but also learned a great deal about APIs, environment variables, and debugging.
