import xml.etree.ElementTree as ET

def crear_xml():
    root = ET.Element("students")

    for i in range(1, 6):
        student = ET.SubElement(root, "student")
        student.set("id", str(i))  

        name = ET.SubElement(student, "name")
        name.text = f"Nombre{i}"

        surname = ET.SubElement(student, "surname")
        surname.text = f"Apellido{i}"

        email = ET.SubElement(student, "email")
        email.text = f"email{i}@example.com"

        dni = ET.SubElement(student, "dni")
        dni.text = f"DNI{i}"

    tree = ET.ElementTree(root)

    tree.write("students.xml")
    
    with open("students.xml", "r") as file:
        contingut = file.read()
        print(contingut)

crear_xml()
