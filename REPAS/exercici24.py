import json

import json

def mostrar_json():
    with open("books.json", "r") as file:
        content = file.read()
        data = json.loads(content)
        print(json.dumps(data, indent=2))

mostrar_json()

        