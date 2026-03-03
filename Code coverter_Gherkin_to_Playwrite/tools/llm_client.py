import requests
import json
import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

def generate_text(prompt, model="codellama", valid_json=False):
    """
    Generates text using the local Ollama instance.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2  # Low temperature for code generation
        }
    }
    
    if valid_json:
        payload["format"] = "json"

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
    except requests.exceptions.RequestException as e:
        print(f"Error calling Ollama: {e}")
        return None

if __name__ == "__main__":
    # Test
    print("Testing LLM Client...")
    res = generate_text("Write a hello world function in TypeScript")
    print(res)
