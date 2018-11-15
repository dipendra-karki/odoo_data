# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Timesheet Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['l10n_be', 'sale_data', 'timesheet_data', 'sale_timesheet'],
    'data': [
        'data/project_data.xml',
        'data/product_data.xml',
        'data/sale_data.xml',
        'data/timesheet_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
