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
