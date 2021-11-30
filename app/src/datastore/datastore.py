from typing import Protocol, Any

from app.src.core.messages.events import DomainEvent


class EventStore(Protocol):
    def publish(self, obj: DomainEvent):
        ...

    def state(self):
        ...
