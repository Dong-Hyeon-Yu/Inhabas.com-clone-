from dataclasses import dataclass
from datetime import datetime


@dataclass
class BoardDTO(object):
    """
    Data Transfer Object For Board.
    Do use this object not django ORM object when implementing Services, Views
    """
    pk:         int
    title:      str
    writer:     int
    created:    datetime
    fix:        datetime
    type:       int
    content:    str
