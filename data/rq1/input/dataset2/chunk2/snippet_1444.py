#Source: https://stackoverflow.com/questions/71016869/attributeerror-ir-ui-menu-object-has-no-attribute-report-action-when-genera
from odoo import models, fields

class hotelreport(models.TransientModel):
    _name = 'hotel.report.wizard'

    employee = fields.Many2one('res.users', string="Employee")
    from_date = fields.Date(string="Starting Date")
    to_date = fields.Date(string="Ending Date")

    def action_print_report(self):
        data = {
            'start_date': self.from_date,
            'end_date': self.to_date,
            'employee': self.employee.id
        }
        return self.env.ref('hotel_promo.print_report').report_action(self, data=data)