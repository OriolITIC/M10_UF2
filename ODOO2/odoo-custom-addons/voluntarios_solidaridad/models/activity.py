from odoo import models, fields, api

class Activity(models.Model):
    _name = 'voluntarios_solidaridad.activity'
    _description = 'Infromación actividad'

    name = fields.Char(string='Name')
    volunteer_ids = fields.Many2many('voluntarios_solidaridad.volunteer', 'activity_volunteer_rel', string='Voluntarios')