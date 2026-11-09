import os
from config import CHAR_LIMIT

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        work_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_dir_abs, file_path))
            
        if os.path.commonpath([work_dir_abs, target_dir]) != work_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_dir, "r") as f:
            file_content_str = f.read(CHAR_LIMIT)
            if f.read(1):
                file_content_str += f'[...File "{file_path}" truncated at {CHAR_LIMIT} characters]'
        return file_content_str

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Gives the contents of the file or files specified",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path(file_path) where you get the content from.",
                },
            },
            "required": ["file_path"]
        },
    },
}