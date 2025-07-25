import os
from langchain_ollama import OllamaLLM

def main():
    print("\n🤖 LLM Starter Agent (Ollama CLI)")
    print("Type 'exit' to quit.\n")

    # Initialize LLM
    llm = OllamaLLM(model="qwen2.5:1.5b")  # selects the model for ollama to use
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Exiting. Goodbye!")
            break

        response = llm.invoke(user_input) # sends http call to ollama, and gets response
        print(f"LLM: {response}\n")

if __name__ == "__main__":
    main()