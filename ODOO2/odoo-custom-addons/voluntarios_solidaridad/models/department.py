from odoo import models, fields, api

class Department(models.Model):
    _name = 'voluntarios_solidaridad.department'
    _description = 'Información departamento'

    name = fields.Char(string='Nombre')
    code = fields.Char(string='Código')
    phone = fields.Char(string='Teléfono')
    volunteer_ids = fields.Many2many('voluntarios_solidaridad.volunteer', 'department_volunteer_rel', string='Voluntarios')

     # Campo para contar el número de voluntarios asociados a este departamento
    volunteer_count = fields.Integer(string='Número de Voluntarios', compute='_compute_volunteer_count')

    @api.depends('volunteer_ids')
    def _compute_volunteer_count(self):
        for department in self:
            department.volunteer_count = len(department.volunteer_ids)