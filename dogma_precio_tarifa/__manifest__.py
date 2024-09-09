# -*- coding: utf-8 -*-
{
    'name': "Agrega columna en lista de productos, con el precio calculado tarifa",
    'description': """
        Agrega columna en lista de productos, con el precio calculado tarifa
    """,
    'category': 'Ventas',
    'version': '20230827',
    'depends': ['stock','purchase','sale_management','sale','account'],
    'data': [
        'views/sale_views.xml',
    ],
    'license': 'AGPL-3',
}
