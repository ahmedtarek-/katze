# README

## Intro
The application is divided into these modules:
1. Api that contains the endpoint for cats
2. External api that communicates with the cats service
3. Cache layer that stores the requests for persistence

## Usage
1. Clone
2. Create virtualenv
3. Run release cats script
```
source setup_and_release_cats.sh
```

## API Example
```
http://127.0.0.1:8000/cats/funny
```
will return 
```
[
    {
        "img": "127.0.0.1:8000/media/funny_0.png"
    },
    {
        "img": "127.0.0.1:8000/media/funny_1.png"
    },
    {
        "img": "127.0.0.1:8000/media/funny_2.png"
    },
    {
        "img": "127.0.0.1:8000/media/funny_3.png"
    },
    {
        "img": "127.0.0.1:8000/media/funny_4.png"
    }
]
```

## Versions
* Python: 3.7.0
* Django: 2.1.2

## Cache
* Uses Django DatabaseCache to store tag/paths as key/value pair
* Uses filesystem to store actual images in server to be able to serve it

## Git commits pattern
All commits follows this pattern
```[tag] description```

## Improvements
1. Use documentation package (swagger or redoc)
2. Separate tests for each module (each module should be completely separate service)
