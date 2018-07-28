import random
import string

from datetime import datetime, timedelta

from flask import request, jsonify

from plivo.app import db

from plivo.models.sms import SMS
from plivo.providers.redis import RedisProvider
from plivo.services.outbound.validator import OutboundSmsValidator


class OutboundSmsService(object):
    validator = OutboundSmsValidator()
    rclient = RedisProvider.get_instance()

    def post_outbound_sms():
        data = request.data

        success, msg = validator.validate_input(data)
        # Raise bad request
        if not success:
            return jsonify(msg), 400

        sender = data.get('from')
        receiver = data.get('to')
        sms_text = data.get('text')

        success, msg = validator.validate_inbound_sms(sender, receiver, sms_text)
        # Raise bad request
        if not success:
            return jsonify(msg), 400

        success, msg = validator.validate_for_stop_words(sender, receiver)
        # Raise bad request
        if not success:
            return jsonify(msg), 400

        success, msg = check_rate_limit(sender)
        # Raise bad request
        if not success:
            return jsonify(msg), 429

        try:
            sms = SMS(sender=sender, receiver=receiver, sms_text=sms_text)
            db.session.add(sms)
            db.session.commit()
            msg = {
                'message': 'outbound sms is ok', 'error': ''
            }

            return jsonify(msg), 200
        except Exception:
            msg = {
                'message': '',
                'error': 'unknown failure'
            }
            return jsonify(msg), 400

    def check_rate_limit():
        conn = instance.get_conn()
        total_seconds = timedelta(hours=1).total_seconds()
        current_hour = datetime.now().hour
        key = 'from:' + str(sender) + ':' + current_hour
        counter = conn.get(key)
        if value is None:
            conn.setex(key, total_seconds, 1)
        else:
            counter = int(counter)
            if counter < 50:
                conn.incr(key)
                return True, {}
            else:
                return False, {
                    'message': '',
                    'error': 'limit reached for from ' + str(sender),
                }
