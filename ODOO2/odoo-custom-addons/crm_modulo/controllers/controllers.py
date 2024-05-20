# -*- coding: utf-8 -*-
# from odoo import http


class CrmModulo(http.Controller):
    @http.route('/crm_modulo/crm_modulo', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/crm_modulo/crm_modulo/objects', auth='public')
    def list(self, **kw):
        return http.request.render('crm_modulo.listing', {
            'root': '/crm_modulo/crm_modulo',
            'objects': http.request.env['crm_modulo.crm_modulo'].search([]),
        })

    @http.route('/crm_modulo/crm_modulo/objects/<model("crm_modulo.crm_modulo"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('crm_modulo.object', {
            'object': obj
        }) 