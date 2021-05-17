import xml.etree.ElementTree as ET
import yaml

def make_nested_dict(item_list):
    nested_dict = {}
    for item in item_list:
        if len(list(item)):
            nested_dict[str(item.tag)] = make_nested_dict(item)
        else:
            nested_dict[str(item.tag)] = item.text

    return nested_dict   
 

def xml_to_yaml(xml_filename, yaml_filename):

    with open(yaml_filename, 'w') as file:
        root = ET.parse(xml_filename).getroot()
        nested_dict = make_nested_dict(root) 
        final_yaml = yaml.safe_dump(nested_dict, file, sort_keys=False)

xml_to_yaml('XML_RateRequest_Avstrija_Economy_ESU.xml', 'new.yaml')      

