# -*- coding: utf-8 -*-
from odoo import http


class ImpactoSocial(http.Controller):
    @http.route('/impacto_social/impacto_social', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/impacto_social/impacto_social/objects', auth='public')
    def list(self, **kw):
        return http.request.render('impacto_social.listing', {
            'root': '/impacto_social/impacto_social',
            'objects': http.request.env['impacto_social.impacto_social'].search([]),
        })

    @http.route('/impacto_social/impacto_social/objects/<model("impacto_social.impacto_social"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('impacto_social.object', {
            'object': obj
        })
