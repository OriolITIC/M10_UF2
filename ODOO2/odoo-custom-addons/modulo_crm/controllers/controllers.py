# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloCrm(http.Controller):
#     @http.route('/modulo_crm/modulo_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_crm/modulo_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_crm.listing', {
#             'root': '/modulo_crm/modulo_crm',
#             'objects': http.request.env['modulo_crm.modulo_crm'].search([]),
#         })

#     @http.route('/modulo_crm/modulo_crm/objects/<model("modulo_crm.modulo_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_crm.object', {
#             'object': obj
#         })
