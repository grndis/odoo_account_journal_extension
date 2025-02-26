from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.depends('company_id', 'invoice_filter_type_domain')
    def _compute_suitable_journal_ids(self):
        for m in self:
            company = m.company_id or self.env.company
            # Remove the journal type filter to allow all types
            m.suitable_journal_ids = self.env['account.journal'].search([
                *self.env['account.journal']._check_company_domain(company),
                # Remove the type filter to allow all journal types
            ])

