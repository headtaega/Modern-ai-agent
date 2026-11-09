import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        work_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_dir_abs, file_path))
                
        if os.path.commonpath([work_dir_abs, target_dir]) != work_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        
        with open(target_dir, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes info(content) onto a specified file(file_path).",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path of the file to write to",
                },
                "content": {
                    "type": "string",
                    "description": "The text content to write to the file",
                },
            },
            "required": ["file_path", "content"]
        },
    },
}