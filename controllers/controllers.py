# -*- coding: utf-8 -*-
# from odoo import http


# class CustomBudget(http.Controller):
#     @http.route('/custom_budget/custom_budget/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_budget/custom_budget/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_budget.listing', {
#             'root': '/custom_budget/custom_budget',
#             'objects': http.request.env['custom_budget.custom_budget'].search([]),
#         })

#     @http.route('/custom_budget/custom_budget/objects/<model("custom_budget.custom_budget"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_budget.object', {
#             'object': obj
#         })
