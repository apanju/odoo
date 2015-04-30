from openerp.osv import fields, osv
import time
import datetime
from openerp import tools
from openerp.osv.orm import except_orm
from openerp.tools.translate import _
from dateutil.relativedelta import relativedelta

class fleet_vehicle(osv.Model):

    _inherit = {'fleet.fleet_vehicle'}

    _columns = {
        'old_plate_number': fields.char('Old Plate Number'),
        'type':fields.selection([('car','Car'), ('bike','Bike'), ('truck','Truck'), ('minibus','Mini Bus')], 'Vehicle Type'),
        'use_state':fields.selection([('new','New'), ('inuse','In Use'), ('sell','Sell'), ('sold','Sold'), ('stolen','Stolen')], 'Usage state'),
        'fuel_tank_size':fields.integer('Tank Size (L)'),
        'engine_size':fields.integer('Engine Size (cc)'),
        }