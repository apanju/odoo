from openerp.osv import fields, osv

class fleet_vehicle(osv.Model):
    _inherit = 'fleet.vehicle'

    _columns = {
        'old_plate_number': fields.char('Old Plate Number'),
        'type':fields.selection([('car','Car'), ('bike','Bike'), ('truck','Truck'), ('minibus','Mini Bus')], 'Vehicle Type'),
        'use_state':fields.selection([('new','New'), ('inuse','In Use'), ('sell','Sell'), ('sold','Sold'), ('stolen','Stolen')], 'Usage state'),
        'fuel_tank_size':fields.integer('Tank Size (L)'),
        'engine_size':fields.integer('Engine Size (cc)'),
        }