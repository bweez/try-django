from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from .models import Article
from .forms import ArticleForm

from django.template.loader import render_to_string
import random


def article_search_view(request):

    # Prints the details about the properties
    # within the class that any object is an instance of
    # print(dir(request))

    # Prints the values being passed to a GET query
    # in the QueryDict class
    # Example output: <QueryDict: {q:['query']}
    # print(dir(request.GET))

    query_dict = dict(request.GET)

    # <input type="text" name="q" />
    # this form input is what defines the request dictionary
    # query = query_dict.get('q')

    try:
        query = int(query_dict.get('q'))
    except:
        query = None

    article = None
    if query is not None:
        article = Article.objects.get(id=query)
    context = {object: article}

    return render(request, 'articles/search.html', context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        # simplified form handling
        new_article = form.save()

        # old example form handling:
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # new_article = Article.objects.create(title=title, content=content)
        # context['title'] = title
        # context['content'] = content

        # used as context after the content is created
        # to show the end-user
        context['object'] = new_article
        context['created'] = True

        # another way to clear the form after it has been submitted
        # context['form'] = ArticleForm()

    return render(request, 'articles/create.html', context=context)


def article_details_view(request, slug=None):
    article = None
    if id is not None:
        try:
            article = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except:
            raise Http404

    context = {article: article}

    return render(request, 'articles/detail.html', context=context)
