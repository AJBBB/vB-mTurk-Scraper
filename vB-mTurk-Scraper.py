#! /usr/bin/env python

from bs4 import BeautifulSoup
import requests


def forum_sel():
    forum = str(raw_input("Enter forum url(ex turkturk.com):"))
    return forum


def get_thread():
    todays_thread = int(raw_input("Enter todays thread number: "))
    return todays_thread

def create_url():
    selected_forum = forum_sel()
    todays_thread = get_thread()
    forum_url = "%s/printthread.php?t=%s&pp=40&page=" % (selected_forum,
    todays_thread)
    return forum_url


def get_start():
    # Defines a counter from which page to start
    page_number = int(raw_input("Enter page to start on:(Default: 0) "))
    return page_number


def get_end():
    # Defines the amount of pages to run through
    last_page = int(raw_input("Enter # pages to run through / last page: "))
    return last_page


def get_eod():
    # Should we print to a pastebin style log? Is it end of the day?
    e_o_d = raw_input("End of day (True/False) :")
    return e_o_d


def write_file(file_name, write_mode, file_text):
    text_file = open(file_name, write_mode)
    text_file.write(file_text)
    text_file.close()


def clear_update_htm(silent):
    # Open the log, write over it with just css data
    write_file("mturklinks.html", "w",
        "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"> ")
    if silent is False:  # Check if we are running in silent or not
        print "Cleared & Wrote css line to the file"


def run_through(silent):
    forum_url = create_url()
    page_number = get_start()
    last_page = get_end()
    e_o_d = get_eod()

    for pages in range(0, last_page):
        page_number = page_number + 1  # increment page to check
        hit_links = requests.get("http://" + str(forum_url) + str(page_number))
        data = hit_links.text
        soup = BeautifulSoup(data)

        for link in soup.find_all('a'):  # finds all links on the page
            if link.get('href').startswith('https://www.mturk.com/mturk/preview?groupId='):
                # Write to a log/webpage
                write_file("mturklinks.html", "a+",
                    "<a class=\"button\" href=\"" + link.get('href') +
                    "\"> Link </a><br><br>\n")
                if silent is False:  # Check if we are running in silent or not
                    print "Wrote " + link.get('href') + " to the file."
                if e_o_d is True:
                    write_file("forumlog.txt", "a+", link.get('href') + "\n")


if __name__ == "__main__":
    clear_update_htm(True)  # Set to false to print output to console
    run_through(True)  # Set to false to print output to console
