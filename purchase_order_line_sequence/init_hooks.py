# -*- coding: utf-8 -*-
# © 2018 initOS GmbH (<http://www.initos.com>)
# Author: Mathias Francke <mathias.francke at initos.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    """
    Creates columns for sequence and sequence2 and fills them automatically to
    speed up installation process in populated database.
    """
    _logger.info('Working on PRE INIT HOOK...')

    # Add columns
    _logger.info('Adding sequence and sequence2 to purchase_order_line...')
    t_begin = datetime.now()
    cmd = """
        ALTER TABLE purchase_order_line
        ADD COLUMN IF NOT EXISTS sequence  integer,
        ADD COLUMN IF NOT EXISTS sequence2 integer;
        """
    cr.execute(cmd)
    _logger.info('Time needed: %s', (str(datetime.now() - t_begin),))

    # fill new columns with data
    _logger.info('Filling sequence and sequence2 of purchase_order_line with '
                 'initial value (9999)...')
    t_begin = datetime.now()
    cmd = """
        UPDATE purchase_order_line 
           SET sequence = 9999, 
               sequence2 = 9999;
        """
    cr.execute(cmd)
    _logger.info('Time needed: %s', (str(datetime.now() - t_begin),))

    _logger.info('Finished working on PRE INIT HOOK...')
