#Boa:Frame:Frame1

import wx
import wx.richtext

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1COMBOBOX1, wxID_FRAME1LISTCTRL1, 
 wxID_FRAME1LISTCTRL2, wxID_FRAME1LISTCTRL3, wxID_FRAME1RICHTEXTCTRL1, 
 wxID_FRAME1RICHTEXTCTRL2, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, 
 wxID_FRAME1STATICTEXT11, wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, 
 wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, 
 wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, wxID_FRAME1TEXTCTRL7, 
] = [wx.NewId() for _init_ctrls in range(31)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(368, 14), size=wx.Size(964, 703),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Penyusunan APBdesa')
        self.SetClientSize(wx.Size(964, 703))
        self.Center(wx.BOTH)

        self.listCtrl1 = wx.ListCtrl(id=wxID_FRAME1LISTCTRL1, name='listCtrl1',
              parent=self, pos=wx.Point(8, 40), size=wx.Size(576, 184),
              style=wx.LC_ICON)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Anggaran Pendapatan', name='staticText1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(144, 17), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Tahun Anggaran', name='staticText2', parent=self,
              pos=wx.Point(592, 8), size=wx.Size(105, 17), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Nomor Rekening', name='staticText3', parent=self,
              pos=wx.Point(592, 80), size=wx.Size(109, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Uraian', name='staticText4', parent=self,
              pos=wx.Point(592, 128), size=wx.Size(44, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Jumlah', name='staticText5', parent=self,
              pos=wx.Point(600, 448), size=wx.Size(46, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Keterangan', name='staticText6', parent=self,
              pos=wx.Point(600, 480), size=wx.Size(75, 17), style=0)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self, pos=wx.Point(728, 112), size=wx.Size(216, 320),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl1.SetLabel(u'')

        self.listCtrl2 = wx.ListCtrl(id=wxID_FRAME1LISTCTRL2, name='listCtrl2',
              parent=self, pos=wx.Point(8, 264), size=wx.Size(576, 192),
              style=wx.LC_ICON)

        self.listCtrl3 = wx.ListCtrl(id=wxID_FRAME1LISTCTRL3, name='listCtrl3',
              parent=self, pos=wx.Point(8, 496), size=wx.Size(576, 192),
              style=wx.LC_ICON)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Anggaran Belanja', name='staticText7', parent=self,
              pos=wx.Point(8, 232), size=wx.Size(116, 17), style=0)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'Aggaran Pembiayaan', name='staticText8', parent=self,
              pos=wx.Point(8, 464), size=wx.Size(140, 17), style=0)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Rekening Utama', name='staticText9', parent=self,
              pos=wx.Point(592, 48), size=wx.Size(109, 17), style=0)

        self.comboBox1 = wx.ComboBox(choices=['1.1. Pendapatan Asli Desa',
              '1.2.Pendapatan Transfer', '1.3.Pendapatan Lain-lain',
              '2.1.Bidang Penyelenggaran Pemerintahan Desa',
              '2.2.Bidang Pelaksanaan Pembangunan Desa',
              '2.3.Bidang Pembinanaan Kemasyarakatan',
              '2.4.Bidang Pemberdayaan Masyarakat', '2.5.Bidang Tak Terduga',
              '3.1.Penerimaan Pembiayaan', '3.2.Pengeluaran Pembiayaan' ],
              id=wxID_FRAME1COMBOBOX1, name='comboBox1', parent=self,
              pos=wx.Point(728, 40), size=wx.Size(216, 27), style=0, value=u'')
        self.comboBox1.SetLabel(u'')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(728, 80), size=wx.Size(152, 24),
              style=0, value=u'')

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(728, 8), size=wx.Size(152, 24), style=0,
              value=u'')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(728, 440), size=wx.Size(152, 24),
              style=0, value=u'')

        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL2,
              parent=self, pos=wx.Point(728, 472), size=wx.Size(216, 100),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl2.SetLabel(u'')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(432, 8), size=wx.Size(152, 24), style=0,
              value=u'')

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(432, 232), size=wx.Size(152, 24),
              style=0, value=u'')

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(432, 464), size=wx.Size(152, 24),
              style=0, value=u'')

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Jumlah Total', name='staticText10', parent=self,
              pos=wx.Point(328, 232), size=wx.Size(81, 17), style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Jumlah Total', name='staticText11', parent=self,
              pos=wx.Point(336, 464), size=wx.Size(81, 17), style=0)

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'Jumlah Total', name='staticText12', parent=self,
              pos=wx.Point(336, 8), size=wx.Size(81, 17), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Tambah Data',
              name='button1', parent=self, pos=wx.Point(600, 592),
              size=wx.Size(128, 30), style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Edit Data',
              name='button2', parent=self, pos=wx.Point(736, 592),
              size=wx.Size(109, 30), style=0)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'Keluar',
              name='button3', parent=self, pos=wx.Point(848, 592),
              size=wx.Size(104, 30), style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(728, 640), size=wx.Size(216, 27),
              style=0, value=u'')

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'Surplus/Defisit', name='staticText13', parent=self,
              pos=wx.Point(600, 640), size=wx.Size(95, 17), style=0)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'Cetak APB Desa',
              name='button4', parent=self, pos=wx.Point(600, 672),
              size=wx.Size(352, 30), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
