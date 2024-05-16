from odoo import models, fields

class Survey(models.Model):
    _name = 'eventos_solidaridad.survey'
    _description = 'Encuesta de satisfaccion'

    name = fields.Char(string='Nombre encuestas', required=True)
    date_sent = fields.Datetime(string='Fecha envio')
    responses = fields.Text(string='Respuestas')
    event_id = fields.Many2one('eventos_solidaridad.event', string='Evento')
    participant_id = fields.Many2one('eventos_solidaridad.participant', string='Participante')
