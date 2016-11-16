from openerp.osv import fields, osv

class hr_employee(osv.osv):
    _inherit = "res.partner"

    _columns = {
        'tin_number'                     : fields.char('TIN Number', size=64),
        'vrn_number'                     : fields.char('VRN Number', size=64),
    }