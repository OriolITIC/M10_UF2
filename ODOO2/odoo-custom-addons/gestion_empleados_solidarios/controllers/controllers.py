# -*- coding: utf-8 -*-
from odoo import http


class GestionEmpleadosSolidarios(http.Controller):
    @http.route('/gestion_empleados_solidarios/gestion_empleados_solidarios', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/gestion_empleados_solidarios/gestion_empleados_solidarios/objects', auth='public')
    def list(self, **kw):
        return http.request.render('gestion_empleados_solidarios.listing', {
            'root': '/gestion_empleados_solidarios/gestion_empleados_solidarios',
            'objects': http.request.env['gestion_empleados_solidarios.gestion_empleados_solidarios'].search([]),
        })

    @http.route('/gestion_empleados_solidarios/gestion_empleados_solidarios/objects/<model("gestion_empleados_solidarios.gestion_empleados_solidarios"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gestion_empleados_solidarios.object', {
            'object': obj
        })
