from odoo import models, fields

class ShareDividend(models.Model):
    _name = 'share.management.dividend'
    _description = 'Share Dividend'

    shareholder_id = fields.Many2one('share.management.shareholder', string='Shareholder', required=True)
    amount = fields.Float(string='Amount', required=True)
    date = fields.Date(string='Date', default=fields.Date.today)