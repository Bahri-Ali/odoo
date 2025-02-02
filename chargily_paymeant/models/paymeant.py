from odoo import  models , fields

class Paymeant(models.Model):
    _name = 'paymeant'
    _log_access= False

    date = fields.Date(string='dat of paymeant')
    transaction = fields.Float()
    blance = fields.Float()
    reference = fields.Float()
    state = fields.Char(string="state", required=False, )
    tva = fields.Float()




