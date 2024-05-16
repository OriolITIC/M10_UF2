# -*- coding: utf-8 -*-
from odoo import http


class InventarioSolidaridad(http.Controller):
    @http.route('/inventario_solidaridad/inventario_solidaridad', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/inventario_solidaridad/inventario_solidaridad/objects', auth='public')
    def list(self, **kw):
        return http.request.render('inventario_solidaridad.listing', {
            'root': '/inventario_solidaridad/inventario_solidaridad',
            'objects': http.request.env['inventario_solidaridad.inventario_solidaridad'].search([]),
        })

    @http.route('/inventario_solidaridad/inventario_solidaridad/objects/<model("inventario_solidaridad.inventario_solidaridad"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('inventario_solidaridad.object', {
            'object': obj
        })
