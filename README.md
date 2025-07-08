# 🤖 Prompt-Based AI CLI Tool using Ollama

> A simple CLI-based application that allows users to send text prompts or input files to a local LLM (via Ollama), and receive intelligent responses. Designed to demonstrate interaction with local language models using command-line tools.

---

## 🧠 Overview

This tool provides a flexible interface for experimenting with LLM prompts using direct command-line input or from `.txt` files, and saving the output to a response file.

Supports:

- 💬 Prompt input directly or from text files
- 🧠 Uses locally running LLM via Ollama (`llama3` by default)
- 💾 Optional saving of output responses to files
- 🛠️ Minimal dependencies, runs entirely offline

---

## 🔍 Features

- 🧾 Accept prompt input via `--prompt` flag or `--file` path
- 📥 Reads prompt text from predefined folders
- 📤 Outputs the response to a file (optional)
- 🧠 Uses Ollama’s local inference engine for fast responses
- 🚫 No API key or external calls required

---

## 🛠️ Tech Stack

| Component   | Technology     |
|-------------|----------------|
| CLI Tool    | Python + argparse |
| LLM Engine  | Ollama (local) |
| Request API | `requests`     |

---

## 📁 Input/Output Folder Usage

- All prompt `.txt` files are placed in `input_prompts/`
- Output response files will be saved in `output_responses/`

You can customize file names using the `--file` and `--output` flags.

---

## 🚀 How to Run

### 🔸 Option A: Provide Prompt via CLI

```bash
python day4prompt.py "What is AI?"
```
### 🔸 Option B: Read Prompt from File and Save Output

```bash
python week1.py --file input_prompts/one_shot.txt --output output_responses/response.txt
```
### 🔸 Option C: Direct Prompt with Model and Custom Output

```bash
python week1.py --prompt "Explain quantum computing" --model llama3 --output output_responses/quantum.txt
```
