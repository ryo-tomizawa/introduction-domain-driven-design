from baggage import Baggage

class PhysicalDistributionBase:
    def ship(self, baggage: Baggage):
        return baggage
    
    def recieve(self, baggage: Baggage):
        print(baggage._id._id)

    # self = PhysicalDistributionBase()
    def transport(self, baggage: Baggage):
        shipped_baggage = self.ship(baggage)
        self.recieve(shipped_baggage)


if __name__ == '__main__':
    from baggage_id import BaggageId
    baggage = Baggage(BaggageId('id'))
    physical_distribution_base = PhysicalDistributionBase()

    physical_distribution_base.transport(baggage)