#Boa:Frame:laporan_penduduk

import wx
import wx.calendar
import sqlite3

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return laporan_penduduk(parent)

[wxID_LAPORAN_PENDUDUK, wxID_LAPORAN_PENDUDUKBUTTON1, 
 wxID_LAPORAN_PENDUDUKBUTTON10, wxID_LAPORAN_PENDUDUKBUTTON11, 
 wxID_LAPORAN_PENDUDUKBUTTON12, wxID_LAPORAN_PENDUDUKBUTTON13, 
 wxID_LAPORAN_PENDUDUKBUTTON14, wxID_LAPORAN_PENDUDUKBUTTON15, 
 wxID_LAPORAN_PENDUDUKBUTTON2, wxID_LAPORAN_PENDUDUKBUTTON3, 
 wxID_LAPORAN_PENDUDUKBUTTON4, wxID_LAPORAN_PENDUDUKBUTTON5, 
 wxID_LAPORAN_PENDUDUKBUTTON6, wxID_LAPORAN_PENDUDUKBUTTON7, 
 wxID_LAPORAN_PENDUDUKBUTTON8, wxID_LAPORAN_PENDUDUKBUTTON9, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX1, wxID_LAPORAN_PENDUDUKCOMBOBOX10, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX2, wxID_LAPORAN_PENDUDUKCOMBOBOX3, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX4, wxID_LAPORAN_PENDUDUKCOMBOBOX5, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX6, wxID_LAPORAN_PENDUDUKCOMBOBOX7, 
 wxID_LAPORAN_PENDUDUKCOMBOBOX8, wxID_LAPORAN_PENDUDUKCOMBOBOX9, 
 wxID_LAPORAN_PENDUDUKLISTCTRL1, wxID_LAPORAN_PENDUDUKSTATICTEXT1, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT10, wxID_LAPORAN_PENDUDUKSTATICTEXT11, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT12, wxID_LAPORAN_PENDUDUKSTATICTEXT13, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT14, wxID_LAPORAN_PENDUDUKSTATICTEXT15, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT16, wxID_LAPORAN_PENDUDUKSTATICTEXT17, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT18, wxID_LAPORAN_PENDUDUKSTATICTEXT19, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT2, wxID_LAPORAN_PENDUDUKSTATICTEXT20, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT21, wxID_LAPORAN_PENDUDUKSTATICTEXT22, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT23, wxID_LAPORAN_PENDUDUKSTATICTEXT24, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT25, wxID_LAPORAN_PENDUDUKSTATICTEXT26, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT27, wxID_LAPORAN_PENDUDUKSTATICTEXT28, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT3, wxID_LAPORAN_PENDUDUKSTATICTEXT4, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT5, wxID_LAPORAN_PENDUDUKSTATICTEXT6, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT7, wxID_LAPORAN_PENDUDUKSTATICTEXT8, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT9, wxID_LAPORAN_PENDUDUKTEXTCTRL1, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL10, wxID_LAPORAN_PENDUDUKTEXTCTRL11, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL12, wxID_LAPORAN_PENDUDUKTEXTCTRL13, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL14, wxID_LAPORAN_PENDUDUKTEXTCTRL2, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL3, wxID_LAPORAN_PENDUDUKTEXTCTRL4, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL5, wxID_LAPORAN_PENDUDUKTEXTCTRL6, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL7, wxID_LAPORAN_PENDUDUKTEXTCTRL8, 
 wxID_LAPORAN_PENDUDUKTEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(69)]

