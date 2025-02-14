from odoo import http

class CustomProductController(http.Controller):
  @http.route('/products',auth='public',website=True)
  def list_products(self,**kwargs):
    products = http.request.env['custom.product'].sudo().search([])
    return http.request.render('custom_product.report_product_template',{'products':products})