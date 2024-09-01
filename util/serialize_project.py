"""
Utility that serializes the entire project (all .cpp in src and .h in include) as one large string
with filenames included.

Intention is to allow for faster turnaround speed when using LLMs, at least once the project is small,
once it gets bigger I'd need some kind of filtering mechanism, maybe only including function names,
filtering for specific regex matching names and the like.

This is closely related to some CLI tools I've developed for exploring and parsing the AST of python projects

https://github.com/Daniel-Sinkin/ds_util/
"""

import os

import pyperclip
import tiktoken
from termcolor import colored


def serialize_files(directory, extension):
    serialized_content = f"###\n# {directory.upper()} FOLDER\n###\n\n"
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    content = f.read()
                    serialized_content += f"###\n# {file}\n###\n"
                    serialized_content += content + "\n\n"
    return serialized_content


def main():
    # Directories to serialize
    src_dir = "src"
    include_dir = "include"

    # Serialize .cpp files in src and .h files in include
    serialized_string = serialize_files(src_dir, ".cpp")
    serialized_string += serialize_files(include_dir, ".h")

    # Copy to clipboard
    pyperclip.copy(serialized_string)

    # Count number of lines
    num_lines = len(serialized_string.splitlines())

    # Tokenization using tiktoken
    encoding = tiktoken.encoding_for_model("gpt-4")  # Use the GPT-4 tokenizer
    num_tokens = len(encoding.encode(serialized_string))

    # Check if more than 50% of the token limit is reached
    token_limit = 8192  # Assuming GPT-4 Standard with 8k tokens
    if num_tokens > token_limit / 2:
        print(
            colored(
                f"Warning: You have reached {num_tokens} tokens out of {token_limit}. This is more than 50% of the limit.",
                "red",
            )
        )
    else:
        print(f"Number of tokens: {num_tokens}")

    # Print the number of lines copied to the clipboard
    print(f"Number of lines copied to clipboard: {num_lines}")


if __name__ == "__main__":
    main()
