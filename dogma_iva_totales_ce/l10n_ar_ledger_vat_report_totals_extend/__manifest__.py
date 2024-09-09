# -*- coding: utf-8 -*-
{
    'name': "Totales reporte de IVA Argentina",
    'description': """
        Extiende los reportes de IVA para agregar totales por:
        - Tipo de responsable ante el AFIP
        - Tipo de comprobante
        - Otros totales
    """,
    'category': 'Accounting',
    'version': '16.0.1.0.1',
    'depends': ['dogma_iva'],
    'data': [
        'views/l10n_ar_ledger_report_templates.xml'
    ],
    'license': 'AGPL-3',
}
