# -*- coding: utf-8 -*-

from odoo import models, fields, api

"""
class voluntarios_solidaridad(models.Model):
    _name = 'voluntarios_solidaridad.voluntarios_solidaridad'
    _description = 'voluntarios_solidaridad.voluntarios_solidaridad'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100"""

class Activity(models.Model):
    _name = 'voluntarios_solidaridad.activity'
    _description = 'Infromación actividad'

    name = fields.Char(string='Name')
    volunteer_ids = fields.Many2many('voluntarios_solidaridad.volunteer', 'activity_volunteer_rel', string='Voluntarios')

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
    

