This directory contains a python system tray application for OSX.
It uses `rumps <https://github.com/jaredks/rumps>`_.

I wrote this because OSX on my MacBook Pro has the most annoying habit of doing
a 'hard stop' when the battery capacity goes below about 25%.  When I apply
power the machine boots up and I've lost work :-(.

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

I've tried using the **rumps** notification() method, but it usually doesn't
work.
