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

    destinatario = fields.Char(string='Destinatario', required=True)
    asunto = fields.Char(string='Asunto', required=True)
    mensaje = fields.Html(string='Mensaje', required=True)
    fecha_envio = fields.Datetime(string='Fecha de Envío', default=fields.Datetime.now)
    empresa_id = fields.Many2one('email.marketing.empresa', string='Empresa', required=True)
    template_id = fields.Many2one('email.marketing.template', string='Plantilla de Correo', ondelete='set null')




 
