# -*- coding: utf-8 -*-
{
    'name': 'Enriched Fleet by Enriched Solutions Ltd.',
    'version': '1.0',
    'author': 'Enriched Solutions Ltd.',
    'website': 'https://enrichedsolutions.com',
    'category': 'Enriched',
    'sequence': 9,
    'summary': 'Enhanced Vehicle',
    'depends': [
        'fleet'
    ],
    'description': """
Enhanced Vehicle
==================================
This module adds fields (and views) to the standard fleet module

Main Features
-------------
* Vehicle type (Car, Bike, Truck, Mini Bus)
* Fuel type ad engine size
* Status (New, In Use, To Sell)
* Old Plate Number
* Other contracts like city permits
* Number of Keys
""",
    'data': [
            'enriched_fleet_cars.xml',
            'enriched_fleet_data.xml',
            'enriched_fleet_view.xml'
            ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
