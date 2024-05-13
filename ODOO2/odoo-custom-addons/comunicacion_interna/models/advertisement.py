from odoo import models, fields

class Advertisement(models.Model):
    _name = 'comunicacion_interna.advertisement'
    _description = 'Anuncio Interno'

    name = fields.Char(string='Nombre', required=True)
    author_id = fields.Many2one('voluntarios_solidaridad.volunteer', string='Autor', required=True)
    department_id = fields.Many2one('voluntarios_solidaridad.department', string='Department')
    title = fields.Char(string='Titulo', required=True)
    body = fields.Text(string='Cuerpo', required=True)
    attachment_ids = fields.Many2many('ir.attachment', string='Documentos adjuntos')
    highlighted = fields.Boolean(string='Destacado', default=False)
    publication_date = fields.Datetime(string='Fecha publicación', default=fields.Datetime.now)
