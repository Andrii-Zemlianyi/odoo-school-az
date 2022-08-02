from odoo import models, fields


class Doctor(models.Model):
    _name = 'doctor'
    _inherit = ['person.mixin', ]
    _description = 'Doctor'

    specialty = fields.Char(required=True)
    is_intern = fields.Boolean()
    mentor_id = fields.Many2one(comodel_name='doctor', string='Mentor',
                                domain=[('is_intern', '=', False)])

    intern_ids = fields.One2many(comodel_name='doctor',
                                 inverse_name='mentor_id',
                                 string='Interns',
                                 domain=[('is_intern', '=', True)])
    patient_ids = fields.One2many(comodel_name='patient',
                                  inverse_name='personal_doctor_id',
                                  string='Doctor patients')
    description = fields.Text()

    def name_get(self):
        return [(rec.id,
                 "phD %s %s" % (rec.last_name,
                                rec.first_name)
                 ) for rec in self]
