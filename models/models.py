# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ordenador(models.Model):
     _name = 'pcinventario.ordenador'

     name = fields.Char()
     description = fields.Text()
     ubicacion = fields.Char()

     session_ids = fields.One2many(
        'pcinventario.componente', 'ordenador', string="Sessions")

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100


class Componente(models.Model):
     _name = 'pcinventario.componente'
     name = fields.Char()
     description = fields.Text(required=False)

     ordenador = fields.Many2one('pcinventario.ordenador',
        ondelete='cascade', string="Ordenador", required=True)

     categoria = fields.Many2one('pcinventario.categoria',
        ondelete='cascade', string="Categorias", required=True)


class Categoria(models.Model):
     _name = 'pcinventario.categoria'
     name = fields.Char()
     description = fields.Text(required=False)

     componentes = fields.One2many(
        'pcinventario.componente', 'categoria', string="Componentes", required=False)


class Incidencia(models.Model):
     _name = 'pcinventario.incidencia'
     name = fields.Char()
     description = fields.Text(required=False)
     arreglada = fields.Boolean("Arreglada")
     ordenador = fields.Many2many('pcinventario.ordenador', string="Ordenadores")

