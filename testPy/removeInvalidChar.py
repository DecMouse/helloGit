import argparse
from pathlib import Path

#!/usr/bin/env python3
def read_utf8_ignore(path: str):
    """Open and read a text file using UTF-8, ignoring decoding errors."""
    p = Path(path)
    with p.open('r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def main():
    # parser = argparse.ArgumentParser(description="Read a text file with utf-8 ignoring errors")
    # parser.add_argument("file", help="Path to the text file to read")
    # args = parser.parse_args()

    content = read_utf8_ignore("/helloGit/testPy/test.txt")
    print(content)

if __name__ == "__main__":
    main()