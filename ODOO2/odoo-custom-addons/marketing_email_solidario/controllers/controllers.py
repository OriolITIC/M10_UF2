# -*- coding: utf-8 -*-
from odoo import http


class MarketingEmailSolidario(http.Controller):
    @http.route('/marketing_email_solidario/marketing_email_solidario', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/marketing_email_solidario/marketing_email_solidario/objects', auth='public')
    def list(self, **kw):
        return http.request.render('marketing_email_solidario.listing', {
            'root': '/marketing_email_solidario/marketing_email_solidario',
            'objects': http.request.env['marketing_email_solidario.marketing_email_solidario'].search([]),
        })

    @http.route('/marketing_email_solidario/marketing_email_solidario/objects/<model("marketing_email_solidario.marketing_email_solidario"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('marketing_email_solidario.object', {
            'object': obj
        })
