# -*- coding: utf-8 -*-
{
    'name': "jwt auth api",

    'summary': "for mobile and other system that use jwt as an authentication method ",

    'description': "for mobile and other system that use jwt as an authentication method ",

    'author': "Mahmoud",
    'website': "https://www.mah007.net",

    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'sequence': 10,

}
