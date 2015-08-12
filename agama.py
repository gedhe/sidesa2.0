#Boa:Frame:Frame1

import wx
from wx.lib.plot import PolyLine, PlotCanvas, PlotGraphics

def create(parent):
    return Frame1(parent)

[wxID_FRAME1] = [wx.NewId() for _init_ctrls in range(1)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(341, 167), size=wx.Size(911, 445),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(911, 445))

    def __init__(self, parent):
        self._init_ctrls(parent)
