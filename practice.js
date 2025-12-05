// 1. Singleton (Корзина)
class ShoppingCart {
    constructor() {
        if (ShoppingCart.instance) return ShoppingCart.instance;
        this.items = [];
        ShoppingCart.instance = this;
    }
    
    addItem(product, qty = 1) {
        const existing = this.items.find(i => i.product.id === product.id);
        existing ? existing.quantity += qty : this.items.push({ product, quantity: qty });
    }
    
    getTotal() {
        return this.items.reduce((sum, item) => sum + (item.product.price * item.quantity), 0);
    }
}

// 2. Factory Method (Товары)
class ProductFactory {
    static create(type, data) {
        switch(type) {
            case 'electronics': return new Product(data.id, data.name, data.price, 'Electronics');
            case 'clothing': return new Product(data.id, data.name, data.price, 'Clothing');
            default: throw new Error("Unknown type");
        }
    }
}

class Product {
    constructor(id, name, price, category) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.category = category;
    }
}

// 3. Strategy (Скидки)
class NoDiscount {
    calculate(amount) { return amount; }
}

class PercentageDiscount {
    constructor(percent) { this.percent = percent; }
    calculate(amount) { return amount * (1 - this.percent / 100); }
}

class DiscountContext {
    constructor(strategy = new NoDiscount()) { this.strategy = strategy; }
    setStrategy(strategy) { this.strategy = strategy; }
    apply(amount) { return this.strategy.calculate(amount); }
}

// 4. Adapter (Платеж)
class LegacyPayment {
    payLegacy(amount, currency) {
        return { success: true, id: 'LEG_' + Date.now(), amount };
    }
}

class PaymentAdapter {
    constructor(legacy) { this.legacy = legacy; }
    process(amount) {
        const result = this.legacy.payLegacy(amount, 'RUB');
        return { isSuccess: result.success, id: result.id, amount: result.amount };
    }
}

// Использование
class OnlineStore {
    constructor() {
        this.cart = new ShoppingCart();
        this.discounts = new DiscountContext();
        this.payment = new PaymentAdapter(new LegacyPayment());
    }
    
    demo() {
        const p1 = ProductFactory.create('electronics', { id: 1, name: 'Phone', price: 30000 });
        const p2 = ProductFactory.create('clothing', { id: 2, name: 'Shirt', price: 1500 });
        
        this.cart.addItem(p1);
        this.cart.addItem(p2, 2);
        
        console.log("Total:", this.cart.getTotal());
        
        this.discounts.setStrategy(new PercentageDiscount(10));
        const discounted = this.discounts.apply(this.cart.getTotal());
        console.log("After discount:", discounted);
        
        const payResult = this.payment.process(discounted);
        console.log("Payment:", payResult);
        
        const cart2 = new ShoppingCart();
        console.log("Same cart?", this.cart === cart2);
    }
}

const store = new OnlineStore();
store.demo();
