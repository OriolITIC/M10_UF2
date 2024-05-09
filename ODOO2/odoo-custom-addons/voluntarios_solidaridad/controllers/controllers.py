# -*- coding: utf-8 -*-
from odoo import http


class VoluntariosSolidaridad(http.Controller):
    @http.route('/voluntarios_solidaridad/voluntarios_solidaridad', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/voluntarios_solidaridad/voluntarios_solidaridad/objects', auth='public')
    def list(self, **kw):
        return http.request.render('voluntarios_solidaridad.listing', {
            'root': '/voluntarios_solidaridad/voluntarios_solidaridad',
            'objects': http.request.env['voluntarios_solidaridad.voluntarios_solidaridad'].search([]),
        })

    @http.route('/voluntarios_solidaridad/voluntarios_solidaridad/objects/<model("voluntarios_solidaridad.voluntarios_solidaridad"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('voluntarios_solidaridad.object', {
            'object': obj
        })
