#Boa:Frame:cari_kemiskinan

import wx
import wx.lib.buttons
import frm_sideka_menu
import sqlite3

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return cari_kemiskinan(parent)

[wxID_CARI_KEMISKINAN, wxID_CARI_KEMISKINANBUTTON1, 
 wxID_CARI_KEMISKINANBUTTON3, wxID_CARI_KEMISKINANCARI_KK, 
 wxID_CARI_KEMISKINANINPUT_ALAMAT, wxID_CARI_KEMISKINANISIPENDUDUK, 
 wxID_CARI_KEMISKINANNAMA_KK, wxID_CARI_KEMISKINANNOMOR_KK, 
 wxID_CARI_KEMISKINANPROG1, wxID_CARI_KEMISKINANPROG2, 
 wxID_CARI_KEMISKINANPROG3, wxID_CARI_KEMISKINANPROG4, 
 wxID_CARI_KEMISKINANPROG5, wxID_CARI_KEMISKINANPROG6, 
 wxID_CARI_KEMISKINANPROG7, wxID_CARI_KEMISKINANPROG8, 
 wxID_CARI_KEMISKINANSTATICTEXT1, wxID_CARI_KEMISKINANSTATICTEXT10, 
 wxID_CARI_KEMISKINANSTATICTEXT11, wxID_CARI_KEMISKINANSTATICTEXT12, 
 wxID_CARI_KEMISKINANSTATICTEXT13, wxID_CARI_KEMISKINANSTATICTEXT14, 
 wxID_CARI_KEMISKINANSTATICTEXT2, wxID_CARI_KEMISKINANSTATICTEXT3, 
 wxID_CARI_KEMISKINANSTATICTEXT4, wxID_CARI_KEMISKINANSTATICTEXT5, 
 wxID_CARI_KEMISKINANSTATICTEXT6, wxID_CARI_KEMISKINANSTATICTEXT7, 
 wxID_CARI_KEMISKINANSTATICTEXT8, wxID_CARI_KEMISKINANSTATICTEXT9, 
 wxID_CARI_KEMISKINANSTATUS_MISKIN, 
] = [wx.NewId() for _init_ctrls in range(31)]

