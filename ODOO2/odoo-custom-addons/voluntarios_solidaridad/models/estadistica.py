from odoo import models, fields, api

class Estadistica(models.Model):
    _name = 'voluntarios_solidaridad.estadistica'
    _description = 'Estadísticas de Voluntarios'

    name = fields.Char('Nombre', required=True)
    cantidad = fields.Integer('Cantidad', required=True)
    department_id = fields.Many2one('voluntarios_solidaridad.department', string='Departamento')
    volunteer_count = fields.Integer(string='Número de Voluntarios', compute='_compute_volunteer_count')

    @api.depends('department_id')
    def _compute_volunteer_count(self):
        for record in self:
            if record.department_id:
                record.volunteer_count = len(record.department_id.volunteer_ids)
            else:
                record.volunteer_count = 0
    