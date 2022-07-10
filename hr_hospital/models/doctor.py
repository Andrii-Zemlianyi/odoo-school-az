
from odoo import models, fields


class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Doctor'

    name = fields.Char()
    specialty = fields.Char()
    description = fields.Text()
