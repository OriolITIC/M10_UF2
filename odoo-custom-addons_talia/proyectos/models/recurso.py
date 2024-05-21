from odoo import models, fields

class Recurso(models.Model):
    _name = 'proyectos.recurso'
    _description = 'Recurso para el proyecto de la ONG'

    name = fields.Char(string="Nombre", required=True)
    cantidad = fields.Integer(string="Cantidad")
    proyecto_id = fields.Many2one('proyectos.proyecto', string="Proyecto", required=True)
