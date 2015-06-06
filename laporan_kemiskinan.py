#Boa:Frame:laporan_kemiskinan

import wx
import wx.lib.buttons
import sqlite3

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return laporan_kemiskinan(parent)

[wxID_LAPORAN_KEMISKINAN, wxID_LAPORAN_KEMISKINANBLSM, 
 wxID_LAPORAN_KEMISKINANBSM, wxID_LAPORAN_KEMISKINANBUTTON10, 
 wxID_LAPORAN_KEMISKINANBUTTON11, wxID_LAPORAN_KEMISKINANBUTTON12, 
 wxID_LAPORAN_KEMISKINANBUTTON2, wxID_LAPORAN_KEMISKINANBUTTON3, 
 wxID_LAPORAN_KEMISKINANBUTTON4, wxID_LAPORAN_KEMISKINANBUTTON5, 
 wxID_LAPORAN_KEMISKINANBUTTON6, wxID_LAPORAN_KEMISKINANBUTTON7, 
 wxID_LAPORAN_KEMISKINANBUTTON8, wxID_LAPORAN_KEMISKINANBUTTON9, 
 wxID_LAPORAN_KEMISKINANISIPENDUDUK, wxID_LAPORAN_KEMISKINANJKN, 
 wxID_LAPORAN_KEMISKINANKKMISKIN, wxID_LAPORAN_KEMISKINANKKTDKMISKIN, 
 wxID_LAPORAN_KEMISKINANMISKIN, wxID_LAPORAN_KEMISKINANPKH, 
 wxID_LAPORAN_KEMISKINANPROGKESDAERAH, wxID_LAPORAN_KEMISKINANPROGLAIN, 
 wxID_LAPORAN_KEMISKINANPROGPENDAERAH, wxID_LAPORAN_KEMISKINANRASKIN, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT1, wxID_LAPORAN_KEMISKINANSTATICTEXT10, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT11, wxID_LAPORAN_KEMISKINANSTATICTEXT12, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT13, wxID_LAPORAN_KEMISKINANSTATICTEXT14, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT15, wxID_LAPORAN_KEMISKINANSTATICTEXT16, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT17, wxID_LAPORAN_KEMISKINANSTATICTEXT18, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT19, wxID_LAPORAN_KEMISKINANSTATICTEXT2, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT20, wxID_LAPORAN_KEMISKINANSTATICTEXT21, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT22, wxID_LAPORAN_KEMISKINANSTATICTEXT23, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT3, wxID_LAPORAN_KEMISKINANSTATICTEXT4, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT5, wxID_LAPORAN_KEMISKINANSTATICTEXT6, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT7, wxID_LAPORAN_KEMISKINANSTATICTEXT8, 
 wxID_LAPORAN_KEMISKINANSTATICTEXT9, wxID_LAPORAN_KEMISKINANTIDAKMISKIN, 
 wxID_LAPORAN_KEMISKINANTOMBOLKKMISKIN, 
 wxID_LAPORAN_KEMISKINANTOMBOLKKTIDAKMISKIN, 
] = [wx.NewId() for _init_ctrls in range(50)]

