# -*- coding: utf-8 -*-
# newliine
{
    'name': 'Custom Inheritance',
    'version': '1.0',
    'summary': 'Manage Daten von Produzierenden und Konsumierenden der GEI',
    'sequence': -100,
    'description': """Manage Daten von Produzierenden und Konsumierenden der GEI""",
    'category': 'Productivity',
    'depends': ['sale'],
    'data': ['data/mail_template_notification.xml',
             'data/mail_template_notification_us_new_customer.xml',
             'views/partner_form_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
