# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class purchase_order(osv.Model):      

    _inherit = "purchase.order"

    def wkf_confirm_order(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'date_confirm': fields.date.context_today(self,cr,uid,context=context)})
        return super(purchase_order, self).wkf_confirm_order(cr, uid, ids, context=context)

    _columns = {
        'date_confirm': fields.date('Date Confirmed', readonly=1,
                                   help="Date on which purchase order has been confirmed"),        
    }