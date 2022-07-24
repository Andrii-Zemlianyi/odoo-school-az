from odoo import models, fields


class Doctor(models.Model):
    _name = 'doctor'
    _inherit = ['person.mixin',]
    _description = 'Doctor'

    specialty = fields.Char()
    is_intern = fields.Boolean('Is Intern')
    mentor_id = fields.Many2one('doctor', string='Mentor')
    description = fields.Text()
