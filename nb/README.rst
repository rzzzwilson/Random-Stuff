The script here is used to backup my NOTEBOOK, which is a
`TiddlyWiki <http://tiddlywiki.com/>`_ application I keep on a USB memory
stick.  The script backs the stick up into a dated directory in a known
location, does a check on the integrity of the filesystem on the stick
and also limits the total size of the known location directory.

Requirements:
  . Must find mounted NOTEBOOK automatically
  . As easy to use and as error-proof as possible
  . Saves NOTEBOOK in time+date stamped directory
  . Save directory must not exceed defined size limit
  . Check the NOTEBOOK filesystem for errors
