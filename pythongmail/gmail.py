#!/usr/bin/env python2

import urllib 
import feedparser #library we will have to download to a server
import os
from textwrap import wrap
username="username" #this can obviously be put somewhere else and the called
password="password"
com="https://"+username+":"+password+"@mail.google.com/mail/feed/atom"
def auth():
	opener = urllib.FancyURLopener()
	f = opener.open(com)
	feed = f.read()
	return feed

def fill(text, width):
	if len(text) < width:
		return text + ' '*(width-len(text))
	else:
		return text

def readmail(feed):
	atom = feedparser.parse(feed)
	print ""
	print "<feedtitle>%s</feedtitle>" %(atom.feed.title)
	print "<entries>You have %s new mails</entries>" % len(atom.entries)
	length = 120
#formatting magic.
	for i in xrange(len(atom.entries)):
		print "<author>%s</author>" % (
			atom.entries[i].author)
		print "<title>%s</title>" % (
			atom.entries[i].title)

if __name__ == "__main__":
	f = auth()  # Do auth and then get the feed
	readmail(f) # Let the feed be chewed by feedparser
