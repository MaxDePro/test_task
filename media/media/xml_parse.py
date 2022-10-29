import xml.etree.ElementTree as ET

xml_file = "/Users/user/PycharmProjects/test_task_django/test_task/media/media/test_task.xml"


def parse_xml_data(xml_file):
    new_d = {}
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for us in root.findall('user'):
        outer_dict = {}

        first_names = us.find('first_name').text
        last_names = us.find('last_name').text
        if first_names is not None and last_names is not None:
            outer_dict['first_name'] = first_names
            outer_dict['last_name'] = last_names
            new_d[us.attrib.get('id')] = outer_dict
    return new_d


print(parse_xml_data(xml_file))
