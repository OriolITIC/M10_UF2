# -*- coding: utf-8 -*-

from odoo import models, fields, api


class marketing_email_solidario(models.Model):
    _name = 'marketing_email_solidario.marketing_email_solidario'
    _description = 'marketing_email_solidario.marketing_email_solidario'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
