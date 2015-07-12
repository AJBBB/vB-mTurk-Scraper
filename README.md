# vB-mTurk-Scraper
Can scrape vBulletin forums for links to mTurk HITS

Uses Python 2.* (Not 3 Compatible/Tested) Requires BeautifulSoup and requests

This is a very very simple command-line script that guides you through setting the forum, todays thread number, which page you want to start from(counter), and which you want to end on. It outputs to the html file mturklinks and always overwrites it self.

It will also ask a question about End Of Day. If you answer with True it will write to the forumlog.txt file with just the links so you can share that with people, otherwise type in False. (Note: You currently must manually delete everything in the forumlog.txt as the program just appends the data to the file.)

This is perfect for when you wake up! Run it on the hits thread of any vBulletin mTurk forum you like, and you get an html file full of all the hits you missed. (Note: It will include duplicates if people post and then quote the hits)

This has only been tested on Mturkforum.com and Turkernation.com - I would assume any vBulletin forum that allows you to read posts without being logged in would work

MIT Licensed
