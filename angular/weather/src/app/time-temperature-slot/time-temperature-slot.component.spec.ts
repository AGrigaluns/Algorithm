import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TimeTemperatureSlotComponent } from './time-temperature-slot.component';

describe('TimeTemperatureSlotComponent', () => {
  let component: TimeTemperatureSlotComponent;
  let fixture: ComponentFixture<TimeTemperatureSlotComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TimeTemperatureSlotComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TimeTemperatureSlotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
