import ollama
x = input("Escribe algo: ")
respuesta = ollama.chat(
    model="mario-bros",
    messages=[{"role": "user", "content": x}]
)

print(respuesta["message"]["content"])
