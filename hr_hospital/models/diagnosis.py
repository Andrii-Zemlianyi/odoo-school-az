from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Diagnosis(models.Model):
    _name = 'diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(index=True, required=True)
    active = fields.Boolean(default=True)
    doctor_id = fields.Many2one('doctor', string='Doctor',
                                required=True)
    patient_id = fields.Many2one('patient', string='Patient',
                                 required=True)
    disease_id = fields.Many2one('disease', string='Disease',
                                 required=True)
    date_of_diagnosis = fields.Date()
    test_ids = fields.Many2many('patient.test', string='Tests')
    prescribed_treatment = fields.Text()
    comments_of_mentor = fields.Text()

    disease_type_id = fields.Many2one('disease.type', string='Disease type',
                                      related='disease_id.disease_type_id',
                                      store=True)

    @api.constrains('comments_of_mentor', 'doctor_id')
    def check_doctor_is_intern(self):
        for record in self:
            if (not record.comments_of_mentor) and record.doctor_id.is_intern:
                raise UserError(_('Comments have to be fieled by mentor.'))
