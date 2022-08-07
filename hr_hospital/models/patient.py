from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Patient(models.Model):
    _name = 'patient'
    _inherit = ['person.mixin', ]
    _description = 'Patient'

    date_of_bith = fields.Date(required=True)
    age = fields.Integer(compute='_compute_age',
                         compute_sudo=True, store=True)

    passport_series = fields.Char(size=2, )
    passport_number = fields.Char(size=6, )
    passport_issued = fields.Date()
    passport_issued_by = fields.Char()

    contact_person_id = fields.Many2one('contact.person',
                                        string='Contact person')
    personal_doctor_id = fields.Many2one('doctor', string='Personal doctor', )
    description = fields.Text()
    visit_ids = fields.One2many(
        comodel_name='visit', inverse_name='patient_id', string='Visits')
    personal_doctor_history_ids = fields.One2many(
        comodel_name='personal.doctor.history',
        inverse_name='patient_id',
        string='Personal Doctor History')
    diagnosis_ids = fields.One2many(comodel_name='diagnosis',
                                    inverse_name='patient_id',
                                    string='Diagnosises')
    color = fields.Integer("Color Index", default=0)

    @api.depends('date_of_bith')
    def _compute_age(self):
        for man in self:
            man.age = \
                relativedelta(fields.Date.today(), man.date_of_bith).years \
                if man.date_of_bith else 0

    @api.model
    def create(self, vals):
        new_record = super().create(vals)
        if 'personal_doctor_id' in vals:
            self.env['personal.doctor.history'].create({
                'doctor_id': vals['personal_doctor_id'],
                'patient_id': new_record.id,
                'appointment_date': date.today(), })
        return new_record

    def write(self, vals):
        if 'personal_doctor_id' not in vals:
            return super().write(vals)
        for obj in self:
            if obj.personal_doctor_id.id != vals.get('personal_doctor_id'):
                self.env['personal.doctor.history'].create({
                    'doctor_id': vals.get('personal_doctor_id'),
                    'patient_id': obj.id, 'appointment_date': date.today(), })
            super(Patient, obj).write(vals)
        return True
