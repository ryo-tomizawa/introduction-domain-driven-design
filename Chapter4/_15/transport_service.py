from baggage import Baggage
from physical_distribution_base import PhysicalDistributionBase

class TransportService:
    # fromは予約後のため、別の変数名(from_base)に変更
    def transport(self, from_base: PhysicalDistributionBase, to: PhysicalDistributionBase, baggage: Baggage):
        shipped_baggage = from_base.ship(baggage)
        to.recieve(shipped_baggage)


if __name__ == '__main__':
    from baggage_id import BaggageId
    baggage = Baggage(BaggageId('id'))
    from_base = PhysicalDistributionBase()
    to_base = PhysicalDistributionBase()
    transport_service = TransportService()

    transport_service.transport(from_base, to_base, baggage)