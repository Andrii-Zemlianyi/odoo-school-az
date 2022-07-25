from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo import _, models, fields, api


class Patient(models.Model):
    _name = 'patient'
    _inherit = ['person.mixin']
    _description = 'Patient'

    date_of_bith = fields.Date(string='Date of bith', required=True)
    age = fields.Integer(string='Age',
                         compute='_compute_age',
                         compute_sudo=True, store=True)

    passport_series = fields.Char('Passport series')
    passport_number = fields.Char('Passport number')
    passport_issued = fields.Date('Passport issued')
    passport_issued_by = fields.Char('Passport issued by')

    contact_person_id = fields.Many2one('contact.person',
                                        string='Contact person')
    personal_doctor_id = fields.Many2one('doctor', string='Personal doctor')
    description = fields.Text(string='Description')

    @api.depends('date_of_bith')
    def _compute_age(self):
        today = date.today()
        for man in self:
            if man.date_of_bith:
                dob = man.date_of_bith
                rd = relativedelta(today, dob)
                man.age = rd.years

    @api.model
    def create(self, vals):
        new_record = super().create(vals)
        if vals.get('personal_doctor_id'):
            valp = {}
            valp['doctor_id'] = vals['personal_doctor_id']
            valp['patient_id'] = new_record.id
            valp['appointment_date'] = date.today()
            self.env['personal.doctor.history'].create(valp)
        return new_record

    def write(self, vals):
        if vals.get('personal_doctor_id'):
            valp = {}
            valp['doctor_id'] = vals.get('personal_doctor_id')
            valp['patient_id'] = self.id
            valp['appointment_date'] = date.today()
            # rec = self.env['personal.doctor.history'].search([('doctor_id', '=', vals.get('personal_doctor_id')),
            #                                                  ('patient_id', '=', self.id),
            #                                                  ('appointment_date', '=', valp['appointment_date'])],
            #                                                 limit=1)  # first search record
            # if not rec.write(valp):
            self.env['personal.doctor.history'].create(valp)
        super().write(vals)
