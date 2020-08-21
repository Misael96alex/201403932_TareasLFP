import xml.etree.ElementTree as ET

def readXml():
    estructura_xml = ET.parse('Archivo2.xml')
    raiz = estructura_xml.getroot()
    for elemento_hijo in raiz:
        print(elemento_hijo.tag)
