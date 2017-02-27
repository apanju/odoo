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

    STATES = [
        ('pre_quote','Pre Quotation'),
        ('quote','Quotation'),
        ('confirmed','Confirmed'),
        ('final_measure','Final Measurements'),
        ('adv_pay','Advance Payment'),
        ('material_order','Materials Order'),
        ('in_prod','In Production'),
        ('ready_to_deliver','Ready To Deliver'),
        ('material_on_site','Material on Site'),
        ('installation','Installation'),
        ('snag_clean','Snagging / Cleaning'),
        ('ready_for_handover','Ready for Handover'),
        ('works_completed','Works Completed'),
        ('final_payment_pending','Final Payment Pending'),
        ('retention_pending','Retention Pending'),
        ('file_closed','File Closed'),
    ]

    # States that should be folded in Kanban view
    # used by the `state_groups` method
    FOLDED_STATES = [
        'file_closed',
    ]

    def project_state_groups_2(self, cr, uid, ids, domain, read_group_order=None, access_rights_uid=None, context=None):
        # folded is a dictionary of states whose values are true/false to be folded by default in kanban view

        folded = {key: (key in self.FOLDED_STATES) for key, _ in self.STATES}
        # Need to copy self.STATES list before returning it,
        # because odoo modifies the list it gets,
        # emptying it in the process. Bad odoo!
        return self.STATES[:], folded

    _group_by_full = {
        'project_state': project_state_groups_2
    }

    def _read_group_fill_results(self, cr, uid, domain, groupby, remaining_groupbys,
                                 aggregated_fields, count_field,
                                 read_group_result, read_group_order=None, context=None):

        """
        The method seems to support grouping using m2o fields only,
        while we want to group by a simple status field.
        Hence the code below - it replaces simple status values
        with (value, name) tuples.
        """
        if groupby == 'project_state':
            STATES_DICT = dict(self.STATES)
            for result in read_group_result:
                state = result['project_state']
                result['project_state'] = (state, STATES_DICT.get(state))

        return super(project, self)._read_group_fill_results(
            cr, uid, domain, groupby, remaining_groupbys, aggregated_fields,
            count_field, read_group_result, read_group_order, context)

    _columns = {
        'role_client_qs_id': fields.many2one('res.partner', 'Client QS'),
        'role_client_architect_id': fields.many2one('res.partner', 'Client Architect'),
        'role_client_main_contractor_id': fields.many2one('res.partner', 'Main Contractor'),
        'role_qs_id': fields.many2one('res.users', 'QS'),
        'role_main_fundi_id': fields.many2one('res.users', 'Main Fundi'),
        'role_primary_supervisor_id': fields.many2one('res.users', 'Primary Supervisor'),
        'project_number' : fields.char('Project Number', size=64),
        'priority' : fields.selection([('0','Normal'), ('1','High'),('2','Very High'),('3','Landmark')], 'Priority'),
        'accounting_book' : fields.selection([('book_a','Book A'), ('book_b','Book B')], 'Accounting book'),
        'project_state' : fields.selection(STATES,'Project State', default='pre_quote'),
        'advance_payment_received': fields.date('Advance Payment Received'),
        'completion_certificate_received': fields.date('Completion Certificate Received'),
        'final_payment': fields.date('Final Payment'),
        'retention': fields.date('Retention'),
        'file_closed': fields.date('File Closed'),
    }

    _defaults = { 'project_number': _get_project_number, }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: