# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Inheritance_test(models.Model):
    # _name = "inheritance.test"
    _inherit = ["sale.order"]
    confirmed_user_id =fields.Many2one('res.users',string='Confirmed User')

    def delete_sale_order(self):
        """Method to delete the sale order."""
        self.unlink()

