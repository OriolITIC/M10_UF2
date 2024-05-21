from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'esperanza_unida.categoria'
    _description = 'Categoría'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripción')
    product_count = fields.Integer('Número de Productos', compute='_compute_product_count')
    product_ids = fields.One2many('esperanza_unida.producto', 'categoria_id', string='Productos')

    @api.depends('product_ids')
    def _compute_product_count(self):
        for categoria in self:
            categoria.product_count = len(categoria.product_ids)
