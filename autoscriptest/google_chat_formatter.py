from dataclasses import dataclass

@dataclass
class GoogleChatMessage:
    text: str

def format_google_chat_message(google_chat_message: GoogleChatMessage) -> str:
    """
    Format a Google Chat message using Markdown syntax
    """
    return f"