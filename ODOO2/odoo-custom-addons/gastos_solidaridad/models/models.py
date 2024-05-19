# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gastos_solidaridad(models.Model):
    _name = 'gastos_solidaridad.gastos_solidaridad'
    _description = 'gastos_solidaridad.gastos_solidaridad'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
