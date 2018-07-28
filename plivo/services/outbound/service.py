import json
import random
import string
import traceback

from datetime import datetime, timedelta

from flask import request, jsonify

from plivo.app import db

from plivo.models.sms import SMS
from plivo.providers.cache import RedisProvider
from plivo.services.outbound.validator import OutboundSmsValidator


class OutboundSmsService(object):
    validator = OutboundSmsValidator()
    rclient = RedisProvider.get_instance()

    def post_outbound_sms(self):
        data = json.loads(request.data)

        success, msg = self.validator.validate_input(data)
        # Raise bad request
        if not success:
            return jsonify(msg), 400

        sender = data.get('from')
        receiver = data.get('to')
        sms_text = data.get('text')

        success, msg = self.validator.validate_outbound_sms(sender, receiver, sms_text)
        # Raise bad request
        if not success:
            return jsonify(msg), 400

        success, msg = self.validator.validate_for_stop_words(sender, receiver)
        # Raise bad request
        if not success:
            return jsonify(msg), 400

        success, msg = self.check_rate_limit(sender)
        rate_counter = 0
        # Raise bad request
        if not success:
            return jsonify(msg), 429
        else:
            rate_counter = msg['current_rate']

        try:
            sms = SMS(sender=sender, receiver=receiver, sms_text=sms_text)
            db.session.add(sms)
            db.session.commit()
            msg = {
                'message': 'outbound sms is ok', 'error': ''
            }

            resp = jsonify(msg)
            resp.headers.extend({'X-Rate-Limit-Value': str(rate_counter)})
            resp.headers.extend({'X-Rate-Limit-Threshold': '50'})

            return resp, 200
        except Exception:
            tb = traceback.format_exc()
            print tb
            msg = {
                'message': '',
                'error': 'unknown failure'
            }
            return jsonify(msg), 500

    def check_rate_limit(self, sender):
        conn = self.rclient.get_conn()
        total_seconds = int(timedelta(hours=1).total_seconds())
        current_hour = int(datetime.now().hour)
        key = 'ratelimit:' + str(sender) + ':' + str(current_hour)
        counter = conn.get(key)
        if counter is None:
            conn.setex(key, total_seconds, 1)
            return True, {
                'current_rate': 1,
            }
        else:
            counter = int(counter)
            # TODO implement locks for concurrency
            if counter < 50:
                conn.incr(key)
                return True, {
                    'current_rate': counter+1,
                }
            else:
                return False, {
                    'message': '',
                    'error': 'limit reached for from ' + str(sender),
                }
