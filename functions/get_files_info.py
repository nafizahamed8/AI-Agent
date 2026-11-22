import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path=os.path.abspath(working_directory)
        target_dir=os.path.normpath(os.path.join(absolute_path,directory))
        valid_target_dir=os.path.commonpath([absolute_path,target_dir])==absolute_path
        # for dir in target_dir:
        #     if os.path.isdir(dir):
        #         content=os.listdir(dir)
        #         size=os.path.getsize(dir)
        #         name=os.path.dirname(dir)
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        dir_list=[]
        for name in os.listdir(target_dir):
                # print(name)
                path_join=os.path.join(target_dir,name)
                size =os.path.getsize(path_join)
                # print(size)
                content=os.path.isdir(path_join)
                line = f"- {name}: file_size={size} bytes, is_dir={content}"
                dir_list.append(line)
        return "\n".join(dir_list)
        
    except Exception as e:
        return f"Error: {e}"
    
    # for dir in target_dir:
    #     if dir==directory:
    #         content=os.listdir(dir)


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}