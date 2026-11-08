from odoo import models, fields, api

class ProjectVolunteerLine(models.Model):
    _name = 'csr.project.volunteer.line'
    _description = 'Project Volunteer Log'

    project_id = fields.Many2one('csr.project', string='Project', ondelete='cascade')
    volunteer_id = fields.Many2one('csr.volunteer', string='Student', required=True, ondelete='cascade')
    hours = fields.Float('Hours Worked', required=True, default=0.0)

    university_id = fields.Char(related='volunteer_id.university_id', string='University ID', readonly=True)
    major = fields.Char(related='volunteer_id.major', string='Major', readonly=True)

class Project(models.Model):
    _name = 'csr.project'
    _description = 'Community Service Project'

    name = fields.Char('Project Name', required=True)
    fundraising_ids = fields.Many2many('csr.fundraising', string='Donor Organizations')
    contractor_id = fields.Many2one('csr.contractor', 'Primary Contractor')
    
    volunteer_line_ids = fields.One2many('csr.project.volunteer.line', 'project_id', string='Student Volunteers')
    
    description = fields.Text('Description')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    
    progress = fields.Selection([
        ('planning', 'Planning'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ], string='Status', default='planning')
        
    expense_amount = fields.Monetary('Our Expense', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    duration_days = fields.Integer(string='Duration (days)', compute='_compute_duration', store=True)
    color = fields.Integer(string='Color', compute='_compute_color', store=True)

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration_days = (record.end_date - record.start_date).days
            else:
                record.duration_days = 0

    @api.depends('progress')
    def _compute_color(self):
        for record in self:
            if record.progress == 'planning':
                record.color = 1
            elif record.progress == 'ongoing':
                record.color = 3
            elif record.progress == 'completed':
                record.color = 10
            else:
                record.color = 0