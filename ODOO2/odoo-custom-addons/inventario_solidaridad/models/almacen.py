from odoo import models, fields

class Almacen(models.Model):
    _name = 'esperanza_unida.almacen'
    _description = 'Almacén'

    name = fields.Char('Nombre', required=True)
    location = fields.Char('Ubicación', required=True)
    productos_ids = fields.One2many('esperanza_unida.producto', 'almacen_id', string='Productos')
