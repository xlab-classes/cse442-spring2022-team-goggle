import os
import pdb
import xml.etree.ElementTree as ET

cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('../Data/ESHA_Recipes', cur_path)

file_names = os.listdir(new_path)

for file_name in [file_names[0]]:
    mytree = ET.parse(os.path.join(new_path,file_name))
    root = mytree.getroot()

    print([elem.tag for elem in root.iter()][2])
