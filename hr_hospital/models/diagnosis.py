from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
    doctor_id = fields.Many2one('doctor', string='Doctor')
    patient_id = fields.Many2one('patient', string='Patient')
    disease_id = fields.Many2one('disease', string='Disease')
    date_of_diagnosis = fields.Date('Date of diagnosis')
    prescribed_treatment = fields.Text(string='Prescribed treatment')
