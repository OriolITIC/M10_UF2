# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectosSolidaridad(http.Controller):
#     @http.route('/proyectos_solidaridad/proyectos_solidaridad', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyectos_solidaridad/proyectos_solidaridad/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyectos_solidaridad.listing', {
#             'root': '/proyectos_solidaridad/proyectos_solidaridad',
#             'objects': http.request.env['proyectos_solidaridad.proyectos_solidaridad'].search([]),
#         })

#     @http.route('/proyectos_solidaridad/proyectos_solidaridad/objects/<model("proyectos_solidaridad.proyectos_solidaridad"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyectos_solidaridad.object', {
#             'object': obj
#         })
