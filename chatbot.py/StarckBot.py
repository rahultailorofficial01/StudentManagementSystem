import openai

# Set your OpenAI API key
openai.api_key = "your-api-key"
# Replace with your actual API key

def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use other engines like text-davinci-002 or gpt-4
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def chat():
    print("Starck: Hello, I am Starck, your AI chatbot!")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Starck: Goodbye! Have a nice day!")
            break
        
        prompt = f"User: {user_input}\nStarck:"
        response = get_response(prompt)
        print(f"Starck: {response}")

if "__name__" == "__main__":
    chat()