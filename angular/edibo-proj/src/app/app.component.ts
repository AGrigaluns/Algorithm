import {Component, OnInit} from '@angular/core';
import {IInterval, Iinterval} from "./model/iinterval";
import {map, startWith} from "rxjs/operators";
import {interval, Observable} from "rxjs";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'edibo-proj';

  getIntervalTime(dateA: number, dateB: number): IInterval{
    let intervalTime: number = Math.floor((dateA - dateB) / 1000);
    return this.getTime(intervalTime);
  }

  private getTime(time : number) : IInterval{
    let interval: IInterval =
      {days : 0, hours : 0, minutes : 0, seconds: 0};
    interval.days = Math.floor(time / 86400);
    time -= interval.days * 86400;
    interval.hours = Math.floor(time / 3600) % 24;
    time -= interval.hours * 3600;
    interval.minutes = Math.floor(time / 60) % 60;
    time -= interval.minutes * 60;
    interval.seconds = time % 60;
    return interval;
  }

  getCountDown(timeToGo: number): Observable<IInterval> {
    return interval(1000).pipe(startWith(0), map(
      x =>  this.getIntervalTime(timeToGo, Date.now())
    ))
  }
}


