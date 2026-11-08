from odoo import models, fields, api

class Organization(models.Model):
    _name = 'csr.fundraising'
    _description = 'Donor Organization'

    name = fields.Char('Organization Name', required=True)
    
    organization_type = fields.Selection([
        ('corporate', 'Corporate Sponsor'),
        ('ngo', 'NGO / Non-Profit'),
        ('gov', 'Government Entity'),
        ('alumni', 'University Alumni')
    ], string='Organization Type', default='corporate')

    target_amount = fields.Monetary('Pledged Amount', currency_field='currency_id')
    amount_raised = fields.Monetary('Amount Donated', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    
    manager = fields.Char('University Point of Contact')
    
    project_ids = fields.Many2many('csr.project', string='Projects Supported')
    progress_ratio = fields.Float(compute='_compute_progress', string='Donation Progress')

    # New HTML field for color-coded progress
    progress_bar_html = fields.Html(string='Progress Bar', compute='_compute_progress_bar_html')

    color = fields.Integer(string='Color Index')

    @api.depends('amount_raised', 'target_amount')
    def _compute_progress(self):
        for record in self:
            if record.target_amount > 0:
                record.progress_ratio = (record.amount_raised / record.target_amount) * 100
            else:
                record.progress_ratio = 0

    @api.depends('progress_ratio')
    def _compute_progress_bar_html(self):
        for record in self:
            val = record.progress_ratio
            if val < 33:
                color = '#dc3545'  # Red
            elif val < 66:
                color = '#ffc107'  # Yellow/Orange
            else:
                color = '#28a745'  # Green
                
            record.progress_bar_html = f'''
                <div style="background-color: #e9ecef; border-radius: 4px; width: 100%; height: 18px; position: relative; overflow: hidden;">
                    <div style="background-color: {color}; width: {min(val, 100)}%; height: 100%; border-radius: 4px; text-align: center; font-size: 11px; font-weight: bold; color: #fff; line-height: 18px;">
                        {int(val)}%
                    </div>
                </div>
            '''