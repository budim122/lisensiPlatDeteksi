# convert_xml_to_csv.py
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(xml_folder="labeled_data"):
    xml_list = []
    for xml_file in glob.glob(xml_folder + "/*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall("object"):
            value = (root.find("filename").text,
                     int(root.find("size/width").text),
                     int(root.find("size/height").text),
                     member[0].text,
                     int(member.find("bndbox/xmin").text),
                     int(member.find("bndbox/ymin").text),
                     int(member.find("bndbox/xmax").text),
                     int(member.find("bndbox/ymax").text))
            xml_list.append(value)
    column_name = ["filename", "width", "height", "class", "xmin", "ymin", "xmax", "ymax"]
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df.to_csv("labels.csv", index=False)
    print("XML files converted to CSV successfully.")

if __name__ == "__main__":
    xml_to_csv()