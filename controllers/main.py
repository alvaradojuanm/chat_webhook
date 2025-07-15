# -*- coding: utf-8 -*-
from odoo import http
import requests

class ChatWebhookController(http.Controller):
    @http.route('/chat_webhook/send_message', type='json', auth='public', methods=['POST'], csrf=False)
    def send_message(self, message):
        # Obtiene la URL del sistema
        url = http.request.env['ir.config_parameter'].sudo().get_param('chat_webhook.webhook_url')
        if url:
            try:
                resp = requests.post(url, json={'text': message})
                return {'status': 'sent', 'response': resp.json()}
            except Exception as e:
                return {'status': 'error', 'message': str(e)}
        return {'status': 'error', 'message': 'Webhook no configurado'}