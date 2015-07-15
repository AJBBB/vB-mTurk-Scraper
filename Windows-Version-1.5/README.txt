# vB-mTurk-Scraper v1.5
Can scrape vBulletin forums for links to mTurk HITS

Written in: <strong>Python 2.*</strong> (Not 3 Compatible OR Tested)
<br>
Information required to run program:
<ul><li>HITS Thread Number (Changes Daily: 5 digit number found in the thread URL) </li>
<li>Forum URL</li>
<li>Page To Start From (Default: 0)</li>
<li>Number Of Pages To Scrape</li>
</ul>

This is a <strong>very very simple</strong> command-line script. Simply run ```vB-mTurk-Scraper.exe``` and it will guide you through setting the forum you want to scrape, entering todays thread number, which page you want to start from, and how many pages you want to go through.

Note: When entering the address to the forum, enter only the domain, ex: <strong>forum.com</strong>

It outputs all HITs to HITs/<strong>mturklinks-todaysdate.html</strong> by default.

The final question asked is about writing to the HITs/<strong>forumlog-todaysdate.txt</strong> file. If you answer with True it will write to HITs/forumlog-todaysdate.txt file with just the links so you can share that plain text with people.

This is perfect for when you wake up! Run it on the hits thread of any <strong>vBulletin</strong> mTurk forum you like, and you get an html file full of all the hits you missed. (Note: It will include duplicates if people post and then quote the hits)

This has only been tested on Mturkforum.com and Turkernation.com - Any vBulletin forum that allows you to read posts without being logged in should work.

Note To Windows Users: Click "Download ZIP" on the right side of the page. Extract the Windows-Version-1.5 folder and run ```vB-mTurk-Scraper.exe```

MIT Licensed
