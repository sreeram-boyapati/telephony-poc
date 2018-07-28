import json
import os

from datetime import datetime

from flask import request, jsonify

from plivo.app import app, basic_auth
from plivo.models.sms import SMS
from plivo.services.inbound.service import InboundSmsService
from plivo.services.outbound.service import OutboundSmsService



@app.route('/', methods=['GET'])
def hello_world():
    msg = {
        'message': 'Welcome to plivo',
        'error': ''
    }
    return jsonify(msg), 200


@app.route('/inbound/sms', methods=['POST'])
@basic_auth.required
def send_inbound_sms():
    service = InboundSmsService()

    if request.method == 'POST':
        json_msg, status_code = service.post_inbound_sms()
        return json_msg, status_code


@app.route('/outbound/sms', methods=['POST'])
@basic_auth.required
def send_outbound_sms():
    service = OutboundSmsService()

    if request.method == 'POST':
        json_msg, status_code = service.post_outbound_sms()
        return json_msg, status_code
