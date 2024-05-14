#Source: https://stackoverflow.com/questions/65853626/odoo-uncaught-typeerror-cannot-read-property-string-of-undefined-settings-vie
class TicketSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    template_id = fields.Many2one('mail.template', string='Mail template')
    days = fields.Integer('Days')

    def set_values(self):
        super(TicketSettings, self).set_values()
        settings = self.env['ir.config_parameter'].sudo()
        settings.set_param('base.template_id', self.template_id.id)
        settings.set_param('base.days', self.days)

    @api.model
    def get_values(self):
        res = super(TicketSettings, self).get_values()
        settings = self.env['ir.config_parameter'].sudo()
        template_id = settings.get_param('base.template_id')
        days = settings.get_param('base.days')
        res.update(
            template_id = literal_eval(template_id) if template_id else None,
            hours = literal_eval(days) if days else None)
        return res