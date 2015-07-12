# vB-mTurk-Scraper
Can scrape vBulletin forums for links to mTurk HITS

Written in: <strong>Python 2.*</strong> (Not 3 Compatible OR Tested)
<br>
<strong>Requires:</strong> BeautifulSoup and requests

To install BeautifulSoup run:
sudo pip install beautifulsoup4
<strong>OR:</strong> sudo easy_install beautifulsoup4

To install requests run:
sudo pip install requests
<strong>OR:</strong> sudo easy_install requests

Information required to run program:
<ul><li>HITS Thread Number (Changes Daily: 5 digit number found in the thread URL) </li>
<li>Forum URL</li>
<li>Page To Start From</li>
<li>Number Of Pages To Scrape</li>
</ul>

This is a <strong>very very simple</strong> command-line script. Simply run "python vB-mTurk-Scraper.py" and it will guide you through setting the forum you want to scrape, entering todays thread number, which page you want to start from, and how many pages you want to go through.

Note: When entering the address to the forum, enter only the domain, ex: <strong>forum.com</strong>

It outputs all HITS to the html file <strong>mturklinks.html</strong> and always overwrites it self. (No need to worry about clearing the files)

The final question asked is about writing to the <strong>forumlog.txt</strong>. If you answer with True it will write to the forumlog.txt file with just the links so you can share that plain text with people. Otherwise type in False. This always overwrites it self. (No need to worry about clearing the files)

This is perfect for when you wake up! Run it on the hits thread of any <strong>vBulletin</strong> mTurk forum you like, and you get an html file full of all the hits you missed. (Note: It will include duplicates if people post and then quote the hits)

This has only been tested on Mturkforum.com and Turkernation.com - Any vBulletin forum that allows you to read posts without being logged in should work.

MIT Licensed
