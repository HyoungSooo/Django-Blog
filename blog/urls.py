from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostShareView
)
from .feeds import LatestPostsFeed

from datetime import datetime

from django.contrib.auth import get_user_model
from ninja_extra import api_controller, route, status, NinjaExtraAPI, Router
from ninja_extra.permissions import IsAdminUser, IsAuthenticated
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.tokens import SlidingToken
from .models import Post
from ninja.schema import Schema


class PostSchema(Schema):
    title: str
    slug: str
    body: str
    publish: datetime
    created: datetime
    tags: str


api = Router(auth=JWTAuth())


@api.post('/test', response=PostSchema)
def test(request, a: PostSchema):
    a.__dict__.update({'author': request.user, 'status': 'published'})
    Post.objects.create(**a.__dict__)

    data = Post.objects.filter(publish=a.publish).first()
    for i in a.tags.split(','):
        data.tags.add(i)

    return a.__dict__


app_name = 'blog'


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', PostListView.as_view(),
         name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         PostDetailView.as_view(), name='post_detail'),
    path('<int:post_id>/share/', PostShareView.as_view(), name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
