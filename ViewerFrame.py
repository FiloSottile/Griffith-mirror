# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Mar  5 15:24:35 2008

__revision__ = '$Id: $'

# Copyright (c) 2005-2008 Vasco Nunes, Piotr Ożarowski

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

# You may use and distribute this software under the terms of the
# GNU General Public License, version 2 or later

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade

class ViewerFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ViewerFrame.__init__
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.FRAME_TOOL_WINDOW|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.poster = wx.StaticBitmap(self, -1, wx.NullBitmap)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ViewerFrame.__set_properties
        self.SetTitle(_("Poster Viewer"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ViewerFrame.__do_layout
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_6.Add(self.poster, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_6)
        sizer_6.Fit(self)
        self.Layout()
        # end wxGlade

# end of class ViewerFrame


