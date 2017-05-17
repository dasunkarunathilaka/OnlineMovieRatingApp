
from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyD9xx68BT-hCPhKYQcQ2OGKk1oHxLk_Euo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtubeSearch(movieName):

    trailer_name = movieName + " official trailer"

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q = trailer_name,
        part = "id,snippet",
        maxResults = 1
        ).execute()
      
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videoIdentifier = search_result["id"]["videoId"]
        
    videoURL = "https://www.youtube.com/embed/" + videoIdentifier
    # To embed the video into the html, url should be given as above. Not with 'watch/'.

    return videoURL
