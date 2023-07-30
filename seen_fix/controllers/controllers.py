# -*- coding: utf-8 -*-
# from odoo import http


# class SeenFix(http.Controller):
#     @http.route('/seen_fix/seen_fix', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/seen_fix/seen_fix/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('seen_fix.listing', {
#             'root': '/seen_fix/seen_fix',
#             'objects': http.request.env['seen_fix.seen_fix'].search([]),
#         })

#     @http.route('/seen_fix/seen_fix/objects/<model("seen_fix.seen_fix"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('seen_fix.object', {
#             'object': obj
#         })
