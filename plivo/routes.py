import json

from datetime import datetime
from flask import request

from plivo.app import app

from plivo.models.sms import SMS

from plivo.services.inbound.service import InboundSmsService
from plivo.services.outbound.service import OutboundSmsService


@app.route('/inbound/sms', methods=['POST'])
def send_inbound_sms():
    service = InboundSmsService()

    if request.method == 'POST':
        json_msg, status_code = service.post_inbound_sms()
        return json_msg, status_code


@app.route('/outbound/sms', methods=['POST'])
def send_outbound_sms():
    service = OutboundSmsService()

    if request.method == 'POST':
        json_msg, status_code = service.post_outbound_sms()
        return json_msg, status_code
