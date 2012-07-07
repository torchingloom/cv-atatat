from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from forms import *
from extra_views import UpdateWithInlinesView

class ProfileView(DetailView):
    model = User
    template_name = 'account/profile-view.html'


class ProfileOwnerView(ProfileView):
    @method_decorator(user_passes_test(lambda u: u.is_authenticated()))
    def dispatch(self, request, *args, **kwargs):
        return super(DetailView, self).dispatch(request, *args, **kwargs)
    def get_object(self, queryset=None):
        return self.request.user


class ProfileEditView(UpdateWithInlinesView):
    model = User
    template_name = 'account/profile-edit.html'
    success_url = '/profile/view'
    inlines = [ProfileInlineForm]
    form_class = ProfileForm
    def get_object(self):
        return self.request.user


