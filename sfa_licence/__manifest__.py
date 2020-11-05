# -*- coding: utf-8 -*-
{
    'name': "Licences",
    'summary': """
        Application
    """,
    'description': """
        Display Application and stages
    """,
    'athor': "Advance Africa",
    'website': "http://www.advanceafrica.co.za",
    # 'category': 'website',

    'version': '0.26',

    # 'depends': ['base'],
    'depends' : ['portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/application_view.xml',
        'views/license_cancel_view.xml',
        'wizard/cancel_license_wizard.xml',
    ],
    'installable': True,
    'auto_install': False,
}
