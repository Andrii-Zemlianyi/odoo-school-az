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
    mentor_first_name = fields.Char(related='mentor_id.first_name')
    mentor_last_name = fields.Char(related='mentor_id.last_name')
    mentor_midle_name = fields.Char(related='mentor_id.midle_name')
    mentor_specialty = fields.Char(related='mentor_id.specialty')

    description = fields.Text()
    color = fields.Integer("Color Index", default=0)

    def name_get(self):
        return [(rec.id,
                 "phD %s %s" % (rec.last_name,
                                rec.first_name)
                 ) for rec in self]
