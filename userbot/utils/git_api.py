# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""
used to get github api information
for github module
"""

import json
import urllib.request as url

VERSION = "1.0.2"
APIURL = "http://api.github.com/repos/"


def vercheck() -> str:
    return str(VERSION)


# Repo-wise stuff

def getData(repoURL):
    try:
        with url.urlopen(APIURL + repoURL + "/releases") as data_raw:
            repoData = json.loads(data_raw.read().decode())
            return repoData
    except BaseException:
        return None


def getReleaseData(repoData, index):
    if index < len(repoData):
        return repoData[index]
    else:
        return None


# Release-wise stuff

def getAuthor(releaseData):
    if releaseData is None:
        return None
    return releaseData['author']['login']


def getAuthorUrl(releaseData):
    if releaseData is None:
        return None
    return releaseData['author']['html_url']


def getReleaseName(releaseData):
    if releaseData is None:
        return None
    return releaseData['name']


def getReleaseDate(releaseData):
    if releaseData is None:
        return None
    return releaseData['published_at']


def getAssetsSize(releaseData):
    if releaseData is None:
        return None
    return len(releaseData['assets'])


def getAssets(releaseData):
    if releaseData is None:
        return None
    return releaseData['assets']


def getBody(releaseData):  # changelog stuff
    if releaseData is None:
        return None
    return releaseData['body']


# Asset-wise stuff

def getReleaseFileName(asset):
    return asset['name']


def getReleaseFileURL(asset):
    return asset['browser_download_url']


def getDownloadCount(asset):
    return asset['download_count']


def getSize(asset):
    return asset['size']
