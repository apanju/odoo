from openerp.osv import fields, osv

class hr_employee(osv.osv):
    _inherit = "hr.employee"

    _columns = {
        'employee_joining_date'                     : fields.date('Joining Date'),
        'employee_blood_group'                      : fields.selection([('a_pos','A+'), ('a_neg','A-'),('b_pos','B+'), ('b_neg','B-'),('o_pos','O+'), ('o_neg','O-'),('ab_pos','AB+'), ('ab_neg','AB-'),], 'Blood Group'),
        'employee_emergency_contact_name'           : fields.char('Name'),
        'employee_emergency_contact_number'         : fields.char('Contact Number'),
        'employee_emergency_contact_relationship'   : fields.char('Relationship to Employee'),
        'hr_address_w3w'                            : fields.char('W3W Address', size=64),
        'hr_is_tuico_member'                        : fields.boolean('Is Tuico member'),
        'hr_tuico_joining_date'                     : fields.date('Tuico joining date'),
        'hr_nssf_id'                                : fields.char('NSSF ID', size=64),
        'hr_nssf_enrolment_date'                    : fields.date('NSSF Enrolment date'),
        'hr_paye_id'                                : fields.char('PAYE ID', size=64),
        'hr_paye_enrolment_date'                    : fields.date('PAYE Enrolment date'),
        'hr_address'                                : fields.text('Employee Address'),
        'hr_place_of_recruitment'                   : fields.char('Place of recruitment', size=64)
    }