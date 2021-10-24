from datetime import datetime
from DB.models import Board
from entity import BoardEntity

board_type = {
        'notice':       '1',
        'free':         '2',
        'question':     '3',
        'activity':     '4',
        'all':          '5',
        'alpha':        '6',
        'beta':         '7',
        'executives':   '8',
        'suggestion':   '9',
    }


class BoardDatabase(object):
    def __init__(self):
        super()

    def _decode_orm_board(self, orm_board) -> BoardEntity:
        return BoardEntity(
            pk=orm_board.pk,
            title=orm_board.board_title,
            writer=orm_board.board_writer_id,
            created=orm_board.board_created,
            fix=orm_board.board_fixdate,
            type=orm_board.board_type_no_id,
            content=orm_board.board_cont,
        )

    def _get_orm_board(self, pk: int) -> Board:
        try:
            orm_board = Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Board.DoesNotExist

        return orm_board

    def get_board(self, pk: int) -> BoardEntity:
        orm_board = self._get_orm_board(pk)

        return self._decode_orm_board(orm_board)

    def delete_board(self, pk: int) -> None:
        orm_board = self._get_orm_board(pk)

        orm_board.delete()

    def create_board(self, title: str, writer: int, content: str, type: str, fix: datetime) -> BoardEntity:
        try:
            type_no = board_type[type]
        except KeyError:
            raise KeyError(f"Not exist board type {type}")

        orm_board = Board.objects.create(
            board_title=title, board_writer_id=writer, board_cont=content, board_type_no_id=type_no, board_fixdate=fix)

        return self._decode_orm_board(orm_board)

    def update_board(self, pk: int, title: str, content: str, fix: datetime) -> None:
        orm_board = self._get_orm_board(pk)
        orm_board.board_title = title
        orm_board.board_cont = content
        orm_board.board_fixdate = fix
        orm_board.save()
