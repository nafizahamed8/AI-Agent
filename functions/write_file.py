import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolute_path2=os.path.abspath(working_directory)
        targeted_path=os.path.normpath(os.path.join(absolute_path2,file_path))
        valid_targeted_path=os.path.commonpath([absolute_path2,targeted_path])==absolute_path2
        if not valid_targeted_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(targeted_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        dir_name=os.path.dirname(targeted_path)
        new_dir=os.makedirs(dir_name,exist_ok=True)

        with open(targeted_path,"w") as f:
            file_content_write=f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
schema_write_file= {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "safely creates or overwrites a file within an allowed working directory and returns an informational status string for the AI agent",
        "parameters": {
            "type": "object",
            "properties": {
                
                "file_path":{"type":"string",
                             "description":"Path to the file, relative to the working directory"},
                "content":{"type":"string",
                           "description":"The full text to write to the file,the file is created if it doesn't exist"}
                
            },
            "required":["file_path","content"]
        },
    },
}
