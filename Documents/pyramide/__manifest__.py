{
    'name': 'Mon Module',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/user_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mon_module/static/src/css/kanban.css',
        ],
    },
    'application': True,
    
}
