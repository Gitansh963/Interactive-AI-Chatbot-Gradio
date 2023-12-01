import openai
import gradio as gr

# Set your OpenAI API key
# If you have OpenAI API key as a string, enable the below
openai.api_key = "Copy-your-api-key-here"

# Define conversation start and restart sequences
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

# Initial conversation prompt
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

# Function to interact with the OpenAI API and generate responses
def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=0.9,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

# Function to maintain conversation history and generate responses
def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

# Gradio interface setup
block = gr.Blocks()

# Uncomment the line below to run the Gradio interface
# block.launch(chatgpt_clone, inputs=["text", "text"], outputs="text")
