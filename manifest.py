# -*- coding: utf-8 -*-
{
    'name': 'Chat Webhook',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Chat frontend configurable via Webhook',
    'description': 'Agrega un chat emergente que envía mensajes a un webhook configurable.',
    'depends': ['website'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/chat_snippet.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'chat_webhook/static/src/css/chat_styles.css',
            'chat_webhook/static/src/xml/chat_templates.xml',
            'chat_webhook/static/src/js/chat_widget.js',
        ],
        'web.assets_backend': [
            'chat_webhook/static/src/js/settings.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}