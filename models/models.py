# -*- coding: utf-8 -*-
# Part of BossPacific. See LICENSE file for full copyright and licensing details.

import re
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class product_shelf(models.Model):
#    _inherit = ['website']
    _name = 'product_shelf'
    _description = 'Product Category Management'

    name = fields.Char('Name')
    address = fields.Char('Address')


class searchById:
    def searchByCatId(self, categ_id):
        self.env.cr.execute("""
            SELECT id
            FROM product_category
            WHERE complete_name = '%s' """)
        return [categ_id[0] for complete_name in self.env.cr.fetchall()]
