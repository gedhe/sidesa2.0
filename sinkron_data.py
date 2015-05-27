#Boa:Frame:sinkron_data

import wx
import ftplib


def create(parent):
    return sinkron_data(parent)

[wxID_SINKRON_DATA, wxID_SINKRON_DATABUTTON1, wxID_SINKRON_DATABUTTON2, 
 wxID_SINKRON_DATAKUNCI, wxID_SINKRON_DATANAMA, wxID_SINKRON_DATASERVER, 
 wxID_SINKRON_DATASTATICBOX1, wxID_SINKRON_DATASTATICTEXT1, 
 wxID_SINKRON_DATASTATICTEXT2, wxID_SINKRON_DATASTATICTEXT3, 
] = [wx.NewId() for _init_ctrls in range(10)]

class sinkron_data(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SINKRON_DATA, name=u'sinkron_data',
              parent=prnt, pos=wx.Point(656, 293), size=wx.Size(382, 203),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Sinkronisasi Database')
        self.SetClientSize(wx.Size(382, 203))
        self.Center(wx.BOTH)

        self.staticBox1 = wx.StaticBox(id=wxID_SINKRON_DATASTATICBOX1,
              label=u'Sinkron Database', name='staticBox1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(368, 144), style=0)

        self.staticText1 = wx.StaticText(id=wxID_SINKRON_DATASTATICTEXT1,
              label=u'Alamat URL FTP', name='staticText1', parent=self,
              pos=wx.Point(24, 40), size=wx.Size(102, 15), style=0)

        self.staticText2 = wx.StaticText(id=wxID_SINKRON_DATASTATICTEXT2,
              label=u'Username FTP', name='staticText2', parent=self,
              pos=wx.Point(24, 72), size=wx.Size(94, 15), style=0)

        self.staticText3 = wx.StaticText(id=wxID_SINKRON_DATASTATICTEXT3,
              label=u'Password FTP', name='staticText3', parent=self,
              pos=wx.Point(24, 104), size=wx.Size(86, 15), style=0)

        self.server = wx.TextCtrl(id=wxID_SINKRON_DATASERVER, name=u'server',
              parent=self, pos=wx.Point(152, 40), size=wx.Size(216, 25),
              style=0, value='')

        self.nama = wx.TextCtrl(id=wxID_SINKRON_DATANAMA, name=u'nama',
              parent=self, pos=wx.Point(152, 72), size=wx.Size(216, 25),
              style=0, value='')

        self.kunci = wx.TextCtrl(id=wxID_SINKRON_DATAKUNCI, name=u'kunci',
              parent=self, pos=wx.Point(152, 104), size=wx.Size(216, 25),
              style=0, value='')

        self.button1 = wx.Button(id=wxID_SINKRON_DATABUTTON1,
              label=u'Sinkron Data', name='button1', parent=self,
              pos=wx.Point(24, 160), size=wx.Size(176, 30), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_SINKRON_DATABUTTON1)

        self.button2 = wx.Button(id=wxID_SINKRON_DATABUTTON2,
              label=u'Kembali Ke Menu ', name='button2', parent=self,
              pos=wx.Point(208, 160), size=wx.Size(152, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_SINKRON_DATABUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton2Button(self, event):
       
        self.Close()

    def OnButton1Button(self, event):
        server = str(self.server.GetValue())
        nama = str(self.nama.GetValue())
        password = str(self.kunci.GetValue())
        ftp = ftplib.FTP()
        ftp.connect(server)
        ftp.login(nama,password)
        f = open('/opt/sidesa/sidesa', 'rb')
        ftp.cwd('public_html')
        ftp.storbinary('STOR sidesa', f)
        f.close()
        self.pesan = wx.MessageDialog(self,"Data Telah Tersinkronisasi","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
