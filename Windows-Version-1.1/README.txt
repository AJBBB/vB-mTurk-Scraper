Simply run vB-mTurk-Scraper.exe and follow the instructions below.


GitHub README.md:

vB-mTurk-Scraper
Can scrape vBulletin forums for links to mTurk HITS

Information required to run program:

HITS Thread Number (Changes Daily: 5 digit number found in the thread URL)
Forum URL
Page To Start From
Number Of Pages To Scrape

This is a very very simple command-line script. It will guide you through setting the forum you want to scrape, entering todays thread number, which page you want to start from, and how many pages you want to go through.

Note: When entering the address to the forum, enter only the domain, ex: forum.com

It outputs all HITS to the html file mturklinks.html and always overwrites it self. (No need to worry about clearing the files)

The final question asked is about writing to the forumlog.txt. If you answer with True it will write to the forumlog.txt file with just the links so you can share that plain text with people. Otherwise type in False. This always overwrites it self. (No need to worry about clearing the files)

This is perfect for when you wake up! Run it on the hits thread of any vBulletin mTurk forum you like, and you get an html file full of all the hits you missed. (Note: It will include duplicates if people post and then quote the hits)

This has only been tested on Mturkforum.com and Turkernation.com - Any vBulletin forum that allows you to read posts without being logged in should work.

Note To Windows Users: Windows versions will be updated less frequently than the vB-mTurk-Scraper.py file.

MIT Licensed
