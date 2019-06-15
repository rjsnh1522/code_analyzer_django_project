from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse, JsonResponse
from .models import Snippet
from django.views import View
from django.views.generic import ListView, DetailView
from guesslang import Guess
from background_task import background



def guess_language(code_value):
    print("code here")
    lang = Guess().language_name(code_value)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "snippet_snippet", {
            "type": "code_language",
            "message": lang
        }
    )


class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'

    # Use the following snippet to override the context data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # access context dictionary here...
    #     return context


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'


class SnippetCheckView(View):

    def post(self, request):
        code_value = request.POST['code_value']
        guess_language(code_value)
        data = {'data': 'data'}
        return JsonResponse(data)

    def get(self, request):
        import ipdb; ipdb.set_trace()

