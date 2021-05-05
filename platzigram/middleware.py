"""Platzigram middleware"""
#Django
from django.shortcuts import redirect
from django.urls import reverse
class ProfileCompletionMeddleware:
    """Profile completion middleware
        ensure every user that is interacting with the platform
        have the profile picture and biography
    """
    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response


    def __call__(self, request):
        """Code to be execute for each request before the view is called"""
        if not request.user.is_anonymous and not request.user.is_staff:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                    return redirect('users:update_profile')
        response = self.get_response(request)
        return  response