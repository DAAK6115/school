from odoo import models, fields

class Utilisateur(models.Model):
    _name = 'mon_module.utilisateur'
    _description = 'Utilisateur du système pyramidale'

    name = fields.Char(string='Nom', required=True)
    parrain_id = fields.Many2one('mon_module.utilisateur', string='Parrain')
    filleuls_ids = fields.One2many('mon_module.utilisateur', 'parrain_id', string='Filleuls')
    commission = fields.Float(string='Commission', compute='_compute_commission')

    def _compute_commission(self):
        for utilisateur in self:
            utilisateur.commission = len(utilisateur.filleuls_ids) * 10  # Par exemple, 10 unités par filleul
