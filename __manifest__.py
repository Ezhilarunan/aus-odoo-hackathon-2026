{
    'name': 'UniAid',
    'version': '2.0',
    'summary': 'Track student volunteering, external contractors, and community projects',
    'author': 'Your Team Name',
    'category': 'CSR',
    'depends': ['base', 'mail'],
    'assets': {
        'web._assets_primary_variables': [
            ('before', 'web/static/src/scss/primary_variables.scss',
             'community_service/static/src/scss/variables.scss'),
        ],
        'web.assets_backend': [
            'community_service/static/src/scss/theme.scss',
            'community_service/static/src/xml/navbar.xml',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/report_volunteer_certificate.xml',
        'data/mail_template.xml', 
        'views/volunteer_views.xml',
        'views/fundraising_views.xml',
        'views/contractor_views.xml',
        'views/project_views.xml',
        'views/report_project_progress.xml',
        'views/menu.xml', 
        'data/demo_data.xml',
    ],
    'demo': ['data/demo_data.xml'],
    'installable': True,
    'application': True,
}
