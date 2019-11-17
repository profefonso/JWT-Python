from django.urls import path
from django.contrib import admin
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view


from .views import DetailDetail, DetailList, UserCreate, ValidateJWT, UserList

schema_view = get_swagger_view(title='JWT WEB API')


urlpatterns = [
    path('front/betsy/irish/embargo/admin/', admin.site.urls),

    # Swagger API
    path(
        'api/',
        schema_view,
        name='api'
    ),

    # detail
    path(
        'detail/',
        DetailList.as_view(),
        name=DetailList.name
    ),
    re_path(
        '^detail/(?P<pk>[0-9]+)/$',
        DetailDetail.as_view(),
        name=DetailDetail.name
    ),
    path(
        'user/',
        UserCreate.as_view(),
        name='account-create'
    ),
    path(
        'user-list/',
        UserList.as_view(),
        name=UserList.name
    ),
    path(
        'validate/',
        ValidateJWT.as_view(),
        name='validate-token'
    ),
]
