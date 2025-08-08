{
    'name': 'Share Management System',
    'version': '1.0',
    'summary': 'Manage shareholders, transactions, and dividends',
    'depends': ['base', 'contacts'],
    'data': [
        'security/share_management_security.xml',
        'security/ir.model.access.csv',
        'views/share_transaction_views.xml',
        'views/share_dividend_views.xml',   
        'views/shareholder_views.xml',
        'views/share_management_menus.xml',
        'views/share_dashboard_views.xml',
    ],
    'installable': True,
    'application': True,
}