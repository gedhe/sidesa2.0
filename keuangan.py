#Boa:Frame:keuangan

import wx
import penyusunan

def create(parent):
    return keuangan(parent)

[wxID_KEUANGAN, wxID_KEUANGANAPBDESA, wxID_KEUANGANBANKDESA, wxID_KEUANGANBKU, 
 wxID_KEUANGANBUKUKASPEMBANTU, wxID_KEUANGANBUTTON1, wxID_KEUANGANLAPABDESA, 
 wxID_KEUANGANPAJAK, wxID_KEUANGANPERNYATAAN, wxID_KEUANGANRAB, 
 wxID_KEUANGANREALISASIAKHIR, wxID_KEUANGANREALISASIPERTAMA, 
 wxID_KEUANGANSEKTORAL, wxID_KEUANGANSPP, wxID_KEUANGANSTATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(15)]

class keuangan(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_KEUANGAN, name=u'keuangan', parent=prnt,
              pos=wx.Point(425, 114), size=wx.Size(427, 542),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Keuangan Desa')
        self.SetClientSize(wx.Size(427, 542))

        self.apbdesa = wx.Button(id=wxID_KEUANGANAPBDESA, label=u'APB Desa',
              name=u'apbdesa', parent=self, pos=wx.Point(88, 16),
              size=wx.Size(264, 32), style=0)
        self.apbdesa.Bind(wx.EVT_BUTTON, self.OnApbdesaButton,
              id=wxID_KEUANGANAPBDESA)

        self.rab = wx.Button(id=wxID_KEUANGANRAB,
              label=u'Rencana Anggaran Biaya', name=u'rab', parent=self,
              pos=wx.Point(88, 56), size=wx.Size(264, 30), style=0)

        self.bukukaspembantu = wx.Button(id=wxID_KEUANGANBUKUKASPEMBANTU,
              label=u'Buku Kas Pembantu', name=u'bukukaspembantu', parent=self,
              pos=wx.Point(88, 96), size=wx.Size(264, 30), style=0)

        self.spp = wx.Button(id=wxID_KEUANGANSPP,
              label=u'Surat Permintaan Pembayaran', name=u'spp', parent=self,
              pos=wx.Point(88, 136), size=wx.Size(264, 30), style=0)

        self.pernyataan = wx.Button(id=wxID_KEUANGANPERNYATAAN,
              label=u'Pernyataan Tanggung Jawab Belanja', name=u'pernyataan',
              parent=self, pos=wx.Point(88, 176), size=wx.Size(264, 30),
              style=0)

        self.bku = wx.Button(id=wxID_KEUANGANBKU, label=u'Buku Kas Umum',
              name=u'bku', parent=self, pos=wx.Point(88, 216), size=wx.Size(264,
              30), style=0)

        self.pajak = wx.Button(id=wxID_KEUANGANPAJAK,
              label=u'Buku Kas Pembantu Pajak', name=u'pajak', parent=self,
              pos=wx.Point(88, 256), size=wx.Size(264, 30), style=0)

        self.bankdesa = wx.Button(id=wxID_KEUANGANBANKDESA,
              label=u'Buku Bank Desa', name=u'bankdesa', parent=self,
              pos=wx.Point(88, 296), size=wx.Size(264, 30), style=0)

        self.realisasipertama = wx.Button(id=wxID_KEUANGANREALISASIPERTAMA,
              label=u'Laporan Realisasi Semester Pertama',
              name=u'realisasipertama', parent=self, pos=wx.Point(88, 336),
              size=wx.Size(264, 30), style=0)

        self.realisasiakhir = wx.Button(id=wxID_KEUANGANREALISASIAKHIR,
              label=u'Laporan Realisasi Semester Akhir', name=u'realisasiakhir',
              parent=self, pos=wx.Point(88, 376), size=wx.Size(264, 30),
              style=0)

        self.lapabdesa = wx.Button(id=wxID_KEUANGANLAPABDESA,
              label=u'Laporan APB Desa', name=u'lapabdesa', parent=self,
              pos=wx.Point(88, 416), size=wx.Size(264, 30), style=0)

        self.button1 = wx.Button(id=wxID_KEUANGANBUTTON1,
              label=u'Laporan Kekayaan Milik Desa', name='button1', parent=self,
              pos=wx.Point(88, 456), size=wx.Size(264, 30), style=0)

        self.sektoral = wx.Button(id=wxID_KEUANGANSEKTORAL,
              label=u'Program Sektoral', name=u'sektoral', parent=self,
              pos=wx.Point(88, 496), size=wx.Size(264, 30), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_KEUANGANSTATICBOX1,
              label=u'Menu', name='staticBox1', parent=self, pos=wx.Point(16,
              0), size=wx.Size(392, 536), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnApbdesaButton(self, event):
        self.main=penyusunan.create(None)
        self.main.Show()
        