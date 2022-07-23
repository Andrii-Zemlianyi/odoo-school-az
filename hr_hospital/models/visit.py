from odoo import api, fields, models


class Visit(models.Model):
    _name = 'visit'
    _description = 'Visit'
    
    doctor_id = fields.Many2one('doctor', string='Doctor', required=True)
    patient_id = fields.Many2one('patient', string='Patient', required=True)
    date_of_visit = fields.Date('Date of visit', required=True)
    time_reception = fields.Integer('Time reception')
    diagnosis_id = fields.Many2one('diagnosis', string='Diagnosis')
    recommendation = fields.Text('Recommendation')
    