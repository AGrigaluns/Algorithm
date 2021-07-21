import { AfterViewInit, Component, OnInit } from '@angular/core';
import { Meteo } from './meteo';

interface INowWeather {
  longitude: number;
  temperature: number;
  latitude: number;
  wind: number;
  windDirection: number;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit, AfterViewInit {

  vissWeath: any[] = [];

  weatherNow: INowWeather = {
    longitude: 0,
    latitude: 0,
    temperature: 0,
    wind: 0,
    windDirection: 0,
  };

  constructor() {
    navigator.geolocation
      .getCurrentPosition((x) => {
        this.weatherNow.latitude = x.coords.latitude;
        this.weatherNow.longitude = x.coords.longitude;
        this.findMeoteoData(this.weatherNow.longitude, this.weatherNow.latitude);
      });
  }

  ngOnInit(): boolean {
    return true;
  }

  ngAfterViewInit(): void {
  }

  openWeather(weather: any) {
    alert(weather.data.instant.details.air_temperature);
  }

  private async findMeoteoData(longitude: number, latitude: number): Promise<void> {
    const dataStream = await fetch(`https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=${latitude}&lon=${longitude}`);
    const data: Meteo = await dataStream.json();
    const today = data.properties.timeseries[0].data.instant.details;
    this.vissWeath = data.properties.timeseries;
    this.weatherNow.temperature = today.air_temperature;
    this.weatherNow.wind = today.wind_speed;
    this.weatherNow.windDirection = today.wind_from_direction;
  }
}
