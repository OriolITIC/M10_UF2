# -*- coding: utf-8 -*-

from odoo import models, fields, api


class seguimiento_impacto_social(models.Model):
    _name = 'seguimiento_impacto_social.seguimiento_impacto_social'
    _description = 'seguimiento_impacto_social.seguimiento_impacto_social'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
