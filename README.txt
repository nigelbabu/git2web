# Git2Web
## History
### The reason behind it!
We all love git.  No question about it.  We also like to run our own servers a lot of times, especially when its our own firm and we own servers anyway.  Or you don't want to go out of the network, or whatever reason it may be.  One of the most common ways of having a git server is to install gitosis.

Its pretty nice.  Python based.  All the magic is done in a post-receive hook for a repo called gitosis-admin.  For programmers and system admins this is friendly enough.  **But**, its not always programmers that manage the repositories.  There are situations when there's probably only one person in the organization who can manage it and the bus factor becomes quite high.  Even so, it becomes tedious to main this file.

This is the point where git2web was born.  I was talking in #cakephp with a few friends and we realized the dire need of something that can manage gitosis but from a webpage.  There exists RoR tools to do it.  But we wanted an alternative given that its a pain to get RoR working.

### Why Python?
I thought of doing this in PHP first.  But I trust python for stuff like this better.  And I wanted to build a webapp in python anyway.  I tried django but it was too big for this.  I'd envisioned this to be used only in an intranet most of the time.  The first release would be oriented to that.  I'd add more security layers in later releases.

## How to install?
git2web is written in Flask, a micro webdevelopment framework.  Take a look at the Flask wiki to see the various deployment options.  I'd be deploying as a cgi, but feel free to chose your own.

## Status
All configuration can now be read from the web.  New key files can be upload.  That's all there is for now.
