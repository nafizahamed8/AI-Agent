# def main():
#     print("Hello from ai-agent!")


# if __name__ == "__main__":
#     main()

import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions
# import json
from call_function import call_function
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt",type=str,help="User prompt")
parser.add_argument("--verbose",action="store_true",help="Enable verbose output")
args = parser.parse_args()
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError ("No api key")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
# user_prompt="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
# Now we can access `args.user_prompt`
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]
for _ in range(20):
    # call the model, handle responses, etc.
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    tools=available_functions
)
    if not response.usage:
        raise RuntimeError ("No Usage")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    # print("Response:"
    message=response.choices[0].message
    messages.append(message)
    if message.tool_calls:
        for tool_call in message.tool_calls:
            # function_args = json.loads(tool_call.function.arguments or "{}")
            result_message=call_function(tool_call=tool_call,verbose=args.verbose)
            messages.append(result_message)
            
            
            if not result_message["content"]:
                raise Exception ("content is empty")
            
            
            if args.verbose:
                print(f"-> {result_message['content']}")
            
            
            
            
    
    else:
        print(response.choices[0].message.content)
        break
else:
    print("Agent reached the maximum number of iterations without a final response")
    sys.exit(1)


    
        
    

