import ollama

from prompts.ocr_prompts import read_prompts
from settings.ocr_display_settings import DisplaySettings
from ollama import ChatResponse

display_settings = DisplaySettings("PLN", [])

def run(model: str, ctx = 8192, role = "user") -> ChatResponse:
    response = ollama.chat(model=model, messages=[
        {
            'role': role,
            'content': 
            f"""
            DESCRIPTION:
            The image file I have provided is an INVOICE. 
            Read the entire document before extracting values.
            Use only information visible in the document.

            {read_prompts()}

            RULES:
            1. Return only VALID JSON, no markdown, no explanation, no code.
            2. Numbers must be json numbers not strings
            3. Keys for json objects can be found within <KEY></KEY> tag
            4. Do not change any content found in <KEY></KEY> tag.
            6. If a field is missing return 'not found'
            7. Do not change any data, which were found on invoice.
            8. Always return data as they are
            9. Watch out for dots or commas in amounts.
            10. If you are being asked for couple results within one line in prompt please return them as a dictonary within the <KEY> provided.
            """,
            'images': {
                "test.jpg"
            }
        }
    ], options={"num_ctx": ctx})
    
    return response;