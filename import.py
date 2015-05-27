#Boa:Frame:import_data

import wx

def create(parent):
    return import_data(parent)

[wxID_IMPORT_DATA, wxID_IMPORT_DATABUTTON1, wxID_IMPORT_DATABUTTON2, 
 wxID_IMPORT_DATASTATICBOX1, wxID_IMPORT_DATATEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class import_data(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_IMPORT_DATA, name=u'import_data',
              parent=prnt, pos=wx.Point(698, 326), size=wx.Size(303, 161),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Import Database')
        self.SetClientSize(wx.Size(303, 161))
        self.Center(wx.BOTH)

        self.textCtrl1 = wx.TextCtrl(id=wxID_IMPORT_DATATEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(24, 32),
              size=wx.Size(248, 27), style=0, value=u'')

        self.button1 = wx.Button(id=wxID_IMPORT_DATABUTTON1, label='button1',
              name='button1', parent=self, pos=wx.Point(144, 64),
              size=wx.Size(128, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_IMPORT_DATABUTTON1)

        self.staticBox1 = wx.StaticBox(id=wxID_IMPORT_DATASTATICBOX1,
              label='staticBox1', name='staticBox1', parent=self,
              pos=wx.Point(16, 8), size=wx.Size(272, 104), style=0)

        self.button2 = wx.Button(id=wxID_IMPORT_DATABUTTON2,
              label=u'Kembali Ke Menu Utama', name='button2', parent=self,
              pos=wx.Point(72, 120), size=wx.Size(176, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_IMPORT_DATABUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.textCtrl1.SetValue(dialog.GetPath())
        dialog.Destroy()

    def OnButton2Button(self, event):
        event.Skip()
