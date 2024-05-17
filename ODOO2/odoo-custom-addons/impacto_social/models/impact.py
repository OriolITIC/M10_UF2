from odoo import models, fields

class Impact(models.Model):
    _name = 'impacto_social.impact'
    _description = 'Impacto Social'

    name = fields.Char(string='Nombre del Impacto', required=True)
    description = fields.Text(string='Descripción')
    project_id = fields.Many2one('project.project', string='Proyecto Relacionado')
    indicator_ids = fields.One2many('impacto_social.indicator', 'impact_id', string='Indicadores')
    result_ids = fields.One2many('impacto_social.result', 'impact_id', string='Resultados')
    beneficiary_ids = fields.Many2many('impacto_social.beneficiary', string='Beneficiarios')
