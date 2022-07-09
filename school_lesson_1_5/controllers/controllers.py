# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolLesson15(http.Controller):
#     @http.route('/school_lesson_1_5/school_lesson_1_5', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_lesson_1_5/school_lesson_1_5/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_lesson_1_5.listing', {
#             'root': '/school_lesson_1_5/school_lesson_1_5',
#             'objects': http.request.env['school_lesson_1_5.school_lesson_1_5'].search([]),
#         })

#     @http.route('/school_lesson_1_5/school_lesson_1_5/objects/<model("school_lesson_1_5.school_lesson_1_5"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_lesson_1_5.object', {
#             'object': obj
#         })
