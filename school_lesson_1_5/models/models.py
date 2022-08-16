# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school_lesson_1_5(models.Model):
    _name = 'school_lesson_1_5.school_lesson_1_5'
    _description = 'school_lesson_1_5.school_lesson_1_5'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
