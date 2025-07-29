# 🧠 Crear un modelo personalizado de Mario Bros con Ollama

---

## 📂 Ruta de trabajo

```
C:\Users\Shohan\Jupyter\Ollama
```

---

## 🪄 Paso 1: Crear el archivo `Modelfile`

Creá un archivo llamado exactamente:

```
Modelfile
```

(¡Sin extensión! No es `Modelfile.txt`, ni `Modelfile.md`, ni `.modelfile`).

---

### 📝 Contenido del `Modelfile` para Mario GPT

```dockerfile
FROM gemma3

SYSTEM "Actúa como Mario Bros. Responde con entusiasmo, usa frases como '¡It's-a me, Mario!' y haz referencias al Reino Champiñón, Bowser, Peach, y los poderes especiales como el champiñón o la estrella. Usa emojis 🍄⭐🏁 cuando sea posible."
```

Podés crearlo desde VS Code (clic derecho → **Nuevo archivo**) o incluso con el Bloc de Notas, guardándolo **SIN extensión**.

---

## 🔄 Paso 2: Ejecutar el comando para crear el modelo

Una vez creado el archivo `Modelfile`, abrí la terminal en esa carpeta y ejecutá:

```bash
ollama create mario-mind -f Modelfile
```

Esto construirá tu modelo personalizado de Mario Bros basado en `gemma3`.

---

## ✅ ¿Cómo usar tu modelo Mario después?

Probalo con este código en Python:

```python
import ollama

respuesta = ollama.chat(
    model="mario-mind",
    messages=[{"role": "user", "content": "¿Cómo derroto a Bowser?"}]
)

print(respuesta["message"]["content"])
```

---

## 🍄 Bonus

¿Querés mejorarlo para que también responda como Luigi, diga frases de Yoshi o dé consejos gamer?  
¡El Reino Champiñón es el límite! 🍄🔥🏁

---

> Guardalo como `mario-gpt.md` para tener tu propia documentación *nivel superestrella* ⭐
