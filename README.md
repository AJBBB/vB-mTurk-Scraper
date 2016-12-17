# vB-mTurk-Scraper v1.5

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f0321790f66f4f5193ad2371d8c478a1)](https://www.codacy.com/app/ajbbb/vB-mTurk-Scraper-1-5?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AYJAYY/vB-mTurk-Scraper-1.5&amp;utm_campaign=badger)

Scrapes vBulletin forums for links to mTurk HITs

<strong>v1.5</strong> introduced an improved Windows version and there will no longer be duplicates in the logs.

Written in: <strong>Python 2.*</strong> (Not 3 Compatible OR Tested)
<br>
<strong>Linux Requirements:</strong> <a href="http://www.crummy.com/software/BeautifulSoup/">BeautifulSoup</a> and <a href="http://docs.python-requests.org/en/latest/">requests</a>

To install BeautifulSoup run:
```pip install beautifulsoup4```
<strong>OR:</strong> ```easy_install beautifulsoup4```

To install requests run:
```pip install requests```
<strong>OR:</strong> ```easy_install requests```

Information required to run program:
<ul><li>HITs Thread Number (Changes Daily: 5 digit number found in the thread URL) </li>
<li>Forum URL</li>
<li>Page To Start From (Default: 0)</li>
<li>Number Of Pages To Scrape</li>
</ul>

This is a <strong>very very simple</strong> command-line script. Simply run ```python vB-mTurk-Scraper.py``` and it will guide you through setting the forum you want to scrape, entering todays thread number, which page you want to start from, and how many pages you want to go through.

Note: When entering the address to the forum, enter only the domain, ex: <strong>forum.com</strong>

It outputs all HITs to HITs/<strong>mturklinks-todaysdate.html</strong> by default.
 
The final question asked is about writing to the HITs/<strong>forumlog-todaysdate.txt</strong> file. If you answer with True it will write to HITs/forumlog-todaysdate.txt file with just the links so you can share that plain text with people.

This is perfect for when you wake up! Run it on the HITs thread of any <strong>vBulletin</strong> mTurk forum you like, and you get an html file full of all the HITs you missed. (Note: There will be NO duplicates as of <strong>v1.5</strong>)

This has only been tested on Mturkforum.com and Turkernation.com - Any vBulletin forum that allows you to read posts without being logged in should work.

<strong>NOTE:</strong> When setting the number of pages to use, please make sure you are displaying 40 posts per page when checking the site.

<strong>Windows Users:</strong> Click "Download ZIP" on the right side of the page. Extract the Windows-Version-1.5 folder and run ```vB-mTurk-Scraper.exe```

<h2>Screenshots:</h2><br>
<strong>Program Running In Windows:</strong><br>
<img src="http://i.gyazo.com/fd8e97ebeeb3ac1e7e1257e312ef0596.png">
<br>
<strong>Program Running In Xubuntu:</strong></br>
<img src="http://i.imgur.com/LTQJIZF.png">
<br>
<strong>HTML File(Note that visited HITs are red):</strong><br>
<img src="http://i.gyazo.com/bb116d8b2b83d60a25281c444c1a250d.png">


MIT Licensed
