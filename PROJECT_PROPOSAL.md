# Project Proposal: Landmark Search Database

## Introduction

This project is a database for finding landmarks. A landmark is identified as an object or feature that is easily recognizable and helps people determine their location. The database focuses on buildings, bridges, and mountains.

Users can search for landmarks in a specific country or continent. The database returns a ranked list of results based on the user's query. Each returned result includes a picture, description, and location of the landmark. The project also supports latitude and longitude data so the landmark can be shown on a map.

Users should be able to narrow their search by landmark type, including bridges, mountains, or buildings. The search system is designed to use BM25-style ranking through a search index.

## Database Summary

Each landmark tuple stores the following attributes:

| Attribute | Type | Description |
|---|---|---|
| ID | Integer | Unique identifier for each landmark |
| Name | String | Name of the landmark |
| Location | String | Latitude and longitude or general location |
| Description | String | Landmark description |
| Image | String | Image link |
| Type | String | Landmark category |

## Indexing

The database searches through landmark names, descriptions, and locations. Images are not included in the search index because they are links rather than searchable text.

The user sees the original landmark descriptions. Any cleaned or processed text used for indexing should remain separate from the original descriptions so results remain readable.

## Features

### Images

Each tuple has an image associated with it. The image appears in the returned result when a user searches. If no image is available, a default image can be used.

### Locations

Each tuple has a location attribute that includes longitude and latitude when available. Returned results can be displayed with markers on a map.
