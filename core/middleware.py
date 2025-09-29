import logging
from datetime import datetime


class LogRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        print(
            f"[MIDDLEWARE] {datetime.now()} - {request.method} {request.path}")
        print(f"[MIDDLEWARE] User: {request.user}")

        with open('middleware_log.txt', 'a') as f:
            f.write(
                f"{datetime.now()} - {request.method} {request.path} - User: {request.user}\n")

        response = self.get_response(request)

        print(f"[MIDDLEWARE] Response Status: {response.status_code}")
        return response
