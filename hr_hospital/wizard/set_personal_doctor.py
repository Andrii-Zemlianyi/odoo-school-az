from odoo import fields, models


# class Patient(models.Model):
#     _inherit = "patient"
#
#     def action_error(self):
#         if (len(self)) < 2:
#             raise UserError(
#                 ("Please select atleast two Patients to set Personal Doctor"))
#         return {
#             "type": "ir.actions.act_window",
#             "res_model": "set.personal.doctor",
#             "view_mode": "form",
#             "view_type": "form",
#             "target": "new",
#             "context": self._context,
#         }

class SetPersonalDoctor(models.TransientModel):
    _name = "set.personal.doctor.wizard"
    _description = "Set personal doctor"

    doctor_id = fields.Many2one("doctor", string="New personal doctor",
                                required=True, )
    patient_ids = fields.Many2many('patient')

    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        res['patient_ids'] = [(6, 0, self._context.get("active_ids"))]
        return res

    def action_set(self):
        self.ensure_one()
        self.patient_ids.write({"personal_doctor_id": self.doctor_id.id})
        # patient_for_set = self.env["patient"].browse(self._context.get("active_ids"))
        # for patient in patient_for_set:
        #     patient.write({"personal_doctor_id": self.doctor_id.id})
