from odoo import models, fields


class PatientCard(models.Model):
    _name = 'patient.card.line'
    _description = 'Patient Card Line'
    _order = 'card_id, sequence, id'

    card_id = fields.Many2one('patient.card', required=True,
                              ondelete='cascade', index=True,
                              copy=False)
    name = fields.Text(string='Description', required=True)
    sequence = fields.Integer(default=10)

    doctor_id = fields.Many2many('doctor', context={'active_test': False})
    diagnosis_id = fields.Many2many('diagnosis', string='Diagnosis')
    date_of_diagnosis = fields.Date(string='Visit')
