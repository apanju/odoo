# -*- coding: utf-8 -*-
{
    'name': 'Enriched Project Management by Enriched Solutions Ltd.',
    'version': '1.0',
    'author': 'Enriched Solutions Ltd.',
    'website': 'https://enrichedsolutions.com',
    'category': 'Enriched',
    'sequence': 8,
    'summary': 'Projects, Tasks',
    'depends': [
        'project'
    ],
    'description': """
Project and Task extensions to built-in Project Management
==========================================================

* New field of ``phase`` for a project
* New fields for taks including concept of dependant tasks
""",
    'data': [
        'enriched_project_view.xml',
        'enriched_project_data.xml'
    ],
    'demo': [],
    'test': [
    ],
    'init_xml': ['project_numbers.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
