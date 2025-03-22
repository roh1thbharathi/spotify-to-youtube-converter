import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-playlist-converter',
  templateUrl: './playlist-converter.component.html',
  styleUrls: ['./playlist-converter.component.css']
})
export class PlaylistConverterComponent {
  spotifyUrl = '';
  youtubeUrl: string | null = null;
  loading = false;
  error = '';
  copied = false;

  constructor(private http: HttpClient) {}

  convertPlaylist() {
    if (!this.spotifyUrl) return;

    this.loading = true;
    this.error = '';
    this.youtubeUrl = null;
    this.copied = false;

    this.http.post<any>('http://127.0.0.1:8000/api/convert/', {
      spotify_url: this.spotifyUrl
    }).subscribe({
      next: (res) => {
        this.youtubeUrl = res.playlist_url;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Something went wrong! 😢';
        this.loading = false;
        console.error(err);
      }
    });
  }

  copyLink() {
    if (!this.youtubeUrl) return;
    navigator.clipboard.writeText(this.youtubeUrl).then(() => {
      this.copied = true;
      setTimeout(() => (this.copied = false), 2000);
    });
  }
}
