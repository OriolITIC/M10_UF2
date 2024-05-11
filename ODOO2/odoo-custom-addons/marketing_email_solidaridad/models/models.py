# -*- coding: utf-8 -*-

from odoo import models, fields, api

"""
class marketing_email_solidaridad(models.Model):
    _name = 'marketing_email_solidaridad.marketing_email_solidaridad'
    _description = 'marketing_email_solidaridad.marketing_email_solidaridad'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100"""


class Empresa(models.Model):
    _name = 'marketing_digital.empresa'
    _description = 'Información de la Empresa'


    name = fields.Char(string='Nombre')
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')

class CorreoEnviado(models.Model):
    _name = 'marketing_digital.correo_enviado'
    _description = 'Correos Enviados'

    
    email = fields.Char(string='Email')
    asunto = fields.Char(string='Asunto')
    mensaje = fields.Text(string='Mensaje')
    photo = fields.Binary(string='Foto')
    fecha = fields.Date(string='Fecha')


    empresa_id = fields.Many2one('marketing_digital.empresa', string='Empresa')
