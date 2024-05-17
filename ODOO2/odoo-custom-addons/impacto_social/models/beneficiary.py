from odoo import models, fields

class Beneficiary(models.Model):
    _name = 'impacto_social.beneficiary'
    _description = 'Beneficiario del Impacto'

    name = fields.Char(string='Nombre del Beneficiario', required=True)
    email = fields.Char(string='Correo Electrónico')
    phone = fields.Char(string='Teléfono')
    impact_ids = fields.Many2many('impacto_social.impact', string='Impactos Relacionados')
