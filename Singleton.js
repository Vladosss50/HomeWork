class Logger {
    constructor() {
        if (Logger.instance) return Logger.instance;
        this.logs = [];
        Logger.instance = this;
    }
    
    log(message) {
        const timestamp = new Date().toISOString();
        this.logs.push({ message, timestamp });
        console.log(`[${timestamp}] ${message}`);
    }
    
    printLogs() {
        console.log("=== Logs ===");
        this.logs.forEach(log => console.log(`[${log.timestamp}] ${log.message}`));
    }
}

const logger1 = new Logger();
const logger2 = new Logger();
logger1.log("Test 1");
logger2.log("Test 2");
console.log(logger1 === logger2);
logger1.printLogs();
