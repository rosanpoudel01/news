from django.urls import path
from news.views import (
    news_list,
    news_add_view,
    news_delete_view,
    news_edit_view,
    demo_for_ajax,
    news_home,
    news_detail_view,
    search_view,
    news_by_category_view,
)

app_name = "news"
urlpatterns = [
    path("news-list/", news_list, name="news"),
    path("", news_home, name="newshome"),
    path("search/", search_view, name="searchnews"),
    path("news-add/", news_add_view, name="news_add"),
    path("news-edit/<int:newsid>/", news_edit_view, name="news_edit"),
    path("news-delete/", news_delete_view, name="news_delete"),
    path("news/<int:newsid>/", news_detail_view, name="news_detail"),
    path("category/<int:categoryid>/", news_by_category_view, name="catnews"),
    path("demo-for-ajax", demo_for_ajax, name="demo_for_ajax"),
]
