#!/bin/env python
# -*- coding: utf-8 -*-

"""
This is a wxPython program template.

Usage: template_wxpython.py [-d <number>] [-h] [-x]

Where -d <number>  sets the debug level
      -h           prints this help and then stops
      -x           starts the wxPython object inspector
"""

import wx
import wx.html


TemplateName = 'wxPython Template'
TemplateVersion = '0.1'

TileSources = [
               ('Source 1', 'source_1'),
               ('Source 2', 'source_2'),
               ('Source 3', 'source_3'),
              ]

DefaultAppSize = (800, 600)

AboutText = """<p>This is the %(name)s program, version %(version)s. It is
running on version %(wxpy)s of <b>wxPython</b> and %(python)s of <b>Python</b>.
See <a href="http://wiki.wxpython.org">wxPython Wiki</a></p>"""

######
# The About dialog
######

class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if 'gtk2' in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())

class AboutBox(wx.Dialog):
     def __init__(self):
         wx.Dialog.__init__(self, None, -1, 'About <<template>>',
                            style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL)
         hwin = HtmlWindow(self, -1, size=(400,200))
         vers = {}
         vers['python'] = sys.version.split()[0]
         vers['wxpy'] = wx.VERSION_STRING
         vers['name'] = TemplateName
         vers['version'] = TemplateVersion
         hwin.SetPage(AboutText % vers)
         btn = hwin.FindWindowById(wx.ID_OK)
         irep = hwin.GetInternalRepresentation()
         hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+10))
         self.SetClientSize(hwin.GetSize())
         self.CentreOnParent(wx.BOTH)
         self.SetFocus()


######
# The main class
######

class AppFrame(wx.Frame):
    def __init__(self, debug):
        wx.Frame.__init__(self, None, size=DefaultAppSize,
                          title='%s %s' % (TemplateName, TemplateVersion))
        self.SetMinSize(DefaultAppSize)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.panel.SetBackgroundColour(wx.WHITE)
        self.panel.ClearBackground()

        print('AppFrame: debug=%d' % debug)

        # create tileset menuitems
        menuBar = wx.MenuBar()

        tile_menu = wx.Menu()
        self.default_tileset_name = None
        self.tile_menu_data = {}
        for (name, module_name) in TileSources:
            menu_id = tile_menu.Append(wx.ID_ANY, name, name, wx.ITEM_RADIO)
            self.Bind(wx.EVT_MENU, self.onMenuSelect, menu_id)
            self.tile_menu_data[menu_id.Id] = name
        menuBar.Append(tile_menu, '&Tileset')

        quit_menu = wx.Menu()
        about_id = quit_menu.Append(wx.ID_ANY, 'About', 'About the application')
        self.Bind(wx.EVT_MENU, self.onAbout, about_id)
        quit_id = quit_menu.Append(wx.ID_EXIT, 'Quit', 'Quit the application')
        self.Bind(wx.EVT_MENU, self.onQuit, quit_id)
        menuBar.Append(quit_menu, '&File')

        self.SetMenuBar(menuBar)

        # finally, set up application window position
        self.Centre()

    def onMenuSelect(self, event):
        menu_id = event.Id
        tileset_name = self.tile_menu_data[menu_id]
        print('Tileset %s selected' % tileset_name)

    def onAbout(self, event):
        dlg = AboutBox()
        dlg.ShowModal()
        dlg.Destroy()  

    def onQuit(self, event):
        print('Quit selected')
        self.Close()

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
            try:
                debug = int(param)
            except ValueError:
                usage("-d must be followed by an integer, got '%s'" % param)
                sys.exit(1)
        elif opt in ['-h', '--help']:
            usage()
            sys.exit(0)
        elif opt == '-x':       # use this for wxPython programs
            inspector = True

    # start wxPython app
    app = wx.App()
    app_frame = AppFrame(debug)
    app_frame.Show()

    if inspector:
        import wx.lib.inspection
        wx.lib.inspection.InspectionTool().Show()

    app.MainLoop()

