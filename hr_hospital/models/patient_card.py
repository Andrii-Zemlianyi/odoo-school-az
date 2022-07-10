
from odoo import models, fields


class PatientCard(models.Model):
    _name = 'patient.card'
    _description = 'Patient Card'

    name = fields.Char(string='Card Reference',
                       required=True, copy=False, index=True)
    patient = fields.Many2one(
        'patient',  required=True, change_default=True, index=True)

    patient_card_line = fields.One2many('patient.card.line', 'card_id',
                                        string='Card Lines', copy=False,
                                        auto_join=True)

    description = fields.Text()
