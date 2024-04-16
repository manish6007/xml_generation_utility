import json
import xml.etree.ElementTree as ET
import random
import string

def generate_value(data_type):
    """ Generate random data based on the type specified """
    if data_type == 'int':
        return str(random.randint(1, 100))
    elif data_type == 'string':
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    elif data_type == 'float':
        return str(round(random.uniform(5.0, 100.0), 2))
    return ""
"""
def add_elements(parent, fields):
   
    for tag, details in fields.items():
        if 'nested' in details:
            for _ in range(details.get('repeat', 1)):
                child = ET.SubElement(parent, tag, {k: generate_value(v) for k, v in details.get('attributes', {}).items()})
                add_elements(child, details['nested'])
        else:
            ET.SubElement(parent, tag).text = generate_value(details)
"""
def add_elements(parent, fields):
    """ Recursively add elements to the parent based on the fields specification """
    for tag, details in fields.items():
        if 'nested' in details:
            child = ET.SubElement(parent, tag, {k: generate_value(v) for k, v in details.get('attributes', {}).items()})
            add_elements(child, details['nested'])
        else:
            ET.SubElement(parent, tag).text = generate_value(details)


def generate_xml(data):
    root_element = ET.Element(data['root'])
    for _ in range(data['records']):
        add_elements(root_element, data['fields'])
    return ET.ElementTree(root_element)

def write_xml(tree, filename):
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def main(json_path, output_xml):
    with open(json_path, 'r') as file:
        data = json.load(file)
    tree = generate_xml(data)
    write_xml(tree, output_xml)

if __name__ == "__main__":
    import sys
    json_path = sys.argv[1]
    output_xml = sys.argv[2] if len(sys.argv) > 2 else 'output.xml'
    main(json_path, output_xml)
