from odoo import models, fields, api

class ShareTransaction(models.Model):
    _name = 'share.management.transaction'
    _description = 'Share Transaction'

    shareholder_id = fields.Many2one('share.management.shareholder', string='Shareholder', required=True)
    type = fields.Selection([('buy', 'Buy'), ('sell', 'Sell'), ('transfer', 'Transfer')], string='Type', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    price_per_share = fields.Float(string='Price per Share')
    amount = fields.Float(string='Amount', compute='_compute_amount', store=True)
    receiver_id = fields.Many2one('share.management.shareholder', string='Receiver')
    date = fields.Date(string='Date', default=fields.Date.today)

    @api.depends('quantity', 'price_per_share')
    def _compute_amount(self):
        for record in self:
            record.amount = record.quantity * record.price_per_share if record.price_per_share else 0.0

    @api.model
    def create(self, vals):
        record = super(ShareTransaction, self).create(vals)
        record._update_shareholder()
        return record

    def _update_shareholder(self):
        for record in self:
            shareholder = record.shareholder_id
            if record.type == 'buy':
                shareholder.total_shares += record.quantity
                shareholder.total_invested += record.amount
            elif record.type == 'sell':
                shareholder.total_shares -= record.quantity
                shareholder.total_invested -= record.amount
            elif record.type == 'transfer':
                shareholder.total_shares -= record.quantity
                record.receiver_id.total_shares += record.quantity