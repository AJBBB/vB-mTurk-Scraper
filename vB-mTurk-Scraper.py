#! /usr/bin/env python

from bs4 import BeautifulSoup
import requests


def forum_sel():
    # Defines the forum to scrape from
    forum = str(raw_input("Enter forum url(ex: turkturk.com): "))
    return forum


def get_thread():
    # Defines the thread number of todays HIT thread
    todays_thread = int(raw_input("Enter todays thread number: "))
    return todays_thread


def create_url():
    selected_forum = forum_sel()
    todays_thread = get_thread()
    # Builds the URL of the forum to scrape from
    forum_url = "%s/printthread.php?t=%s&pp=40&page=" % (selected_forum,
    todays_thread)
    return forum_url


def get_start():
    # Defines a counter from which page to start
    page_number = int(raw_input("Enter page to start on: (Default: 0): "))
    return page_number


def get_end():
    # Defines the amount of pages to run through
    last_page = int(raw_input("Enter # pages to scrape hits from: "))
    return last_page


def get_eod():
    # Defines if the user wants to write to forumlog.txt
    e_o_d = bool(raw_input("Write to forumlog.txt? (True/False): "))
    return e_o_d


def write_file(file_name, write_mode, file_text):
    # Function to write to files easily
    text_file = open(file_name, write_mode)
    text_file.write(file_text)
    text_file.close()


def clear_update_htm(silent):
    # Open the log, write over it with just css data
    write_file("mturklinks.html", "w",
        "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"> \n")
    if silent is False:  # Check if we are running in silent or not
        print "Cleared & Wrote css line to the file"


def clear_update_txt(silent):
    # Open the log, clear the file.
    write_file("forumlog.txt", "w", "")
    if silent is False:  # Check if we are running in silent or not
        print "Cleared forumlog.txt"


def run_through(silent):
    # Get the forum URL
    forum_url = create_url()
    # Get the page to start from
    page_number = get_start()
    # Get how many pages to run through
    last_page = get_end()
    # Get if the user wants to write to forumlog.txt
    end_of_day = get_eod()

    for pages in range(0, last_page):
        # Increment page to check
        page_number = page_number + 1
        # Build the URL with page_number to scrape from
        hit_links = requests.get("http://" + str(forum_url) + str(page_number))
        data = hit_links.text
        soup = BeautifulSoup(data)

        for link in soup.find_all('a'):  # Finds all links on the page
            if link.get('href').startswith('https://www.mturk.com/mturk/preview?groupId='):
                # Write to the mturklinks.html file with all links
                write_file("mturklinks.html", "a+",
                    "<a class=\"button\" href=\"" + link.get('href') +
                    "\"> Link </a><br><br>\n")
                if silent is False:  # Check if we are running in silent or not
                    print "Wrote " + link.get('href') + " to the file."
                if end_of_day is True:  # Check if user will write to forumlog
                    write_file("forumlog.txt", "a+", link.get('href') + "\n")

def finish():
    print "Successfully scraped the forum."


if __name__ == "__main__":
    clear_update_htm(True)  # Set to false to print output to console
    clear_update_txt(True)  # Set to false to print output to console
    run_through(True)  # Set to false to print output to console
    finish()  # Prints out a finished message
