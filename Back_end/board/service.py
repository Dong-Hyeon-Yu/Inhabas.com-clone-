import abc
from board.dao import BoardDAO


##
# Board Interface
##
class BoardServiceInterface(object):
    """
    Board Service Interface.
    Implement this interface according to Use Cases,
    """
    def __init__(self, board_dao: BoardDAO):
        self.db = board_dao

    @abc.abstractmethod
    def set_params(self, *args):
        raise NotImplemented

    @abc.abstractmethod
    def execute(self):
        raise NotImplemented
