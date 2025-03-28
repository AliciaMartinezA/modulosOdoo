# -*- coding: utf-8 -*-

from odoo import models, fields, api


from odoo import models, fields

class Animal(models.Model):
    _name = 'zoo.animal'
    _description = 'Animal del Zoológico'

    name = fields.Char(string='Nombre')
    species = fields.Char(string='Especie')
    identifier = fields.Char(string='Identificador')
    country_id = fields.Many2one('res.country', string='País de Procedencia', required=True)
    age = fields.Integer(string='Edad')
    entry_date = fields.Date(string='Fecha de Entrada')


class Cuidador(models.Model):
    _name = 'zoo.cuidador'
    _description = 'Cuidador del Zoológico'

    name = fields.Char(string='Nombre')
    surname = fields.Char(string='Apellidos')
    position = fields.Selection([
        ('supervisor', 'Supervisor'),
        ('encargado', 'Encargado'),
        ('cuidador', 'Cuidador')
    ], string='Cargo')
    hire_date = fields.Date(string='Fecha de Incorporación')


class Espacio(models.Model):
    _name = 'zoo.espacio'
    _description = 'Espacio del Zoológico'

    code = fields.Char(string='Código de Espacio')
    space_type = fields.Selection([
        ('jaula', 'Jaula'),
        ('vallado', 'Vallado'),
        ('acuario', 'Acuario'),
        ('terrarium', 'Terrarium')
    ], string='Tipo')
    thematic_area = fields.Selection([
        ('europa', 'Europa'),
        ('asia', 'Asia'),
        ('africa', 'África'),
        ('america', 'América'),
        ('oceania', 'Oceanía')
    ], string='Área Temática')