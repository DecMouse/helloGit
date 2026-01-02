import argparse
import json
import re
import sys
from xml.etree.ElementTree import Element, tostring
from xml.dom import minidom

#!/usr/bin/env python3
"""
JSON2XML.py

Convert a JSON file to XML and save to an output file.

Usage:
        python JSON2XML.py input.json output.xml [--root ROOTNAME]

If --root is omitted the root element name is derived from the input filename
(or defaults to "root" if input is "-" for stdin).
"""

def _safe_tag(name):
                # Replace invalid chars and ensure tag doesn't start with digit
                if not isinstance(name, str) or name == "":
                                return "item"
                tag = re.sub(r"[^a-zA-Z0-9_:.-]", "_", name)
                if re.match(r"^[0-9]", tag):
                                tag = "n_" + tag
                return tag

def _build_xml(elem, value):
                # Recursively build XML under elem from Python data types
                if value is None:
                                return
                if isinstance(value, dict):
                                for k, v in value.items():
                                                child = Element(_safe_tag(k))
                                                elem.append(child)
                                                _build_xml(child, v)
                elif isinstance(value, list):
                                # For lists, create repeated child elements named "item" unless caller supplies a wrapper key
                                for item in value:
                                                child = Element("item")
                                                elem.append(child)
                                                _build_xml(child, item)
                else:
                                # primitive value
                                elem.text = str(value)

def json_to_xml_obj(root_name, obj):
                root = Element(_safe_tag(root_name))
                _build_xml(root, obj)
                return root

def pretty_xml_string(element):
                raw = tostring(element, "utf-8")
                parsed = minidom.parseString(raw)
                return parsed.toprettyxml(indent="  ")

def main():
                parser = argparse.ArgumentParser(description="Convert JSON to XML")
                parser.add_argument("input", "input.json")
                parser.add_argument("output", "output.xml")
                parser.add_argument("root", "Root")
                args = parser.parse_args()

                # Read JSON
                try:
                                if args.input == "-":
                                                data = json.load(sys.stdin)
                                                inferred_root = "root"
                                else:
                                                with open(args.input, "r", encoding="utf-8") as f:
                                                                data = json.load(f)
                                                inferred_root = re.sub(r"\.json$", "", args.input.split("/")[-1], flags=re.IGNORECASE) or "root"
                except Exception as e:
                                print(f"Error reading JSON: {e}", file=sys.stderr)
                                sys.exit(2)

                root_name = args.root if args.root else inferred_root
                xml_root = json_to_xml_obj(root_name, data)
                xml_text = pretty_xml_string(xml_root)

                try:
                                if args.output == "-":
                                                sys.stdout.write(xml_text)
                                else:
                                                with open(args.output, "w", encoding="utf-8") as f:
                                                                f.write(xml_text)
                except Exception as e:
                                print(f"Error writing XML: {e}", file=sys.stderr)
                                sys.exit(3)

if __name__ == "__main__":
                main()