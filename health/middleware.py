class SecurityHeadersMiddleware:
    """Add conservative browser security headers for the demo service."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.setdefault("Content-Security-Policy", "default-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'")
        response.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        return response
