class Vehicle:
    def __init__(self, marca, model, any_fabricacio, color, num_portes, velocitat_maxima):
        self.marca = marca
        self.model = model
        self.any_fabricacio = any_fabricacio
        self.color = color
        self.num_portes = num_portes
        self.velocitat_maxima = velocitat_maxima

    def get_marca(self):
        return self.marca

    def get_model(self):
        return self.model

    def get_any_fabricacio(self):
        return self.any_fabricacio

    def get_color(self):
        return self.color

    def get_num_doors(self):
        return self.num_portes

    def get_velocitat_maxima(self):
        return self.velocitat_maxima

    def set_marca(self, marca):
        self.marca = marca

    def set_model(self, model):
        self.model = model

    def set_any_fabricacio(self, any_fabricacio):
        self.any_fabricacio = any_fabricacio

    def set_color(self, color):
        self.color = color

    def set_num_doors(self, num_portes):
        self.portes = num_portes

    def set_velocitat_maxima(self, velocitat_maxima):
        self.velocitat_maxima = velocitat_maxima

    def parts(self):
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"Any de fabricació: {self.any_fabricacio}")
        print(f"Color: {self.color}")
        print(f"Nombre de portes: {self.num_portes}")
        print(f"Velocitat màxima: {self.velocitat_maxima} km/h")

    def to_dict(self):
        return {
            'marca': self.marca,
            'model': self.model,
            'any_fabricacio': self.any_fabricacio,
            'color': self.color,
            'num_portes': self.num_portes,
            'velocitat_maxima': self.velocitat_maxima
        }


