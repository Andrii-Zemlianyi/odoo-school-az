from odoo import fields, models


class PersonMixin(models.AbstractModel):
    """ПІБ, телефон, емейл, фото, стать,
        унаслідувати від неї моделі 
        Лікар, Пацієнт, Контактна особа"""
    _name = 'person.mixin'
    _description = 'Person mixin'

    name = fields.Char()
    first_name = fields.Char('First Name',
                             required=True)
    last_name = fields.Char('Last Name',
                            required=True)
    midle_name = fields.Char('Midle Name')
    gender = fields.Selection(
        default='other',
        selection=[('male', _('Male')),
                   ('female', _('Female')),
                   ('other', _('Other / Undefined'))], )
    phone = fields.Char('Phone')
    email = fields.Char('Email')
    photo = fields.Image("Photo", max_width=512, max_height=512)

def name_get(self):
    return [(rec.id, "%s %s %s" % (rec.last_name, rec.first_name, rec.midle_name)) for rec in self]
