from odoo import models, fields

class Categoria(models.Model):
    _name = 'esperanza_unida.categoria'
    _description = 'Categoría de Producto'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
