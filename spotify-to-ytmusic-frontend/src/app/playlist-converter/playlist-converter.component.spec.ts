import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlaylistConverterComponent } from './playlist-converter.component';

describe('PlaylistConverterComponent', () => {
  let component: PlaylistConverterComponent;
  let fixture: ComponentFixture<PlaylistConverterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlaylistConverterComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlaylistConverterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
