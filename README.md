# vB-mTurk-Scraper
Can scrape vBulletin forums for links to mTurk HITS 

Requires BeautifulSoup and requests

This is a very simple command-line script that guides you through setting the forum, todays thread number, which page you want to start from(counter), and which you want to end on. It outputs to the html file mturklinks and always overwrites it self.

There is also a question about End Of Day, if you type in True it will write to the forumlog.txt file with just the links so you can share that with people.

This program is perfect for when you wake up, run it on the forum you like, and have an html file full of all the hits you missed today. (Note: It will include duplicates if people post and then quote the hits)
