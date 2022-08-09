from odoo import _, fields, models


class PersonMixin(models.AbstractModel):
    _name = 'person.mixin'
    _description = 'Person mixin'

    active = fields.Boolean(default=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    midle_name = fields.Char()
    gender = fields.Selection(
        default='other',
        selection=[('male', _('Male')),
                   ('female', _('Female')),
                   ('other', _('Other / Undefined'))], )
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Image(max_width=512, max_height=512)

    def name_get(self):
        res = []
        for rec in self:
            if rec.midle_name:
                mn = rec.midle_name
            else:
                mn = ""
            res.append((rec.id,
                        "%s %s %s" % (rec.last_name, rec.first_name, mn)
                        ))
        return res
