from ocr import run

AI_MODEL = "qwen2.5vl:3b"
CTX = 8192

try:
  response = run(model=AI_MODEL, ctx=CTX)
  print(response['message']['content'])
except ConnectionError:
  print("Error happened while connecting to Ollama. [Ollama isn't running.]")