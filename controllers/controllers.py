# -*- coding: utf-8 -*-
from odoo import http

# class Pcinventaro(http.Controller):
#     @http.route('/pcinventaro/pcinventaro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pcinventaro/pcinventaro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pcinventaro.listing', {
#             'root': '/pcinventaro/pcinventaro',
#             'objects': http.request.env['pcinventaro.pcinventaro'].search([]),
#         })

#     @http.route('/pcinventaro/pcinventaro/objects/<model("pcinventaro.pcinventaro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pcinventaro.object', {
#             'object': obj
#         })