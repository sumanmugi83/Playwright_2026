import requests
import sys

def check_ollama(model_name="codellama"):
    url = "http://localhost:11434/api/tags"
    try:
        print(f"Checking Ollama connection at {url}...")
        response = requests.get(url)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [m['name'] for m in models]
            print("Ollama is RUNNING.")
            print(f"Available models: {model_names}")
            
            # Check for codellama (loose match for tags like codellama:latest)
            if any(model_name in name for name in model_names):
                print(f"[OK] Model '{model_name}' found.")
                return True
            else:
                print(f"[FAIL] Model '{model_name}' NOT found. Please run 'ollama pull {model_name}'")
                return False
        else:
            print(f"❌ Ollama returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Ollama. is it running? (http://localhost:11434)")
        return False
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return False

if __name__ == "__main__":
    success = check_ollama()
    if not success:
        sys.exit(1)
