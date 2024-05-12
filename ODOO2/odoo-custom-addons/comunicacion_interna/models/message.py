from odoo import models, fields

class Message(models.Model):
    _name = 'comunicacion_interna.message'
    _description = 'Mensajes Internos'

    name = fields.Char(string='Asunto', required=True)
    body = fields.Text(string='Cuerpo', required=True)
    author_id = fields.Many2one('voluntarios_solidaridad.volunteer', string='Autor', required=True)
    recipient_ids = fields.Many2many('voluntarios_solidaridad.volunteer', 
                                 'ci_message_recipient_rel', 
                                 'message_id', 
                                 'volunteer_id', 
                                 string='Destinatarios')

    department_ids = fields.Many2many('voluntarios_solidaridad.department', 
                                   'ci_message_department_rel',  
                                   'message_id', 
                                   'department_id', 
                                   string='Departamentos')


