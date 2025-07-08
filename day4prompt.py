import argparse
import requests
import json
import sys

def generate_response(prompt, model='llama3'):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            print("\Model Response:")
            print(result["response"])
        else:
            print(f"\Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"\nException occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send prompt to Ollama LLM")
    parser.add_argument("prompt", type=str, help="The prompt to send to the LLM")
    parser.add_argument("--model", type=str, default="llama3", help="The name of the Ollama model to use")
    
    args = parser.parse_args()
    generate_response(args.prompt, args.model)
