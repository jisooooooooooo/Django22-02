
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ # IP주소/blog

    path('',views.PostList.as_view()),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('category/<str:slug>/',views.category_page)
    #path('',views.index), #IP주소/blog
    #path('<int:pk>/',views.single_post_page)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)