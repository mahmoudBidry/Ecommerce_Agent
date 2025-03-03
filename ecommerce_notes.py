from typing import Optional
from llama_index.core.tools import FunctionTool
import os
from datetime import datetime

class EcommerceNotes:
    def __init__(self, notes_file: str = "customer_notes.txt"):
        self.notes_file = notes_file
        if not os.path.exists(self.notes_file):
            # Create empty file if it doesn't exist
            open(self.notes_file, 'a').close()

    def add_note(self, content: str, category: Optional[str] = "general") -> str:
        """Add a new customer service note."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_line = f"[{timestamp}] ({category}): {content}\n"
        
        with open(self.notes_file, 'a') as f:
            f.write(note_line)
        
        return f"Note saved successfully: {content}"

    def get_recent_notes(self, limit: int = 5) -> str:
        """Retrieve the most recent customer service notes."""
        try:
            with open(self.notes_file, 'r') as f:
                # Read all lines and get the last 'limit' lines
                lines = f.readlines()
                recent_notes = lines[-limit:] if lines else []
                
            if not recent_notes:
                return "No notes found."
            
            return "".join(recent_notes)
        except Exception as e:
            return f"Error reading notes: {str(e)}"

# Create notes tool
notes_manager = EcommerceNotes()

ecommerce_notes_tool = FunctionTool.from_defaults(
    fn=notes_manager.add_note,
    name="add_customer_note",
    description="Add a note about customer interactions, preferences, or issues. Args: content (the note text), category (optional: type of note)"
)

ecommerce_notes_query = FunctionTool.from_defaults(
    fn=notes_manager.get_recent_notes,
    name="get_recent_notes",
    description="Retrieve recent customer service notes. Args: limit (optional: number of notes to retrieve, default 5)"
)
