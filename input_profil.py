#Boa:Frame:input_profil_desa

import wx
import sqlite3
import shutil
import os
import frm_sideka_menu

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()


def create(parent):
    return input_profil_desa(parent)

[wxID_INPUT_PROFIL_DESA, wxID_INPUT_PROFIL_DESAALAMAT, 
 wxID_INPUT_PROFIL_DESABUPATI, wxID_INPUT_PROFIL_DESABUTTON1, 
 wxID_INPUT_PROFIL_DESACAMAT, wxID_INPUT_PROFIL_DESADESA, 
 wxID_INPUT_PROFIL_DESADUSUN1, wxID_INPUT_PROFIL_DESADUSUN2, 
 wxID_INPUT_PROFIL_DESADUSUN3, wxID_INPUT_PROFIL_DESADUSUN4, 
 wxID_INPUT_PROFIL_DESADUSUN5, wxID_INPUT_PROFIL_DESADUSUN6, 
 wxID_INPUT_PROFIL_DESAEKBANG, wxID_INPUT_PROFIL_DESAKABUPATEN, 
 wxID_INPUT_PROFIL_DESAKADES, wxID_INPUT_PROFIL_DESAKECAMATAN, 
 wxID_INPUT_PROFIL_DESAKESRA, wxID_INPUT_PROFIL_DESAKEUANGAN, 
 wxID_INPUT_PROFIL_DESAKODE, wxID_INPUT_PROFIL_DESALABEL_ALAMAT, 
 wxID_INPUT_PROFIL_DESALABEL_DUKUH, wxID_INPUT_PROFIL_DESALABEL_KADES, 
 wxID_INPUT_PROFIL_DESALABEL_KECAMATAN, wxID_INPUT_PROFIL_DESALABEL_KODE_DESA, 
 wxID_INPUT_PROFIL_DESALABEL_NAMA_DESA, wxID_INPUT_PROFIL_DESALABEL_PROPINSI, 
 wxID_INPUT_PROFIL_DESALABEL_SEKDES, wxID_INPUT_PROFIL_DESALABEL_WEB, 
 wxID_INPUT_PROFIL_DESALABLE_KABUPATEN, wxID_INPUT_PROFIL_DESALOGOPEMDA, 
 wxID_INPUT_PROFIL_DESANAMAEMAIL, wxID_INPUT_PROFIL_DESANOTELP, 
 wxID_INPUT_PROFIL_DESAPEMERINTAHAN, wxID_INPUT_PROFIL_DESAPROPINSI, 
 wxID_INPUT_PROFIL_DESASEKDES, wxID_INPUT_PROFIL_DESASIMPANGAMBAR, 
 wxID_INPUT_PROFIL_DESASTATICTEXT1, wxID_INPUT_PROFIL_DESASTATICTEXT10, 
 wxID_INPUT_PROFIL_DESASTATICTEXT11, wxID_INPUT_PROFIL_DESASTATICTEXT12, 
 wxID_INPUT_PROFIL_DESASTATICTEXT13, wxID_INPUT_PROFIL_DESASTATICTEXT14, 
 wxID_INPUT_PROFIL_DESASTATICTEXT2, wxID_INPUT_PROFIL_DESASTATICTEXT3, 
 wxID_INPUT_PROFIL_DESASTATICTEXT4, wxID_INPUT_PROFIL_DESASTATICTEXT5, 
 wxID_INPUT_PROFIL_DESASTATICTEXT6, wxID_INPUT_PROFIL_DESASTATICTEXT7, 
 wxID_INPUT_PROFIL_DESASTATICTEXT8, wxID_INPUT_PROFIL_DESASTATICTEXT9, 
 wxID_INPUT_PROFIL_DESATELP, wxID_INPUT_PROFIL_DESATOMBOL_KEMBALI, 
 wxID_INPUT_PROFIL_DESATOMBOL_SIMPAN, wxID_INPUT_PROFIL_DESAUMUM, 
 wxID_INPUT_PROFIL_DESAWEB, 
] = [wx.NewId() for _init_ctrls in range(55)]

