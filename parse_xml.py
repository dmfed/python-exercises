import xml.etree.ElementTree as ET

tree = ET.parse('testxml.xml')
root = tree.getroot()
print(type(tree), type(root))
print(root.tag, root.attrib)
ET.dump(root)

for elem in root:
    print(elem.attrib['name'])
    for content in elem:
        print(content.tag.title(), content.text)
