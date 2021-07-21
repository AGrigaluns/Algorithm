import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { TimeTemperatureSlotComponent } from './time-temperature-slot/time-temperature-slot.component';

@NgModule({
  declarations: [
    AppComponent,
    TimeTemperatureSlotComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
