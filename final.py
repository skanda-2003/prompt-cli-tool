import argparse
import requests
import json
import sys
import os

def read_prompt(prompt=None, file=None):
    if prompt:
        return prompt
    elif file:
        if not os.path.exists(file):
            print(f"\nFile '{file}' not found.")
            sys.exit(1)
        with open(file, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        print("\nNo prompt or file provided. Use --prompt or --file.")
        sys.exit(1)

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
            return result["response"]
        else:
            print(f"\nError {response.status_code}: {response.text}")
            sys.exit(1)
    except Exception as e:
        print(f"\nException occurred: {e}")
        sys.exit(1)

def write_output(response, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response)
        print(f"\nOutput written to {output_file}")
    except Exception as e:
        print(f"\nFailed to write to file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send prompt or file to Ollama and save output to file")
    parser.add_argument("--prompt", type=str, help="Prompt text to send to the LLM")
    parser.add_argument("--file", type=str, help="Path to text file containing prompt (relative to input_prompts/)")
    parser.add_argument("--model", type=str, default="llama3", help="Model name to use (default: llama3)")
    parser.add_argument("--output", type=str, default="output_responses/output.txt", help="Output file path (default: output_responses/output.txt)")

    args = parser.parse_args()

    prompt_text = read_prompt(args.prompt, args.file)
    response = generate_response(prompt_text, args.model)
    write_output(response, args.output)
