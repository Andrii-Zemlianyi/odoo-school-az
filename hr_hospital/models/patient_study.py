from typing_extensions import Required
from odoo import api, fields, models


class PatientStudy(models.Model):
    _name = 'patient.study'
    _description = 'Studies of patients'

    name = fields.Char(string='Name', index=True, required=True)
    patient_id = fields.Many2one('patient', string='Patient',
                                 index=True, required=True)
    doctor_id = fields.Many2one('doctor', string='Doctor',
                                index=True, required=True)
    study_id = fields.Many2one('study.type', string='Study',
                               index=True, required=True)
    sample_id = fields.Many2one('sample.type', string='Sample type',
                                index=True, required=True)
    conclusion = fields.Text('Conclusion', required=True)