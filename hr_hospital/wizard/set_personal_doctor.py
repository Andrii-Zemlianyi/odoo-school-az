from odoo import _, fields, models, api
from odoo.exceptions import UserError


class Patient(models.Model):
    _inherit = "patient"

    def action_error(self):
        if (len(self)) < 2:
            raise UserError(
                ("Please select atleast two Patients to set Personal Doctor"))
        return {
            "type": "ir.actions.act_window",
            "res_model": "set.personal.doctor",
            "view_mode": "form",
            "view_type": "form",
            "target": "new",
            "context": self._context,
        }

class SetPersonalDoctor(models.TransientModel):
    _name = "set.personal.doctor"
    _description = "Set personal doctor"

    doctor_id = fields.Many2one("doctor", string="New personal doctor", required=True,)

    def action_set(self):
        self.ensure_one()
        patient_for_set = self.env["patient"].browse(self._context.get("active_ids"))
        for patient in patient_for_set:
            patient.write({"personal_doctor_id": self.doctor_id.id})
