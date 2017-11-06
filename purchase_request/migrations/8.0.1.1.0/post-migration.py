# -*- coding: utf-8 -*-
# Copyright 2017 Eficent - Miquel Raich
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def populate_purchase_request_picking_type_id(cr):
    openupgrade.logged_query(
        cr,
        """
        UPDATE purchase_request pr
        SET picking_type_id = stock_picking_type.id
        FROM stock_picking_type
        WHERE pr.picking_type_id is NULL and stock_picking_type.id in 
            (SELECT id
             FROM stock_picking_type spt
             WHERE pr.%s = spt.warehouse_id and spt.code = 'incoming'
             LIMIT 1)
        """ % openupgrade.get_legacy_name('warehouse_id'),
    )


@openupgrade.migrate()
def migrate(env, version):
    populate_purchase_request_picking_type_id(env.cr)
