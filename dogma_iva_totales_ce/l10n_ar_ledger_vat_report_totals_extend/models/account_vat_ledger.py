# -*- coding: utf-8 -*-

from odoo import api, models


class AccountVatLedger(models.Model):

    _inherit = 'account.vat.ledger'

    @api.model
    def get_total_by_document_type(self):
        totals_group = dict()
        for record in self:
            for invoice in record.invoice_ids:
                document_type = invoice.move_id.l10n_latam_document_type_id
                self._cumpute_totals_group(
                    invoice, document_type, totals_group)
        return totals_group

    @api.model
    def get_total_by_afip_responsibility_type(self):
        totals_group = dict()
        for record in self:
            for invoice in record.invoice_ids:
                responsibility_type = invoice.partner_id.\
                    l10n_ar_afip_responsibility_type_id
                self._cumpute_totals_group(
                    invoice, responsibility_type, totals_group)
        return totals_group

    def _cumpute_totals_group(self, invoice, group_object, totals_group):
        is_credit = invoice.move_id.l10n_latam_document_type_id\
            .internal_type == 'credit_note'
        if group_object.id not in totals_group:
            totals_group.update({
                group_object.id: {
                    'tipo': group_object.name,
                    'neto_gravado': 0,
                    'neto_no_gravado': 0,
                    'neto_exento': 0,
                    'iva_27': 0,
                    'iva_21': 0,
                    'iva_10_5': 0,
                    'otros': 0,
                    'total_gravado': 0,
                    'total': 0,
                    'currency': invoice.move_id.currency_id
                }
            })

        total = totals_group.get(group_object.id)
        for amount in invoice.move_id.tax_totals['groups_by_subtotal']['Base imponible']:
            tax_name = amount['tax_group_name']
            tax_amount = amount['tax_group_amount'] * -1 if is_credit else amount['tax_group_amount']
            base_amount = amount['tax_group_base_amount'] * -1 if is_credit else amount['tax_group_base_amount']

            if tax_name in ['IVA 21%', 'IVA 10.5%', 'IVA 27%']:
                total['neto_gravado'] += base_amount
            elif tax_name in ['IVA No Gravado', 'IVA 0%']:
                total['neto_no_gravado'] += base_amount
            elif tax_name == 'IVA Exento':
                total['neto_exento'] += base_amount
            else:
                total['otros'] += tax_amount

            if tax_name == 'IVA 27%':
                total['iva_27'] += tax_amount
            elif tax_name == 'IVA 21%':
                total['iva_21'] += tax_amount
            elif tax_name == 'IVA 10.5%':
                total['iva_10_5'] += tax_amount

        total['total_gravado'] = (
            total['neto_gravado'] +
            total['iva_27'] +
            total['iva_21'] +
            total['iva_10_5']
        )
        total['total'] += (
            invoice.move_id.amount_total * -1 if is_credit else invoice.move_id.amount_total
        )

    def get_total_other_taxes(self):
        totals_group = dict()
        for record in self:
            for invoice in record.invoice_ids:
                is_credit = invoice.move_id.l10n_latam_document_type_id\
                    .internal_type == 'credit_note'
                for amount in invoice.move_id.tax_totals['groups_by_subtotal']['Base imponible']:
                    tax_id = amount['tax_group_id']
                    tax_name = amount['tax_group_name']
                    tax_amount = amount['tax_group_amount'] * -1 if is_credit else amount['tax_group_amount']
                    taxes_excluded = [
                        'IVA 21%',
                        'IVA 10.5%',
                        'IVA 27%',
                        'IVA No Gravado',
                        'IVA 0%',
                        'IVA Exento'
                    ]

                    if tax_name not in taxes_excluded:
                        if tax_id not in totals_group:
                            totals_group.update({
                                tax_id: {
                                    'tipo': tax_name,
                                    'total': 0,
                                    'currency': invoice.move_id.currency_id
                                }
                            })

                        total = totals_group.get(tax_id)
                        total['total'] += tax_amount
        return totals_group
