import datetime
from odoo import models, fields, api


class Patient(models.Model):
    _name = 'patient'
    _inherit = ['person.mixin']
    _description = 'Patient'

    date_of_bith = fields.Date('Date of bith', required=True)
    age = fields.Integer(string='Age',
                         compute='_compute_age',
                         compute_sudo=True)
    passport = fields.Char('Passport')
    contact_person_id = fields.Many2one('contact.person',
                                        string='Contact person')
    personal_doctor_id = fields.Many2one('doctor', string='Personal doctor'
                                         )# Todo add record to history
    description = fields.Text(string='Description')


@api.depends('date_of_bith')
def _compute_age(self):
    today = datetime.today()
    for man in self:
        man.age = today.year - man.birthdate.year - \
            ((today.month, today.day) < (man.birthdate.month, man.birthdate.day))
