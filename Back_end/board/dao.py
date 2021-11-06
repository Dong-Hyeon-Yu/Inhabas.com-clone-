from datetime import datetime
from DB.models import Board
from board.dto import BoardDTO

board_type = {
        'notice':       1,
        'free':         2,
        'question':     3,
        'activity':     4,
        'all':          5,
        'alpha':        6,
        'beta':         7,
        'executives':   8,
        'suggestion':   9,
    }


class BoardDAO(object):
    """
    Data Access Object For Board. (DAO)
    This object can access database(board table) using Django ORM.
    when get a board data, this object returns a board DTO not a QuerySet nor a ORM.
    So be careful that using a DAO prevents from using django ORM features directly!
    (ex, related query set, prefetched related set, etc)

    Do not allow db-access-things include django-query outside but here.
    """
    def __init__(self):
        """
        If there are many databases, recommend to make many DAO classes according to each databases.
        This Data Access Object is base on default database.
        """
        super()

    def _decode_orm_board(self, orm_board) -> BoardDTO:
        return BoardDTO(
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

    def _get_type_no(self, type: str) -> int:
        try:
            type_no = board_type[type]
        except KeyError:
            raise KeyError(f"Not exist board type {type}")

        return type_no

    def get_board(self, pk: int) -> BoardDTO:
        orm_board = self._get_orm_board(pk)

        return self._decode_orm_board(orm_board)

    def delete_board(self, pk: int) -> None:
        orm_board = self._get_orm_board(pk)

        orm_board.delete()

    def create_board(self, title: str, writer: int, content: str, type: str, fix: datetime) -> BoardDTO:
        type_no = self._get_type_no(type=type)

        orm_board = Board.objects.create(
            board_title=title, board_writer_id=writer, board_cont=content, board_type_no_id=type_no, board_fixdate=fix)

        return self._decode_orm_board(orm_board)

    def update_board(self, pk: int, title: str, content: str, fix: datetime) -> None:
        orm_board = self._get_orm_board(pk)
        orm_board.board_title = title
        orm_board.board_cont = content
        orm_board.board_fixdate = fix
        orm_board.save()

    def get_board_list(self, type: str) -> [BoardDTO, ]:
        type_no = self._get_type_no(type=type)

        return [self._decode_orm_board(orm_board) for orm_board in Board.objects.filter(board_type_no_id=type_no).all()]
