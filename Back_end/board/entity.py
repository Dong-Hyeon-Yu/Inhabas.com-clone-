from dataclasses import dataclass
from datetime import datetime


@dataclass
class BoardEntity(object):
    pk:         int
    title:      str
    writer:     int
    created:    datetime
    fix:        datetime
    type:       int
    content:    str
