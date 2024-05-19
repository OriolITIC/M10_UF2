from odoo import models, fields

class Indicator(models.Model):
    _name = 'impacto_social.indicator'
    _description = 'Indicador de Impacto'

    name = fields.Char(string='Nombre del Indicador', required=True)
    description = fields.Text(string='Descripción')
    target_value = fields.Float(string='Valor Objetivo')
    achieved_value = fields.Float(string='Valor Alcanzado')
    impact_id = fields.Many2one('impacto_social.impact', string='Impacto Relacionado')

