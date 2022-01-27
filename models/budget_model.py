# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountBudget(models.Model):
    _inherit = 'crossovered.budget'

    # Campos de tipo selección personalizados para el módulo de budget
    departamento = fields.Selection([
        ('comercial', 'Comercial'),
        ('estructura', 'Estructura'),
        ('innovacion', 'Innovación'),
        ('marketing', 'Marketing'),
        ('personal', 'Personal'),
        ('inversiones', 'Inversiones'),
        ('gastosinternos', 'Gastos Internos')
    ], 'Departamento', required=True)

    centro_de_coste = fields.Selection([
        ('barcelona', 'Barcelona'),
        ('madrid', 'Madrid'),
        ('global', 'Global')
    ], 'Centro de Coste', required=True)
