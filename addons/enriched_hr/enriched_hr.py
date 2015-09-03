from openerp.osv import fields, osv

class hr_employee(osv.osv):
    _inherit = "hr.employee"

    _columns = {
       'employee_joining_date': fields.date('Joining Date'),
       'employee_blood_group' : fields.selection([('a_pos','A+'), ('a_neg','A-'),('b_pos','B+'), ('b_neg','B-'),('o_pos','O+'), ('o_neg','O-'),('ab_pos','AB+'), ('ab_neg','AB-'),], 'Blood Group'),
       'employee_emergency_contact_name': fields.char('Name'),
       'employee_emergency_contact_number': fields.char('Contact Number'),
       'employee_emergency_contact_relationship': fields.char('Relationship to Employee')
    }