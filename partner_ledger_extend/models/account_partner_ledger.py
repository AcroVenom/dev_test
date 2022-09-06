from odoo import _,models, fields, api

class ReportPartnerLedger(models.AbstractModel):
    _inherit = "account.partner.ledger"

    def _get_columns_name(self, options):
        columns = super(ReportPartnerLedger, self)._get_columns_name(options)
        columns.insert(4,{'name': _('Invoice Date'), 'class':'date'})
        columns.insert(5,{'name': _('Customer Reference')})
        return columns

    @api.model
    def _get_report_line_move_line(self, options, partner, aml, cumulated_init_balance, cumulated_balance):
        res = super(ReportPartnerLedger, self)._get_report_line_move_line(options, partner, aml, cumulated_init_balance,cumulated_balance)
        res['columns'].insert(3,{'name': aml['date']})
        res['columns'].insert(4,{'name': aml['ref']})
        return res
