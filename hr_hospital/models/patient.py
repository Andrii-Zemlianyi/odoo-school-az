from datetime import date

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class Patient(models.Model):
    _name = 'patient'
    _inherit = ['person.mixin', ]
    _description = 'Patient'

    date_of_bith = fields.Date(string='Date of bith', required=True)
    age = fields.Integer(string='Age',
                         compute='_compute_age',
                         compute_sudo=True, store=True)

    passport_series = fields.Char('Passport series', size=2, )
    passport_number = fields.Char('Passport number', size=6, )
    passport_issued = fields.Date('Passport issued', )
    passport_issued_by = fields.Char('Passport issued by', )

    contact_person_id = fields.Many2one('contact.person',
                                        string='Contact person')
    personal_doctor_id = fields.Many2one('doctor', string='Personal doctor', )
    description = fields.Text(string='Description')

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
            val = vals.deepcopy()
            if obj.contact_person_id:
                val['passport_number'] = '1111 {}'.format(obj.passport_series)
            super('Patient', obj).write(val)
        return True
        # if vals.get('personal_doctor_id'):
        #     valp = {'doctor_id': vals.get('personal_doctor_id'),
        #             'patient_id': self.id, 'appointment_date': date.today()}
        #     # rec = self.env['personal.doctor.history'].search([('doctor_id', '=', vals.get('personal_doctor_id')),
        #     #                                                  ('patient_id', '=', self.id),
        #     #                                                  ('appointment_date', '=', valp['appointment_date'])],
        #     #                                                 limit=1)  # first search record
        #     # if not rec.write(valp):
        #     self.env['personal.doctor.history'].create(valp)
