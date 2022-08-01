import datetime
from odoo import api, fields, models


class Visit(models.Model):
    _name = 'visit'
    _description = 'Visit'

    doctor_id = fields.Many2one('doctor', string='Doctor',
                                index=True, required=True)
    patient_id = fields.Many2one('patient', string='Patient',
                                 index=True, required=True)
    date_of_visit = fields.Datetime('Date of visit', required=True)
    time_reception = fields.Integer('Time reception', required=True)
    end_of_visit =  fields.Datetime('End of visit', compute='_compute_end_of_visit')
    study_ids = fields.Many2many('patient.study', string='Studies')
    diagnosis_id = fields.Many2one('diagnosis', string='Diagnosis')
    recommendation = fields.Text('Recommendation', required=True)

    @api.depends('date_of_visit','time_reception')
    def _compute_end_of_visit(self):
        for rec in self:
            rec.end_of_visit = rec.date_of_visit + \
                datetime.timedelta(minutes=rec.time_reception)