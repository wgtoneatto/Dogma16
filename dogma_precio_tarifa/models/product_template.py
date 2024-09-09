# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    # _inherit = ['product.template', 'product.pricelist']

    def _mostrar_precios_tarifa(self):
        pricelist_ids = self.env['product.pricelist'].search([])
        #_logger.info('************ {0}'.format(pricelist_ids) )

        for product in self:
            for x in range(0,len(pricelist_ids)):
                pricelist_id = pricelist_ids[x]
                tax = (product.taxes_id[0].amount/100)+1
                if x == 0:
                    product.precio_tarifa = pricelist_id._get_product_price(product, 1) * tax
                if x == 1:
                    product.precio_tarifa_1 = pricelist_id._get_product_price(product, 1) * tax
                if x == 2:
                    product.precio_tarifa_2 = pricelist_id._get_product_price(product, 1) * tax / 3
                if x == 3:
                    product.precio_tarifa_3 = pricelist_id._get_product_price(product, 1) * tax / 6
                if x == 4:
                    product.precio_tarifa_4 = pricelist_id._get_product_price(product, 1) * tax / 12
                if x == 5:
                    product.precio_tarifa_5 = pricelist_id._get_product_price(product, 1) * tax / 3
                if x == 6:
                    product.precio_tarifa_6 = pricelist_id._get_product_price(product, 1) * tax / 6
               

    precio_tarifa = fields.Monetary(string='3_Cuotas_s/int', compute='_mostrar_precios_tarifa')
    precio_tarifa_1 = fields.Monetary(string='6_Cuotas_s/int', compute='_mostrar_precios_tarifa')
    precio_tarifa_2 = fields.Monetary(string='Efectivo-15%', compute='_mostrar_precios_tarifa')
    precio_tarifa_3 = fields.Monetary(string='Transferencia/QR-10%', compute='_mostrar_precios_tarifa')
    precio_tarifa_4 = fields.Monetary(string='Plan_Z', compute='_mostrar_precios_tarifa')
    precio_tarifa_5 = fields.Monetary(string='9_Cuotas', compute='_mostrar_precios_tarifa')
    precio_tarifa_6 = fields.Monetary(string='12_Cuotas', compute='_mostrar_precios_tarifa')
