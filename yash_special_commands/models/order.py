from odoo import fields, models
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_partner_ids = fields.Many2many(
        "res.partner", "custom_partner_rel", string=_("Custom Partner Ids")
    )

    def mail_wizard_button(self):
        print("\n\n\n\n\n Mail Wizard Button")
        self.custom_partner_ids = [(5,)]
        [0, 0, {}]
        range_list = []
        for i in range(0, 2):
            cust_dict = {"name": i}
            range_list.append(cust_dict)
        for val in range_list:
            print(":-=>)", val)
            self.custom_partner_ids = [(0, 0, val)]
        # self.custom_partner_ids= [(6,0,[14,23,33])]
        # self.custom_partner_ids = [(4,27)]
        # self.custom_partner_ids= [(2,44)] #Delete
        # self.custom_partner_ids= [(1,43,{'phone':'8460232337'})]
