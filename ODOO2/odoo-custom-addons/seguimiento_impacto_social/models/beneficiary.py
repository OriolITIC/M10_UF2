from odoo import models, fields

class Beneficiary(models.Model):
    _name = 'seguimiento_impacto.beneficiary'
    _description = 'Beneficiario del Impacto'

    name = fields.Char(string='Nombre del Beneficiario', required=True)
    email = fields.Char(string='Correo Electrónico')
    phone = fields.Char(string='Teléfono')
    impact_ids = fields.Many2many('seguimiento_impacto.impact', string='Impactos Relacionados')
