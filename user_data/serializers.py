import xml.etree.ElementTree as ET

xml_file = "/Users/user/PycharmProjects/test_task_django/test_task/media/media/test_task.xml"


def parse_xml_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    final_data_dict = {}

    for us in root.findall('user'):
        outer_dict = {}

        first_names = us.find('first_name').text
        last_names = us.find('last_name').text
        if first_names is not None and last_names is not None:
            outer_dict['first_name'] = first_names
            outer_dict['last_name'] = last_names
            final_data_dict[us.attrib.get('id')] = outer_dict
    return final_data_dict


# print(parse_xml_data(xml_file))
