from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Snippet
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from guesslang import Guess
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)




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


class SnippetIndexView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_index.html'

    # Use the following snippet to override the context data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # access context dictionary here...
    #     return context


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class SnippetListView(View):
    model = Snippet
    template_name = 'snippets/snippet_list.html'

    def get(self, request, *args, **kwargs):
        ctx = {'message': 'Hello Django!'}
        template_name = 'snippets/snippet_list.html'
        snip = Snippet.objects.all()
        page_number = request.GET.get('page', 1)
        paginator = Paginator(snip, 25)
        # import pdb; pdb.set_trace()
        try:
            snippet = paginator.page(page_number)
        except PageNotAnInteger:
            snippet = paginator.page(1)
        except EmptyPage:
            snippet = paginator.page(paginator.num_pages)

        ctx['snippet'] = snippet
        return render(request, template_name, ctx)


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

