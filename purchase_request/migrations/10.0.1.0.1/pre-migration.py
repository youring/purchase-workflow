# -*- coding: utf-8 -*-
# Copyright 2017 bloopark systems (<http://bloopark.de>)
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def force_fields_to_recompute(cr):
    cr.execute("""SELECT column_name
    FROM information_schema.columns
    WHERE table_name='purchase_request_line' AND
    column_name='purchase_state'""")
    if cr.fetchone():
        cr.execute("""
            alter table purchase_request_line drop column purchase_state;
        """)


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    force_fields_to_recompute(env.cr)
