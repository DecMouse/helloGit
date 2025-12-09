# convert an xml file to json file
import xml.etree.ElementTree as ET
import json 

def parse_element(element):
    parsed_data = {}
    for child in element:
        child_data = parse_element(child) if len(child) else child.text
        if child.tag in parsed_data:
            if isinstance(parsed_data[child.tag], list):
                parsed_data[child.tag].append(child_data)
            else:
                parsed_data[child.tag] = [parsed_data[child.tag], child_data]
        else:
            parsed_data[child.tag] = child_data
    return parsed_data

def xml_to_json(xml_file, json_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    json_data = parse_element(root)

    with open(json_file, 'w', encoding='utf-8') as jf:
        json.dump(json_data, jf, indent=4, ensure_ascii=False)
    
if __name__ == "__main__":
    xml_file = 'sample.xml'  # Input XML file
    json_file = 'output.json'  # Output JSON file
    xml_to_json(xml_file, json_file)
    print(f"Converted {xml_file} to {json_file}")

