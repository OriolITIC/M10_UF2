# -*- coding: utf-8 -*-
from odoo import http


class SeguimientoImpactoSocial(http.Controller):
    @http.route('/seguimiento_impacto_social/seguimiento_impacto_social', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/seguimiento_impacto_social/seguimiento_impacto_social/objects', auth='public')
    def list(self, **kw):
        return http.request.render('seguimiento_impacto_social.listing', {
            'root': '/seguimiento_impacto_social/seguimiento_impacto_social',
            'objects': http.request.env['seguimiento_impacto_social.seguimiento_impacto_social'].search([]),
        })

    @http.route('/seguimiento_impacto_social/seguimiento_impacto_social/objects/<model("seguimiento_impacto_social.seguimiento_impacto_social"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('seguimiento_impacto_social.object', {
            'object': obj
        })
