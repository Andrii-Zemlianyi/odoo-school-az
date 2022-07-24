from odoo import api, fields, models


class DiseasesType(models.Model):
    _name = 'diseases.type'
    _description = 'Type of disease'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char('Name', index=True, required=True)
    # complete_name = fields.Char('Complete Name',
    #                             compute='_compute_complete_name',
    #                             store=True)
    parent_id = fields.Many2one('diseases.type', 'Parent Type', index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('diseases.type', 'parent_id', 'Child Type')
