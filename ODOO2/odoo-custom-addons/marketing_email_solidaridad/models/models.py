# # -*- coding: utf-8 -*-

# from odoo import models, fields, api

# """
# class marketing_email_solidaridad(models.Model):
#     _name = 'marketing_email_solidaridad.marketing_email_solidaridad'
#     _description = 'marketing_email_solidaridad.marketing_email_solidaridad'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100"""


# from odoo import models, fields, api

# class EmailTemplate(models.Model):
#     _name = 'email.template'
#     _description = 'Email Template'

#     name = fields.Char(string='Nombre de la plantilla', required=True)
#     subject = fields.Char(string='Asunto', required=True)
#     body = fields.Html(string='Cuerpo del correo', required=True)

# class SentEmail(models.Model):
#     _name = 'sent.email'
#     _description = 'Emails enviados'

#     email_template_id = fields.Many2one('email.template', string='Plantilla de correo', required=True)
#     company_id = fields.Many2one('res.company', string='Compañía', required=True)
#     recipient = fields.Char(string='Destinatario', required=True)
#     subject = fields.Char(string='Asunto', required=True)
#     body = fields.Html(string='Cuerpo del correo', required=True)
#     sent_date = fields.Datetime(string='Fecha de envío', default=fields.Datetime.now)

# class EmailList(models.Model):
#     _name = 'email.list'
#     _description = 'Lista de correos electrónicos'

#     name = fields.Char(string='Nombre de la lista', required=True)
#     company_id = fields.Many2one('res.company', string='Compañía', required=True)
#     email = fields.Char(string='Correo electrónico', required=True)

# class Contact(models.Model):
#     _name = 'res.partner'
#     _inherit = 'res.partner'

#     email_list_id = fields.One2one('email.list', string='Lista de correos electrónicos', required=True)

