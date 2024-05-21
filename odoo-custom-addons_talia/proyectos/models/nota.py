from odoo import models, fields

class Nota(models.Model):
    _name = 'proyectos.nota'
    _description = 'Nota para el proyecto de la ONG'

    name = fields.Char(string="Nombre", required=True)
    contenido = fields.Text(string="Contenido")
    proyecto_id = fields.Many2one('proyectos.proyecto', string="Proyecto", required=True)
