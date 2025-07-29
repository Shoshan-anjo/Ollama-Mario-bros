import requests

res = requests.post("http://localhost:11434/api/generate", json={
    "model": "gemma3",
    "prompt": "Dame un resumen de lo que hace un servidor HTTP.",
    "stream": False
})

print(res.json()["response"])
