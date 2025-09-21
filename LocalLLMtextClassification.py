import json
from urllib import request, error


def ask_gpt_oss(prompt: str, model: str = "gpt-oss:20b", host: str = "http://localhost:11434", timeout: int = 60) -> str:
    url = f"{host.rstrip('/')}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # simplify: get a single JSON response
    }
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(url, data=data, headers={"Content-Type": "application/json"})

    try:
        with request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            obj = json.loads(body.decode("utf-8"))
            return obj.get("response", "")
    except error.HTTPError as e:
        try:
            detail = e.read().decode("utf-8", errors="ignore")
        except Exception:
            detail = ""
        raise RuntimeError(f"Ollama HTTP error {e.code}: {detail}") from e
    except error.URLError as e:
        raise RuntimeError(f"Failed to reach Ollama at {url}: {e.reason}") from e


if __name__ == "__main__":
    import sys
    user_prompt = "Write a one-sentence summary about running LLMs locally."
    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
    
    # model= "llama3.1:8b" or "gpt-oss:20b"
    print(ask_gpt_oss(user_prompt, model="llama3.1:8b"))
