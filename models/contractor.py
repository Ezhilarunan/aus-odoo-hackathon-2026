from odoo import models, fields, api

class Contractor(models.Model):
    _name = 'csr.contractor'
    _description = 'Project Contractor'

    name = fields.Char('Contractor Name', required=True)
    contact_person = fields.Char('Contact Person')
    phone = fields.Char('Phone')
    
    project_ids = fields.One2many('csr.project', 'contractor_id', string='Projects Involved In')
    
    total_expense = fields.Monetary('Total Our Expense', compute='_compute_expenses', store=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    @api.depends('project_ids.expense_amount')
    def _compute_expenses(self):
        for record in self:
            record.total_expense = sum(record.project_ids.mapped('expense_amount'))