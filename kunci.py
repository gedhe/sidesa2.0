#Boa:Dialog:kunci

import wx
import sqlite3


db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()
    
def create(parent):
    return kunci(parent)

[wxID_KUNCI, wxID_KUNCIBUTTON1, wxID_KUNCIBUTTON2, wxID_KUNCISTATICTEXT1, 
 wxID_KUNCITEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class kunci(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_KUNCI, name=u'kunci', parent=prnt,
              pos=wx.Point(693, 350), size=wx.Size(340, 133),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Ganti Password')
        self.SetClientSize(wx.Size(340, 133))
        self.Center(wx.BOTH)

        self.staticText1 = wx.StaticText(id=wxID_KUNCISTATICTEXT1,
              label=u'Password', name='staticText1', parent=self,
              pos=wx.Point(16, 24), size=wx.Size(60, 15), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_KUNCITEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(88, 16), size=wx.Size(232, 25), style=0,
              value='')

        self.button1 = wx.Button(id=wxID_KUNCIBUTTON1, label=u'Simpan',
              name='button1', parent=self, pos=wx.Point(48, 88),
              size=wx.Size(112, 30), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_KUNCIBUTTON1)

        self.button2 = wx.Button(id=wxID_KUNCIBUTTON2, label=u'Ke Menu',
              name='button2', parent=self, pos=wx.Point(168, 88),
              size=wx.Size(128, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_KUNCIBUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        konci = str(self.textCtrl1.GetValue())
        isinya = "SELECT * FROM password WHERE nama='admin'"
        cur.execute(isinya)
        kunci = cur.fetchone()[1]
        oneng = "UPDATE password SET kunci='"+konci+"' WHERE nama='admin'"
        cur.execute(oneng)
        db.commit()
        db.close()
        self.Close()
        self.Destroy()

    def OnButton2Button(self, event):
        self.Close()
        self.Destroy()
