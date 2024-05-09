# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crmsolidaridad(models.Model):
    _name = 'crm.lead'
    _description = 'CRM Lead'
    TIPO_CLIENTE =[
        ('empresa','Empresa'),
        ('individual','Individual'),
        ('otro','Otro')


    ]


    name = fields.Text(string='Name',required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    tipo_cliente = fields.Selection(
        selection=TIPO_CLIENTE,
        string='Tipo de cliente'
    )
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
