# -*- coding: utf-8 -*-
{
    'name': 'Online Input Formular',
    'version': '1.0',
    'summary': 'Online Input Formular Produzierende Konsumierende',
    'sequence': -100,
    'description': """Manage Daten von Produzierenden und Konsumierenden der GEI""",
    'category': 'Productivity',
    'depends': ['mail','website','sale'],
    'data': [
        'views/website_form_consumer.xml',
        'views/website_form_consumer_old.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
