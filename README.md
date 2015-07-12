# vB-mTurk-Scraper
Can scrape vBulletin forums for links to mTurk HITS

Uses Python 2.* (Not 3 Compatible/Tested) Requires BeautifulSoup and requests

This is a very very simple command-line script that guides you through setting the forum you want to scrap, entering todays thread number, which page you want to start from, and how many pages you want to go through. It outputs to the html file mturklinks.html and always overwrites it self. (No need to worry about clearing the files)

The final question asked is about writing to the forumlog.txt. If you answer with True it will write to the forumlog.txt file with just the links so you can share that plain text with people. Otherwise type in False. This always overwrites it self. (No need to worry about clearing the files)

This is perfect for when you wake up! Run it on the hits thread of any vBulletin mTurk forum you like, and you get an html file full of all the hits you missed. (Note: It will include duplicates if people post and then quote the hits)

This has only been tested on Mturkforum.com and Turkernation.com - I would assume any vBulletin forum that allows you to read posts without being logged in would work

MIT Licensed
