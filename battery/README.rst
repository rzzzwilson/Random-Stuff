This directory contains a python system tray application for OSX.
It uses `rumps <https://github.com/jaredks/rumps>`_.

I wrote this because OSX on my MacBook Pro has the most annoying habit of doing
a 'hard stop' when the battery capacity goes below about 25%.  When I apply
power the machine boots up and I've lost work :-(.  The RTC also has had a
lobotomy, displaying 00:00 1 Jan 2015 UTC on boot until a network connection
is made and NTP does its thing.  This is very annoying as the time difference
is so large that NTP won't update the clock until I unlock the "time and date"
settings dialog.

Apple states that there should be a warning that battery capacity is low,
but I found that doesn't happen on my machine.  It's about 2.5 years old
but the battery is in good shape, according to the Apple diagnostics.

Using
=====

Once you copy the **battery** file to your special place, modify **run_battery**
to start **battery** from that place.  Then through
"System Preferences|Users & Groups"
start **run_battery** as a terminal program.

Dependencies
============

You have to do:

::

    pip install rumps

to get **rumps** itself.  But you need XCode before installing **rumps**.
A mere **4.4GiB** download!?

And you may also need to install **pyobc** via pip.

Caveats
=======

The **rumps** notification() method doesn't seem too reliable, often failing
to raise a notification?

Wrap up
=======

This little thing does work, but my rMBP crashes without warning with any
remaining charge between 25% and 55%.  This makes this tool useless.

I finally got a "service battery" indication, and Apple is now replacing
(apparently) my laptop.  For some reason, this takes them **ALMOST FOUR WEEKS!**
Consider not using Apple for my next laptop.
