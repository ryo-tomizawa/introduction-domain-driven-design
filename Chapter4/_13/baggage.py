from baggage_id import BaggageId

class Baggage:
    def __init__(self, id: BaggageId) -> None:
        self._id = id

    @property
    def id(self):
        return self._id