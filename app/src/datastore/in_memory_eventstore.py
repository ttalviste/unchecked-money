from app.src.core.messages.events import DomainEvent
from app.src.datastore.datastore import EventStore


class InMemoryEventStore(EventStore):
    def __init__(self):
        self.events: list = []

    def publish(self, obj: DomainEvent) -> None:
        assert isinstance(obj, (DomainEvent,))
        self.events.append(obj)

    def state(self) -> int:
        return len(self.events)
