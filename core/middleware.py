from django.contrib import messages
from django.contrib.auth import logout


class SessionTimeoutMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if (
            request.user.is_authenticated
            and not request.session.get_expiry_age()
        ):
            messages.warning(
                request,
                "Your session has expired. Please log in again."
            )

            logout(request)

        response = self.get_response(request)

        return response