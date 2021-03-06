import notifications.urls
from django.urls import include
from django.urls import path

from . import views
from .views import CommentCreateView
from .views import CommentDeleteView
from .views import CommentUpdateView
from .views import ExploreListView
from .views import PostDeleteView
from .views import PostDetailView
from .views import PostListView
from .views import PostUpdateView


# second- truncated request is sent here and a match is searched for in url patterns again
urlpatterns = [
    path("", PostListView.as_view(), name="wildpan-home"),
    path("about/us/", views.aboutUs, name="wildpan-about-us"),
    path("about/jobs/", views.aboutJobs, name="wildpan-about-jobs"),
    path("about/", views.redirectAboutView, name="wildpan-about-us-redirect"),
    path("explore/", ExploreListView.as_view(), name="wildpan-explore"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"
    ),
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
    path("comment/<int:pk>/", CommentCreateView.as_view(), name="comment-form"),
    path("profile/<str:username>/", views.public_profile, name="public-profile"),
    # path('profile/<str:username>/', views.PublicProfileView.as_view(), name='public-profile'),
    path("post/new/", views.post, name="post-add"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path(
        "profile/<str:username>/followers/",
        views.FollowerListView.as_view(),
        name="follower-list",
    ),
    path(
        "profile/<str:username>/following/",
        views.FollowerListView.as_view(),
        name="following-list",
    ),
    path("post/<int:pk>/likes/", views.LikeListView.as_view(), name="likes-list"),
    path("search/", views.SearchListView.as_view(), name="search-list"),
    path("likepost/", views.likePost, name="likepost"),
    path(
        "inbox/notifications/", include(notifications.urls, namespace="notifications")
    ),
    path("<str:username>/", views.public_profile, name="public-profile-base"),
]
