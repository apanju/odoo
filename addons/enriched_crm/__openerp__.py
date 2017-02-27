# -*- coding: utf-8 -*-
{
    'name': 'Modifications to Odoo CRM (Contacts) by Enriched Solutions Ltd.',
    'version': '1.0',
    'sequence': 1,
    'complexity': "easy",
    'category': 'Enriched',
    'description': """
Add fields to contact records and display these
    """,
    'author': 'Enriched Solutions Ltd.',
    'website': 'enrichedsolutions.com',
    'depends': ["crm"],
    'init_xml': [],
    'data': [
        "enriched_crm_view.xml"
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
