#Boa:Frame:edit_profil

import wx
import sqlite3
import shutil
import os

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()


def create(parent):
    return edit_profil(parent)

[wxID_EDIT_PROFIL, wxID_EDIT_PROFILALAMAT, wxID_EDIT_PROFILBUPATI, 
 wxID_EDIT_PROFILBUTTON1, wxID_EDIT_PROFILCAMAT, wxID_EDIT_PROFILDESA, 
 wxID_EDIT_PROFILDUSUN1, wxID_EDIT_PROFILDUSUN2, wxID_EDIT_PROFILDUSUN3, 
 wxID_EDIT_PROFILDUSUN4, wxID_EDIT_PROFILDUSUN5, wxID_EDIT_PROFILDUSUN6, 
 wxID_EDIT_PROFILEKBANG, wxID_EDIT_PROFILKABUPATEN, wxID_EDIT_PROFILKADES, 
 wxID_EDIT_PROFILKECAMATAN, wxID_EDIT_PROFILKESRA, wxID_EDIT_PROFILKEUANGAN, 
 wxID_EDIT_PROFILKODE, wxID_EDIT_PROFILLABEL_ALAMAT, 
 wxID_EDIT_PROFILLABEL_DUKUH, wxID_EDIT_PROFILLABEL_KADES, 
 wxID_EDIT_PROFILLABEL_KECAMATAN, wxID_EDIT_PROFILLABEL_KODE_DESA, 
 wxID_EDIT_PROFILLABEL_NAMA_DESA, wxID_EDIT_PROFILLABEL_PROPINSI, 
 wxID_EDIT_PROFILLABEL_SEKDES, wxID_EDIT_PROFILLABEL_WEB, 
 wxID_EDIT_PROFILLABLE_KABUPATEN, wxID_EDIT_PROFILLOGOPEMDA, 
 wxID_EDIT_PROFILNAMAEMAIL, wxID_EDIT_PROFILNORUT, wxID_EDIT_PROFILNOTELP, 
 wxID_EDIT_PROFILPEMERINTAHAN, wxID_EDIT_PROFILPROPINSI, 
 wxID_EDIT_PROFILSEKDES, wxID_EDIT_PROFILSIMPANGAMBAR, 
 wxID_EDIT_PROFILSTATICTEXT1, wxID_EDIT_PROFILSTATICTEXT10, 
 wxID_EDIT_PROFILSTATICTEXT11, wxID_EDIT_PROFILSTATICTEXT12, 
 wxID_EDIT_PROFILSTATICTEXT13, wxID_EDIT_PROFILSTATICTEXT14, 
 wxID_EDIT_PROFILSTATICTEXT2, wxID_EDIT_PROFILSTATICTEXT3, 
 wxID_EDIT_PROFILSTATICTEXT4, wxID_EDIT_PROFILSTATICTEXT5, 
 wxID_EDIT_PROFILSTATICTEXT6, wxID_EDIT_PROFILSTATICTEXT7, 
 wxID_EDIT_PROFILSTATICTEXT8, wxID_EDIT_PROFILSTATICTEXT9, 
 wxID_EDIT_PROFILTELP, wxID_EDIT_PROFILTOMBOL_KEMBALI, 
 wxID_EDIT_PROFILTOMBOL_SIMPAN, wxID_EDIT_PROFILUMUM, wxID_EDIT_PROFILWEB, 
] = [wx.NewId() for _init_ctrls in range(56)]

