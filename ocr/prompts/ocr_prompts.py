PROMPTS = {
    "total_amount": {
        "prompt": "Can you please read the total amount on the invoice.",
        "json_display": "total_amount",
    },
    "total_amount_vat": {
        "prompt": "Can you please read VAT amount paid on the invoice.",
        "json_display": "total_amount_vat",
    },
    "currency": {
        "prompt": "Can you please read currency of the invoice paid amount.",
        "json_display": "currency",
    },
    "invoice_number": {
        "prompt": "Can you please read the invoice number of the invoice.",
        "json_display": "invoice_number"
    },
    "invoice_issue_date": {
        "prompt": "Can you please read the invoice issue date.",
        "json_display": "invoice_issue_data"
    },
    "invoice_due_date": {
        "prompt": "Can you please read the invoice due date.",
        "json_display": "invoice_due_data"
    },
    "invoice_items": {
        "prompt": "Can you please read the invoice item and the following description <KEY>description</KEY>, amount <KEY>amount</KEY>, price <KEY>price</KEY>.",
        "json_display": "invoice_items"
    }, 
    "invoice_my_comapny": {
        "prompt": "Can you please read the invoice company that sent the invoice and the following company name <KEY>company_name</KEY>, full address <KEY>full_address</KEY>, email<KEY>email</KEY>, city <KEY>city</KEY>",
        "json_display": "invoice_my_company"
    },
    "invoice_billed_company": {
        "prompt": "Can you please read the invoice company that was billed in the invoice and the following company name <KEY>company_name</KEY>, full address <KEY>full_address</KEY>, email<KEY>email</KEY>, city <KEY>city</KEY>",
        "json_display": "invoice_billed_company"
    },
}

PROMPTS_TO_EXTRACT = ["total_amount", "total_amount_vat", "currency", "invoice_number", "invoice_issue_date", "invoice_due_date",
"invoice_items", "invoice_my_comapny", "invoice_billed_company"]

def read_prompt(prompt: str) -> str:
    return f"{PROMPTS[prompt]['prompt']}. <KEY>{PROMPTS[prompt]['json_display']}</KEY>" 

def read_prompts() -> str:
    if PROMPTS_TO_EXTRACT.__len__() == 0: return ""

    prompts: str = ""
    for extract_prompt in PROMPTS_TO_EXTRACT:
        prompts += "\n" + read_prompt(extract_prompt)
    return prompts