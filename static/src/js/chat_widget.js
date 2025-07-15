odoo.define('chat_webhook.chat_widget', function (require) {
  'use strict';
  const ajax = require('web.ajax');

  document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('chat-toggle-button');
    const popup = document.getElementById('chat-popup');
    const closeBtn = document.getElementById('chat-close');
    const sendBtn = document.getElementById('chat-send');
    const input = document.getElementById('chat-input-field');
    const messagesContainer = document.getElementById('chat-messages');

    function appendMessage(text, sender) {
      const msgEl = document.createElement('div');
      msgEl.className = sender === 'user' ? 'chat-message user' : 'chat-message bot';
      msgEl.textContent = text;
      messagesContainer.appendChild(msgEl);
      messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    toggle.addEventListener('click', () => popup.classList.toggle('hidden'));
    closeBtn.addEventListener('click', () => popup.classList.add('hidden'));

    sendBtn.addEventListener('click', () => {
      const message = input.value.trim();
      if (!message) return;
      appendMessage(message, 'user');
      ajax.jsonRpc('/chat_webhook/send_message', 'call', { message })
        .then(response => {
          const botText = (response.response && response.response.text) || 'Error al recibir respuesta';
          appendMessage(botText, 'bot');
        });
      input.value = '';
    });
  });
});