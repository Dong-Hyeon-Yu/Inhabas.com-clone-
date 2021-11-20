from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view
from board.factory import NoticeBoardListControllerFactory


@api_view(['GET'])
@login_required
def notice_board_list_view():
    # body, status = NoticeBoardListController(GetBoardListServiceImpl(BoardDAO())).get()
    body, status = NoticeBoardListControllerFactory.create()  # 위와 같이 작성해야하는걸 factory 로 해결

    return JsonResponse(data=body, status=status, safe=False)


# /board/notice
class NoticeBoardListView(View):
    controller_factory = None

    # @method_decorator(permission_required('board.list_notice_board', raise_exception=True), name='dispatch')
    def get(self, request, *args, **kwargs):
        body, status = self.controller_factory.create().execute()
        return JsonResponse(data=body, status=status, safe=False)

    # @method_decorator(permission_required('board.create_notice_board', raise_exception=True), name='dispatch')
    def post(self):
        pass