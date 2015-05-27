#Boa:Dialog:sumberdata

import wx
import importmitradesa
import importdisdukcapil

def create(parent):
    return sumberdata(parent)

[wxID_SUMBERDATA, wxID_SUMBERDATABUTTON1, wxID_SUMBERDATABUTTON2, 
 wxID_SUMBERDATABUTTON3, wxID_SUMBERDATABUTTON4, wxID_SUMBERDATABUTTON5, 
 wxID_SUMBERDATASTATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(7)]

class sumberdata(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_SUMBERDATA, name=u'sumberdata',
              parent=prnt, pos=wx.Point(733, 282), size=wx.Size(233, 249),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Sumber Data Import')
        self.SetClientSize(wx.Size(233, 249))
        self.Center(wx.BOTH)

        self.staticBox1 = wx.StaticBox(id=wxID_SUMBERDATASTATICBOX1,
              label=u'Pilhan Data', name='staticBox1', parent=self,
              pos=wx.Point(16, 8), size=wx.Size(200, 184), style=0)

        self.button1 = wx.Button(id=wxID_SUMBERDATABUTTON1,
              label=u'DISDUKCAPIL', name='button1', parent=self,
              pos=wx.Point(32, 32), size=wx.Size(168, 30), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_SUMBERDATABUTTON1)

        self.button2 = wx.Button(id=wxID_SUMBERDATABUTTON2,
              label=u'SID Sejenis 1', name='button2', parent=self,
              pos=wx.Point(32, 72), size=wx.Size(168, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_SUMBERDATABUTTON2)

        self.button3 = wx.Button(id=wxID_SUMBERDATABUTTON3,
              label=u'SID Sejenis 2', name='button3', parent=self,
              pos=wx.Point(32, 112), size=wx.Size(168, 30), style=0)

        self.button4 = wx.Button(id=wxID_SUMBERDATABUTTON4,
              label=u'SID Sejenis 3', name='button4', parent=self,
              pos=wx.Point(32, 152), size=wx.Size(168, 30), style=0)

        self.button5 = wx.Button(id=wxID_SUMBERDATABUTTON5,
              label=u'Kembali Ke Menu', name='button5', parent=self,
              pos=wx.Point(32, 208), size=wx.Size(168, 30), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_SUMBERDATABUTTON5)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.main=importdisdukcapil.create(None)
        self.main.Show()
        self.Close()

    def OnButton2Button(self, event):
        self.main=importmitradesa.create(None)
        self.main.Show()
        self.Close()

    def OnButton5Button(self, event):
        self.Close()
