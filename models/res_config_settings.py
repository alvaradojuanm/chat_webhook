# -*- coding: utf-8 -*-
from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    chat_webhook_url = fields.Char(
        string='Webhook URL',
        config_parameter='chat_webhook.webhook_url',
        help='URL a la que se envían los mensajes de chat'
    )
    chat_enabled = fields.Boolean(
        string='Chat habilitado',
        config_parameter='chat_webhook.enabled',
        default=False,
        help='Permite activar o desactivar el chat en el frontend'
    )