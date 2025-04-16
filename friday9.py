from openai import OpenAI
from dotenv import load_dotenv
import os
import tkinter as tk

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

# Create the client
client = OpenAI()

# Define the function to handle submit
def get_completion():
    user_prompt = prompt_entry.get()
    
    if not user_prompt.strip():
        output_text.set("Please enter a prompt.")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_prompt}]
        )
        output_text.set(response.choices[0].message.content)
    except Exception as e:
        output_text.set(f"Error: {e}")

# GUI setup
root = tk.Tk()
root.title("OpenAI Chat Prompt")

# Prompt input
tk.Label(root, text="Enter your prompt:").pack(pady=(10, 0))
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=get_completion)
submit_button.pack(pady=5)

# Output area
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, wraplength=400, justify="left")
output_label.pack(pady=10)

# Run the app
root.mainloop()






















