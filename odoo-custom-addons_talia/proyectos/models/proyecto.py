from odoo import models, fields

class Proyecto(models.Model):
    _name = 'proyectos.proyecto'
    _description = 'Proyecto para la ONG'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    start_date = fields.Date(string="Fecha de Inicio")
    end_date = fields.Date(string="Fecha de Fin")
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En Progreso'),
        ('done', 'Finalizado'),
    ], string="Estado", default='draft')
    responsable_id = fields.Many2one('res.users', string="Responsable")
    tarea_ids = fields.One2many('proyectos.tarea', 'proyecto_id', string="Tareas")
    nota_ids = fields.One2many('proyectos.nota', 'proyecto_id', string="Notas")
    recurso_ids = fields.One2many('proyectos.recurso', 'proyecto_id', string="Recursos")
    presupuesto_ids = fields.One2many('proyectos.presupuesto', 'proyecto_id', string="Presupuestos")
