#Source: https://stackoverflow.com/questions/50950043/typeerror-nonetype-object-is-not-subscriptable-odoo-11-custom-report
from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)
class SockValuationReport(models.TransientModel):
    _name = 'report.stock_valuation_flora'
    _description = 'Sotck valuation report for floravert'

    @api.multi
    def render_report(self):
        products = self.env['product.template'].search([])
        data = {}
        categ_dict = {}
        for product in products:
            valuation = 0
            if(product.categ_id.name in categ_dict):
                valuation = product.standard_price * product.qty_available
                categ_dict[product.categ_id.name]['valuation'] = categ_dict[product.categ_id.name]['valuation'] + valuation
            else:
                categ_dict[product.categ_id.name] = {'categ_name':product.categ_id.name, 'valuation':product.standard_price * product.qty_available}
        data['products'] = products
        data['categ_value']= categ_dict
        _logger.info(data)
        return self.env.ref('stock_printer.report_stock_product_valuation').report_action(self,data=data)