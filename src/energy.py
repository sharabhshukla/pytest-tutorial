class Microgrid:
    def __init__(self, production_capacity, storage_capacity):
        self.production_capacity = production_capacity  # Maximum energy production capacity
        self.storage_capacity = storage_capacity  # Maximum energy storage capacity
        self.current_storage = 0  # Current energy stored
        self.consumption = 0  # Current energy consumption

    def produce_energy(self, amount):
        """Simulate energy production."""
        if amount > self.production_capacity:
            amount = self.production_capacity
        self.current_storage += amount
        if self.current_storage > self.storage_capacity:
            self.current_storage = self.storage_capacity

    def consume_energy(self, amount):
        """Simulate energy consumption."""
        if amount > self.current_storage:
            amount = self.current_storage
        self.current_storage -= amount
        self.consumption += amount

    def get_status(self):
        """Return the current status of the microgrid."""
        return {
            'production_capacity': self.production_capacity,
            'storage_capacity': self.storage_capacity,
            'current_storage': self.current_storage,
            'consumption': self.consumption
        }

    def simulate(self, production_schedule, consumption_schedule):
        """Simulate the microgrid operation over a period.

        Args:
            production_schedule (list): List of energy production amounts.
            consumption_schedule (list): List of energy consumption amounts.
        """
        for production, consumption in zip(production_schedule, consumption_schedule):
            self.produce_energy(production)
            self.consume_energy(consumption)

# Example usage
microgrid = Microgrid(production_capacity=100, storage_capacity=500)
production_schedule = [80, 90, 100, 70, 60]
consumption_schedule = [50, 60, 70, 80, 90]
microgrid.simulate(production_schedule, consumption_schedule)
status = microgrid.get_status()
print(status)