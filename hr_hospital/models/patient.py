
from odoo import models, fields


class Patient(models.Model):
    _name = 'patient'
    _description = 'Patient'

    name = fields.Char()
    age = fields.Integer()
    description = fields.Text()