class laporan_kemiskinan(wx.Frame):
    def _init_coll_isipenduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor NIK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Lengkap', width=250)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=260)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Status Kemiskinan', width=100)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LAPORAN_KEMISKINAN,
              name=u'laporan_kemiskinan', parent=prnt, pos=wx.Point(396, 134),
              size=wx.Size(911, 545), style=wx.FRAME_NO_TASKBAR,
              title=u'Sistem Laporan Data Kemiskinan')
        self.SetClientSize(wx.Size(911, 545))
        self.Center(wx.BOTH)

        self.isipenduduk = wx.ListCtrl(id=wxID_LAPORAN_KEMISKINANISIPENDUDUK,
              name=u'isipenduduk', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(896, 256), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)
        self.isipenduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected,
              id=wxID_LAPORAN_KEMISKINANISIPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT1,
              label=u'Jumlah Keluarga Miskin ', name='staticText1', parent=self,
              pos=wx.Point(8, 280), size=wx.Size(150, 15), style=0)

        self.staticText2 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT2,
              label=u'Jumlah Keluarga Tidak Miskin', name='staticText2',
              parent=self, pos=wx.Point(8, 312), size=wx.Size(183, 15),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT3,
              label=u'Program Perlindungan Sosial', name='staticText3',
              parent=self, pos=wx.Point(8, 344), size=wx.Size(185, 15),
              style=0)

        self.miskin = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANMISKIN,
              name=u'miskin', parent=self, pos=wx.Point(296, 280),
              size=wx.Size(80, 25), style=0, value='')

        self.tidakmiskin = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANTIDAKMISKIN,
              name=u'tidakmiskin', parent=self, pos=wx.Point(296, 312),
              size=wx.Size(80, 25), style=0, value='')

        self.raskin = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANRASKIN,
              name=u'raskin', parent=self, pos=wx.Point(136, 368),
              size=wx.Size(80, 25), style=0, value='')

        self.jkn = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANJKN, name=u'jkn',
              parent=self, pos=wx.Point(136, 400), size=wx.Size(80, 25),
              style=0, value='')

        self.blsm = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANBLSM, name=u'blsm',
              parent=self, pos=wx.Point(136, 432), size=wx.Size(80, 25),
              style=0, value='')

        self.bsm = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANBSM, name=u'bsm',
              parent=self, pos=wx.Point(136, 464), size=wx.Size(80, 25),
              style=0, value='')

        self.pkh = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANPKH, name=u'pkh',
              parent=self, pos=wx.Point(600, 368), size=wx.Size(80, 25),
              style=0, value='')

        self.progkesdaerah = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANPROGKESDAERAH,
              name=u'progkesdaerah', parent=self, pos=wx.Point(600, 400),
              size=wx.Size(80, 25), style=0, value='')

        self.progpendaerah = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANPROGPENDAERAH,
              name=u'progpendaerah', parent=self, pos=wx.Point(600, 432),
              size=wx.Size(80, 25), style=0, value='')

        self.proglain = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANPROGLAIN,
              name=u'proglain', parent=self, pos=wx.Point(600, 464),
              size=wx.Size(80, 25), style=0, value='')

        self.staticText4 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT4,
              label=u'1.  Raskin', name='staticText4', parent=self,
              pos=wx.Point(8, 368), size=wx.Size(62, 15), style=0)

        self.staticText5 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT5,
              label=u'2.  JKN', name='staticText5', parent=self, pos=wx.Point(8,
              400), size=wx.Size(42, 15), style=0)

        self.staticText6 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT6,
              label=u'3.  BLSM', name='staticText6', parent=self,
              pos=wx.Point(8, 432), size=wx.Size(57, 15), style=0)

        self.staticText7 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT7,
              label=u'4.  BSM', name='staticText7', parent=self, pos=wx.Point(8,
              464), size=wx.Size(50, 15), style=0)

        self.staticText8 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT8,
              label=u'5.  PKH', name='staticText8', parent=self,
              pos=wx.Point(432, 368), size=wx.Size(47, 15), style=0)

        self.staticText9 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT9,
              label=u'6.  Prog Kes Daerah', name='staticText9', parent=self,
              pos=wx.Point(432, 400), size=wx.Size(127, 15), style=0)

        self.staticText10 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT10,
              label=u'7. Prog Pend Daerah', name='staticText10', parent=self,
              pos=wx.Point(432, 432), size=wx.Size(133, 15), style=0)

        self.staticText11 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT11,
              label=u'8.  Program Lain', name='staticText11', parent=self,
              pos=wx.Point(432, 464), size=wx.Size(106, 15), style=0)

        self.button2 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON2,
              label=u'Kembali Ke Menu', name='button2', parent=self,
              pos=wx.Point(368, 504), size=wx.Size(200, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON2)

        self.button5 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON5,
              label=u'Lihat Laporan', name='button5', parent=self,
              pos=wx.Point(424, 312), size=wx.Size(115, 24), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON5)

        self.button3 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON3,
              label=u'Lihat Laporan', name='button3', parent=self,
              pos=wx.Point(280, 368), size=wx.Size(115, 24), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON3)

        self.button4 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON4,
              label=u'Lihat Laporan', name='button4', parent=self,
              pos=wx.Point(280, 400), size=wx.Size(115, 24), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON4)

        self.button6 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON6,
              label=u'Lihat Laporan', name='button6', parent=self,
              pos=wx.Point(280, 432), size=wx.Size(115, 24), style=0)
        self.button6.Bind(wx.EVT_BUTTON, self.OnButton6Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON6)

        self.button7 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON7,
              label=u'Lihat Laporan', name='button7', parent=self,
              pos=wx.Point(280, 464), size=wx.Size(115, 24), style=0)
        self.button7.Bind(wx.EVT_BUTTON, self.OnButton7Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON7)

        self.button8 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON8,
              label=u'Lihat Laporan', name='button8', parent=self,
              pos=wx.Point(736, 368), size=wx.Size(115, 24), style=0)
        self.button8.Bind(wx.EVT_BUTTON, self.OnButton8Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON8)

        self.button9 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON9,
              label=u'Lihat Laporan', name='button9', parent=self,
              pos=wx.Point(736, 400), size=wx.Size(115, 24), style=0)
        self.button9.Bind(wx.EVT_BUTTON, self.OnButton9Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON9)

        self.button10 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON10,
              label=u'Lihat Laporan', name='button10', parent=self,
              pos=wx.Point(736, 432), size=wx.Size(115, 24), style=0)
        self.button10.Bind(wx.EVT_BUTTON, self.OnButton10Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON10)

        self.button11 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON11,
              label=u'Lihat Laporan', name='button11', parent=self,
              pos=wx.Point(736, 464), size=wx.Size(115, 24), style=0)
        self.button11.Bind(wx.EVT_BUTTON, self.OnButton11Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON11)

        self.button12 = wx.Button(id=wxID_LAPORAN_KEMISKINANBUTTON12,
              label=u'Lihat Laporan', name='button12', parent=self,
              pos=wx.Point(424, 280), size=wx.Size(115, 24), style=0)
        self.button12.Bind(wx.EVT_BUTTON, self.OnButton12Button,
              id=wxID_LAPORAN_KEMISKINANBUTTON12)

        self.staticText12 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT12,
              label=u'Jiwa', name='staticText12', parent=self, pos=wx.Point(384,
              320), size=wx.Size(25, 17), style=0)

        self.staticText13 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT13,
              label=u'Jiwa', name='staticText13', parent=self, pos=wx.Point(224,
              376), size=wx.Size(25, 17), style=0)

        self.staticText14 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT14,
              label=u'Jiwa', name='staticText14', parent=self, pos=wx.Point(224,
              408), size=wx.Size(25, 17), style=0)

        self.staticText15 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT15,
              label=u'Jiwa', name='staticText15', parent=self, pos=wx.Point(224,
              440), size=wx.Size(25, 17), style=0)

        self.staticText16 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT16,
              label=u'Jiwa', name='staticText16', parent=self, pos=wx.Point(224,
              472), size=wx.Size(25, 17), style=0)

        self.staticText17 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT17,
              label=u'Jiwa', name='staticText17', parent=self, pos=wx.Point(688,
              376), size=wx.Size(25, 17), style=0)

        self.staticText18 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT18,
              label=u'Jiwa', name='staticText18', parent=self, pos=wx.Point(688,
              408), size=wx.Size(25, 17), style=0)

        self.staticText19 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT19,
              label=u'Jiwa', name='staticText19', parent=self, pos=wx.Point(688,
              440), size=wx.Size(25, 17), style=0)

        self.staticText20 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT20,
              label=u'Jiwa', name='staticText20', parent=self, pos=wx.Point(688,
              472), size=wx.Size(25, 17), style=0)

        self.staticText21 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT21,
              label=u'Jiwa', name='staticText21', parent=self, pos=wx.Point(384,
              288), size=wx.Size(25, 17), style=0)

        self.kkmiskin = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANKKMISKIN,
              name=u'kkmiskin', parent=self, pos=wx.Point(584, 280),
              size=wx.Size(80, 27), style=0, value=u'')

        self.kktdkmiskin = wx.TextCtrl(id=wxID_LAPORAN_KEMISKINANKKTDKMISKIN,
              name=u'kktdkmiskin', parent=self, pos=wx.Point(584, 312),
              size=wx.Size(80, 27), style=0, value=u'')

        self.staticText22 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT22,
              label=u'KK', name='staticText22', parent=self, pos=wx.Point(672,
              288), size=wx.Size(17, 17), style=0)

        self.staticText23 = wx.StaticText(id=wxID_LAPORAN_KEMISKINANSTATICTEXT23,
              label=u'KK', name='staticText23', parent=self, pos=wx.Point(672,
              320), size=wx.Size(17, 17), style=0)

        self.tombolkktidakmiskin = wx.Button(id=wxID_LAPORAN_KEMISKINANTOMBOLKKTIDAKMISKIN,
              label=u'Lihat Laporan KK', name=u'tombolkktidakmiskin',
              parent=self, pos=wx.Point(696, 312), size=wx.Size(144, 24),
              style=0)
        self.tombolkktidakmiskin.Bind(wx.EVT_BUTTON,
              self.OnTombolkktidakmiskinButton,
              id=wxID_LAPORAN_KEMISKINANTOMBOLKKTIDAKMISKIN)

        self.tombolkkmiskin = wx.Button(id=wxID_LAPORAN_KEMISKINANTOMBOLKKMISKIN,
              label=u'Lihat Laporan KK', name=u'tombolkkmiskin', parent=self,
              pos=wx.Point(696, 280), size=wx.Size(144, 24), style=0)
        self.tombolkkmiskin.Bind(wx.EVT_BUTTON, self.OnTombolkkmiskinButton,
              id=wxID_LAPORAN_KEMISKINANTOMBOLKKMISKIN)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton2Button(self, event):
        self.Close()

    
    def lihatmiskin(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE kemiskinan='Miskin' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1
    
    def lihattidakmiskin(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE kemiskinan='Tidak Miskin' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1
    
    def lihatmiskin1(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE kemiskinan='Miskin' AND kematian='Tidak' AND shdk='Kepala Keluarga'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1
    
    def lihatmiskin2(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE kemiskinan='Tidak Miskin' AND kematian='Tidak' AND shdk='Kepala Keluarga'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1
    
    
    def promis1(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE promis1='RASKIN' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1
    
    def promis2(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE promis2='JKN' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1              
            
    def promis3(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE promis3='BLSM' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1                
    
    def promis4(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE promis4='BSM' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1              

    def promis5(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE promis5='PKH' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1                

    def promis6(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE promis6='Prog. Kesehatan Daerah' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1               
            
    def promis7(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE promis7='Prog. Pendidikan Daerah' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1   
    
    def promis8(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE promis8='Prog. Lain' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1           

    def OnButton12Button(self, event):
        self.lihatmiskin()
        sql = "SELECT COUNT(*) FROM penduduk WHERE kemiskinan='Miskin' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.miskin.SetValue(str(hasil))
        event.Skip()
    
    def OnButton3Button(self, event):
        self.promis1()
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis1='RASKIN' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.raskin.SetValue(str(hasil))
        event.Skip()

    def OnButton4Button(self, event):
        self.promis2()
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis2='JKN' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.jkn.SetValue(str(hasil))
        event.Skip()

    def OnButton6Button(self, event):
        self.promis3()
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis3='BLSM' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.blsm.SetValue(str(hasil))
        event.Skip()

    def OnButton7Button(self, event):
        self.promis4()
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis4='BSM' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.bsm.SetValue(str(hasil))

        event.Skip()

    def OnButton8Button(self, event):
        self.promis5()
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis5='PKH' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.pkh.SetValue(str(hasil))

        event.Skip()

    def OnButton9Button(self, event):
        self.promis6()
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis6='Prog. Kesehatan Daerah' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.progkesdaerah.SetValue(str(hasil))

        event.Skip()

    def OnButton10Button(self, event):
        self.promis7()
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis7='Prog. Pendidikan Daerah' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.progpendaerah.SetValue(str(hasil))

        event.Skip()

    def OnButton11Button(self, event):
        self.promis8()
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis8='Prog. Lain' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.proglain.SetValue(str(hasil))

        event.Skip()
        
    def OnIsipendudukListItemSelected(self, event):
        
        event.Skip()  

    def OnButton5Button(self, event):
        self.lihattidakmiskin()
        sql = "SELECT COUNT(*) FROM penduduk WHERE kemiskinan='Tidak Miskin' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.tidakmiskin.SetValue(str(hasil))
        event.Skip()

    def OnTombolkktidakmiskinButton(self, event):
        self.lihatmiskin2()
        sql = "SELECT COUNT(*) FROM penduduk WHERE kemiskinan='Tidak Miskin' AND kematian='Tidak' AND shdk='Kepala Keluarga'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.kktdkmiskin.SetValue(str(hasil))
        event.Skip()
        

    def OnTombolkkmiskinButton(self, event):
        self.lihatmiskin1()
        sql = "SELECT COUNT(*) FROM penduduk WHERE kemiskinan='Miskin' AND kematian='Tidak' AND shdk='Kepala Keluarga'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.kkmiskin.SetValue(str(hasil))
        event.Skip()
            
                



