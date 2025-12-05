class NewsAgency {
    constructor() { this.subscribers = []; }
    subscribe(observer) { this.subscribers.push(observer); }
    unsubscribe(observer) {
        const index = this.subscribers.indexOf(observer);
        if (index > -1) this.subscribers.splice(index, 1);
    }
    publish(news) {
        console.log(`News: ${news}`);
        this.subscribers.forEach(sub => sub.update(news));
    }
}

class Subscriber {
    constructor(name) { this.name = name; }
    update(news) { console.log(`${this.name} received: ${news}`); }
}

const agency = new NewsAgency();
const user1 = new Subscriber("Alex");
const user2 = new Subscriber("Maria");

agency.subscribe(user1);
agency.subscribe(user2);
agency.publish("New update!");
agency.unsubscribe(user1);
agency.publish("Another news");
