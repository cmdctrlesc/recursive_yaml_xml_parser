from xml.etree import ElementTree
import yaml

def generate_xml(yaml_dict, parent_node=None, key=None):

    if parent_node is None:
        node= ElementTree.Element(key)
    else:
        node= ElementTree.SubElement(parent_node, key)

    for key,value in yaml_dict.items():
        if isinstance(value, dict):
            generate_xml(value, node, key)
        else:
            child= ElementTree.SubElement(node, key)
            child.text= value

    return node

def yaml_to_xml(yaml_filename, xml_filename):

    with open(yaml_filename) as file:

        yaml_dict = yaml.safe_load(file)
        my_xml = generate_xml(yaml_dict)
        tree = ElementTree.ElementTree(my_xml)
        tree.write(xml_filename)  

yaml_to_xml('new.yaml', 'shit.xml')
