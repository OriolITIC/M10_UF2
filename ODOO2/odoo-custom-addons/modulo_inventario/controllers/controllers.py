# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloInventario(http.Controller):
#     @http.route('/modulo_inventario/modulo_inventario', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_inventario/modulo_inventario/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_inventario.listing', {
#             'root': '/modulo_inventario/modulo_inventario',
#             'objects': http.request.env['modulo_inventario.modulo_inventario'].search([]),
#         })

#     @http.route('/modulo_inventario/modulo_inventario/objects/<model("modulo_inventario.modulo_inventario"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_inventario.object', {
#             'object': obj
#         })
