from odoo import models, fields

class Participant(models.Model):
    _name = 'eventos_solidaridad.participant'
    _description = 'Participante en evento de Esperanza Solidaria'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Telefono')
    event_id = fields.Many2one('eventos_solidaridad.event', string='Evento')
    survey_ids = fields.One2many('eventos_solidaridad.survey', 'participant_id', string='Encuestas completadas')
