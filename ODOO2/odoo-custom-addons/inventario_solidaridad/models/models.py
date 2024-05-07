# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class inventario_solidaridad(models.Model):
#     _name = 'inventario_solidaridad.inventario_solidaridad'
#     _description = 'inventario_solidaridad.inventario_solidaridad'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
