# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class project_phase(osv.osv):
    _name = "enriched_project.project_phase"
    _description = "Phase of project"
    _order = "sequence"

    _columns = {
        'name': fields.char('Phase Name', required=True, translate=True),
        'description': fields.text('Description'),
        'sequence': fields.integer('Sequence'),
    }

    _defaults = {
        'sequence': 1
    }

class project(osv.osv):
    _description = "Project"
    _inherit = 'project.project'

    def _get_project_number(self, cr, uid,context, *args):
        obj_sequence = self.pool.get('ir.sequence')
        return obj_sequence.next_by_code(cr, uid, 'enrichedprojectsequencecode', context=context)

    _columns = {
        'role_client_qs_id': fields.many2one('res.partner', 'Client QS'),
        'role_client_architect_id': fields.many2one('res.partner', 'Client Architect'),
        'role_client_main_contractor_id': fields.many2one('res.partner', 'Main Contractor'),
        'role_qs_id': fields.many2one('res.users', 'QS'),
        'role_main_fundi_id': fields.many2one('res.users', 'Main Fundi'),
        'role_primary_supervisor_id': fields.many2one('res.users', 'Primary Supervisor'),
        'project_number' : fields.char('Project Number', size=64),
        'priority' : fields.selection([('normal','Normal'), ('high','High'),('very_high','Very High'),('landmark','Landmark')], 'Priority'),
        'accounting_book' : fields.selection([('book_a','Book A'), ('book_b','Book B')], 'Accounting book'),
    }

    _defaults = { 'project_number': _get_project_number, }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: