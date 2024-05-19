# -*- coding: utf-8 -*-
from odoo import http


class GastosSolidaridad(http.Controller):
    @http.route('/gastos_solidaridad/gastos_solidaridad', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/gastos_solidaridad/gastos_solidaridad/objects', auth='public')
    def list(self, **kw):
        return http.request.render('gastos_solidaridad.listing', {
            'root': '/gastos_solidaridad/gastos_solidaridad',
            'objects': http.request.env['gastos_solidaridad.gastos_solidaridad'].search([]),
        })

    @http.route('/gastos_solidaridad/gastos_solidaridad/objects/<model("gastos_solidaridad.gastos_solidaridad"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gastos_solidaridad.object', {
            'object': obj
        })
