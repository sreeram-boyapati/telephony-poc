import logging

logger = logging.getLogger('InboundSMS')
RATELIMIT_THRESHOLD = 50


class InboundSmsValidator():

    def validate_input(data):
        if data.get('sender') is None:
            return False, {
                'message': '',
                'error': 'from input is missing'
            }

        if data.get('receiver') is None:
            return False, {
                'message': '',
                'error': 'to input is missing'
            }

        if data.get('sms_text') is None:
            return False, {
                'message': '',
                'error': 'text input is missing'
            }

        return True, dict()


    def validate_inbound_sms(sender, receiver, sms_text):
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
