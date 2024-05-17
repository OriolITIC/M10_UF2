from odoo import models, fields

class Impact(models.Model):
    _name = 'seguimiento_impacto.impact'
    _description = 'Impacto Social'

    name = fields.Char(string='Nombre del Impacto', required=True)
    description = fields.Text(string='Descripción')
    project_id = fields.Many2one('project.project', string='Proyecto Relacionado')
    indicator_ids = fields.One2many('seguimiento_impacto.indicator', 'impact_id', string='Indicadores')
    result_ids = fields.One2many('seguimiento_impacto.result', 'impact_id', string='Resultados')
    beneficiary_ids = fields.Many2many('seguimiento_impacto.beneficiary', string='Beneficiarios')
