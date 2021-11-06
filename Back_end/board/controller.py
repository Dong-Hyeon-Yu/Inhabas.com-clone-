from board.serializer import BoardSerializer
from board.serviceImpl import GetBoardListServiceImpl


class NoticeBoardListController:
    def __init__(self, board_service_provider: GetBoardListServiceImpl):
        self.board_service_provider = board_service_provider

    def execute(self):
        try:
            board_list = self.board_service_provider \
                                .set_params(type='notice') \
                                .execute()
        except KeyError as e:  # service provider 에서 type dict 오류 시
            body = {'error': e.__str__}  # 메세지 출력 어떻게 하는거지..?
            status = 404
        else:
            body = BoardSerializer.serialize_all(board_list)
            status = 200

        return body, status
