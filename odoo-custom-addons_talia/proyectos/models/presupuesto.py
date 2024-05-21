from odoo import models, fields

class Presupuesto(models.Model):
    _name = 'proyectos.presupuesto'
    _description = 'Presupuesto del Proyecto'

    name = fields.Char(string="Nombre", required=True)
    monto_estimado = fields.Float(string="Monto Estimado")
    monto_real = fields.Float(string="Monto Real")
    proyecto_id = fields.Many2one('proyectos.proyecto', string="Proyecto", required=True)
