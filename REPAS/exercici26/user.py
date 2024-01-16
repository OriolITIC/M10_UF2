class User:
    def __init__(self, nom, cognom, edat, sexe, email, data_naixement):
        self.nom = nom
        self.cognom = cognom
        self.edat = edat
        self.sexe = sexe
        self.email = email
        self.data_naixement = data_naixement

    def get_nom(self):
        return self.nom

    def get_cognom(self):
        return self.cognom

    def get_edat(self):
        return self.edat

    def get_sexe(self):
        return self.sexe

    def get_email(self):
        return self.email

    def get_data_naixement(self):
        return self.data_naixement 

    def set_nom(self, nom):
        self.nom = nom

    def set_cognom(self, cognom):
        self.cognom = cognom
    
    def set_edat(self, edat):
        self.edat = edat

    def set_sexe(self, sexe):
        self.sexe = sexe

    def set_email(self, email):
        self.email = email

    def set_data_naixement(self, data_naixement):
        self.data_naixement = data_naixement

    def parts(self):
        print(f"Nom: {self.nom}")
        print(f"Cognom: {self.cognom}")
        print(f"Edat: {self.edat}")
        print(f"Sexe: {self.sexe}")
        print(f"Email: {self.email}")
        print(f"Data naixement: {self.data_naixement}")

    def to_dict(self):
        return {
            'nom': self.nom,
            'cognom': self.cognom,
            'edat': self.edat,
            'sexe': self.sexe,
            'email': self.email,
            'data_naixement': self.data_naixement
        }


