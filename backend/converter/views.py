from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import convert_spotify_to_youtube

@api_view(['POST'])
def convert_playlist(request):
    """Receives a Spotify URL and returns a YouTube Music playlist link"""
    spotify_url = request.data.get('spotify_url')

    if not spotify_url:
        return Response({'error': 'No URL provided'}, status=400)

    youtube_links = convert_spotify_to_youtube(spotify_url)
    return Response(youtube_links)  # ✅ Sends back playlist URL

