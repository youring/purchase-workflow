# -*- coding: utf-8 -*-
# Copyright 2017 Eficent - Miquel Raich
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def map_product_template_purchase_request(cr):
    openupgrade.logged_query(
        cr,
        """
        UPDATE product_template pt
        SET purchase_request = pp.%s
        FROM product_product pp
        WHERE pp.%s is not NULL
        """ % (openupgrade.get_legacy_name('purchase_request'),
               openupgrade.get_legacy_name('purchase_request'))
    )


@openupgrade.migrate()
def migrate(env, version):
    map_product_template_purchase_request(env.cr)
