from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Doctor(models.Model):
    _name = 'doctor'
    _inherit = ['person.mixin', ]
    _description = 'Doctor'

    specialty = fields.Char('specialty', required=True)
    is_intern = fields.Boolean('Is Intern')
    mentor_id = fields.Many2one('doctor', string='Mentor')
    description = fields.Text()

    def name_get(self):
        return [(rec.id,
                 "phD %s %s" % (rec.last_name,
                                rec.first_name)
                 ) for rec in self]

    @api.constrains('is_intern', 'mentor_id')
    def check_intern(self):
        for doctor in self:
            is_mentor_intern = doctor.mentor_id.is_intern
            if doctor.is_intern and is_mentor_intern is True:
                raise ValidationError(_('The intern can not be mentor!'))
