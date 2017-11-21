from django.conf.urls import url
from .views import TodoitemAjax  # , todo_listCreateView

urlpatterns = [  # url(r'^$', todo_listCreateView.as_view()),
    url(r'^author-ajax/$', TodoitemAjax),
]
