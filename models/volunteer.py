from odoo import models, fields, api

class Volunteer(models.Model):
    _name = 'csr.volunteer'
    _description = 'Student Volunteer Profile'
    _rec_name = 'name'

    name = fields.Char('Student Name', required=True)
    university_id = fields.Char('University ID')
    major = fields.Char('Major', default='Computer Science')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    
    sssd_registered = fields.Boolean('Registered with Sharjah Social Services')
    red_crescent_registered = fields.Boolean('Emirates Red Crescent Volunteer')
    
    volunteer_line_ids = fields.One2many('csr.project.volunteer.line', 'volunteer_id', string='Project Logs')
    
    total_hours = fields.Float(string='Total Volunteering Hours', compute='_compute_total_hours', store=True)

    @api.depends('volunteer_line_ids.hours', 'volunteer_line_ids.project_id.progress')
    def _compute_total_hours(self):
        for volunteer in self:
            completed_lines = volunteer.volunteer_line_ids.filtered(lambda l: l.project_id.progress == 'completed')
            volunteer.total_hours = sum(completed_lines.mapped('hours'))

    def action_send_certificate_email(self):
        self.ensure_one()
        template = self.env.ref('community_service.email_template_volunteer_certificate', raise_if_not_found=False)
        if template and self.email:
            template.send_mail(self.id, force_send=True)
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Email Sent',
                    'message': f'Certificate successfully sent to {self.email}',
                    'type': 'success',
                    'sticky': False,
                }
            }