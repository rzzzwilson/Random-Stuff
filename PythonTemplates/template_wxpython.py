#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a wxPython program template.

This comments describes the use of the code/module below.
It may be printed if a 'usage' option is implemented.
"""

import wx

TemplateName = 'Python wxPython Template'
TemplateVersion = '0.1'

TileSources = [
               ('Source 1', 'source_1'),
               ('Source 2', 'source_2'),
               ('Source 3', 'source_3'),
              ]

DefaultAppSize = (800, 600)

# if wxPython, we start with a Frame()
class AppFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, size=DefaultAppSize,
                          title='%s %s' % (TemplateName, TemplateVersion))
        self.SetMinSize(DefaultAppSize)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.panel.SetBackgroundColour(wx.WHITE)
        self.panel.ClearBackground()

        # create tileset menuitems
        menuBar = wx.MenuBar()
        tile_menu = wx.Menu()

        self.default_tileset_name = None
        for (name, module_name) in TileSources:
            new_id = wx.NewId()
            tile_menu.Append(new_id, name, name, wx.ITEM_RADIO)
            self.Bind(wx.EVT_MENU, self.onMenuSelect)

        menuBar.Append(tile_menu, "&Tileset")
        self.SetMenuBar(menuBar)

        # finally, set up application window position
        self.Centre()

    def onMenuSelect(self, event):
        pass

##############################################################################

if __name__ == '__main__':
    import sys
    import getopt
    import traceback

    # to help the befuddled user
    def usage(msg=None):
        if msg:
            print(('*'*80 + '\n%s\n' + '*'*80) % msg)
        print(__doc__)

    # our own handler for uncaught exceptions
    def excepthook(type, value, tb):
        msg = '\n' + '=' * 80
        msg += '\nUncaught exception:\n'
        msg += ''.join(traceback.format_exception(type, value, tb))
        msg += '=' * 80 + '\n'
        print(msg)
        tkinter_error(msg)
        sys.exit(1)

    # plug our handler into the python system
    sys.excepthook = excepthook

    # parse the program params
    argv = sys.argv[1:]

    try:
        (opts, args) = getopt.getopt(argv, 'd:hx', ['debug=', 'help'])
    except getopt.error:
        usage()
        sys.exit(1)

    debug = 10              # no logging
    inspector = False

    for (opt, param) in opts:
        if opt in ['-d', '--debug']:
            debug = param
        elif opt in ['-h', '--help']:
            usage()
            sys.exit(0)
        elif opt == '-x':       # use this for wxPython programs
            inspector = True

    # start wxPython app
    app = wx.App()
    app_frame = AppFrame()
    app_frame.Show()

    if inspector:
        import wx.lib.inspection
        wx.lib.inspection.InspectionTool().Show()

    app.MainLoop()