class edit_profil(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EDIT_PROFIL, name=u'edit_profil',
              parent=prnt, pos=wx.Point(394, 189), size=wx.Size(911, 435),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Edit Profil Desa')
        self.SetClientSize(wx.Size(911, 435))
        self.Center(wx.BOTH)

        self.label_nama_desa = wx.StaticText(id=wxID_EDIT_PROFILLABEL_NAMA_DESA,
              label=u'Nama Desa', name=u'label_nama_desa', parent=self,
              pos=wx.Point(192, 16), size=wx.Size(77, 17), style=0)

        self.label_kecamatan = wx.StaticText(id=wxID_EDIT_PROFILLABEL_KECAMATAN,
              label=u'Kecamatan', name=u'label_kecamatan', parent=self,
              pos=wx.Point(192, 48), size=wx.Size(73, 17), style=0)

        self.lable_kabupaten = wx.StaticText(id=wxID_EDIT_PROFILLABLE_KABUPATEN,
              label=u'Kabupaten', name=u'lable_kabupaten', parent=self,
              pos=wx.Point(192, 80), size=wx.Size(70, 17), style=0)

        self.label_propinsi = wx.StaticText(id=wxID_EDIT_PROFILLABEL_PROPINSI,
              label=u'Propinsi', name=u'label_propinsi', parent=self,
              pos=wx.Point(192, 112), size=wx.Size(51, 17), style=0)

        self.desa = wx.TextCtrl(id=wxID_EDIT_PROFILDESA, name=u'desa',
              parent=self, pos=wx.Point(280, 16), size=wx.Size(240, 24),
              style=0, value='')

        self.kabupaten = wx.TextCtrl(id=wxID_EDIT_PROFILKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(280, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.propinsi = wx.TextCtrl(id=wxID_EDIT_PROFILPROPINSI,
              name=u'propinsi', parent=self, pos=wx.Point(280, 112),
              size=wx.Size(240, 24), style=0, value='')

        self.pemerintahan = wx.TextCtrl(id=wxID_EDIT_PROFILPEMERINTAHAN,
              name=u'pemerintahan', parent=self, pos=wx.Point(656, 16),
              size=wx.Size(240, 24), style=0, value='')

        self.ekbang = wx.TextCtrl(id=wxID_EDIT_PROFILEKBANG, name=u'ekbang',
              parent=self, pos=wx.Point(656, 48), size=wx.Size(240, 24),
              style=0, value='')

        self.keuangan = wx.TextCtrl(id=wxID_EDIT_PROFILKEUANGAN,
              name=u'keuangan', parent=self, pos=wx.Point(656, 80),
              size=wx.Size(240, 24), style=0, value='')

        self.kesra = wx.TextCtrl(id=wxID_EDIT_PROFILKESRA, name=u'kesra',
              parent=self, pos=wx.Point(656, 112), size=wx.Size(240, 24),
              style=0, value='')

        self.label_web = wx.StaticText(id=wxID_EDIT_PROFILLABEL_WEB,
              label=u'Alamat Web', name=u'label_web', parent=self,
              pos=wx.Point(192, 144), size=wx.Size(104, 17), style=0)

        self.label_kode_desa = wx.StaticText(id=wxID_EDIT_PROFILLABEL_KODE_DESA,
              label=u'No Kode Desa', name=u'label_kode_desa', parent=self,
              pos=wx.Point(192, 176), size=wx.Size(91, 17), style=0)

        self.label_kades = wx.StaticText(id=wxID_EDIT_PROFILLABEL_KADES,
              label=u'Nama KADES', name=u'label_kades', parent=self,
              pos=wx.Point(192, 208), size=wx.Size(88, 17), style=0)

        self.label_sekdes = wx.StaticText(id=wxID_EDIT_PROFILLABEL_SEKDES,
              label=u'Nama SEKDES', name=u'label_sekdes', parent=self,
              pos=wx.Point(192, 240), size=wx.Size(96, 17), style=0)

        self.label_alamat = wx.StaticText(id=wxID_EDIT_PROFILLABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(47, 17), style=0)

        self.label_dukuh = wx.StaticText(id=wxID_EDIT_PROFILLABEL_DUKUH,
              label=u'Daftar Nama Dusun / Dukuh', name=u'label_dukuh',
              parent=self, pos=wx.Point(16, 304), size=wx.Size(576, 17),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT1,
              label=u'1.', name='staticText1', parent=self, pos=wx.Point(16,
              328), size=wx.Size(13, 17), style=0)

        self.dusun1 = wx.TextCtrl(id=wxID_EDIT_PROFILDUSUN1, name=u'dusun1',
              parent=self, pos=wx.Point(40, 328), size=wx.Size(256, 24),
              style=0, value='')

        self.dusun2 = wx.TextCtrl(id=wxID_EDIT_PROFILDUSUN2, name=u'dusun2',
              parent=self, pos=wx.Point(40, 360), size=wx.Size(256, 24),
              style=0, value='')

        self.dusun3 = wx.TextCtrl(id=wxID_EDIT_PROFILDUSUN3, name=u'dusun3',
              parent=self, pos=wx.Point(336, 328), size=wx.Size(256, 24),
              style=0, value='')

        self.dusun4 = wx.TextCtrl(id=wxID_EDIT_PROFILDUSUN4, name=u'dusun4',
              parent=self, pos=wx.Point(336, 360), size=wx.Size(256, 24),
              style=0, value='')

        self.dusun5 = wx.TextCtrl(id=wxID_EDIT_PROFILDUSUN5, name=u'dusun5',
              parent=self, pos=wx.Point(640, 328), size=wx.Size(256, 24),
              style=0, value='')

        self.dusun6 = wx.TextCtrl(id=wxID_EDIT_PROFILDUSUN6, name=u'dusun6',
              parent=self, pos=wx.Point(640, 360), size=wx.Size(256, 24),
              style=0, value='')

        self.alamat = wx.TextCtrl(id=wxID_EDIT_PROFILALAMAT, name=u'alamat',
              parent=self, pos=wx.Point(280, 272), size=wx.Size(280, 24),
              style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT3,
              label=u'2.', name='staticText3', parent=self, pos=wx.Point(16,
              360), size=wx.Size(13, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT4,
              label=u'3.', name='staticText4', parent=self, pos=wx.Point(312,
              328), size=wx.Size(13, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT5,
              label=u'4.', name='staticText5', parent=self, pos=wx.Point(312,
              360), size=wx.Size(13, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT6,
              label=u'5.', name='staticText6', parent=self, pos=wx.Point(616,
              328), size=wx.Size(13, 17), style=0)

        self.staticText7 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT7,
              label=u'6.', name='staticText7', parent=self, pos=wx.Point(616,
              360), size=wx.Size(13, 17), style=0)

        self.kecamatan = wx.TextCtrl(id=wxID_EDIT_PROFILKECAMATAN,
              name=u'kecamatan', parent=self, pos=wx.Point(280, 48),
              size=wx.Size(240, 24), style=0, value='')

        self.tombol_simpan = wx.Button(id=wxID_EDIT_PROFILTOMBOL_SIMPAN,
              label=u'Simpan Data', name=u'tombol_simpan', parent=self,
              pos=wx.Point(280, 392), size=wx.Size(192, 30), style=0)
        self.tombol_simpan.Bind(wx.EVT_BUTTON, self.OnTombol_simpanButton,
              id=wxID_EDIT_PROFILTOMBOL_SIMPAN)

        self.tombol_kembali = wx.Button(id=wxID_EDIT_PROFILTOMBOL_KEMBALI,
              label=u'Kembali Ke Menu', name=u'tombol_kembali', parent=self,
              pos=wx.Point(480, 392), size=wx.Size(184, 30), style=0)
        self.tombol_kembali.Bind(wx.EVT_BUTTON, self.OnTombol_kembaliButton,
              id=wxID_EDIT_PROFILTOMBOL_KEMBALI)

        self.telp = wx.StaticText(id=wxID_EDIT_PROFILTELP, label=u'Telp',
              name=u'telp', parent=self, pos=wx.Point(568, 272),
              size=wx.Size(25, 15), style=0)

        self.notelp = wx.TextCtrl(id=wxID_EDIT_PROFILNOTELP, name=u'notelp',
              parent=self, pos=wx.Point(608, 272), size=wx.Size(128, 25),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT2,
              label=u'Email', name='staticText2', parent=self, pos=wx.Point(744,
              272), size=wx.Size(36, 15), style=0)

        self.namaemail = wx.TextCtrl(id=wxID_EDIT_PROFILNAMAEMAIL,
              name=u'namaemail', parent=self, pos=wx.Point(792, 272),
              size=wx.Size(104, 25), style=0, value='')

        self.web = wx.TextCtrl(id=wxID_EDIT_PROFILWEB, name=u'web', parent=self,
              pos=wx.Point(280, 144), size=wx.Size(240, 24), style=0,
              value=u'')

        self.kode = wx.TextCtrl(id=wxID_EDIT_PROFILKODE, name=u'kode',
              parent=self, pos=wx.Point(280, 176), size=wx.Size(240, 24),
              style=0, value=u'')

        self.kades = wx.TextCtrl(id=wxID_EDIT_PROFILKADES, name=u'kades',
              parent=self, pos=wx.Point(280, 208), size=wx.Size(240, 24),
              style=0, value=u'')

        self.sekdes = wx.TextCtrl(id=wxID_EDIT_PROFILSEKDES, name=u'sekdes',
              parent=self, pos=wx.Point(280, 240), size=wx.Size(240, 24),
              style=0, value=u'')

        self.staticText8 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT8,
              label=u'Kaur Pemerintahan', name='staticText8', parent=self,
              pos=wx.Point(528, 16), size=wx.Size(117, 17), style=0)

        self.staticText9 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT9,
              label=u'Kaur Ekbang', name='staticText9', parent=self,
              pos=wx.Point(528, 48), size=wx.Size(76, 17), style=0)

        self.staticText10 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT10,
              label=u'Kaur Keuangan', name='staticText10', parent=self,
              pos=wx.Point(528, 80), size=wx.Size(92, 17), style=0)

        self.staticText11 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT11,
              label=u'Kaur Kesra', name='staticText11', parent=self,
              pos=wx.Point(528, 112), size=wx.Size(92, 17), style=0)

        self.camat = wx.TextCtrl(id=wxID_EDIT_PROFILCAMAT, name=u'camat',
              parent=self, pos=wx.Point(656, 176), size=wx.Size(240, 24),
              style=0, value='')

        self.umum = wx.TextCtrl(id=wxID_EDIT_PROFILUMUM, name=u'umum',
              parent=self, pos=wx.Point(656, 144), size=wx.Size(240, 24),
              style=0, value='')

        self.bupati = wx.TextCtrl(id=wxID_EDIT_PROFILBUPATI, name=u'bupati',
              parent=self, pos=wx.Point(656, 208), size=wx.Size(240, 24),
              style=0, value='')

        self.staticText12 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT12,
              label=u'Kaur Umum', name='staticText12', parent=self,
              pos=wx.Point(528, 144), size=wx.Size(73, 17), style=0)

        self.staticText13 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT13,
              label=u'Nama Camat', name='staticText13', parent=self,
              pos=wx.Point(528, 176), size=wx.Size(79, 17), style=0)

        self.staticText14 = wx.StaticText(id=wxID_EDIT_PROFILSTATICTEXT14,
              label=u'Nama Bupati', name='staticText14', parent=self,
              pos=wx.Point(528, 208), size=wx.Size(79, 17), style=0)

        self.logopemda = wx.TextCtrl(id=wxID_EDIT_PROFILLOGOPEMDA,
              name=u'logopemda', parent=self, pos=wx.Point(16, 208),
              size=wx.Size(168, 24), style=0, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_EDIT_PROFILSIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'/opt/sidesa/png/')

        self.norut = wx.TextCtrl(id=wxID_EDIT_PROFILNORUT, name=u'norut',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(152, 24),
              style=0, value=u'')

        self.button1 = wx.Button(id=wxID_EDIT_PROFILBUTTON1,
              label=u'Upload Logo Pemda', name='button1', parent=self,
              pos=wx.Point(16, 240), size=wx.Size(168, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_EDIT_PROFILBUTTON1)

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
            self.norut.SetValue(str(hasil[0]))
            
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
              
        else : 
            self.pesan = wx.MessageDialog(self,"Data Identitas Desa Belum Diinput. Silahkan Input Data Profil Terlebih Dahulu ","Peringatan",wx.OK) 
            self.pesan.ShowModal() 
            self.Close()
            self.Destroy()
        
            
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
        nourut = str(self.norut.GetValue())
        
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
            add_update = "UPDATE identitas SET logopemda = '"+gbr+"pemda.jpg', nama_kaur_kesra = '"+kesra+"', nama_kaur_keuangan = '"+keuangan+"', nama_kaur_umum = '"+umum+"', nama_kaur_ekbang = '"+ekbang+"', nama_camat = '"+camat+"', nama_kaur_pemerintahan = '"+pemerintahan+"', nama_bupati = '"+bupati+"', dusun6 = '"+dusun6+"', dusun5 = '"+dusun5+"', dusun4 = '"+dusun4+"', dusun3 = '"+dusun3+"', dusun2 = '"+dusun2+"', dusun1 = '"+dusun1+"', nama_desa = '"+desa+"', nama_kecamatan='"+kecamatan+"', nama_kabupaten='"+kabupaten+"', nama_propinsi='"+propinsi+"', alamat_kantor='"+alamat+"', website='"+web+"', email='"+namaemail+"', no_telp='"+notelp+"', nama_kades='"+kades+"', nama_sekdes='"+sekdes+"', nokode='"+kode+"'  WHERE no=1 " 
            cur.execute(add_update)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Identitas Desa Terupdate ","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.Close()
            self.Destroy()
            
            
        elif filepath == gbr+desa+'.jpg':
            add_update = "UPDATE identitas SET logopemda = '"+filepath+"', nama_kaur_kesra = '"+kesra+"', nama_kaur_keuangan = '"+keuangan+"', nama_kaur_umum = '"+umum+"', nama_kaur_ekbang = '"+ekbang+"', nama_camat = '"+camat+"', nama_kaur_pemerintahan = '"+pemerintahan+"', nama_bupati = '"+bupati+"', dusun6 = '"+dusun6+"', dusun5 = '"+dusun5+"', dusun4 = '"+dusun4+"', dusun3 = '"+dusun3+"', dusun2 = '"+dusun2+"', dusun1 = '"+dusun1+"', nama_desa = '"+desa+"', nama_kecamatan='"+kecamatan+"', nama_kabupaten='"+kabupaten+"', nama_propinsi='"+propinsi+"', alamat_kantor='"+alamat+"', website='"+web+"', email='"+namaemail+"', no_telp='"+notelp+"', nama_kades='"+kades+"', nama_sekdes='"+sekdes+"', nokode='"+kode+"'  WHERE no=1 " 
            cur.execute(add_update)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Identitas Desa Terupdate ","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.Close()
            self.Destroy()
              
        else :
            shutil.copy2(filepath, gbr+desa+'.jpg')       
            add_update = "UPDATE identitas SET logopemda = '"+gbr+desa+".jpg', nama_kaur_kesra = '"+kesra+"', nama_kaur_keuangan = '"+keuangan+"', nama_kaur_umum = '"+umum+"', nama_kaur_ekbang = '"+ekbang+"', nama_camat = '"+camat+"', nama_kaur_pemerintahan = '"+pemerintahan+"', nama_bupati = '"+bupati+"', dusun6 = '"+dusun6+"', dusun5 = '"+dusun5+"', dusun4 = '"+dusun4+"', dusun3 = '"+dusun3+"', dusun2 = '"+dusun2+"', dusun1 = '"+dusun1+"', nama_desa = '"+desa+"', nama_kecamatan='"+kecamatan+"', nama_kabupaten='"+kabupaten+"', nama_propinsi='"+propinsi+"', alamat_kantor='"+alamat+"', website='"+web+"', email='"+namaemail+"', no_telp='"+notelp+"', nama_kades='"+kades+"', nama_sekdes='"+sekdes+"', nokode='"+kode+"'  WHERE no=1 " 
            cur.execute(add_update)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Identitas Desa Terupdate ","Konfirmasi",wx.OK) 
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
