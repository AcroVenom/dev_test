# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerLedgerExtend(http.Controller):
#     @http.route('/partner_ledger_extend/partner_ledger_extend', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_ledger_extend/partner_ledger_extend/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_ledger_extend.listing', {
#             'root': '/partner_ledger_extend/partner_ledger_extend',
#             'objects': http.request.env['partner_ledger_extend.partner_ledger_extend'].search([]),
#         })

#     @http.route('/partner_ledger_extend/partner_ledger_extend/objects/<model("partner_ledger_extend.partner_ledger_extend"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_ledger_extend.object', {
#             'object': obj
#         })
