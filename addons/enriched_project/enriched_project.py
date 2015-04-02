# -*- coding: utf-8 -*-

from datetime import datetime, date
from lxml import etree
import time

from openerp import SUPERUSER_ID
from openerp import tools
from openerp.addons.resource.faces import task as Task
from openerp.osv import fields, osv
from openerp.tools.translate import _

# class project(osv.osv):
#     _description = "Project"
#     _inherit = ['project.project']
#
#     _columns = {
#         'active': fields.boolean('Active', help=""),
#      }
#
#
# class task(osv.osv):
#     _description = "Task"
#     _inherit = ['project.task']
#
#     _columns = {
#         'phase': fields.many2one('enriched_project.project_phase', 'Phase')
#         'depends_on': fields.many2one('project.task', 'Parent Task', )
#     }

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

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
