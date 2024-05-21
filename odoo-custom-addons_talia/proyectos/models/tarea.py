from odoo import models, fields

class Tarea(models.Model):
    _name = 'proyectos.tarea'
    _description = 'Tarea para el proyecto de la ONG'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha_inicio = fields.Date(string="Fecha de Inicio")
    fecha_fin = fields.Date(string="Fecha de Fin")
    proyecto_id = fields.Many2one('proyectos.proyecto', string="Proyecto")
    dependencia_ids = fields.Many2many('proyectos.tarea', 'tarea_dependencia_rel', 'tarea_id', 'dependencia_id', string="Dependencias")
    prioridad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ], string="Prioridad", default='media')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ], string="Estado", default='pendiente')
