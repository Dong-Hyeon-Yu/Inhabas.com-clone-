from board.dto import BoardDTO


class BoardSerializer:
    def __init__(self):
        pass

    @staticmethod
    def serialize(board: BoardDTO):
        return {
            'id': board.pk,
            'title': board.title,
            'content': board.content,
            'writer': board.writer,
            'date_created': board.created,
            'date_fixed': board.fix,
        }

    @staticmethod
    def serialize_all(board_list: [BoardDTO, ]):
        return [BoardSerializer.serialize(board) for board in board_list]