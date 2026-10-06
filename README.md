# Chat Local con Ollama y Gemma 2B

Práctica académica de la asignatura de ASIX (Accesos a Datos y Ficheros). 
El objetivo es crear un chat local que se conecta a un modelo de IA mediante Ollama.

## Descripción

Esta práctica consiste en un script Python que permite interactuar con un modelo de lenguaje 
local a través de Ollama. El modelo utilizado es **Gemma 2B** (`gemma2:2b`).

## Por qué no se usa Azure

No se utilizó Microsoft Azure OpenAI debido a restricciones corporativas del entorno 
universitario que impiden el acceso a servicios externos. Por ello, se optó por una solución 
local con Ollama.

## Requisitos previos

- Python 3.12 o superior
- Ollama instalado y configurado en el equipo local
- Modelo Gemma 2B descargado (`gemma2:2b`)

## Instalación

1. Clonar este repositorio
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Iniciar Ollama y asegurarse de que el modelo esté disponible

## Uso

Ejecutar el script de chat:

```bash
python chat_local.py
```

El chat iniciará y mostrará el prompt `Tú:`. Escriba `salir` para terminar la conversación.

## Funcionalidades

- Conexión local a Ollama en `http://localhost:11434/api/generate`
- Interacción por consola con el modelo Gemma 2B
- Salida formateada de las respuestas de la IA