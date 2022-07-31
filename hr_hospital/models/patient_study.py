from odoo import api, fields, models


class PatientStudy(models.Model):
    _name = 'patient.study'
    _description = 'Studies of patients'

    name = fields.Char(string='Name', index=True, required=True)
    patient_id = fields.Many2one(comodel_name='patient',
                                 string='Patient',
                                 required=True)
    doctor_id = fields.Many2one(comodel_name='doctor',
                                string='Doctor',
                                required=True)
    study_id = fields.Many2one(comodel_name='study.type',
                               string='Study',
                               required=True)
    sample_id = fields.Many2one(comodel_name='sample.type',
                                string='Sample type',
                                required=True)
    conclusion = fields.Text(string='Conclusion', required=True)
