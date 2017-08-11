class VultrAPIException(Exception):
    def __init__(self, status_code=None):

        VULTR_RESPONSE_CODE = {
            400: 'Invalid API location. Check the URL that you are using.',
            403: 'Invalid or missing API key. Check that your API key is present and matches your assigned key.',
            405: 'Invalid HTTP method. Check that the method (POST|GET) matches what the documentation indicates.',
            412: 'Request failed. Check the response body for a more detailed description.',
            500: 'Internal server error. Try again at a later time.',
            503: 'Rate limit hit. API requests are limited to an average of 2/s. Try your request again later.'
        }

        if status_code not in VULTR_RESPONSE_CODE:
            raise Exception('Vultr API response code is unknown')

        Exception.__init__(self, VULTR_RESPONSE_CODE[status_code])
