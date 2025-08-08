# Share Management System

## Purpose
This Odoo module manages shareholders, share transactions (buy/sell/transfer), dividends, and provides a dashboard.

## Installation
1. Place `share_management` in your Odoo addons directory.
2. Update apps list: `./odoo-bin -c <config-file> --update-apps`.
3. In Odoo UI, go to Apps, search "Share Management System", and install.

## Testing
1. Log in as a Share Manager (assign group in Users settings).
2. Go to Share Management > Shareholders, create a shareholder (e.g., Name="Alice Brown", Total Shares=100, Total Invested=1000).
3. Go to Transactions, create a buy transaction (Quantity=50, Price per Share=10).
4. Go to Dividends, create a dividend (Amount=400).
5. Verify shareholder form updates: Total Shares=150, Total Invested=1500, Dividend Received=400.
6. Go to Dashboard, verify pie chart shows share distribution.
7. Log in as Share Viewer, verify read-only access.