import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PlaylistConverterComponent } from './playlist-converter/playlist-converter.component';


@NgModule({
  declarations: [
    AppComponent,
    PlaylistConverterComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,  
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
