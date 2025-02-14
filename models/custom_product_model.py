from odoo import models, fields, api

class CustomProduct(models.Model):
  _name = 'custom.product'
  _description = 'Custom Product'

  name = fields.char(string='Product Name',required=True)
  price = fields.Float(string='Price')
  stock = fields.Integer(string="Stock")

  @api.depends('stock')
  def check_stock(self):
    for record in self:
      if record.stock < 1:
        raise ValueError('Stock is empty!')