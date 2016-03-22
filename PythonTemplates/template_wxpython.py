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

        # initialise tileset handling
        self.tile_source = None
        # a dict of "gui_id: (name, module_name, object)" tuples
        self.id2tiledata = {}
        # a dict of "name: gui_id"
        self.name2guiid = {}

        self.default_tileset_name = None
        for (name, module_name) in TileSources:
            new_id = wx.NewId()
            tile_menu.Append(new_id, name, name, wx.ITEM_RADIO)
            self.Bind(wx.EVT_MENU, self.onTilesetSelect)
            self.id2tiledata[new_id] = (name, module_name, None)
            self.name2guiid[name] = new_id
            if name == DefaultTileset:
                self.default_tileset_name = name

        if self.default_tileset_name is None:
            raise Exception('Bad DefaultTileset (%s) or TileSources (%s)'
                            % (DefaultTileset, str(TileSources)))

        menuBar.Append(tile_menu, "&Tileset")
        self.SetMenuBar(menuBar)

        self.tile_source = tiles.Tiles()

        # build the GUI
        self.make_gui(self.panel)

        # do initialisation stuff - all the application stuff
        self.init()

        # finally, set up application window position
        self.Centre()

        # create select event dispatch directory
        self.demo_select_dispatch = {}

        # finally, bind events to handlers
        self.pyslip.Bind(pyslip.EVT_PYSLIP_SELECT, self.handle_select_event)
        self.pyslip.Bind(pyslip.EVT_PYSLIP_BOXSELECT, self.handle_select_event)
        self.pyslip.Bind(pyslip.EVT_PYSLIP_POSITION, self.handle_position_event)
        self.pyslip.Bind(pyslip.EVT_PYSLIP_LEVEL, self.handle_level_change)

        # select the required tileset
        item_id = self.name2guiid[self.default_tileset_name]
        tile_menu.Check(item_id, True)

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
        log(msg)
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

    # alternatively, start a CLI program
    result = main(debug)
    sys.exit(result)

