from odoo import fields, models


class DiseaseType(models.Model):
    _name = 'disease.type'
    _description = 'Type of disease'
    _parent_name = "parent_id"
    _parent_store = True

    name = fields.Char('Name', index=True, required=True)
    parent_id = fields.Many2one('disease.type', 'Parent Type', index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('disease.type', 'parent_id', 'Child Type')
