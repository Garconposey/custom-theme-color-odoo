# -*- coding: utf-8 -*-
{
    'name': 'Custom Theme Colors',
    'version': '18.0.1.0.0',
    'summary': 'Personnalisation des couleurs Odoo',
    'description': """
        Module pour personnaliser les couleurs de l'interface Odoo.
        Change la couleur principale de violet vers votre couleur préférée.
    """,
    'category': 'Hidden',
    'author': 'Auxil HOUESSOU',
    'website': '',
    'depends': ['web', 'mail'],
    'data': [
        'data/color_config.xml',
        'views/email_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_theme/static/src/css/variables.css',
            'custom_theme/static/src/css/custom.css',
        ],
        'web.assets_frontend': [
            'custom_theme/static/src/css/variables.css',
            'custom_theme/static/src/css/custom.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}