from odoo import fields, models


class Disease(models.Model):
    _name = 'disease'
    _description = 'Disease'

    name = fields.Char(index=True, required=True)
    active = fields.Boolean(default=True)
    disease_type_id = fields.Many2one('disease.type',
                                      string='Disease type',
                                      required=True,
                                      )
    description = fields.Text()
