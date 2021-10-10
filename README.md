# repetition-bot

This bot tweets out the same Kierkegaard quotation every day. At least, if you set up a cronjob to make it run every day.

Since Twitter does not like the posting of duplicate statuses, it inserts permutations of blank unicode symbols into the main tweet.

The true significance of this bot lies in the generation and insertion of these invisible strings.

## Dependencies
```
pip install tweepy
```

## Unscientific Postscript

The version of this bot running at [@Constant_in_ius](https://twitter.com/Constant_in_ius) no longer uses tweepy. Twitter repeatedly blocked its API key, would unblock it at my request, then block it again – until they stopped responding and left it mute.

I enjoyed the irony of this dynamic, though am disappointed it did not conclude in my (bot's) favour.

The current bot controls an automated instance of Chrome via Selenium, avoiding the API altogether. I hope this will prove somewhat more resilient to attempts to shut it down, if only because it may emulate humanity more passably.

The new bot is here: https://github.com/lexipenia/repetition-bot-2