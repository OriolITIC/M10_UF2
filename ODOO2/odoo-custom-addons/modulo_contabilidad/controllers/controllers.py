# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloContabilidad(http.Controller):
#     @http.route('/modulo_contabilidad/modulo_contabilidad', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_contabilidad/modulo_contabilidad/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_contabilidad.listing', {
#             'root': '/modulo_contabilidad/modulo_contabilidad',
#             'objects': http.request.env['modulo_contabilidad.modulo_contabilidad'].search([]),
#         })

#     @http.route('/modulo_contabilidad/modulo_contabilidad/objects/<model("modulo_contabilidad.modulo_contabilidad"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_contabilidad.object', {
#             'object': obj
#         })
