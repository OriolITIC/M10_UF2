# -*- coding: utf-8 -*-
from odoo import http


class ProyectoSolidario(http.Controller):
    @http.route('/proyecto_solidario/proyecto_solidario', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/proyecto_solidario/proyecto_solidario/objects', auth='public')
    def list(self, **kw):
        return http.request.render('proyecto_solidario.listing', {
            'root': '/proyecto_solidario/proyecto_solidario',
            'objects': http.request.env['proyecto_solidario.proyecto_solidario'].search([]),
        })

    @http.route('/proyecto_solidario/proyecto_solidario/objects/<model("proyecto_solidario.proyecto_solidario"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('proyecto_solidario.object', {
            'object': obj
        })
