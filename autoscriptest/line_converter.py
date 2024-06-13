from dataclasses import dataclass

@dataclass
class LineMessage:
    text: str

def convert_line_message(line_message: LineMessage) -> str:
    """
    Convert a Line message to a string
    """
    return line_message.text.replace("\n", "  \n")