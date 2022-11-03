
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # IP주소/blog

    path('',views.PostList.as_view()),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('category/<str:slug>/',views.category_page), # IP주소/blog/category/slug/
    path('tag/<str:slug>/', views.tag_page), #IP주소/blog/tag/slug/

    #path('',views.index), #IP주소/blog
    #path('<int:pk>/',views.single_post_page)
]

