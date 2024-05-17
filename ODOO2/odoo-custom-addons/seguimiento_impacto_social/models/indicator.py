from odoo import models, fields

class Indicator(models.Model):
    _name = 'seguimiento_impacto.indicator'
    _description = 'Indicador de Impacto'

    name = fields.Char(string='Nombre del Indicador', required=True)
    description = fields.Text(string='Descripción')
    target_value = fields.Float(string='Valor Objetivo')
    achieved_value = fields.Float(string='Valor Alcanzado')
    impact_id = fields.Many2one('seguimiento_impacto.impact', string='Impacto Relacionado')
