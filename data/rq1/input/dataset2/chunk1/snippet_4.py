#Source: https://stackoverflow.com/questions/60106043/odoo-12-attributeerror-int-object-has-no-attribute-get
student_id = fields.Many2one('res.users', 'Etudiant', readonly=True, required=True, default=lambda self: self.choice_student()  )

@api.onchange('projet_terminer_id')
def choice_student(self):
    return self.env['res.users'].sudo().search([ ('id','=', 45)]).id