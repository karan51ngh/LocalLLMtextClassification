import urllib.error
from promptConstants import *
import pandas as pd
from LocalLLMtextClassification import callLLMBinaryClassifier

def classify_advertisement(text: str) -> bool:

    host = "http://localhost:11434"
    model = "gpt-oss:20b" # model= "llama3.1:8b" or "gpt-oss:20b"

    try:
        label = callLLMBinaryClassifier(fewShotPrompt(text), host=host, model=model)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"Ollama API HTTPError {e.code}: {detail}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Ollama API connection error: {e}") from e
    except Exception as e:
        raise RuntimeError(f"Ollama API error: {e}") from e

    # Normalize and interpret the response
    label = label.replace("-", "_").strip()
    if label == "AD" or label.startswith("AD "):
        return True
    if label == "NOT_AD" or label.startswith("NOT"):
        return False
    # Fallback: default to not an ad if ambiguous
    return False

def classify_advertisement_log(text: str) -> str:
    try:
        result = classify_advertisement(text)
        print(f"[{'AD' if result else 'NOT_AD'}] {text}")
        print("\n")
        return 'AD' if result else 'NOT_AD'
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    input_file = 'csvFiles/linkedin_posts.csv'
    df = pd.read_csv(input_file)
    print(f"Classification started. Data loaded from '{input_file}'.")
    
    source_column_name = df.columns[0]
    df['processed_output'] = df[source_column_name].apply(classify_advertisement_log)
    output_file = 'csvFiles/output_data.csv'
    df.to_csv(output_file, index=False)

    print(f"Processing complete. Data saved to '{output_file}'.")