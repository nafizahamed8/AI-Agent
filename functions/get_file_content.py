import os
from config import MAX_CHARS
def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        absolute_path1=os.path.abspath(working_directory)
        target_path=os.path.normpath(os.path.join(absolute_path1,file_path))
        valid_file_path=os.path.commonpath([absolute_path1,target_path])==absolute_path1
        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        

        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        
        # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string+=f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"

schema_get_file__content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Read the content of the file path and read truncated characters when the file is very long",
        "parameters": {
            "type": "object",
            "properties": {
                # "working_directory": {
                #     "type": "string",
                #     "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                # },
                "file_path":{"type":"string",
                             "description":"Path to the file, relative to the working directory"},
                
            },
            "required":["file_path"]
        },
    },
}
