from datetime import datetime, timedelta
from odoo import models, fields, api

class Producto(models.Model):
    _name = 'esperanza_unida.producto'
    _description = 'Producto'

    name = fields.Char('Nombre', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    categoria_id = fields.Many2one('esperanza_unida.categoria', string='Categoría', required=True)
    almacen_id = fields.Many2one('esperanza_unida.almacen', string='Almacén', required=True)
    fecha_caducidad = fields.Date('Fecha de Caducidad')
    talla = fields.Selection([('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], string='Talla')
    categoria_name = fields.Char(related='categoria_id.name', string='Nombre de la Categoría', store=True)

    @api.onchange('categoria_id')
    def _onchange_categoria_id(self):
        if self.categoria_id.name != 'Ropa':
            self.talla = False
        if self.categoria_id.name != 'Alimentos':
            self.fecha_caducidad = False

    @api.model
    def productos_proximos_a_caducar(self):
        fecha_limite = datetime.now() + timedelta(days=60)
        return self.search([('fecha_caducidad', '<=', fecha_limite.strftime('%Y-%m-%d'))])
