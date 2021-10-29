import abc
from datetime import datetime
from board.repository import BoardDatabase


##
# Board Interface
##
class BoardInteractor(object):
    def __init__(self, board_db: BoardDatabase):
        self.db = board_db

    @abc.abstractmethod
    def set_params(self, *args):
        raise NotImplemented

    @abc.abstractmethod
    def execute(self):
        raise NotImplemented


class CreateBoardInteractor(BoardInteractor):
    def set_params(self, title: str, writer: int, content: str, type: str, fix: datetime = None):
        self.title = title
        self.writer = writer
        self.content = content
        self.type = type
        self.fix = fix

        return self

    def execute(self):
        return self.db.create_board(self.title, self.writer, self.content, self.type, self.fix)


class GetBoardInteractor(BoardInteractor):
    def set_params(self, pk: int):
        self.pk = pk

        return self

    def execute(self):
        return self.db.get_board(pk=self.pk)


class UpdateBoardInteractor(BoardInteractor):
    def set_params(self, pk: int, title: str, content: str, fix: datetime = None):
        self.pk = pk
        self.title = title
        self.content = content
        self.fix = fix

        return self

    def execute(self):
        return self.db.update_board(self.pk, self.title, self.content, self.fix)


class DeleteBoardInteractor(BoardInteractor):
    def set_params(self, pk: int):
        self.pk = pk

        return self

    def execute(self):
        return self.db.delete_board(pk=self.pk)


class GetBoardListInteractor(BoardInteractor):
    def set_params(self, type: str):
        self.type = type

        return self

    def execute(self):
        return self.db.get_board_list(type=self.type)

