#Source: https://stackoverflow.com/questions/71184884/attributeerror-str-object-has-no-attribute-get-odoo14
from odoo import fields, models, api

class  CreateExam(models.TransientModel):
    _name = 'exam.wizards'
    _description = 'Create exams'

    std_wiz = fields.Many2one(
        comodel_name='std.record',
        string='Student',
        required=False)
    std_subject = fields.Many2one('std.subject',string="Subject")
    std_marks=fields.Float(string="Marks")

    def save_btn(self):
        print("saved")
        return True