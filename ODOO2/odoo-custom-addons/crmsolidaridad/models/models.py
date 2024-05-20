from odoo import models, fields, api

class Contactos(models.Model):
    _name = 'crmsolidaridad.contactos'
    _description = 'Contacto descripción'

    name = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono')
    correo = fields.Char(string='Correo Electrónico')
    tipo_contacto = fields.Selection(
        [('voluntario','Voluntario'),
         ('donante','Donante')],
        string='Tipo de contacto',
        required=True
    )
    @api.model
    def create_contacto(self, name, telefono, correo, tipo_contacto):
        contacto_data = {
            "name": name,
            "telefono": telefono,
            "correo": correo,
            "tipo_contacto": tipo_contacto
        }
        return self.create(contacto_data)


class Donantes(models.Model):
    _name = "crmsolidaridad.donantes"
    _description = "Donantes CRM"

    mayor_de_edad = fields.Boolean(string='Es mayor de edad')
    fecha_ultima_donacion = fields.Date(string='Fecha última de donación')
    contacto_id = fields.Many2one('crmsolidaridad.contactos', string='Contacto')
    donaciones_relacionadas = fields.One2many('crmsolidaridad.donaciones', 'donante_id', string='Donaciones')

    @staticmethod
    def create_donante(self, mayor_de_edad, fecha_ultima_donacion, contacto_id):
        donante_data = {
            "mayor_de_edad": mayor_de_edad,
            "fecha_ultima_donacion": fecha_ultima_donacion,
            "contacto_id": contacto_id
        }
        return self.create(donante_data)

class Donacion(models.Model):
    _name = "crmsolidaridad.donaciones"
    _description = "Donaciones CRM"

    que_dona = fields.Selection(
        [('ropa', 'Ropa'), ('comida', 'Comida')],
        string='Donación'
    )
    cantidad = fields.Integer(string='Cantidad')
    fecha_donacion = fields.Date(string='Fecha de donación', default=fields.Date.today)
    donante_id = fields.Many2one('crmsolidaridad.donantes', string='Donante', inverse_name='donaciones_relacionadas')

    @staticmethod
    def create_donacion(self, que_dona, cantidad, fecha_donacion, donante_id):
        donacion_data = {
            "que_dona": que_dona,
            "cantidad": cantidad,
            "fecha_donacion": fecha_donacion,
            "donante_id": donante_id
        }
        return self.create(donacion_data)
