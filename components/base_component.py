from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from entity import Entity
    from engine import Engine

class BaseComponent:
    entity: Entity   #Owning entity instance.

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine
