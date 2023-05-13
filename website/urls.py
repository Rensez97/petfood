from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, HondListView, KatListView, KnaagdierListView, ApotheekListView, OverOnsView, AanbiedingView, ZoekView, ProductView

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='petfood-home'),
    path('aanbiedingen/', AanbiedingView.as_view(), name='aanbiedingen-algemeen'),
    path('hond/', HondListView.as_view(), name='hond-algemeen'),
    path('kat/', KatListView.as_view(), name='kat-algemeen'),
    path('knaagdier/', KnaagdierListView.as_view(), name='knaagdier-algemeen'),
    path('apotheek/', ApotheekListView.as_view(), name='apotheek-algemeen'),
    path('overons/', OverOnsView.as_view(), name='over-ons'),
    path('zoeken/', ZoekView.as_view(), name='zoeken'),
    path('product/', ProductView.as_view(), name='product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
