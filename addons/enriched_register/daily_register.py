from datetime import datetime
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT
from openerp.osv import fields, osv

class hr_employee(osv.osv):
    _inherit = "hr.employee"
    _description = "Employee"

    def _get_am_start_hour(self):
        return 8

    def _get_am_end_hour(self):
        return 13

    def _get_pm_start_hour(self):
        return 14

    def _get_pm_end_hour(self):
        return 17

    def _get_is_morning(self):
        now = datetime.now()
        return now.hour < self._get_pm_start_hour()

    def _has_signed_in_this_session(self, cr, uid, ids, name, args, context=None):
        PM_START_HOUR = self._get_pm_start_hour()
        result = {}
        if not ids:
            return result
        for id in ids:
            result[id] = False

        now = datetime.now()
        isMorning = self._get_is_morning()

        cr.execute('SELECT hr_attendance.name, hr_attendance.employee_id \
                FROM ( \
                    SELECT MAX(name) AS name, employee_id \
                    FROM hr_attendance \
                    WHERE action in (\'sign_in\') \
                    GROUP BY employee_id \
                ) AS foo \
                LEFT JOIN hr_attendance \
                    ON (hr_attendance.employee_id = foo.employee_id \
                        AND hr_attendance.name = foo.name) \
                WHERE hr_attendance.employee_id IN %s',(tuple(ids),))
        for res in cr.fetchall():
            action_date = datetime.strptime(res[0], DEFAULT_SERVER_DATETIME_FORMAT)
            signed_in_today = action_date.date() == now.date()
            signed_in_correct_session = isMorning and action_date.hour < PM_START_HOUR or action_date.hour >= PM_START_HOUR
            result[res[1]] = signed_in_today and signed_in_correct_session
        return result

    def _register_state(self, cr, uid, ids, name, args, context=None):
        result = {}
        if not ids:
            return result
        for id in ids:
            result[id] = 'absent'

        leave_states = self._get_leave_status(cr, uid, ids, name, args)
        attend_state = self._has_signed_in_this_session(cr, uid, ids, name, args)

        for id in ids:
            result[id] = attend_state[id] and 'present' or \
                            leave_states[id]['current_leave_state'] == 'validate' and 'on_leave' or 'absent'

        return result

    def _search_register_state(self, cr, uid, obj, name, args, context):
        res_ids = []
        res = []
        ids = obj.search(cr,uid,[]) # ids of employees
        for field, operator, value in args:
            for staff in self.browse(cr, uid, ids): # foreach employee
                if staff.register_state == value:
                    res_ids.append(staff.id)
        res.append(('id', 'in', res_ids))
        return res

    _columns = {
       'register_state': fields.function(_register_state, type='selection', selection=[('absent', 'Absent'), ('on_leave', 'On Leave'), ('present', 'Present')], string='Register', fnct_search=_search_register_state)
    }

    def attendance_action_force_sign_in(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        action_date = datetime.now()
        # action = context.get('action', False)
        hr_attendance = self.pool.get('hr.attendance')
        #warning_sign = {'sign_in': _('Sign In'), 'sign_out': _('Sign Out')}
        for employee in self.browse(cr, uid, ids, context=context):
            #if not action:
            #    if employee.state == 'present': break
            #    if employee.state == 'absent': action = 'sign_in'

            if self._get_is_morning():
                action_date = action_date.replace(hour=self._get_am_start_hour(), minute=0, second=0)
                if employee.state == 'absent':
                    if self._action_check(cr, uid, employee.id, action_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT), context):
                        vals = {'action': 'sign_in', 'employee_id': employee.id, 'name': action_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT)}
                        hr_attendance.create(cr, uid, vals, context=context)

                action_date = action_date.replace(hour=self._get_am_end_hour(), minute=0, second=0)
                if self._action_check(cr, uid, employee.id, action_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT), context):
                        vals = {'action': 'sign_out', 'employee_id': employee.id, 'name': action_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT)}
                        hr_attendance.create(cr, uid, vals, context=context)
            else:
                action_date = action_date.replace(hour=self._get_pm_start_hour(), minute=0, second=0)
                if employee.state == 'absent':
                    if self._action_check(cr, uid, employee.id, action_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT), context):
                        vals = {'action': 'sign_in', 'employee_id': employee.id, 'name': action_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT)}
                        hr_attendance.create(cr, uid, vals, context=context)

                action_date = action_date.replace(hour=self._get_pm_end_hour(), minute=0, second=0)
                if self._action_check(cr, uid, employee.id, action_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT), context):
                        vals = {'action': 'sign_out', 'employee_id': employee.id, 'name': action_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT)}
                        hr_attendance.create(cr, uid, vals, context=context)
        return True