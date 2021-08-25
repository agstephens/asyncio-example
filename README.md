# asyncio-example

This repository shows an example of using Async IO in Python.
It demonstrates use of the `asyncio` and `aiohttp` libraries.

NOTE: this code was copied from this excellent tutorial video:

- Title:  "How to Speed Up API Requests With Async Python"
- Author: "Pretty Printed"
- URL:    https://www.youtube.com/watch?v=ln99aRAcRt0&list=RDCMUC-QDfvrRIDB6F0bIO4I4HkQ&index=1

## Requirements and installation

Create a virtual environment (or conda environment) and install the 
requirements:

```
pip install -r requirements.txt
```

## Overview

Imagine you want to calculate the average number of views for all the videos
in a given YouTube channel.

In this case we want to look at the CEDA YouTube channel:

 https://www.youtube.com/channel/UCYjSH2ET9nLMhDcXa5y2OMg/videos

We can use the YouTube API, which requires use of an API Token.

There are 3 steps in the workflow:

1. Get the ID of the "Uploads" part of the CEDA channel [x1]
2. Get a list of IDs for each video on the CEDA channel [x1]
3. For each video ID, get the number of view counts [xMANY] 

## Step 1: Get an API key

This page explains how to generate a YouTube API key:

 https://blog.hubspot.com/website/how-to-get-youtube-api-key

Once you have a key, create a module called `key.py` in this directory,
with the contents:

```
key = "<your_api_key>"
```

## Step 2: See some example URLs (using your key)

To understand the different API calls that can be made, you can now run:

```
python show-example-youtube-api-urls.py
```

It will insert your API key into three example URLs to that you could paste
into your browser to see the responses from.

## Step 3: Run the "sync" (i.e. blocking) version of the code

The traditional version of the code uses the `requests` library to talk to
the YouTube API.

Each call to the API waits for a response, so each call is _blocking_ in that 
respect.

E.g.:

```
Starting to search through videos...
Number of videos: 74
Average number of views: 89.66216216216216
--- 10.906799793243408 seconds ---
``` 

You can see that it takes more than 10 seconds.

## Step 4: Run the "async" (non-blocking) version of the code

This employs the `asyncio` library and the `aiohttp` to create an asynchronous
client session that manages HTTP requests whilst allowing other asynchronous
tasks to be run. In this case, it can run many of them concurrently, which 
speeds up the process significantly...

```
$ python get-youtube-viewcounts-async.py
Starting to search through videos...
Number of videos: 74
Average number of views: 89.66216216216216
--- 0.5810856819152832 seconds ---
```

## Step 5: Delve in...

Look into the async script (`get-youtube-viewcounts-async.py`) and learn about
how the `async` and `await` keywords are used to define tasks that can run
concurrently. And tell your friends about it :-)


