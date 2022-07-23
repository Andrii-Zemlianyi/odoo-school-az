from odoo import models, fields


class Doctor(models.Model):
    _name = 'doctor'
    _inherit = ['person.mixin',]
    _description = 'Doctor'

    specialty = fields.Char()
    description = fields.Text()
