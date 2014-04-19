
#from django.http import HttpResponse

#def home(request):
#    return HttpResponse("You're looking at the home page.")

from django.views.generic import TemplateView, FormView
from elephantblog.views import ArchiveIndexView
from taggit.models import Tag
from lbp.forms import UnsubscribeForm
from pennyblack.module.subscriber.models import NewsletterSubscriber

class HomeView(TemplateView):
    template_name = "homepage2.html"

class TagView(ArchiveIndexView):
    def get_queryset(self):
        queryset=super(TagView,self).get_queryset()
        slug = self.kwargs['slug'].lower()
        self.tag = Tag.objects.get(slug=slug)
        return queryset.filter(tags=self.tag)
#    the match is not case-sensitive so use the same case all times.

    def get_context_data(self, **kwargs):
        return super(TagView,self).get_context_data(tag=self.tag, **kwargs)

class UnsubscribeView(FormView):
    form_class = UnsubscribeForm
    success_url = '/newsletter/unsubscribe/confirm/'

    def form_valid(self, form):
        person = NewsletterSubscriber.objects.get_or_add(form.cleaned_data['email'])
        person.unsubscribe()
        return super(UnsubscribeView, self).form_valid(form)
