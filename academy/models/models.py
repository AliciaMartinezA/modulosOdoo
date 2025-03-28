# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Academy(models.Model):
     _name = 'academy.academy'
     _description = 'academy.academy'

     name = fields.Char()
     begin_date = fields.Datetime(string='Start Date') 
     end_date = fields.Datetime(string='End Date') 
     capacity = fields.Integer(string='Capacity') 
     content_type = fields.Selection([ 
    ('theoretical', 'Theoretical'), 
    ('practical', 'Practical'), 
    ('problems', 'Problem Resolution'), 
    ('intensive', 'Intensive') 
    ], string='Type of Content')

