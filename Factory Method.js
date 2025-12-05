class BankPayment {
    process(amount) { return `Bank payment: ${amount}`; }
}

class CardPayment {
    process(amount) { return `Card payment: ${amount}`; }
}

class CryptoPayment {
    process(amount) { return `Crypto payment: ${amount}`; }
}

class PaymentFactory {
    create(type) {
        switch(type.toLowerCase()) {
            case 'bank': return new BankPayment();
            case 'card': return new CardPayment();
            case 'crypto': return new CryptoPayment();
            default: throw new Error("Unknown type");
        }
    }
}

const factory = new PaymentFactory();
const payment = factory.create('bank');
console.log(payment.process(1000));
