##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
try:
    from base64 import encodebytes
except ImportError:  # 3+
    from base64 import encodestring as encodebytes

import logging
import re
from ast import literal_eval

from odoo import _, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class AccountVatLedger(models.Model):

    _inherit = "account.vat.ledger"
    _order = "date_from desc"

    def get_vat_import(self, vat, code):
        import_vat = 0
        for v in vat:
            if v['Id'] == code:
                import_vat = import_vat + v['Importe']
        return import_vat
