import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-time-temperature-slot',
  templateUrl: './time-temperature-slot.component.html',
  styleUrls: ['./time-temperature-slot.component.css']
})
export class TimeTemperatureSlotComponent implements OnInit {
  @Input() weather: any;

  constructor() {
  }

  ngOnInit(): void {
  }

}
