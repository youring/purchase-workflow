# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
#           <contact@eficent.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase Invoice Status",
    "summary": "Compute the invoice status for purchase orders",
    "version": "9.0.1.0.0",
    "category": "Purchases",
    "website": "https://github.com/OCA/account-invoicing",
    "author": "Eficent, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "purchase",
    ],
    "data": [
        "views/purchase_view.xml",
    ],
}
