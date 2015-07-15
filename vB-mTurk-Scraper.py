#! /usr/bin/env python

from bs4 import BeautifulSoup
from requests import get
from datetime import date
from os import remove


def forum_sel():
    """Defines the forum to scrape from"""
    forum = str(raw_input("Enter forum url(ex: forum.com): "))
    return forum


def get_thread():
    """Defines the thread number of todays HIT thread"""
    todays_thread = int(raw_input("Enter todays thread number: "))
    return todays_thread


def create_url():
    selected_forum = forum_sel()
    todays_thread = get_thread()
    """Builds the URL of the forum to scrape from"""
    forum_url = "%s/printthread.php?t=%s&pp=40&page=" % (selected_forum,
    todays_thread)
    return forum_url


def get_start():
    """Defines a counter from which page to start"""
    page_number = int(raw_input("Enter page to start on: (Default: 0): "))
    return page_number


def get_end():
    """Defines the amount of pages to run through"""
    last_page = int(raw_input("Enter # pages to scrape hits from: "))
    return last_page


def get_eod():
    """Defines if the user wants to write to forumlog.txt"""
    end_of_day = bool(raw_input("Write to forumlog.txt? (True/False): "))
    return end_of_day


def write_file(file_name, write_mode, file_text):
    """Function to write to files easily"""
    text_file = open(file_name, write_mode)
    text_file.write(file_text)
    text_file.close()


def clear_update_htm(silent):
    todays_date = date.today()
    """Open the log, write over it with just css data"""
    write_file("./HITs/mturklinks-" + str(todays_date) + ".html", "w",
        "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"> \n")
    if silent is False:  # Check if we are running in silent or not
        print "Cleared & Wrote css line to the file"


def clear_update_txt(silent):
    """Open the log, clear the file."""
    todays_date = date.today()
    write_file("./HITs/forumlog-" + str(todays_date) + ".txt", "w", "")
    if silent is False:  # Check if we are running in silent or not
        print "Cleared forumlog.txt"


def run_through(silent):
    forum_url = create_url()  # Get the forum URL
    page_number = get_start()  # Get the page to start from
    last_page = get_end()  # Get how many pages to run through
    end_of_day = get_eod()  # Get if the user wants to write to forumlog.txt

    for pages in range(0, last_page):  # Go through all pages given
        page_number = page_number + 1  # Increment page to check
        # Build the URL with page_number to scrape from
        hit_links = get("http://" + str(forum_url) + str(page_number))
        data = hit_links.text
        soup = BeautifulSoup(data)
        todays_date = date.today()
        progress_bar = "Scraping From Page: [" + str(page_number) + "]"

        for link in soup.find_all('a'):  # Go through all the links on the page
            if link.get('href').startswith(
                'https://www.mturk.com/mturk/preview?groupId='):
                # Write to the mturklinks.html file with all links
                write_file("./HITs/mturklinks-"
                    + str(todays_date) + ".html", "a+",
                    "<a class=\"button\" href=\"" + link.get('href') +
                    "\"> Link </a><br><br>\n")
                if silent is False:  # Check if we are running in silent or not
                    print progress_bar
                if end_of_day is True:  # Check if user will write to forumlog
                    write_file("./HITs/forumlog-" + str(todays_date) +
                    ".txt", "a+", link.get('href') + "\n")


def clean_dupes_log(delete_old):
    todays_date = date.today()
    lines_seen = set()  # Create a place to store lines already seen
    outfilename = "./HITs/forumlog-" + str(todays_date) + "-Clean.txt"
    infilename = "./HITs/forumlog-" + str(todays_date) + ".txt"
    outfile = open(outfilename, "w")
    for line in open(infilename, "r"):
        if line not in lines_seen:  # This outputs all non-duplicates
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    if delete_old is True:
        remove(infilename)


def clean_dupes_html(delete_old):
    todays_date = date.today()
    lines_seen = set()  # Create a place to store lines already seen
    outfilename = "./HITs/mturklinks-" + str(todays_date) + "-Clean.html"
    infilename = "./HITs/mturklinks-" + str(todays_date) + ".html"
    outfile = open(outfilename, "w")
    for line in open(infilename, "r"):
        if line not in lines_seen:  # This outputs all non-duplicates
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    if delete_old is True:
        remove(infilename)


def finish():
    """Finish off the program by shutting off colorama & wait for user"""
    print("""Successfully scraped the forum.
        Your HITs can be found in the HITs folder.""")
    raw_input("Press enter to close the program...")


if __name__ == "__main__":
    clear_update_htm(True)  # Set to false to print output to console
    clear_update_txt(True)  # Set to false to print output to console
    run_through(False)  # Set to True to remove the current page output
    clean_dupes_log(True)  # Set to False to leave duplicate files there
    clean_dupes_html(True)  # Set to False to leave duplicate files there
    finish()  # Prints out a finished message
