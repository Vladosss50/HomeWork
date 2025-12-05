class OldWeatherService {
    getFahrenheit() { return Math.floor(Math.random() * 50) + 32; }
}

class WeatherAdapter {
    constructor(oldService) { this.oldService = oldService; }
    getCelsius() {
        const f = this.oldService.getFahrenheit();
        return Math.round((f - 32) * 5 / 9);
    }
}

const oldService = new OldWeatherService();
const adapter = new WeatherAdapter(oldService);
console.log(`F: ${oldService.getFahrenheit()}, C: ${adapter.getCelsius()}`);
