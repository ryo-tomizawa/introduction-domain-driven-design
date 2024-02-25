from baggage import Baggage

class PhysicalDistributionBase:
    def ship(self, baggage: Baggage):
        return baggage
    
    def recieve(self, baggage: Baggage):
        pass


if __name__ == '__main__':
    from baggage_id import BaggageId
    baggage = Baggage(BaggageId('id'))
    physical_distribution_base = PhysicalDistributionBase()

    ship_baggage = physical_distribution_base.ship(baggage)
    print(ship_baggage._id._id)