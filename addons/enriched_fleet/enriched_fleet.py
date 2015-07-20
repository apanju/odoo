from openerp.osv import fields, osv

class fleet_vehicle(osv.Model):
    _inherit = 'fleet.vehicle'

    _columns = {
        'old_plate_number': fields.char('Old Plate Number'),
        'type':fields.selection([('car','Car'), ('bike','Bike'), ('truck','Truck'), ('minibus','Mini Bus')], 'Vehicle Type'),
        'fuel_tank_size':fields.integer('Tank Size'),
        'engine_size':fields.integer('Engine Size'),
		'num_keys':fields.integer('Number of Keys'),
        }

class hr_employee(osv.osv):
    _inherit = "hr.employee"

    _columns = {
       'drivers_licence_number': fields.char('Driving Licence Number'),
       'drivers_licence_date_from': fields.date('Driving Licence Valid From'),
       'drivers_licence_date_to': fields.date('Driving Licence Valid To'),
       'driver_agreement_signed': fields.binary('Drivers Agreement Signed')
    }