from odoo import models, fields

class Producto(models.Model):
    _name = 'esperanza_unida.producto'
    _description = 'Producto'

    name = fields.Char('Nombre', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    categoria_id = fields.Many2one('esperanza_unida.categoria', string='Categoría', required=True)
    almacen_id = fields.Many2one('esperanza_unida.almacen', string='Almacén', required=True)
    fecha_caducidad = fields.Date('Fecha de Caducidad', required=False)
