from django.urls import path
from .views import TopIndexView
from .views import CoStoreDetailView
from .views import CoInquiryForm
from .views import TopLoginView
from .views import CoCheckInquiryInfoView
from .views import TestView
from .views import CoInquiryPerfectView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'top'
urlpatterns = [
    path('', TopIndexView.as_view(), name='index'),  # トップページ
    path('topdetail/<int:pk>/',CoStoreDetailView.as_view(),name="detail"),#詳細ページ #<int:pk>
    path('topinquiry/',CoInquiryForm.as_view(),name="inquiry"),#問い合わせ
    path('login/',TopLoginView.as_view(),name="login"),#ログインページ
    path('test/<str:userid>',TestView.as_view(),name="test"),#テストページ
    path('topcheckinquiry/',CoCheckInquiryInfoView.as_view(),name="checkinquiry"),#問い合わせ内容確認
    path('inquiryperfect/',CoInquiryPerfectView.as_view(),name="inquiryperfect"),#問い合わせ完了画面
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)