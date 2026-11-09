import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        work_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_dir_abs, file_path))
                    
        if os.path.commonpath([work_dir_abs, target_dir]) != work_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]
        if args:
            command.extend(args)

        completed_process = subprocess.run(command, text=True, timeout=30, 
        capture_output=True, cwd=work_dir_abs)
        final_str = ""

        if completed_process.returncode != 0:
            final_str += f"Process exited with code {completed_process.returncode}"

        if not completed_process.stdout and not completed_process.stderr:
            final_str += "No output produced"
        else:
            if completed_process.stdout:
                final_str += f"STDOUT: {completed_process.stdout}"
            
            if completed_process.stderr:
                final_str += f"STDERR: {completed_process.stderr}"
            
        return final_str
        
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a specified python file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path of the file to run the code",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "optional arguments",
                }
            },
            "required": ["file_path"]
        },
    },
}