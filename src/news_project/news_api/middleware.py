from django.shortcuts import redirect


class RedirectOn403Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 403 and not request.path.startswith('/login/'):
            return redirect('login')
        return response
