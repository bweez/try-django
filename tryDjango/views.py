"""
To render html web pages
"""

from django.http import HttpResponse

from articles.models import Article
from django.template.loader import render_to_string
import random




# args and keyword args kwargs are all of the arguments being passed to a function
def home_view(request, *args, **kwargs):
    """
    Take a request and 
    return HTML as a response
    """

    articles = Article.objects.all()

    context = {articles: articles}

    HTML_STRING = render_to_string("home-view.html", context=context)

    # Simple example worth deleting
    # number = random.randint(10,100)

    # HTML_STR = f"""
    # <h1>Hello world! {number}</h1>
    # """
    # return HttpResponse(HTML_STR)
    return HttpResponse(HTML_STRING)
