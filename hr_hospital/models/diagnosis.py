from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'diagnosis'
    _description = 'Diagnosis'

    name = fields.Char('Name', index=True, required=True)
    doctor_id = fields.Many2one('doctor', string='Doctor',
                                 index=True, required=True)
    patient_id = fields.Many2one('patient', string='Patient',
                                 index=True, required=True)
    disease_id = fields.Many2one('disease', string='Disease',
                                 index=True, required=True)
    date_of_diagnosis = fields.Date('Date of diagnosis')
    prescribed_treatment = fields.Text(string='Prescribed treatment')
    comments_of_mentor = fields.Text('Comments of mentor', required=True)
