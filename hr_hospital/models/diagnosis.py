from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
    description = fields.Text()
