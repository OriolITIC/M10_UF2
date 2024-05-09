# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloEmpleados(http.Controller):
#     @http.route('/modulo_empleados/modulo_empleados', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_empleados/modulo_empleados/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_empleados.listing', {
#             'root': '/modulo_empleados/modulo_empleados',
#             'objects': http.request.env['modulo_empleados.modulo_empleados'].search([]),
#         })

#     @http.route('/modulo_empleados/modulo_empleados/objects/<model("modulo_empleados.modulo_empleados"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_empleados.object', {
#             'object': obj
#         })
