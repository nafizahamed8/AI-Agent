import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    
    try:
        absolutepath2=os.path.abspath(working_directory)
        target_file_path=os.path.normpath(os.path.join(absolutepath2,file_path))
        validate_file_path=os.path.commonpath([absolutepath2,target_file_path])==absolutepath2
        if not validate_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file_path.endswith('py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file_path]
        if args is not None:
            command.extend(args)
        
        result=subprocess.run(command,cwd=absolutepath2,capture_output=True,text=True,timeout=30)
        output = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            return "No output produced"
        if result.stdout:
            output.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr}")
        return "\n".join(output)
    except Exception as e:
         return f"Error: executing Python file: {e}"

schema_run_python_file ={
    "type": "function",
    "function":{
        "name": "run_python_file",
        "description": "safely runs a Python file inside the permitted working "
        "directory, with a 30-second timeout, and returns its output errors and exit status as a string the LLM can read and respond to",
        "parameters":{
            "type":"object",
            "properties": {
                "file_path":{"type":"string",
                             "description":"Path to the file, relative to the working directory"},
                "args":{"type":"array",
                        "description":"Command line argument and they are optional",
                        "items":{"type":"string"}},
                
                
            },
            "required":["file_path",]
        },
    },
}
