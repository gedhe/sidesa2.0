#Boa:Frame:potensi_tambak

import wx
import wx.richtext
import sqlite3


db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return potensi_tambak(parent)

[wxID_POTENSI_TAMBAK, wxID_POTENSI_TAMBAKEDIT, wxID_POTENSI_TAMBAKHAPUS, 
 wxID_POTENSI_TAMBAKINPUT_JUMLAH, wxID_POTENSI_TAMBAKINPUT_PEMILIK, 
 wxID_POTENSI_TAMBAKINPUT_TAMBAK, wxID_POTENSI_TAMBAKKEMBALI, 
 wxID_POTENSI_TAMBAKNO, wxID_POTENSI_TAMBAKRICHTEXTCTRL1, 
 wxID_POTENSI_TAMBAKSTATICTEXT1, wxID_POTENSI_TAMBAKSTATICTEXT2, 
 wxID_POTENSI_TAMBAKSTATICTEXT3, wxID_POTENSI_TAMBAKSTATICTEXT4, 
 wxID_POTENSI_TAMBAKTAMBAH, wxID_POTENSI_TAMBAKTAMBAK, 
] = [wx.NewId() for _init_ctrls in range(15)]

class potensi_tambak(wx.Frame):
    def _init_coll_tambak_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='No',
              width=30)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Potensi', width=150)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Jumlah/Luas', width=150)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Pemilik', width=175)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT,
              heading='Keterangan', width=260)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_POTENSI_TAMBAK, name=u'potensi_tambak',
              parent=prnt, pos=wx.Point(471, 194), size=wx.Size(784, 445),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Potensi Pertambakan / Kolam Ikan')
        self.SetClientSize(wx.Size(784, 445))
        self.Center(wx.BOTH)

        self.tambak = wx.ListCtrl(id=wxID_POTENSI_TAMBAKTAMBAK, name=u'tambak',
              parent=self, pos=wx.Point(8, 8), size=wx.Size(768, 208),
              style=wx.LC_REPORT)
        self._init_coll_tambak_Columns(self.tambak)
        self.tambak.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnTambakListItemSelected, id=wxID_POTENSI_TAMBAKTAMBAK)

        self.staticText1 = wx.StaticText(id=wxID_POTENSI_TAMBAKSTATICTEXT1,
              label=u'Nama Tambak', name='staticText1', parent=self,
              pos=wx.Point(16, 240), size=wx.Size(151, 15), style=0)

        self.input_tambak = wx.ComboBox(choices=['Tambak Laut', 'Tambak Darat'],
              id=wxID_POTENSI_TAMBAKINPUT_TAMBAK, name=u'input_tambak',
              parent=self, pos=wx.Point(168, 240), size=wx.Size(240, 25),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_POTENSI_TAMBAKSTATICTEXT2,
              label=u'Jumlah / Luas', name='staticText2', parent=self,
              pos=wx.Point(16, 272), size=wx.Size(86, 15), style=0)

        self.staticText3 = wx.StaticText(id=wxID_POTENSI_TAMBAKSTATICTEXT3,
              label=u'Pemilik', name='staticText3', parent=self,
              pos=wx.Point(424, 240), size=wx.Size(63, 15), style=0)

        self.staticText4 = wx.StaticText(id=wxID_POTENSI_TAMBAKSTATICTEXT4,
              label=u'Keterangan', name='staticText4', parent=self,
              pos=wx.Point(424, 272), size=wx.Size(74, 15), style=0)

        self.input_jumlah = wx.TextCtrl(id=wxID_POTENSI_TAMBAKINPUT_JUMLAH,
              name=u'input_jumlah', parent=self, pos=wx.Point(168, 272),
              size=wx.Size(80, 25), style=0, value='')

        self.no = wx.TextCtrl(id=wxID_POTENSI_TAMBAKNO, name=u'no', parent=self,
              pos=wx.Point(-100, -100), size=wx.Size(80, 25), style=0,
              value='')

        self.input_pemilik = wx.TextCtrl(id=wxID_POTENSI_TAMBAKINPUT_PEMILIK,
              name=u'input_pemilik', parent=self, pos=wx.Point(528, 240),
              size=wx.Size(248, 25), style=0, value='')

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_POTENSI_TAMBAKRICHTEXTCTRL1,
              parent=self, pos=wx.Point(528, 272), size=wx.Size(248, 112),
              style=wx.richtext.RE_MULTILINE, value='')

        self.tambah = wx.Button(id=wxID_POTENSI_TAMBAKTAMBAH, label=u'Tambah',
              name=u'tambah', parent=self, pos=wx.Point(160, 400),
              size=wx.Size(128, 30), style=0)
        self.tambah.Bind(wx.EVT_BUTTON, self.OnTambahButton,
              id=wxID_POTENSI_TAMBAKTAMBAH)

        self.edit = wx.Button(id=wxID_POTENSI_TAMBAKEDIT, label=u'Edit',
              name=u'edit', parent=self, pos=wx.Point(296, 400),
              size=wx.Size(112, 30), style=0)
        self.edit.Bind(wx.EVT_BUTTON, self.OnEditButton,
              id=wxID_POTENSI_TAMBAKEDIT)

        self.hapus = wx.Button(id=wxID_POTENSI_TAMBAKHAPUS, label=u'Hapus',
              name=u'hapus', parent=self, pos=wx.Point(416, 400),
              size=wx.Size(112, 30), style=0)
        self.hapus.Bind(wx.EVT_BUTTON, self.OnHapusButton,
              id=wxID_POTENSI_TAMBAKHAPUS)

        self.kembali = wx.Button(id=wxID_POTENSI_TAMBAKKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(536, 400), size=wx.Size(136, 30), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_POTENSI_TAMBAKKEMBALI)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.IsiList()

    def IsiList(self):    
        self.tambak.DeleteAllItems()
        sql = "SELECT * FROM potensitambak"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        pottambak = self.tambak.GetItemCount() 
        for i in hasil : 
            self.tambak.InsertStringItem(pottambak, "%s"%i[0]) 
            self.tambak.SetStringItem(pottambak,1,"%s"%i[1]) 
            self.tambak.SetStringItem(pottambak,2,"%s"%i[2])
            self.tambak.SetStringItem(pottambak,3,"%s"%i[3]) 
            self.tambak.SetStringItem(pottambak,4,"%s"%i[4]) 
            pottambak = pottambak + 1 
    
    def IsiObject(self) : 
        caritambak=str(self.no.GetValue())
        sql="SELECT * FROM potensitambak WHERE no='%s'"%(caritambak)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.no.SetValue(str(hasil[0]))
            self.input_tambak.SetValue(str(hasil[1]))
            self.input_jumlah.SetValue(str(hasil[2]))
            self.input_pemilik.SetValue(str(hasil[3]))
            self.richTextCtrl1.SetValue(str(hasil[4]))
        else : 
            self.pesan = wx.MessageDialog(self,"Data Potensi Tambak Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.no.Clear()
            self.no.SetFocus()   
                
    def OnTambahButton(self, event):
        no = str(self.no.GetValue())
        inputtambak = str(self.input_tambak.GetValue())
        inputjumlah = str(self.input_jumlah.GetValue())
        inputpemilik = str(self.input_pemilik.GetValue())
        inputketerangan = str(self.richTextCtrl1.GetValue())
        add_tambak="INSERT INTO potensitambak (namapotensi, jumlah, pemilik, keterangan) VALUES('"+(inputtambak)+"', '"+(inputjumlah)+"', '"+(inputpemilik)+"', '"+(inputketerangan)+"')"
        cur.execute(add_tambak)
        db.commit()
        self.input_tambak.SetValue('')
        self.input_jumlah.Clear()
        self.input_pemilik.Clear()
        self.richTextCtrl1.Clear()
        self.pesan = wx.MessageDialog(self,"Data Baru Tambak Disimpan","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        
        

    def OnEditButton(self, event):
        no = str(self.no.GetValue())
        inputtambak = str(self.input_tambak.GetValue())
        inputjumlah = str(self.input_jumlah.GetValue())
        inputpemilik = str(self.input_pemilik.GetValue())
        inputketerangan = str(self.richTextCtrl1.GetValue())
        sql = "UPDATE potensitambak SET namapotensi = '"+inputtambak+"', jumlah = '"+inputjumlah+"', pemilik = '"+inputpemilik+"', keterangan = '"+inputketerangan+"'   WHERE no = '"+no+"'"
        cur.execute(sql)
        db.commit()
        self.input_tambak.SetValue('')
        self.input_jumlah.Clear()
        self.input_pemilik.Clear()
        self.richTextCtrl1.Clear()
        self.pesan = wx.MessageDialog(self,"Data Baru Tambak Disimpan","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        

    def OnHapusButton(self, event):
        self.pesan = wx.MessageDialog(self,"Yakin Akan Dihapus","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()
        no = str(self.no.GetValue())
        inputtambak = str(self.input_tambak.GetValue())
        inputjumlah = str(self.input_jumlah.GetValue())
        inputpemilik = str(self.input_pemilik.GetValue())
        inputketerangan = str(self.richTextCtrl1.GetValue())
        sql = "DELETE FROM potensitambak   WHERE no = '"+no+"'"
        cur.execute(sql)
        db.commit()
        self.input_tambak.SetValue('')
        self.input_jumlah.Clear()
        self.input_pemilik.Clear()
        self.richTextCtrl1.Clear()
        self.pesan = wx.MessageDialog(self,"Data Baru Tambak Dihapus","Konfirmasi",wx.OK) 
        self.pesan.ShowModal()

    def OnKembaliButton(self, event):
        self.Close()
        self.Destroy()

    def OnTambakListItemSelected(self, event):
        self.currentItem = event.m_itemIndex # mengambil no index baris yang dipilih 
        b=self.tambak.GetItem(self.currentItem).GetText() # no index baris dikonversi ke text/ string 
        self.no.SetValue(b) 
        self.IsiObject() 
        event.Skip()    
