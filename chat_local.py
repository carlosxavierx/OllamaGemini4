import requests
import sys

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma2:2b"


def obtener_respuesta(prompt):
    """Envía un prompt a Ollama y devuelve la respuesta del modelo."""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=30,
        )
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        return "Error: No se puede conectar con Ollama. ¿Está corriendo y accesible en localhost:11434?"
    except requests.exceptions.Timeout:
        return "Error: La petición a Ollama excedió el tiempo de espera (30 segundos)."
    except requests.exceptions.RequestException as e:
        return f"Error en la petición a Ollama: {e}"

    try:
        data = response.json()
    except ValueError:
        return "Error: La respuesta de Ollama no es un JSON válido."

    if "response" not in data:
        return "Error: La respuesta de Ollama no contiene el campo esperado 'response'."

    return data["response"]


def main():
    print("Chat local con Ollama")
    print("Escribe 'salir' para terminar\n")

    while True:
        try:
            prompt = input("Tú: ")
        except (EOFError, KeyboardInterrupt):
            print("\nSaliendo...")
            sys.exit(0)

        if prompt.lower() == "salir":
            break

        respuesta = obtener_respuesta(prompt)

        print(f"IA: {respuesta}\n")


if __name__ == "__main__":
    main()