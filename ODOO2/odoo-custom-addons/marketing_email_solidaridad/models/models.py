# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Empresa(models.Model):
    _name = 'email.marketing.empresa'
    _description = 'Empresa para email marketing'


    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico', required=True)
    description = fields.Text(string='Descripción')
    contact_type = fields.Selection([
        ('empresa', 'Empresa'),
        ('particular', 'Particular')
    ], string='Tipo de Contacto', default='empresa', required=True)


class EmailEnviado(models.Model):
    _name = 'email.marketing.enviado'
    _description = 'Correos electrónicos enviados'


    destinatarios_ids = fields.Many2many('email.marketing.empresa', string='Destinatarios', required=True)
    asunto = fields.Char(string='Asunto', required=True)
    mensaje = fields.Html(string='Mensaje', required=True)
    fecha_envio = fields.Datetime(string='Fecha de Envío', default=fields.Datetime.now)
    empresa_id = fields.Many2one('email.marketing.empresa', string='Empresa')
    


    @api.depends('destinatarios_ids')
    def _compute_destinatario_emails(self):
        for record in self:
            record.destinatario_emails = ", ".join(dest.email for dest in record.destinatarios_ids)


    destinatario_emails = fields.Char(string='Destinatarios Emails', compute='_compute_destinatario_emails')
class Donante(models.Model):
    _name = 'accounting.donante'
    _description = 'Registro de Donantes'

    name = fields.Char(string='Nombre del Donante', default='Anónimo')
    fecha_donacion = fields.Date(string='Fecha de la Donación', required=True, default=fields.Date.today)
    tipo_donacion = fields.Selection([
        ('dinero', 'Dinero'),
        ('ropa', 'Ropa'),
        ('comida', 'Comida'),
        ('otros', 'Otros')
    ], string='Tipo de Donación', required=True)
    cantidad_dinero = fields.Float(string='Cantidad de Dinero')
    descripcion_donacion = fields.Text(string='Descripción de la Donación')
    uso_especifico = fields.Char(string='Uso Específico')
