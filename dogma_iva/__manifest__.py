# For copyright and license notices, see __manifest__.py file in module root
# directory or check the readme files

{
    "name": "VAT Ledger for Argentina",
    "version": "16.0.0.0.2",
    "category": "Accounting",
    "license": "AGPL-3",
    "summary": "VAT Ledger, VAT Digital Ledger and VAT Reports for Argentina",
    "author": "Odoo Community Association (OCA), Codize, Exemax, ADHOC SA, Moldeo Interactive",
    "website": "https://github.com/OCA/l10n-argentina",
    "depends": ["base", "l10n_ar", "report_xlsx", "l10n_ar_reports"],
    "external_dependencies": {},
    "data": [
        "report/account_vat_ledger.xml",
    ],
    "maintainers": ["Walter"],
    "installable": True,
}
