import json

def crear_i_mostrar_json():

    datos_json = {
        "books": [
            {
                "title": "Libro1",
                "cover": "Portada1",
                "year": 2022,
                "pages": 300
            },
            {
                "title": "Libro2",
                "cover": "Portada2",
                "year": 2020,
                "pages": 250
            },
            {
                "title": "Libro3",
                "cover": "Portada3",
                "year": 2021,
                "pages": 400
            },
            {
                "title": "Libro4",
                "cover": "Portada4",
                "year": 2019,
                "pages": 350
            }
        ]
    }


    json_str = json.dumps(datos_json, indent=2)

    print(json_str)
    with open("books.json", "w") as archivo_json:
        archivo_json.write(json_str)

crear_i_mostrar_json()
