# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
# from odoo.osv import expression
# from odoo.exceptions import UserError, ValidationError
# from bisect import bisect_left
# from collections import defaultdict
# import re

class ProdCons(models.Model):
    _name = "gei.prod_cons"
    _description = "contact of gei consumer or producer"

    firstname = fields.Char(string="Vorname", required = True)
    surename = fields.Char(string="Nachname", required = True)
    persontype = fields.Selection([
        ('private','Privatperson'),
        ('enterprise','Unternehmen')],
        required = True, default = 'private'
    )
    customer_number = fields.Integer(string="Kundennummer", required=True)

