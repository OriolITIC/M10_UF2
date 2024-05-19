
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
    client_type = fields.Selection([('voluntario', 'Voluntario'), ('donante', 'Donante')], string='Client Type', default='donante')

    @api.model
    def create_crm_client(self, name, email=None, phone=None, client_type='donante'):
        vals = {
            'name': name,
            'email': email,
            'phone': phone,
            'client_type': client_type,
        }
        return self.create(vals)
    

    
class CustomCRMVolunteer(models.Model):
    _name='voluntarios.crm.volunteer'
    _description='Custom CRM Voluntario'
    _inherit='custom.crm.client'

    mayor_que_18 = fields.Boolean(string='Es mayor de edad')
    last_volunteer_date = fields.Date(string='Last Volunteer Date')

    @api.model
    def create_voluntario(self, name, email=None, phone=None, client_type='Voluntario', mayor_que_18=True, last_volunteer_date=None):
        vals = {
            'name': name,
            'email': email,
            'phone': phone,
            'client_type': 'voluntario',
            'Es mayor de edad': mayor_que_18,
            'Last Volunteer Date': last_volunteer_date
          
        }
        return self.create(vals)
    
class CustomCRMDonante(models.Model):
    _name='donaciones.crm.donante'
    _description='Custom CRM Donante'
    _inherit='custom.crm.client'

    mayor_que_18 = fields.Boolean(string='Es mayor de edad')
   

    @api.model
    def create_donante(self, name, email=None, phone=None, client_type='Donante', mayor_que_18=True):
        vals = {
            'name': name,
            'email': email,
            'phone': phone,
            'client_type': 'donante',
            'Es mayor de edad':mayor_que_18
          
        }
        return self.create(vals)
    
    

class CustomCRMDonaciones(models.Model):
    _name='donaciones.crm.donantes'
    _description='Custom CRM Donaciones'

    name= fields.Text(string='Donation Reference',required=True, copy=False, index=True, default=lambda self :'New donation')

    donante = fields.Many2one('custom.crm.client', string='Donante', required=True)
    fecha_donacion = fields.Date(string='Fecha de Donación', required=True)
    cantidad = fields.Float(string='Cantidad', required=True)
    descripcion = fields.Text(string='Descripción')
    tipo_de_donacion = fields.Selection(

        string ='Type',
        selection = [('ropa','Ropa'),('alimento','Alimento'),('otro','otro')]

    )



""" 

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

 """


