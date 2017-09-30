# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     implement a simple general purpose aggregator
#
# Author:       Pavlos P
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator

Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""
import urllib.request
import urllib.error
import re
import sys


def read_url(each_url, topic):
    """
    Reads the url and searches for content related to a specific topic
    if there are results, calls the write_to_file()

    :param each_url:(string) the url address
    :param topic:(string) topic to be researched and reported on
    """
    try:

        with urllib.request.urlopen(each_url) as url_file:
            article = url_file.read().decode('UTF-8')
            pattern = r'\>([^\<]*\b{}\b.*?)\<'.format(topic)
            matches = re.findall(pattern, article, re.IGNORECASE | re.DOTALL)

            if matches:
                write_to_file(topic, each_url, '\n'.join(matches))

    except urllib.error.URLError as url_err:
        print('\nError opening url: ', each_url, url_err)
    except UnicodeDecodeError as decode_err:
        print('Error decoding url: ', each_url, decode_err)


def write_to_file(topic, each_url, all_references):
    """
    Writes to a file the content of the research

    :param topic: (string) topic to be researched and reported on
    :param each_url:(string) the url address
    :param all_references:(string) the content related to the topic
    """
    with open(topic + '_summary.txt', 'a', encoding='utf-8') as new_file:
        new_file.write('\n%s%s\n%s\n_________________________________'
                       '\n' % ('Source url:', each_url, all_references))


def read_arguments():
    """
    Reads the arguments from the terminal
    exits if the argvs are not 3

    :return: the filename and the topic
    """
    if len(sys.argv) != 3:
        print('Error:  invalid number of arguments')
        print('Usage: aggregator.py filename topic')
        sys.exit()
    else:
        filename = sys.argv[1]
        topic = (sys.argv[2])
    return filename, topic


def proceed_file_(filename, topic):
    """
    Opens the file and passes the url addresses and the topic as
    arguments in the read_url()

    :param filename:(string) the filename
    :param topic: (string) the topic for research
    """
    with open(filename, 'r', encoding='utf-8') as my_file:
        for each_url in my_file:
            read_url(each_url, topic)


def main():
    filename, topic = read_arguments()
    proceed_file_(filename, topic)


if __name__ == '__main__':
    main()
