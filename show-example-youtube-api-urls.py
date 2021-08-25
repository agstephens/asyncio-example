#!/usr/bin/env python

# Standard imports
import requests

from key import key

channel_id = "UCYjSH2ET9nLMhDcXa5y2OMg" # CEDA channel

example_urls = {
    "List content of CEDA Youtube channel": f"https://www.googleapis.com/youtube/v3/channels?id={channel_id}&key={key}&part=contentDetails",
    "List content of specific Youtube playlist": f"https://www.googleapis.com/youtube/v3/playlistItems?playlistId=UUYjSH2ET9nLMhDcXa5y2OMg&part=contentDetails&key={key}",
    "List statistics for a specific video": f"https://www.googleapis.com/youtube/v3/videos?id=N0LK8yFcKQ0&key={key}&part=statistics"
}

print()
for endpoint, url in example_urls.items():
    print(endpoint, ":\n", url, "\n")

