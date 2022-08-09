from odoo import models, fields


class ContactPerson(models.Model):
    _name = 'contact.person'
    _inherit = ['person.mixin', ]
    _description = 'Contact person'

    description = fields.Text()
