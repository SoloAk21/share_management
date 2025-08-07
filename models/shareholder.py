from odoo import models, fields

class Shareholder(models.Model):
    _name = 'share.management.shareholder'
    _description = 'Shareholder'

    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    total_shares = fields.Float(string='Total Shares', default=0.0)
    total_invested = fields.Float(string='Total Invested', default=0.0)
    share_percent = fields.Float(string='Share Percentage', compute='_compute_share_percent', store=True)
    dividend_received = fields.Float(string='Dividend Received', compute='_compute_dividend_received', store=True)

    def _compute_share_percent(self):
        total_shares_all = sum(self.env['share.management.shareholder'].search([]).mapped('total_shares'))
        for record in self:
            record.share_percent = (record.total_shares / total_shares_all * 100) if total_shares_all else 0.0

    def _compute_dividend_received(self):
        for record in self:
            dividends = self.env['share.management.dividend'].search([('shareholder_id', '=', record.id)])
            record.dividend_received = sum(dividends.mapped('amount'))