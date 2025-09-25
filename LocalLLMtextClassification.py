import json
from urllib import request, error
import urllib

def callLLMBinaryClassifier(prompt: str, model: str = "gpt-oss:20b", host: str = "http://localhost:11434", timeout: int = 60) -> str:
    url = f"{host.rstrip('/')}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False, # simplify: get a single JSON response
        "options": {
            "temperature": 0
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers={"Content-Type": "application/json"})
    
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
    }

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read()
    parsed = json.loads(body.decode("utf-8"))
    content = parsed.get("response", "")
    return str(content).strip().upper()


# if __name__ == "__main__":
#     import sys
#     user_prompt = "Write a one-sentence summary about running LLMs locally."
#     if len(sys.argv) > 1:
#         user_prompt = " ".join(sys.argv[1:])
    
#     # model= "llama3.1:8b" or "gpt-oss:20b"
#     print(callOllamaClassifier(user_prompt, model="llama3.1:8b"))
