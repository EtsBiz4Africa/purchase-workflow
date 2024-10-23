# Copyright (C) 2022 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models
from odoo.tools import is_html_empty


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("partner_id", "company_id")
    def onchange_partner_id(self):
        for order in self:
            if not is_html_empty(order.partner_id.purchase_note):
                order.update({"notes": order.partner_id.purchase_note})
            elif not is_html_empty(order.company_id.purchase_note):
                order.update({"notes": order.company_id.purchase_note})
            return super().onchange_partner_id()
