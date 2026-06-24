PROMPTS = {
    "total_amount": {
        "prompt": f"Can you please read the total amount on the invoice.",
        "json_display": "total_amount",
    },
    "total_amount_vat": {
        "prompt": f"Can you please read VAT amount paid on the invoice.",
        "json_display": "total_amount_vat",
    },
    "currency": {
        "prompt": f"Can you please read currency of the invoice paid amount.",
        "json_display": "currency",
    },
}

PROMPTS_TO_EXTRACT = ["total_amount", "total_amount_vat", "currency"]

def read_prompt(prompt: str) -> str:
    return f"{PROMPTS[prompt]['prompt']}. <KEY>{PROMPTS[prompt]['json_display']}</KEY>" 

def read_prompts() -> str:
    if PROMPTS_TO_EXTRACT.__len__() == 0: return ""

    prompts: str = ""
    for extract_prompt in PROMPTS_TO_EXTRACT:
        prompts += "\n" + read_prompt(extract_prompt)
    return prompts