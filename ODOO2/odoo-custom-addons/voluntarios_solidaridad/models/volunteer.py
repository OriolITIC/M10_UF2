from odoo import models, fields, api

class Volunteer(models.Model):
    _name = 'voluntarios_solidaridad.volunteer'
    _description = 'Información voluntario'

    photo = fields.Binary(string='Foto')
    name = fields.Char(string='Nombre')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Telefono')
    city = fields.Char(string='Ciudad')
    department_id = fields.Many2one('voluntarios_solidaridad.department', string='Departamento')
    activities_ids = fields.Many2many('voluntarios_solidaridad.activity', 'activity_volunteer_rel', string='Actividades')