# -*- coding: utf-8 -*-


{
    'name': 'product_shelf',
    'category': 'Tools',
    'author': 'Chiran Kandel',
    'summary': 'View database products in well-organised manner.',
    'description': """
This module is designed to enhance drag and functionality to manage the category of products stored in the postgres.
""",
    'version': '1.0',
    'depends': ['base', 'website', 'product'],
    'data': [
        'demo/demo_data.xml',
        'security/ir.model.access.csv',
        'views/product_category_views.xml',
        'static/src/xml/templates.xml'
    ],
    'application': True,
}