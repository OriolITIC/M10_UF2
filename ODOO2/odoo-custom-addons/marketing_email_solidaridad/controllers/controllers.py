# -*- coding: utf-8 -*-
from odoo import http


class MarketingEmailSolidaridad(http.Controller):
    @http.route('/marketing_email_solidaridad/marketing_email_solidaridad', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/marketing_email_solidaridad/marketing_email_solidaridad/objects', auth='public')
    def list(self, **kw):
        return http.request.render('marketing_email_solidaridad.listing', {
            'root': '/marketing_email_solidaridad/marketing_email_solidaridad',
            'objects': http.request.env['marketing_email_solidaridad.marketing_email_solidaridad'].search([]),
        })

    @http.route('/marketing_email_solidaridad/marketing_email_solidaridad/objects/<model("marketing_email_solidaridad.marketing_email_solidaridad"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('marketing_email_solidaridad.object', {
            'object': obj
        })
