# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Modelo crmsolidaridad
class crmsolidaridad(models.Model):
    _name = 'crmsolidaridad.crmsolidaridad'
    _description = 'crmsolidaridad.crmsolidaridad'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


class CustomCRMClient(models.Model):
    _name = 'custom.crm.client'
    _description = 'Custom CRM Client'
    #_description = 'Pipeline'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    client_type = fields.Selection([('individual', 'Individual'), ('company', 'Company')], string='Client Type', default='individual')

    @api.model
    def create_crm_client(self, name, email=None, phone=None, client_type='individual'):
        vals = {
            'name': name,
            'email': email,
            'phone': phone,
            'client_type': client_type,
        }
        return self.create(vals)
    

class CustomCRMPipeline(models.Model):
    _name = 'custom.crm.pipeline'
    _description = 'Custom CRM Pipeline'

    name = fields.Char(string='Title', required=True)
    cliente_id = fields.Many2one('custom.crm.client', string='Cliente', required=True)

    @api.model
    def create_crm_pipeline_nuevo(self, name, cliente_id):
        vals = {
            'name': name,
            'cliente_id': cliente_id,
        }
        return self.create(vals)
