import json
import string

from datetime import datetime, timedelta

from flask import request, jsonify

from plivo.app import db

from plivo.models.sms import SMS
from plivo.providers.redis import RedisProvider
from plivo.services.inbound.validator import InboundSmsValidator
from plivo.services.outbound.validator import OutboundSmsValidator


class InboundSmsService(object):
    validator = InboundSmsValidator()

    def post_inbound_sms(self):
        data = json.loads(request.data)

        success, msg = self.validator.validate_input(data)
        # Raise bad request
        if not success:
            return jsonify(msg), 400

        sender = data.get('from')
        receiver = data.get('to')
        sms_text = data.get('text')

        success, msg = self.validator.validate_inbound_sms(sender, receiver, sms_text)
        # Raise bad request
        if not success:
            return jsonify(msg), 400

        try:
            sms = SMS(sender=sender, receiver=receiver, sms_text=sms_text)
            db.session.add(sms)
            db.session.commit()
            msg = {
                'message': 'inbound sms is ok', 'error': ''
            }
            # TODO use redis pipelining
            instance = RedisProvider().get_instance()
            conn = instance.get_conn()

            if ((text == 'STOP') or
                (text == 'STOP\r') or
                (text == 'STOP\n') or
                (text == 'STOP\r\n')):
                # there can be multiple pairs with sender-receiver
                total_seconds = timedelta(hours=4).total_seconds()

                key = 'stop:' + str(sender) + ':' + str(receiver)
                conn.setex(key, total_seconds, 1)

            return jsonify(msg), 200
        except Exception:
            msg = {
                'message': '',
                'error': 'unknown failure'
            }
            return jsonify(msg), 400
