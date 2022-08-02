import datetime
from odoo import api, fields, models


class Visit(models.Model):
    _name = 'visit'
    _description = 'Visit'

    doctor_id = fields.Many2one(comodel_name='doctor',
                                string='Doctor',
                                index=True, required=True)
    patient_id = fields.Many2one(comodel_name='patient',
                                 string='Patient',
                                 index=True, required=True)
    date_of_visit = fields.Datetime(required=True)
    time_reception = fields.Integer(string='Time reception (minutes)',
                                    required=True)
    end_of_visit = fields.Datetime(compute='_compute_end_of_visit')
    test_ids = fields.Many2many(comodel_name='patient.test',
                                string='Tests')
    diagnosis_id = fields.Many2one(comodel_name='diagnosis',
                                   string='Diagnosis')
    recommendation = fields.Text()

    def name_get(self):
        return [(rec.id,
                 "Visit %s at %s" % (rec.id,
                                     rec.date_of_visit)
                 ) for rec in self]

    @api.depends('date_of_visit', 'time_reception')
    def _compute_end_of_visit(self):
        for rec in self:
            rec.end_of_visit = rec.date_of_visit + \
                datetime.timedelta(minutes=rec.time_reception)
