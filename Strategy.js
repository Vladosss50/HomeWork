class CourierDelivery {
    calculate(price) { return price + 5; }
}

class PostDelivery {
    calculate(price) { return price + (price * 0.1); }
}

class DroneDelivery {
    calculate(price) { return price + 15; }
}

class DeliveryContext {
    constructor(strategy = null) { this.strategy = strategy; }
    setStrategy(strategy) { this.strategy = strategy; }
    calculate(price) {
        if (!this.strategy) throw new Error("No strategy");
        return this.strategy.calculate(price);
    }
}

const delivery = new DeliveryContext();
delivery.setStrategy(new CourierDelivery());
console.log(delivery.calculate(100));
