import logging

logger = logging.getLogger('InboundSMS')
RATELIMIT_THRESHOLD = 50


class InboundSmsValidator():

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

        if data.get('from') == data.get('to'):
            return False, {
                'message': '',
                'error': 'from/to cannot be same'
            }

        if data.get('text') is None:
            return False, {
                'message': '',
                'error': 'text input is missing'
            }

        return True, dict()


    def validate_inbound_sms(self, sender, receiver, sms_text):
        # validate lengths
        if not 6 <= len(sender) <= 16:
            return False, {
                'message': '',
                'error': 'from input is invalid'
            }

        if not 6 <= len(receiver) <= 16:
            return False, {
                'message': '',
                'error': 'to input is invalid'
            }

        if not 1 <= len(sms_text) <= 120:
            return False, {
                'message': '',
                'error': 'text input is invalid'
            }

        return True, dict()
