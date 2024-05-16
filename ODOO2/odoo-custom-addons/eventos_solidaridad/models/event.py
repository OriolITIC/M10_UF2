from odoo import models, fields

class Event(models.Model):
    _name = 'eventos_solidaridad.event'
    _description = 'Eventos de Esperanza Solidaria'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    date_start = fields.Datetime(string='Fecha inicio', required=True)
    date_end = fields.Datetime(string='Fecha finalización')
    location = fields.Char(string='Localización')
    budget = fields.Float(string='Presupuesto')
    project_id = fields.Many2one('project.project', string='Related Project')
    participant_ids = fields.Many2many('eventos_solidaridad.participant', string='Participantes')
    task_ids = fields.One2many('eventos_solidaridad.task', 'event_id', string='Tareas')
    survey_id = fields.Many2one('eventos_solidaridad.survey', string='Encuestas')
