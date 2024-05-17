from odoo import models, fields

class Event(models.Model):
    _name = 'comunicacion_interna.event'
    _description = 'Eventos Internos'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    start_date = fields.Datetime(string='Fecha de inicio', required=True)
    end_date = fields.Datetime(string='Fecha de fin', required=True)
    location = fields.Char(string='Ubicación')
    organizer_id = fields.Many2one('voluntarios_solidaridad.volunteer', string='Organizador', required=True)
    participant_ids = fields.Many2many('voluntarios_solidaridad.volunteer', 
                                   'ci_event_participant_rel', 
                                   'event_id', 
                                   'volunteer_id', 
                                   string='Participantes')
    department_ids = fields.Many2many('voluntarios_solidaridad.department', 
                                  'ci_event_department_rel', 
                                  'event_id', 
                                  'department_id', 
                                  string='Departamentos')
