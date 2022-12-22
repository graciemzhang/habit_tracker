Script to keep track of how long you've been doing a sequence of habits

# Tools used
- richtext
- sqlite3

# CURRENT
## features:
- resets if any one of the habits are not completed
- keeps track of day streak
- notifies user to fill out form -> must have cron enabled, only set up for mac right now

## set up:
- asks what habits you want to keep track of
- asks if you want to be notified

## database:
sqlite
- habits
- number of restarts
- day started

## features to consider in the future:
- allowing inserting + deleting of habits
- setting up a streak that you want to reach

# PROBLEMS / AREAS TO ADD ON/IMPROVE
- Will add days onto your streak if you never filled out that days form
- Must manually go in and delete database if you set something up incorrectly