class laporan_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LAPORAN_PENDUDUK,
              name=u'laporan_penduduk', parent=prnt, pos=wx.Point(386, 154),
              size=wx.Size(928, 506), style=wx.FRAME_NO_TASKBAR,
              title=u'Sistem Laporan Penduduk')
        self.SetClientSize(wx.Size(928, 506))
        self.Center(wx.BOTH)

        self.staticText1 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT1,
              label=u'Jumlah Keluarga KK Sementara', name='staticText1',
              parent=self, pos=wx.Point(16, 184), size=wx.Size(216, 15),
              style=0)

        self.staticText2 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT2,
              label=u'Jumlah Keluarga KK Tetap', name='staticText2',
              parent=self, pos=wx.Point(16, 224), size=wx.Size(200, 15),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT3,
              label=u'Jumlah Penduduk Laki - Laki', name='staticText3',
              parent=self, pos=wx.Point(16, 256), size=wx.Size(224, 15),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT4,
              label=u'Jumlah Penduduk Perempuan', name='staticText4',
              parent=self, pos=wx.Point(16, 288), size=wx.Size(224, 15),
              style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(248, 184),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL2,
              name='textCtrl2', parent=self, pos=wx.Point(248, 216),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl3 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL3,
              name='textCtrl3', parent=self, pos=wx.Point(248, 248),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl4 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL4,
              name='textCtrl4', parent=self, pos=wx.Point(248, 280),
              size=wx.Size(50, 25), style=0, value='')

        self.button1 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON1,
              label=u'Lihat Data', name='button1', parent=self,
              pos=wx.Point(336, 216), size=wx.Size(96, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON1)

        self.button2 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON2,
              label=u'Lihat Data', name='button2', parent=self,
              pos=wx.Point(336, 248), size=wx.Size(96, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON2)

        self.button3 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON3,
              label=u'Lihat Data', name='button3', parent=self,
              pos=wx.Point(816, 312), size=wx.Size(96, 24), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON3)

        self.button4 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON4,
              label=u'Lihat Data', name='button4', parent=self,
              pos=wx.Point(816, 184), size=wx.Size(96, 24), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON4)

        self.staticText7 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT7,
              label=u'Jumlah Pendidikan Akhir', name='staticText7', parent=self,
              pos=wx.Point(448, 192), size=wx.Size(176, 15), style=0)

        self.comboBox1 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX1, name='comboBox1', parent=self,
              pos=wx.Point(624, 184), size=wx.Size(96, 25), style=0, value='')

        self.textCtrl5 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL5,
              name='textCtrl5', parent=self, pos=wx.Point(728, 184),
              size=wx.Size(50, 25), style=0, value='')

        self.staticText8 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT8,
              label=u'Jumlah Saat Ini Pendidikan', name='staticText8',
              parent=self, pos=wx.Point(448, 224), size=wx.Size(200, 15),
              style=0)

        self.comboBox2 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX2, name='comboBox2', parent=self,
              pos=wx.Point(624, 216), size=wx.Size(96, 25), style=0, value='')

        self.textCtrl6 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL6,
              name='textCtrl6', parent=self, pos=wx.Point(728, 216),
              size=wx.Size(50, 25), style=0, value='')

        self.staticText9 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT9,
              label=u'Status Perkawinan', name='staticText9', parent=self,
              pos=wx.Point(448, 288), size=wx.Size(152, 15), style=0)

        self.comboBox3 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX3, name='comboBox3', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(96, 25), style=0, value='')

        self.button5 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON5,
              label=u'Lihat Data', name='button5', parent=self,
              pos=wx.Point(816, 216), size=wx.Size(96, 24), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON5)

        self.button6 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON6,
              label=u'Lihat Data', name='button6', parent=self,
              pos=wx.Point(336, 184), size=wx.Size(96, 24), style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON6)

        self.staticText10 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT10,
              label=u'Difabelitas', name='staticText10', parent=self,
              pos=wx.Point(448, 320), size=wx.Size(120, 15), style=0)

        self.comboBox4 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX4, name='comboBox4', parent=self,
              pos=wx.Point(624, 280), size=wx.Size(96, 25), style=0, value='')

        self.staticText11 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT11,
              label=u'Status Tinggal', name='staticText11', parent=self,
              pos=wx.Point(448, 352), size=wx.Size(152, 15), style=0)

        self.comboBox5 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX5, name='comboBox5', parent=self,
              pos=wx.Point(624, 312), size=wx.Size(96, 25), style=0, value='')

        self.staticText12 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT12,
              label=u'Pekerjaan', name='staticText12', parent=self,
              pos=wx.Point(448, 256), size=wx.Size(120, 15), style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL7,
              name='textCtrl7', parent=self, pos=wx.Point(248, 312),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl8 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL8,
              name='textCtrl8', parent=self, pos=wx.Point(248, 344),
              size=wx.Size(50, 25), style=0, value='')

        self.staticText13 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT13,
              label=u'Status Penduduk', name='staticText13', parent=self,
              pos=wx.Point(448, 384), size=wx.Size(144, 15), style=0)

        self.comboBox6 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX6, name='comboBox6', parent=self,
              pos=wx.Point(624, 344), size=wx.Size(96, 25), style=0, value='')

        self.comboBox7 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX7, name='comboBox7', parent=self,
              pos=wx.Point(624, 376), size=wx.Size(96, 25), style=0, value='')

        self.staticText14 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT14,
              label=u'Resiko Kehamilan', name='staticText14', parent=self,
              pos=wx.Point(448, 416), size=wx.Size(160, 15), style=0)

        self.comboBox8 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX8, name='comboBox8', parent=self,
              pos=wx.Point(624, 408), size=wx.Size(96, 25), style=0, value='')

        self.textCtrl9 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL9,
              name='textCtrl9', parent=self, pos=wx.Point(728, 248),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl10 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL10,
              name='textCtrl10', parent=self, pos=wx.Point(728, 280),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl11 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL11,
              name='textCtrl11', parent=self, pos=wx.Point(728, 312),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl12 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL12,
              name='textCtrl12', parent=self, pos=wx.Point(728, 344),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl13 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL13,
              name='textCtrl13', parent=self, pos=wx.Point(728, 376),
              size=wx.Size(50, 25), style=0, value='')

        self.textCtrl14 = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKTEXTCTRL14,
              name='textCtrl14', parent=self, pos=wx.Point(728, 408),
              size=wx.Size(50, 25), style=0, value='')

        self.button7 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON7,
              label=u'Lihat Data', name='button7', parent=self,
              pos=wx.Point(336, 344), size=wx.Size(96, 24), style=0)
        self.button7.Bind(wx.EVT_BUTTON, self.OnButton7Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON7)

        self.button8 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON8,
              label=u'Lihat Data', name='button8', parent=self,
              pos=wx.Point(816, 248), size=wx.Size(96, 24), style=0)
        self.button8.Bind(wx.EVT_BUTTON, self.OnButton8Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON8)

        self.button9 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON9,
              label=u'Lihat Data', name='button9', parent=self,
              pos=wx.Point(816, 280), size=wx.Size(96, 24), style=0)
        self.button9.Bind(wx.EVT_BUTTON, self.OnButton9Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON9)

        self.button10 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON10,
              label=u'Lihat Data', name='button10', parent=self,
              pos=wx.Point(336, 312), size=wx.Size(96, 24), style=0)
        self.button10.Bind(wx.EVT_BUTTON, self.OnButton10Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON10)

        self.button11 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON11,
              label=u'Lihat Data', name='button11', parent=self,
              pos=wx.Point(816, 344), size=wx.Size(96, 24), style=0)
        self.button11.Bind(wx.EVT_BUTTON, self.OnButton11Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON11)

        self.button12 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON12,
              label=u'Lihat Data', name='button12', parent=self,
              pos=wx.Point(816, 376), size=wx.Size(96, 24), style=0)
        self.button12.Bind(wx.EVT_BUTTON, self.OnButton12Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON12)

        self.button13 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON13,
              label=u'Lihat Data', name='button13', parent=self,
              pos=wx.Point(816, 408), size=wx.Size(96, 24), style=0)
        self.button13.Bind(wx.EVT_BUTTON, self.OnButton13Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON13)

        self.button14 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON14,
              label=u'Lihat Data', name='button14', parent=self,
              pos=wx.Point(336, 280), size=wx.Size(96, 24), style=0)
        self.button14.Bind(wx.EVT_BUTTON, self.OnButton14Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON14)

        self.button15 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON15,
              label=u'Kembali Ke Menu', name='button15', parent=self,
              pos=wx.Point(360, 448), size=wx.Size(224, 30), style=0)
        self.button15.Bind(wx.EVT_BUTTON, self.OnButton15Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON15)

        self.staticText5 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT5,
              label=u'Agama', name='staticText5', parent=self, pos=wx.Point(16,
              320), size=wx.Size(42, 17), style=0)

        self.comboBox9 = wx.ComboBox(choices=['Islam', 'Kristen Protestan',
              'Kristen Katolik', 'Hindu', 'Budha', 'Konghuchu',
              'Aliran Kepercayaan', 'Agama Lainnya'],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX9, name='comboBox9', parent=self,
              pos=wx.Point(144, 312), size=wx.Size(96, 24), style=0, value=u'')
        self.comboBox9.SetLabel(u'')
        self.comboBox9.Bind(wx.EVT_COMBOBOX, self.OnComboBox9Combobox,
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX9)

        self.staticText6 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT6,
              label=u'Kewarganegaraan', name='staticText6', parent=self,
              pos=wx.Point(16, 344), size=wx.Size(108, 17), style=0)

        self.comboBox10 = wx.ComboBox(choices=[],
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX10, name='comboBox10',
              parent=self, pos=wx.Point(144, 344), size=wx.Size(96, 24),
              style=0, value=u'')
        self.comboBox10.SetLabel(u'')
        self.comboBox10.Bind(wx.EVT_COMBOBOX, self.OnComboBox9Combobox,
              id=wxID_LAPORAN_PENDUDUKCOMBOBOX10)

        self.listCtrl1 = wx.ListCtrl(id=wxID_LAPORAN_PENDUDUKLISTCTRL1,
              name='listCtrl1', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(888, 168), style=wx.LC_ICON)

        self.staticText15 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT15,
              label=u'KK', name='staticText15', parent=self, pos=wx.Point(304,
              224), size=wx.Size(17, 17), style=0)

        self.staticText16 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT16,
              label=u'KK', name='staticText16', parent=self, pos=wx.Point(304,
              192), size=wx.Size(17, 17), style=0)

        self.staticText17 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT17,
              label=u'Jiwa', name='staticText17', parent=self, pos=wx.Point(304,
              288), size=wx.Size(25, 17), style=0)

        self.staticText18 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT18,
              label=u'Jiwa', name='staticText18', parent=self, pos=wx.Point(304,
              320), size=wx.Size(25, 17), style=0)

        self.staticText19 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT19,
              label=u'Jiwa', name='staticText19', parent=self, pos=wx.Point(304,
              352), size=wx.Size(25, 17), style=0)

        self.staticText20 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT20,
              label=u'Jiwa', name='staticText20', parent=self, pos=wx.Point(784,
              192), size=wx.Size(25, 17), style=0)

        self.staticText21 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT21,
              label=u'Jiwa', name='staticText21', parent=self, pos=wx.Point(784,
              224), size=wx.Size(25, 17), style=0)

        self.staticText22 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT22,
              label=u'Jiwa', name='staticText22', parent=self, pos=wx.Point(784,
              256), size=wx.Size(25, 17), style=0)

        self.staticText23 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT23,
              label=u'Jiwa', name='staticText23', parent=self, pos=wx.Point(784,
              288), size=wx.Size(25, 17), style=0)

        self.staticText24 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT24,
              label=u'Jiwa', name='staticText24', parent=self, pos=wx.Point(784,
              352), size=wx.Size(25, 17), style=0)

        self.staticText25 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT25,
              label=u'Jiwa', name='staticText25', parent=self, pos=wx.Point(304,
              256), size=wx.Size(25, 17), style=0)

        self.staticText26 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT26,
              label=u'Jiwa', name='staticText26', parent=self, pos=wx.Point(784,
              384), size=wx.Size(25, 17), style=0)

        self.staticText27 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT27,
              label=u'Jiwa', name='staticText27', parent=self, pos=wx.Point(784,
              416), size=wx.Size(25, 17), style=0)

        self.staticText28 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT28,
              label=u'Jiwa', name='staticText28', parent=self, pos=wx.Point(784,
              320), size=wx.Size(25, 17), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton15Button(self, event):
        
        self.Close()

    def OnButton1Button(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE jenis_kelamin='Laki-laki'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.textCtrl2.SetValue(str(hasil))
        event.Skip()
        

    def OnButton2Button(self, event):
        event.Skip()

    def OnButton3Button(self, event):
        event.Skip()

    def OnButton4Button(self, event):
        event.Skip()

    def OnButton5Button(self, event):
        event.Skip()

    def OnButton6Button(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE shdk='Kepala Keluarga'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.textCtrl1.SetValue(str(hasil))
        event.Skip()

    def OnButton7Button(self, event):
        event.Skip()

    def OnButton8Button(self, event):
        event.Skip()

    def OnButton9Button(self, event):
        event.Skip()

    def OnButton10Button(self, event):
        event.Skip()

    def OnButton11Button(self, event):
        event.Skip()

    def OnButton12Button(self, event):
        event.Skip()

    def OnButton13Button(self, event):
        event.Skip()

    def OnButton14Button(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE jenis_kelamin='Perempuan'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.textCtrl4.SetValue(str(hasil))
        event.Skip()
        event.Skip()

    def OnComboBox9Combobox(self, event):
        event.Skip()
