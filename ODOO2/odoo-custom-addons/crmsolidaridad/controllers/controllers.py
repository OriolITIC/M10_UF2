# -*- coding: utf-8 -*-
from odoo import http


class Crmsolidaridad(http.Controller):
    @http.route('/crmsolidaridad/crmsolidaridad', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/crmsolidaridad/crmsolidaridad/objects', auth='public')
    def list(self, **kw):
        return http.request.render('crmsolidaridad.listing', {
            'root': '/crmsolidaridad/crmsolidaridad',
            'objects': http.request.env['crmsolidaridad.crmsolidaridad'].search([]),
        })

    @http.route('/crmsolidaridad/crmsolidaridad/objects/<model("crmsolidaridad.crmsolidaridad"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('crmsolidaridad.object', {
            'object': obj
        })
