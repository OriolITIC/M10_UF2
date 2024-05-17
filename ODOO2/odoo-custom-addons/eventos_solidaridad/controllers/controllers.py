# -*- coding: utf-8 -*-
from odoo import http


class EventosSolidaridad(http.Controller):
    @http.route('/eventos_solidaridad/eventos_solidaridad', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/eventos_solidaridad/eventos_solidaridad/objects', auth='public')
    def list(self, **kw):
        return http.request.render('eventos_solidaridad.listing', {
            'root': '/eventos_solidaridad/eventos_solidaridad',
            'objects': http.request.env['eventos_solidaridad.eventos_solidaridad'].search([]),
        })

    @http.route('/eventos_solidaridad/eventos_solidaridad/objects/<model("eventos_solidaridad.eventos_solidaridad"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('eventos_solidaridad.object', {
            'object': obj
        })
