#Source: https://stackoverflow.com/questions/56903546/how-to-resolve-error-typeerror-strptime-argument-1-must-be-str-not-bool
class AttendanceModificationRequest(models.Model):

    _name = 'attendance.modification.request'
    _description = 'Attendance modification Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def _get_employee_id(self):
        employee_rec = self.env['hr.employee'].search([('user_id', '=',
                self.env.uid)], limit=1)
        return employee_rec.id

    employee_id = fields.Many2one('hr.employee', 'Employee',
                                  readonly=True,
                                  default=_get_employee_id,
                                  required=True)
    user_id = fields.Many2one(
        'res.users',
        string='User',
        track_visibility='onchange',
        readonly=True,
        states={'draft': [('readonly', False)]},
        default=lambda self: self.env.user,
        )
    state = fields.Selection([('draft', 'Pending'), ('waiting',
                             'Waiting for approval'), ('approved',
                             'Approved'), ('cancel', 'Cancelled')],
                             readonly=True,
                             help='Gives the state of the attendance request modification .'
                             , default='draft')
    modification_date = fields.Date('Date')
    time_check_in_1 = fields.Datetime('Check in')
    time_check_out_1 = fields.Datetime('Check out')
    note = fields.Text('Note')
    attendance_id = fields.Many2one('hr.attendance', string='Attendance'
                                    )

    @api.multi
    def modification_approval(self):
        attend_signin_ids = self.env['hr.attendance'
                ].search([('employee_id', '=', self.employee_id.id)])
        check_in_date = \
            datetime.datetime.strptime(self.time_check_in_1,
                DEFAULT_SERVER_DATETIME_FORMAT).date()
        check_out_date = \
            datetime.datetime.strptime(self.time_check_out_1,
                DEFAULT_SERVER_DATETIME_FORMAT).date()
        for record in self:
            attendance_check_in_date = \
                datetime.datetime.strptime(record.attendance_id.check_in,
                    DEFAULT_SERVER_DATETIME_FORMAT).date()
            attendance_check_out_date = \
                datetime.datetime.strptime(record.attendance_id.check_out,
                    DEFAULT_SERVER_DATETIME_FORMAT).date()
            if record.attendance_id.employee_id == self.employee_id \
                and check_in_date == attendance_check_in_date:
                record.attendance_id.check_in = self.time_check_in_1
                record.attendance_id.check_out = self.time_check_out_1
        return self.write({'state': 'approved'})