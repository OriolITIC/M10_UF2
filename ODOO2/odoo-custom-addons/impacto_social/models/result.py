from odoo import models, fields

class Result(models.Model):
    _name = 'impacto_social.result'
    _description = 'Resultado del Impacto'

    name = fields.Char(string='Nombre del Resultado', required=True)
    description = fields.Text(string='Descripción')
    date = fields.Date(string='Fecha del Resultado')
    value = fields.Float(string='Valor del Resultado')
    indicator_id = fields.Many2one('impacto_social.indicator', string='Indicador Relacionado')
    impact_id = fields.Many2one('impacto_social.impact', string='Impacto Relacionado')
