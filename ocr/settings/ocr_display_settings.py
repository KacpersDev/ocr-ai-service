from dataclasses import dataclass

@dataclass
class DisplaySettings:
    preferred_currency: str
    fields_to_extract: list[str]