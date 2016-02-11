This directory contains a python system tray application for OSX.
It uses `rumps <https://github.com/jaredks/rumps>`_.

I wrote this because OSX on my MacBook Pro has the most annoying habit
of 'crashing' when the battery capacity goes below about 25%.  When I apply
power the machine boots up and I've lost work :-(.

Apple states that the machine should warn that battery capacity is low,
but I found that doesn't happen on my machine.  It's about 2.5 years old.

Dependencies
============

You have to do:

::

    pip install rumps

to get **rumps** itself.  But you need XCode before installing **rumps**.
A mere **4.4GiB** download!?

Caveats
=======

I've tried using the **rumps** notification() method, but it usually doesn't
work.
