# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ordenador(models.Model):
     _name = 'pcinventaro.ordenador'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     session_ids = fields.One2many(
        'pcinventaro.componente', 'ordenador', string="Sessions")

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100


class Componente(models.Model):
     _name = 'pcinventaro.componente'
     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     ordenador = fields.Many2one('pcinventaro.ordenador',
        ondelete='cascade', string="Ordenador", required=True)

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100

