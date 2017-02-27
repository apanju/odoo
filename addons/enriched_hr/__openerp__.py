# -*- coding: utf-8 -*-
{
    'name': 'Modifications to Odoo Human Resources by Enriched Solutions Ltd.',
    'version': '1.0',
    'sequence': 1,
    'complexity': "easy",
    'category': 'Enriched',
    'description': """
Add fields to HR records and display these
    """,
    'author': 'Enriched Solutions Ltd.',
    'website': 'enrichedsolutions.com',
    'depends': ["hr"],
    'init_xml': [],
    'data': [
        "enriched_hr_view.xml"
    ],
    'js': [],
    'css': [],
    'demo_xml': [],
    'test': [],
    'qweb' : [],
    'installable': True,
    'auto_install': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
