from odoo import fields, models


class TestType(models.Model):
    _name = 'test.type'
    _description = 'Type of test'
    _parent_name = "parent_id"
    _parent_store = True

    name = fields.Char(index=True, required=True)
    active = fields.Boolean(default=True)
    parent_id = fields.Many2one('test.type', 'Parent Type', index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('test.type', 'parent_id', 'Child Type')