class input_profil_desa(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_INPUT_PROFIL_DESA,
              name=u'input_profil_desa', parent=prnt, pos=wx.Point(396, 189),
              size=wx.Size(911, 435), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Input Profil Desa')
        self.SetClientSize(wx.Size(911, 435))
        self.Center(wx.BOTH)

        self.label_nama_desa = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_NAMA_DESA,
              label=u'Nama Desa', name=u'label_nama_desa', parent=self,
              pos=wx.Point(192, 16), size=wx.Size(77, 17), style=0)

        self.label_kecamatan = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_KECAMATAN,
              label=u'Kecamatan', name=u'label_kecamatan', parent=self,
              pos=wx.Point(192, 48), size=wx.Size(73, 17), style=0)

        self.lable_kabupaten = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABLE_KABUPATEN,
              label=u'Kabupaten', name=u'lable_kabupaten', parent=self,
              pos=wx.Point(192, 80), size=wx.Size(70, 17), style=0)

        self.label_propinsi = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_PROPINSI,
              label=u'Propinsi', name=u'label_propinsi', parent=self,
              pos=wx.Point(192, 112), size=wx.Size(51, 17), style=0)

        self.desa = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESADESA, name=u'desa',
              parent=self, pos=wx.Point(280, 16), size=wx.Size(240, 24),
              style=0, value='')

        self.kabupaten = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(280, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.propinsi = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAPROPINSI,
              name=u'propinsi', parent=self, pos=wx.Point(280, 112),
              size=wx.Size(240, 24), style=0, value='')

        self.pemerintahan = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAPEMERINTAHAN,
              name=u'pemerintahan', parent=self, pos=wx.Point(656, 16),
              size=wx.Size(240, 24), style=0, value='')

        self.ekbang = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAEKBANG,
              name=u'ekbang', parent=self, pos=wx.Point(656, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.keuangan = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAKEUANGAN,
              name=u'keuangan', parent=self, pos=wx.Point(656, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.kesra = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAKESRA, name=u'kesra',
              parent=self, pos=wx.Point(656, 112), size=wx.Size(240, 24),
              style=0, value='')

        self.label_web = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_WEB,
              label=u'Alamat Web', name=u'label_web', parent=self,
              pos=wx.Point(192, 144), size=wx.Size(104, 17), style=0)

        self.label_kode_desa = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_KODE_DESA,
              label=u'No Kode Desa', name=u'label_kode_desa', parent=self,
              pos=wx.Point(192, 176), size=wx.Size(91, 17), style=0)

        self.label_kades = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_KADES,
              label=u'Nama KADES', name=u'label_kades', parent=self,
              pos=wx.Point(192, 208), size=wx.Size(88, 17), style=0)

        self.label_sekdes = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_SEKDES,
              label=u'Nama SEKDES', name=u'label_sekdes', parent=self,
              pos=wx.Point(192, 240), size=wx.Size(96, 17), style=0)

        self.label_alamat = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(47, 17), style=0)

        self.label_dukuh = wx.StaticText(id=wxID_INPUT_PROFIL_DESALABEL_DUKUH,
              label=u'Daftar Nama Dusun / Dukuh', name=u'label_dukuh',
              parent=self, pos=wx.Point(16, 304), size=wx.Size(576, 17),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT1,
              label=u'1.', name='staticText1', parent=self, pos=wx.Point(16,
              328), size=wx.Size(13, 17), style=0)

        self.dusun1 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESADUSUN1,
              name=u'dusun1', parent=self, pos=wx.Point(40, 328),
              size=wx.Size(256, 24), style=0, value='')

        self.dusun2 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESADUSUN2,
              name=u'dusun2', parent=self, pos=wx.Point(40, 360),
              size=wx.Size(256, 24), style=0, value='')

        self.dusun3 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESADUSUN3,
              name=u'dusun3', parent=self, pos=wx.Point(336, 328),
              size=wx.Size(256, 24), style=0, value='')

        self.dusun4 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESADUSUN4,
              name=u'dusun4', parent=self, pos=wx.Point(336, 360),
              size=wx.Size(256, 24), style=0, value='')

        self.dusun5 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESADUSUN5,
              name=u'dusun5', parent=self, pos=wx.Point(640, 328),
              size=wx.Size(256, 24), style=0, value='')

        self.dusun6 = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESADUSUN6,
              name=u'dusun6', parent=self, pos=wx.Point(640, 360),
              size=wx.Size(256, 24), style=0, value='')

        self.alamat = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAALAMAT,
              name=u'alamat', parent=self, pos=wx.Point(280, 272),
              size=wx.Size(280, 24), style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT3,
              label=u'2.', name='staticText3', parent=self, pos=wx.Point(16,
              360), size=wx.Size(13, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT4,
              label=u'3.', name='staticText4', parent=self, pos=wx.Point(312,
              328), size=wx.Size(13, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT5,
              label=u'4.', name='staticText5', parent=self, pos=wx.Point(312,
              360), size=wx.Size(13, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT6,
              label=u'5.', name='staticText6', parent=self, pos=wx.Point(616,
              328), size=wx.Size(13, 17), style=0)

        self.staticText7 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT7,
              label=u'6.', name='staticText7', parent=self, pos=wx.Point(616,
              360), size=wx.Size(13, 17), style=0)

        self.kecamatan = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAKECAMATAN,
              name=u'kecamatan', parent=self, pos=wx.Point(280, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.tombol_simpan = wx.Button(id=wxID_INPUT_PROFIL_DESATOMBOL_SIMPAN,
              label=u'Simpan Data', name=u'tombol_simpan', parent=self,
              pos=wx.Point(280, 392), size=wx.Size(192, 30), style=0)
        self.tombol_simpan.Bind(wx.EVT_BUTTON, self.OnTombol_simpanButton,
              id=wxID_INPUT_PROFIL_DESATOMBOL_SIMPAN)

        self.tombol_kembali = wx.Button(id=wxID_INPUT_PROFIL_DESATOMBOL_KEMBALI,
              label=u'Kembali Ke Menu', name=u'tombol_kembali', parent=self,
              pos=wx.Point(480, 392), size=wx.Size(184, 30), style=0)
        self.tombol_kembali.Bind(wx.EVT_BUTTON, self.OnTombol_kembaliButton,
              id=wxID_INPUT_PROFIL_DESATOMBOL_KEMBALI)

        self.telp = wx.StaticText(id=wxID_INPUT_PROFIL_DESATELP, label=u'Telp',
              name=u'telp', parent=self, pos=wx.Point(568, 272),
              size=wx.Size(25, 15), style=0)

        self.notelp = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESANOTELP,
              name=u'notelp', parent=self, pos=wx.Point(608, 272),
              size=wx.Size(128, 25), style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT2,
              label=u'Email', name='staticText2', parent=self, pos=wx.Point(744,
              272), size=wx.Size(36, 15), style=0)

        self.namaemail = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESANAMAEMAIL,
              name=u'namaemail', parent=self, pos=wx.Point(792, 272),
              size=wx.Size(104, 25), style=0, value='')

        self.web = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAWEB, name=u'web',
              parent=self, pos=wx.Point(280, 144), size=wx.Size(240, 24),
              style=0, value=u'')

        self.kode = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAKODE, name=u'kode',
              parent=self, pos=wx.Point(280, 176), size=wx.Size(240, 24),
              style=0, value=u'')

        self.kades = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAKADES, name=u'kades',
              parent=self, pos=wx.Point(280, 208), size=wx.Size(240, 24),
              style=0, value=u'')

        self.sekdes = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESASEKDES,
              name=u'sekdes', parent=self, pos=wx.Point(280, 240),
              size=wx.Size(240, 24), style=0, value=u'')

        self.staticText8 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT8,
              label=u'Kaur Pemerintahan', name='staticText8', parent=self,
              pos=wx.Point(528, 16), size=wx.Size(117, 17), style=0)

        self.staticText9 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT9,
              label=u'Kaur Ekbang', name='staticText9', parent=self,
              pos=wx.Point(528, 48), size=wx.Size(76, 17), style=0)

        self.staticText10 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT10,
              label=u'Kaur Keuangan', name='staticText10', parent=self,
              pos=wx.Point(528, 80), size=wx.Size(92, 17), style=0)

        self.staticText11 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT11,
              label=u'Kaur Kesra', name='staticText11', parent=self,
              pos=wx.Point(528, 112), size=wx.Size(92, 17), style=0)

        self.camat = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESACAMAT, name=u'camat',
              parent=self, pos=wx.Point(656, 176), size=wx.Size(240, 24),
              style=0, value='')

        self.umum = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESAUMUM, name=u'umum',
              parent=self, pos=wx.Point(656, 144), size=wx.Size(240, 24),
              style=0, value='')

        self.bupati = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESABUPATI,
              name=u'bupati', parent=self, pos=wx.Point(656, 208),
              size=wx.Size(240, 24), style=0, value='')

        self.staticText12 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT12,
              label=u'Kaur Umum', name='staticText12', parent=self,
              pos=wx.Point(528, 144), size=wx.Size(73, 17), style=0)

        self.staticText13 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT13,
              label=u'Nama Camat', name='staticText13', parent=self,
              pos=wx.Point(528, 176), size=wx.Size(79, 17), style=0)

        self.staticText14 = wx.StaticText(id=wxID_INPUT_PROFIL_DESASTATICTEXT14,
              label=u'Nama Bupati', name='staticText14', parent=self,
              pos=wx.Point(528, 208), size=wx.Size(79, 17), style=0)

        self.logopemda = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESALOGOPEMDA,
              name=u'logopemda', parent=self, pos=wx.Point(16, 208),
              size=wx.Size(168, 24), style=0, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_INPUT_PROFIL_DESASIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'/opt/sidesa/png/')

        self.button1 = wx.Button(id=wxID_INPUT_PROFIL_DESABUTTON1,
              label=u'Upload Logo Pemda', name='button1', parent=self,
              pos=wx.Point(16, 240), size=wx.Size(168, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_INPUT_PROFIL_DESABUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.cekdata()
    
    def cekdata(self):
        sql="SELECT * FROM identitas WHERE no=1"
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil :
            
            self.desa.SetValue(str(hasil[15]))
            self.kecamatan.SetValue(str(hasil[16]))
            self.kabupaten.SetValue(str(hasil[17]))
            self.propinsi.SetValue(str(hasil[18]))
            self.alamat.SetValue(str(hasil[19]))
            self.web.SetValue(str(hasil[20]))
            self.kode.SetValue(str(hasil[25]))
            self.kades.SetValue(str(hasil[23]))
            self.sekdes.SetValue(str(hasil[24]))
            self.pemerintahan.SetValue(str(hasil[7]))
            self.ekbang.SetValue(str(hasil[5]))
            self.keuangan.SetValue(str(hasil[3]))
            self.kesra.SetValue(str(hasil[2]))
            self.umum.SetValue(str(hasil[4]))
            self.camat.SetValue(str(hasil[6]))
            self.bupati.SetValue(str(hasil[8]))
            self.dusun1.SetValue(str(hasil[14]))
            self.dusun2.SetValue(str(hasil[13]))
            self.dusun3.SetValue(str(hasil[12]))
            self.dusun4.SetValue(str(hasil[11]))
            self.dusun5.SetValue(str(hasil[10]))
            self.dusun6.SetValue(str(hasil[9]))
            self.notelp.SetValue(str(hasil[22]))
            self.namaemail.SetValue(str(hasil[21]))
            self.logopemda.SetValue(str(hasil[1]))
            self.tombol_simpan.Disable()
            self.button1.Disable()
             
            self.PhotoMaxSize = 150
            img = wx.Image(self.logopemda.GetValue(), wx.BITMAP_TYPE_ANY)
            W = img.GetWidth()
            H = img.GetHeight()
            if W > H:
                NewW = self.PhotoMaxSize
                NewH = self.PhotoMaxSize * H / W
            else:
                NewH = self.PhotoMaxSize
                NewW = self.PhotoMaxSize * W / H
                img = img.Scale(NewW,NewH)
                self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(16, 16))
            self.pesan = wx.MessageDialog(self,"Data Identitas Sudah Dimasukkan Anda Hanya Diperkenankan Untuk Mengedit Data Identitas Desa. Silahkan Buka Edit Profil Desa ","Peringatan",wx.OK) 
            self.pesan.ShowModal()    
        else : 
            self.loadgambar()
            self.tombol_simpan.Enable()
            self.button1.Enable()
      
            
    def loadgambar(self):
        self.PhotoMaxSize = 150
        img = wx.Image('/opt/sidesa/png/pemda.jpg', wx.BITMAP_TYPE_ANY)
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
            
        img = img.Scale(NewW,NewH)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(16, 16))
 
  
    def OnTombol_kembaliButton(self, event):
        
        
        self.Close()
        self.Destroy()
        

    def OnTombol_simpanButton(self, event):
        desa = str(self.desa.GetValue())
        kecamatan = str(self.kecamatan.GetValue())
        kabupaten = str(self.kabupaten.GetValue())
        propinsi = str(self.propinsi.GetValue())
        alamat = str(self.alamat.GetValue())
        web = str(self.web.GetValue())
        kode = str(self.kode.GetValue())
        kades = str(self.kades.GetValue())
        sekdes = str(self.sekdes.GetValue())
        pemerintahan = str(self.pemerintahan.GetValue())
        ekbang = str(self.ekbang.GetValue())
        keuangan = str(self.keuangan.GetValue())
        kesra = str(self.kesra.GetValue())
        umum = str(self.umum.GetValue())
        camat = str(self.camat.GetValue())
        bupati = str(self.bupati.GetValue())
        dusun1 = str(self.dusun1.GetValue())
        dusun2 = str(self.dusun2.GetValue())
        dusun3 = str(self.dusun3.GetValue())
        dusun4 = str(self.dusun4.GetValue())
        dusun5 = str(self.dusun5.GetValue())
        dusun6 = str(self.dusun6.GetValue())
        notelp = str(self.notelp.GetValue())
        namaemail = str(self.namaemail.GetValue())
        gbr = str(self.simpangambar.GetValue())
        filepath = str(self.logopemda.GetValue())
        
        if desa == '':
            self.pesan = wx.MessageDialog(self,"Nama Desa Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif kecamatan == '':
            self.pesan = wx.MessageDialog(self,"Nama Kecamatan Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif kabupaten == '':
            self.pesan = wx.MessageDialog(self,"Nama Kabupaten Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()        
        elif propinsi == '':
            self.pesan = wx.MessageDialog(self,"Nama Propinsi Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif kode == '':
            self.pesan = wx.MessageDialog(self,"Kode Desa Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif kades == '':
            self.pesan = wx.MessageDialog(self,"Nama Kepala Desa Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif filepath == '':
            add_identitas="INSERT INTO identitas (logopemda,nama_kaur_kesra,nama_kaur_keuangan,nama_kaur_umum,nama_kaur_ekbang, nama_camat, nama_kaur_pemerintahan, nama_bupati,dusun6, dusun5, dusun4, dusun3, dusun2, dusun1, nama_desa, nama_kecamatan, nama_kabupaten, nama_propinsi, alamat_kantor, website, email, no_telp, nama_kades, nama_sekdes, nokode) VALUES('"+(gbr)+"pemda.jpg','"+(kesra)+"','"+(keuangan)+"','"+(umum)+"','"+(ekbang)+"','"+(camat)+"','"+(pemerintahan)+"','"+(bupati)+"','"+(dusun6)+"', '"+(dusun5)+"', '"+(dusun4)+"', '"+(dusun3)+"', '"+(dusun2)+"', '"+(dusun1)+"', '"+(desa)+"', '"+(kecamatan)+"', '"+(kabupaten)+"', '"+(propinsi)+"', '"+(alamat)+"', '"+(web)+"', '"+(namaemail)+"', '"+(notelp)+"', '"+(kades)+"', '"+(sekdes)+"', '"+(kode)+"')"
            cur.execute(add_identitas)
            db.commit()
        else :
            shutil.copy2(filepath, gbr+desa+'.jpg')       
            add_identitas="INSERT INTO identitas (logopemda,nama_kaur_kesra,nama_kaur_keuangan,nama_kaur_umum,nama_kaur_ekbang, nama_camat, nama_kaur_pemerintahan, nama_bupati,dusun6, dusun5, dusun4, dusun3, dusun2, dusun1, nama_desa, nama_kecamatan, nama_kabupaten, nama_propinsi, alamat_kantor, website, email, no_telp, nama_kades, nama_sekdes, nokode) VALUES('"+(gbr)+(desa)+".jpg','"+(kesra)+"','"+(keuangan)+"','"+(umum)+"','"+(ekbang)+"','"+(camat)+"','"+(pemerintahan)+"','"+(bupati)+"','"+(dusun6)+"', '"+(dusun5)+"', '"+(dusun4)+"', '"+(dusun3)+"', '"+(dusun2)+"', '"+(dusun1)+"', '"+(desa)+"', '"+(kecamatan)+"', '"+(kabupaten)+"', '"+(propinsi)+"', '"+(alamat)+"', '"+(web)+"', '"+(namaemail)+"', '"+(notelp)+"', '"+(kades)+"', '"+(sekdes)+"', '"+(kode)+"')"
            cur.execute(add_identitas)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Identitas Desa Tersimpan ","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.Close()
            self.Destroy()
            

    def OnButton1Button(self, event):
        wildcard = "JPG PNG BMP File (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Ambil File",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.logopemda.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()
        
    def onView(self):
        filepath = self.logopemda.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
            
        img = img.Scale(NewW,NewH)
        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
