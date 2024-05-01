# -*- coding: utf-8 -*-
from odoo import http


class GastosSolidarios(http.Controller):
    @http.route('/gastos_solidarios/gastos_solidarios', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/gastos_solidarios/gastos_solidarios/objects', auth='public')
    def list(self, **kw):
        return http.request.render('gastos_solidarios.listing', {
            'root': '/gastos_solidarios/gastos_solidarios',
            'objects': http.request.env['gastos_solidarios.gastos_solidarios'].search([]),
        })

    @http.route('/gastos_solidarios/gastos_solidarios/objects/<model("gastos_solidarios.gastos_solidarios"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gastos_solidarios.object', {
            'object': obj
        })