class cari_kemiskinan(wx.Dialog):
    
    def _init_coll_isipenduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor NIK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Penduduk', width=250)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=260)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Status Kemiskinan', width=100)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_CARI_KEMISKINAN,
              name=u'cari_kemiskinan', parent=prnt, pos=wx.Point(428, 180),
              size=wx.Size(843, 453), style=wx.FRAME_NO_TASKBAR,
              title=u'Cari Data Kemiskinan')
        self.SetClientSize(wx.Size(843, 453))
        self.Center(wx.BOTH)

        self.isipenduduk = wx.ListCtrl(id=wxID_CARI_KEMISKINANISIPENDUDUK,
              name=u'penduduk', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(808, 184), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)
        self.isipenduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected,
              id=wxID_CARI_KEMISKINANISIPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT1,
              label=u'Nomor Induk Kependudukan', name='staticText1',
              parent=self, pos=wx.Point(376, 200), size=wx.Size(178, 17),
              style=0)

        self.cari_kk = wx.TextCtrl(id=wxID_CARI_KEMISKINANCARI_KK,
              name=u'cari_kk', parent=self, pos=wx.Point(560, 200),
              size=wx.Size(168, 25), style=0, value='')

        self.button1 = wx.Button(id=wxID_CARI_KEMISKINANBUTTON1, label=u'Cari',
              name='button1', parent=self, pos=wx.Point(744, 200),
              size=wx.Size(80, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_CARI_KEMISKINANBUTTON1)

        self.staticText2 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT2,
              label=u'Nomor KK', name='staticText2', parent=self,
              pos=wx.Point(16, 240), size=wx.Size(65, 15), style=0)

        self.nomor_kk = wx.TextCtrl(id=wxID_CARI_KEMISKINANNOMOR_KK,
              name=u'nomor_kk', parent=self, pos=wx.Point(96, 232),
              size=wx.Size(312, 25), style=wx.TE_READONLY, value='')

        self.staticText3 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT3,
              label=u'Alamat', name='staticText3', parent=self,
              pos=wx.Point(416, 232), size=wx.Size(47, 15), style=0)

        self.input_alamat = wx.TextCtrl(id=wxID_CARI_KEMISKINANINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(472, 232),
              size=wx.Size(352, 25), style=wx.TE_READONLY, value=u'')

        self.staticText4 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT4,
              label=u'Nama', name='staticText4', parent=self, pos=wx.Point(16,
              264), size=wx.Size(102, 17), style=0)

        self.nama_kk = wx.TextCtrl(id=wxID_CARI_KEMISKINANNAMA_KK,
              name=u'nama_kk', parent=self, pos=wx.Point(96, 264),
              size=wx.Size(312, 25), style=wx.TE_READONLY, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT5,
              label=u'Status Kemiskinan', name='staticText5', parent=self,
              pos=wx.Point(416, 264), size=wx.Size(119, 15), style=0)

        self.status_miskin = wx.TextCtrl(id=wxID_CARI_KEMISKINANSTATUS_MISKIN,
              name=u'status_miskin', parent=self, pos=wx.Point(552, 264),
              size=wx.Size(272, 25), style=wx.TE_READONLY, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT6,
              label=u'Program Perlindungan Sosial', name='staticText6',
              parent=self, pos=wx.Point(16, 296), size=wx.Size(185, 15),
              style=0)

        self.button3 = wx.Button(id=wxID_CARI_KEMISKINANBUTTON3,
              label=u'Kembali Ke Menu', name='button3', parent=self,
              pos=wx.Point(312, 400), size=wx.Size(184, 30), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_CARI_KEMISKINANBUTTON3)

        self.prog1 = wx.TextCtrl(id=wxID_CARI_KEMISKINANPROG1, name=u'prog1',
              parent=self, pos=wx.Point(24, 320), size=wx.Size(187, 27),
              style=wx.TE_READONLY, value=u'')

        self.prog2 = wx.TextCtrl(id=wxID_CARI_KEMISKINANPROG2, name=u'prog2',
              parent=self, pos=wx.Point(24, 360), size=wx.Size(187, 27),
              style=wx.TE_READONLY, value=u'')

        self.prog3 = wx.TextCtrl(id=wxID_CARI_KEMISKINANPROG3, name=u'prog3',
              parent=self, pos=wx.Point(232, 320), size=wx.Size(187, 27),
              style=wx.TE_READONLY, value=u'')

        self.prog4 = wx.TextCtrl(id=wxID_CARI_KEMISKINANPROG4, name=u'prog4',
              parent=self, pos=wx.Point(232, 360), size=wx.Size(187, 27),
              style=wx.TE_READONLY, value=u'')

        self.prog5 = wx.TextCtrl(id=wxID_CARI_KEMISKINANPROG5, name=u'prog5',
              parent=self, pos=wx.Point(440, 320), size=wx.Size(187, 27),
              style=wx.TE_READONLY, value=u'')

        self.prog6 = wx.TextCtrl(id=wxID_CARI_KEMISKINANPROG6, name=u'prog6',
              parent=self, pos=wx.Point(440, 360), size=wx.Size(187, 27),
              style=wx.TE_READONLY, value=u'')

        self.prog7 = wx.TextCtrl(id=wxID_CARI_KEMISKINANPROG7, name=u'prog7',
              parent=self, pos=wx.Point(648, 320), size=wx.Size(187, 27),
              style=wx.TE_READONLY, value=u'')

        self.staticText7 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT7,
              label=u'1', name='staticText7', parent=self, pos=wx.Point(8, 328),
              size=wx.Size(9, 17), style=0)

        self.staticText8 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT8,
              label=u'2', name='staticText8', parent=self, pos=wx.Point(8, 368),
              size=wx.Size(9, 17), style=0)

        self.staticText9 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT9,
              label=u'3', name='staticText9', parent=self, pos=wx.Point(216,
              328), size=wx.Size(9, 17), style=0)

        self.staticText10 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT10,
              label=u'4', name='staticText10', parent=self, pos=wx.Point(216,
              368), size=wx.Size(9, 17), style=0)

        self.staticText11 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT11,
              label=u'5', name='staticText11', parent=self, pos=wx.Point(424,
              328), size=wx.Size(9, 17), style=0)

        self.staticText12 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT12,
              label=u'6', name='staticText12', parent=self, pos=wx.Point(424,
              368), size=wx.Size(9, 17), style=0)

        self.staticText13 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT13,
              label=u'7', name='staticText13', parent=self, pos=wx.Point(632,
              328), size=wx.Size(9, 17), style=0)

        self.staticText14 = wx.StaticText(id=wxID_CARI_KEMISKINANSTATICTEXT14,
              label=u'8', name='staticText14', parent=self, pos=wx.Point(632,
              368), size=wx.Size(9, 17), style=0)

        self.prog8 = wx.TextCtrl(id=wxID_CARI_KEMISKINANPROG8, name=u'prog8',
              parent=self, pos=wx.Point(648, 360), size=wx.Size(187, 27),
              style=wx.TE_READONLY, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.awal()
    
    def awal(self):
        self.IsiList()
        self.cari_kk.SetValue('')
        self.nama_kk.SetValue('')
        self.input_alamat.SetValue('')
        self.status_miskin.SetValue('')
        self.nomor_kk.SetValue('')
        self.prog1.SetValue('')
        self.prog2.SetValue('')
        self.prog3.SetValue('')
        self.prog4.SetValue('')
        self.prog5.SetValue('')
        self.prog6.SetValue('')
        self.prog7.SetValue('')
        self.prog8.SetValue('')    
        
    def IsiList(self): 
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1
    
    def Isi_Object(self) : 
        carikk=str(self.cari_kk.GetValue())
        sql="SELECT * FROM penduduk WHERE nik='%s'"%(carikk)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.nomor_kk.SetValue(str(hasil[16]))
            self.nama_kk.SetValue(str(hasil[2]))
            self.input_alamat.SetValue(str(hasil[21]))
            self.status_miskin.SetValue(str(hasil[30]))
            self.prog1.SetValue(str(hasil[49]))
            self.prog2.SetValue(str(hasil[50]))
            self.prog3.SetValue(str(hasil[51]))
            self.prog4.SetValue(str(hasil[52]))
            self.prog5.SetValue(str(hasil[53]))
            self.prog6.SetValue(str(hasil[54]))
            self.prog7.SetValue(str(hasil[55]))
            self.prog8.SetValue(str(hasil[56]))
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.cari_kk.Clear()
            self.cari_kk.SetFocus()
            
    def OnButton3Button(self, event):
        self.Close()
    
    def OnIsipendudukListItemSelected(self, event):
        self.currentItem = event.m_itemIndex # mengambil no index baris yang dipilih 
        b=self.isipenduduk.GetItem(self.currentItem).GetText() # no index baris dikonversi ke text/ string 
        self.cari_kk.SetValue(b) 
        self.Isi_Object()
        event.Skip()    

    def OnButton1Button(self, event):
        self.Isi_Object()

    
        
   
