# -*- coding: utf-8 -*-
{
    'name': 'Modifications to Odoo by Enriched Solutions Ltd.',
    'version': '1.0',
    'sequence': 1,
    'complexity': "easy",
    'category': 'Enriched',
    'description': """
Add static links to other Enriched services (import, issue management)

Remove some ``Phone Home`` features from core Odoo 8.0:
-------------------------------------------------------
* Stop Scheduler for Sending Company/Database information to Odoo/OpenERP company.
* Remove ``Your OpenERP is not supported.``.
* Change sequence of the ``Apps`` and ``Update`` menu and arrange ``Installed Modules`` at first position.

Thanks to: Ruchir Shukla (www.bizzappdev.com) for module ``Stop Phoning Home``
    """,
    'author': 'Enriched Solutions Ltd.',
    'website': 'enrichedsolutions.com',
    'depends': ["mail",'web'],
    'init_xml': [],
    'data': [
        "base_view.xml",
        "mail_data.xml",
        "webclient_templates.xml",
        "static_links_view.xml"
    ],
    'js': ['static/src/js/enriched.js'],
    'css': ['static/src/css/enriched.css'],
    'demo_xml': [],
    'test': [],
    'qweb' : ["static/src/xml/base.xml"],
    'installable': True,
    'auto_install': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
