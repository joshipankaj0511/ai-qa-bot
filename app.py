import os
import openai

try:
    openai.api_key = os.environ["OPENAI_API_KEY"]
except KeyError:
    print("Error: The OPENAI_API_KEY environment variable is not set.")
    exit()

def ask_ai(question):
    """
    This function takes a question, sends it to the OpenAI API,
    and returns the assistant's reply.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to run the chatbot loop.
    """
    print("AI Q&A Bot is ready! Type 'exit' to quit.")
    while True:
        user_question = input("You: ")
        if user_question.lower() == 'exit':
            print("Goodbye!")
            break
        ai_response = ask_ai(user_question)
        print(f"AI: {ai_response}")

if __name__ == "__main__":
    main()
