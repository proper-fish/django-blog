from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', login_required(views.PostAdd.as_view()), name='post_new'),
    path('post/<int:pk>/edit/', login_required(views.PostEdit.as_view()), name='post_edit'),
    path('drafts/', login_required(views.BlogDrafts.as_view()), name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('suggest/', views.suggest_news, name='suggest_news'),
    path('suggested_news/', views.suggested_list, name='suggested_list'),
]
