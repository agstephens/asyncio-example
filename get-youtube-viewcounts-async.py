#!/usr/bin/env python

# Standard imports
import time
import sys
import requests

# Imports for Async version
import aiohttp
import asyncio

# Get a valid google/youtube API key
from key import key


start_time = time.time()

channel_id = 'UCYjSH2ET9nLMhDcXa5y2OMg' # CEDA channel

# Get the URL for the "uploads" playlist
url = (f'https://www.googleapis.com/youtube/v3/channels?id={channel_id}'
      f'&key={key}&part=contentDetails')
r = requests.get(url)
results = r.json()['items']
playlist_id = results[0]['contentDetails']['relatedPlaylists']['uploads']

# Get the playlist 
url = (f'https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist_id}'
       f'&key={key}&part=contentDetails')

video_ids = []

while True:
    r = requests.get(url)
    results = r.json()

    if 'nextPageToken' in results:
        nextPageToken = results['nextPageToken']
    else:
        nextPageToken = None

    if 'items' in results:
        for item in results['items']:
            videoId = item['contentDetails']['videoId']
            video_ids.append(videoId)

    if nextPageToken:
        url = (f'https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist_id}'
               f'&key={key}&part=contentDetails&pageToken={nextPageToken}')
    else:
        break
        
view_counts = []


async def main_async():
    # Get view counts for all videos
    start_time = time.time()

    print('Starting to search through videos...')
    async with aiohttp.ClientSession() as session:
        tasks = []
        for video_id in video_ids:
            task = asyncio.ensure_future(get_video_data_async(session, video_id))
            tasks.append(task)

        view_counts = await asyncio.gather(*tasks)

    print('Number of videos:', len(view_counts))
    print('Average number of views:', sum(view_counts) / len(view_counts))
    print(f'--- {(time.time() - start_time)} seconds ---')

        
async def get_video_data_async(session, video_id):
    url = (f'https://www.googleapis.com/youtube/v3/videos?id={video_id}'
           f'&key={key}&part=statistics')

    async with session.get(url) as response:
        result_data = await response.json()
        return get_view_count(result_data)


def get_view_count(result_data):
    results = result_data['items']
    viewCount = results[0]['statistics']['viewCount']
    return int(viewCount)


if __name__ == "__main__":
    asyncio.run(main_async())

