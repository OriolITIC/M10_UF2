from odoo import models, fields

class Task(models.Model):
    _name = 'eventos_solidaridad.task'
    _description = 'Tarea de evento'

    name = fields.Char(string='Nombre tarea', required=True)
    description = fields.Text(string='Descripción')
    deadline = fields.Datetime(string='Vencimiento')
    responsible_id = fields.Many2one('voluntarios_solidaridad.volunteer', string='Responsable', required=True)
    event_id = fields.Many2one('eventos_solidaridad.event', string='Evento')
    state = fields.Selection([
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completado')
    ], string='Estado', default='pending')
