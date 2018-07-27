import logging

from plivo.providers.redis import RedisProvider

logger = logging.getLogger('InboundSMS')
RATELIMIT_THRESHOLD = 50


class OutboundSMSValidator():
    rclient = RedisProvider().get_instance()

    def validate_input(data):
        if data.get('from') is None:
            return False, {
                'message': '',
                'error': 'from input is missing'
            }

        if data.get('to') is None:
            return False, {
                'message': '',
                'error': 'to input is missing'
            }

        if data.get('text') is None:
            return False, {
                'message': '',
                'error': 'text is missing'
            }

        return True, dict()

    def validate_inbound_sms(sender, receiver, sms_text):
        # validate lengths
        if not 6 <= len(sender) <= 16:
            return False, {
                'message': '',
                'error': 'from parameter is invalid'
            }

        if not 6 <= len(receiver) <= 16:
            return False, {
                'message': '',
                'error': 'to parameter is invalid'
            }

        if not 1 <= len(sms_text) <= 120:
            return False, {
                'message': '',
                'error': 'text parameter is invalid'
            }

    def validate_for_stop_words(sender, receiver):
        """if the stop word for the number is cached
        """
        conn = rclient.get_conn()
        value = conn.get('stop:' + str(receiver) + ':' + str(sender))
        if value:
            return True, dict()
        else:
            return False, {
                'message': '',
                'error': 'unknown failure',
            }
