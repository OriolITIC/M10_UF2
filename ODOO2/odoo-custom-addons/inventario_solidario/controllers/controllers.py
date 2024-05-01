# -*- coding: utf-8 -*-
from odoo import http


class InventarioSolidario(http.Controller):
    @http.route('/inventario_solidario/inventario_solidario', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/inventario_solidario/inventario_solidario/objects', auth='public')
    def list(self, **kw):
        return http.request.render('inventario_solidario.listing', {
            'root': '/inventario_solidario/inventario_solidario',
            'objects': http.request.env['inventario_solidario.inventario_solidario'].search([]),
        })

    @http.route('/inventario_solidario/inventario_solidario/objects/<model("inventario_solidario.inventario_solidario"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('inventario_solidario.object', {
            'object': obj
        })
