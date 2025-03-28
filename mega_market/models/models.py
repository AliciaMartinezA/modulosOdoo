# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MegaMarketElectrodomestico(models.Model):
    _name = 'mega_market.electrodomestico'
    _description = 'Electrodoméstico'

    name = fields.Char('Nombre')
    codigo_producto = fields.Char('Código de Producto')
    pais_id = fields.Many2one('res.country', 'País', required=True)
    importe_compra = fields.Float('Importe de Compra')
    moneda_id = fields.Many2one('res.currency', 'Moneda de Compra', required=True)
    precio_venta = fields.Float('Precio de Venta')

class MegaMarketCliente(models.Model):
    _name = 'mega_market.cliente'
    _description = 'Cliente'

    name = fields.Char('Nombre')
    apellidos = fields.Char('Apellidos')
    nif = fields.Char('NIF')
    direccion = fields.Text('Dirección')
    fecha_nacimiento = fields.Date('Fecha de Nacimiento')
    telefono = fields.Char('Teléfono')

