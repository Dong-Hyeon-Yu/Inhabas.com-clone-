from django.urls import path
from .factory import NoticeBoardListControllerFactory
from .views_example import NoticeBoardListView

urlpatterns = [
    path('notice', NoticeBoardListView.as_view(controller_factory=NoticeBoardListControllerFactory)),
]