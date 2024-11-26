from django.contrib.auth.models import AnonymousUser  
from django.http import HttpResponseForbidden  
from datetime import datetime, timedelta  

list_ban = {}  

class LoggerMiddleware:  
    def __init__(self, get_response):  
        self.get_response = get_response  
        self.activate = {}  

    def __call__(self, request):  
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')  
        user = "AnonymousUser" if isinstance(request.user, AnonymousUser) else str(request.user)  

        response = self.get_response(request)  

        self.activate.update({  
            'ip': ip,  
            'user': user,  
            "view": self._get_view_name(request),  
            "host": request.get_host(),  
        })  

        try:  
            with open('loggers.log', "a") as f:  
                f.write(f"{self.activate}\n")  
        except Exception as e:  
            print(f"Error writing to log file: {e}")  

        return response  

    def _get_view_name(self, request):  
        view_name = getattr(request, 'resolver_match', None)  
        if view_name:  
            return f"{view_name.view_name} ({view_name.url_name})"  
        return "No view associated"  


