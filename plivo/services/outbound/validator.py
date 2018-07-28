import logging

from plivo.providers.cache import RedisProvider

logger = logging.getLogger('InboundSMS')
RATELIMIT_THRESHOLD = 50


class OutboundSmsValidator():
    rclient = RedisProvider.get_instance()

    def validate_input(self, data):
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

    def validate_outbound_sms(self, sender, receiver, sms_text):
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

        return True, dict()

    def validate_for_stop_words(self, sender, receiver):
        """if the stop word for the number is cached
        """
        conn = self.rclient.get_conn()
        key = 'stop:{}:{}'.format(receiver, sender)
        value = conn.get(key)
        if value:
            return False, {
                'message': '',
                'error': 'sms from `from` and `to` to blocked by STOP request',
            }
        else:
            return True, dict()
