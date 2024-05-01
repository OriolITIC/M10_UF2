# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gestion_empleados_solidarios(models.Model):
    _name = 'gestion_empleados_solidarios.gestion_empleados_solidarios'
    _description = 'gestion_empleados_solidarios.gestion_empleados_solidarios'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
