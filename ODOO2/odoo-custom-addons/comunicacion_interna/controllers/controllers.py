# -*- coding: utf-8 -*-
# from odoo import http


# class ComunicacionInterna(http.Controller):
#     @http.route('/comunicacion_interna/comunicacion_interna', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comunicacion_interna/comunicacion_interna/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('comunicacion_interna.listing', {
#             'root': '/comunicacion_interna/comunicacion_interna',
#             'objects': http.request.env['comunicacion_interna.comunicacion_interna'].search([]),
#         })

#     @http.route('/comunicacion_interna/comunicacion_interna/objects/<model("comunicacion_interna.comunicacion_interna"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comunicacion_interna.object', {
#             'object': obj
#         })
