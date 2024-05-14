#Source: https://stackoverflow.com/questions/65881511/odoo-12-getting-typeerror-on-while-trying-to-access-models-record-from-record
import odoo.http as http
from odoo import SUPERUSER_ID
from odoo import registry as registry_get
from odoo.api import Environment
import json


class Controller(http.Controller):

    @http.route('/test', type='http', auth='public', website=False)
    def handler(self):
        registry = registry_get('ceres')
        with registry.cursor() as cr:
            env = Environment(cr, SUPERUSER_ID, {})
            attendee = env['product.template'].sudo().search([])
        return attendee 