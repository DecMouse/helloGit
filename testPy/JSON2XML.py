from typing import Any, Optional
import json
import argparse
import sys
from xml.sax.saxutils import escape as _escape

#!/usr/bin/env python3
"""
JSON2XML.py

Utility to convert a Python JSON-like object to XML.

Provides:
- json_to_xml(obj, root_name='root', indent=None) -> str

Usage (CLI):
    python JSON2XML.py input.json -o output.xml --root data --indent 2
If no input file is provided, reads JSON from stdin.
"""



def json_to_xml(obj: Any, root_name: str = "root", indent: Optional[int] = None) -> str:
        """
        Convert a JSON-like Python object to an XML string.

        Parameters:
        - obj: dict/list/primitive representing JSON.
        - root_name: name of the outermost XML element.
        - indent: number of spaces for pretty printing. If None, output is compact.

        Behavior:
        - dict keys become child element names.
        - list values produce repeated child elements with the same key name.
        - None is rendered as an empty element (<tag/>).
        - Strings are XML-escaped.
        """
        def to_compact(value: Any, tag: str) -> str:
                if isinstance(value, dict):
                        inner = "".join(to_compact(v, k) for k, v in value.items())
                        return f"<{tag}>{inner}</{tag}>"
                if isinstance(value, list):
                        return "".join(to_compact(item, tag) for item in value)
                if value is None:
                        return f"<{tag}/>"
                return f"<{tag}>{_escape(str(value))}</{tag}>"

        lines = []

        def append_pretty(value: Any, tag: str, level: int) -> None:
                pad = " " * (indent * level)
                if isinstance(value, dict):
                        lines.append(f"{pad}<{tag}>")
                        for k, v in value.items():
                                append_pretty(v, k, level + 1)
                        lines.append(f"{pad}</{tag}>")
                        return
                if isinstance(value, list):
                        for item in value:
                                append_pretty(item, tag, level)
                        return
                if value is None:
                        lines.append(f"{pad}<{tag}/>")
                        return
                lines.append(f"{pad}<{tag}>{_escape(str(value))}</{tag}>")

        if indent is None:
                return to_compact(obj, root_name)
        append_pretty(obj, root_name, 0)
        return "\n".join(lines)


def _main():
        parser = argparse.ArgumentParser(description="Convert JSON to XML")
        parser.add_argument("input", nargs="?", help="Input JSON file (default: stdin)")
        parser.add_argument("-o", "--output", help="Output XML file (default: stdout)")
        parser.add_argument("--root", default="root", help="Root element name (default: root)")
        parser.add_argument("--indent", type=int, default=None,
                                                help="Number of spaces for indentation (default: compact)")
        args = parser.parse_args()

        if args.input:
                with open(args.input, "r", encoding="utf-8") as f:
                        data = json.load(f)
        else:
                data = json.load(sys.stdin)

        xml = json_to_xml(data, root_name=args.root, indent=args.indent)

        if args.output:
                with open(args.output, "w", encoding="utf-8") as f:
                        f.write(xml)
        else:
                sys.stdout.write(xml)


if __name__ == "__main__":
        _main()