from odoo import fields, models


class SampleType(models.Model):
    _name = 'sample.type'
    _description = 'Type of sample'
  
    name = fields.Char('Name', index=True, required=True)
    active = fields.Boolean(default=True)
    description = fields.Text('Description')
  