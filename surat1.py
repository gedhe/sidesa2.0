#Boa:Frame:Frame1

import wx
import wx.html
import wx.stc

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1HTMLWINDOW1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(334, 0), size=wx.Size(767, 715),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(767, 715))

        self.htmlWindow1 = wx.html.HtmlWindow(id=wxID_FRAME1HTMLWINDOW1,
              name='htmlWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(767, 715), style=wx.html.HW_SCROLLBAR_AUTO)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.htmlWindow1.LoadPage("/opt/sidesa/hasil2.pdf")
