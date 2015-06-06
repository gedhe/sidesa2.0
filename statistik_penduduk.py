#Boa:Frame:data_statistik_penduduk

import wx
import wx.lib.buttons
import frm_sideka_menu
import piramidapenduduk
import matplotlib.pyplot as plt
import sqlite3

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return data_statistik_penduduk(parent)

[wxID_DATA_STATISTIK_PENDUDUK, 
 wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON1, 
 wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON2, 
 wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON3, 
 wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON4, 
 wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON5, 
 wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON6, 
 wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON7, 
 wxID_DATA_STATISTIK_PENDUDUKKOTAK_STATISTIK_PENDUDUK, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEHAMILAN, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEPEMILIKAN_DOKUMEN, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KONTRASEPSI, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_MENU, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_AKHIR, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_SEDANG, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PERBANDINGAN, 
 wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PIRAMIDA_PENDUDUK, 
] = [wx.NewId() for _init_ctrls in range(17)]

class data_statistik_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_DATA_STATISTIK_PENDUDUK,
              name=u'data_statistik_penduduk', parent=prnt, pos=wx.Point(569,
              197), size=wx.Size(562, 385), style=wx.FRAME_NO_TASKBAR,
              title=u'Data Statistik Penduduk')
        self.SetClientSize(wx.Size(562, 385))
        self.Center(wx.BOTH)

        self.kotak_statistik_penduduk = wx.StaticBox(id=wxID_DATA_STATISTIK_PENDUDUKKOTAK_STATISTIK_PENDUDUK,
              label=u'Statistik Penduduk', name=u'kotak_statistik_penduduk',
              parent=self, pos=wx.Point(16, 16), size=wx.Size(528, 320),
              style=0)

        self.tombol_piramida_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PIRAMIDA_PENDUDUK,
              label=u'Piramida Penduduk', name=u'tombol_piramida_penduduk',
              parent=self, pos=wx.Point(32, 40), size=wx.Size(240, 31),
              style=0)
        self.tombol_piramida_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_piramida_pendudukButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PIRAMIDA_PENDUDUK)

        self.tombol_perbandingan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PERBANDINGAN,
              label=u'Perbandingan Kepala Keluarga',
              name=u'tombol_perbandingan', parent=self, pos=wx.Point(32, 80),
              size=wx.Size(240, 31), style=0)
        self.tombol_perbandingan.Bind(wx.EVT_BUTTON,
              self.OnTombol_perbandinganButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PERBANDINGAN)

        self.tombol_pendidikan_akhir = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_AKHIR,
              label=u'Pendidikan Terakhir', name=u'tombol_pendidikan_akhir',
              parent=self, pos=wx.Point(32, 120), size=wx.Size(240, 31),
              style=0)
        self.tombol_pendidikan_akhir.Bind(wx.EVT_BUTTON,
              self.OnTombol_pendidikan_akhirButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_AKHIR)

        self.tombol_pendidikan_sedang = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_SEDANG,
              label=u'Pendidikan Sedang Ditempuh',
              name=u'tombol_pendidikan_sedang', parent=self, pos=wx.Point(32,
              160), size=wx.Size(240, 31), style=0)
        self.tombol_pendidikan_sedang.Bind(wx.EVT_BUTTON,
              self.OnTombol_pendidikan_sedangButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_PENDIDIKAN_SEDANG)

        self.tombol_kehamilan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEHAMILAN,
              label=u'Resiko Kehamilan', name=u'tombol_kehamilan', parent=self,
              pos=wx.Point(32, 200), size=wx.Size(240, 31), style=0)
        self.tombol_kehamilan.Bind(wx.EVT_BUTTON, self.OnTombol_kehamilanButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEHAMILAN)

        self.tombol_kontrasepsi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'tombol_kontrasepsi',
              parent=self, pos=wx.Point(32, 240), size=wx.Size(240, 31),
              style=0)
        self.tombol_kontrasepsi.Bind(wx.EVT_BUTTON,
              self.OnTombol_kontrasepsiButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KONTRASEPSI)

        self.tombol_kepemilikan_dokumen = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEPEMILIKAN_DOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'tombol_kepemilikan_dokumen',
              parent=self, pos=wx.Point(32, 280), size=wx.Size(240, 31),
              style=0)
        self.tombol_kepemilikan_dokumen.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_KEPEMILIKAN_DOKUMEN)

        self.tombol_menu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_MENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_menu', parent=self,
              pos=wx.Point(176, 344), size=wx.Size(240, 31), style=0)
        self.tombol_menu.Bind(wx.EVT_BUTTON, self.OnTombol_menuButton,
              id=wxID_DATA_STATISTIK_PENDUDUKTOMBOL_MENU)

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON1,
              label=u'Agama', name='genBitmapTextButton1', parent=self,
              pos=wx.Point(280, 40), size=wx.Size(240, 31), style=0)
        self.genBitmapTextButton1.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON1)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON2,
              label=u'Pekerjaan', name='genBitmapTextButton2', parent=self,
              pos=wx.Point(280, 80), size=wx.Size(240, 31), style=0)
        self.genBitmapTextButton2.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON2)

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON3,
              label=u'Usia Penduduk', name='genBitmapTextButton3', parent=self,
              pos=wx.Point(280, 120), size=wx.Size(240, 31), style=0)
        self.genBitmapTextButton3.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON3)

        self.genBitmapTextButton4 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON4,
              label=u'Kematian Kelahiran', name='genBitmapTextButton4',
              parent=self, pos=wx.Point(280, 160), size=wx.Size(240, 31),
              style=0)
        self.genBitmapTextButton4.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON4)

        self.genBitmapTextButton5 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON5,
              label=u'Status Kependudukan', name='genBitmapTextButton5',
              parent=self, pos=wx.Point(280, 200), size=wx.Size(240, 31),
              style=0)
        self.genBitmapTextButton5.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON5)

        self.genBitmapTextButton6 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON6,
              label=u'WNI / WNA', name='genBitmapTextButton6', parent=self,
              pos=wx.Point(280, 240), size=wx.Size(240, 31), style=0)
        self.genBitmapTextButton6.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON6)

        self.genBitmapTextButton7 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON7,
              label=u'Status Perkawinan', name='genBitmapTextButton7',
              parent=self, pos=wx.Point(280, 280), size=wx.Size(240, 31),
              style=0)
        self.genBitmapTextButton7.Bind(wx.EVT_BUTTON,
              self.OnTombol_kepemilikan_dokumenButton,
              id=wxID_DATA_STATISTIK_PENDUDUKGENBITMAPTEXTBUTTON7)

    def __init__(self, parent):
        self._init_ctrls(parent)


    def OnTombol_piramida_pendudukButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE jk='L' OR jk='Laki-laki'  AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0]
        has=str(hasil)
        
        sql1 = "SELECT COUNT(*) FROM penduduk WHERE jk='P' OR jk='Perempuan' AND kematian='Tidak'"
        cur.execute(sql1) 
        hasil1 = cur.fetchone()[0]
        has1=str(hasil1)
        
        sql2="SELECT * FROM identitas WHERE no=1"
        cur.execute(sql2)
        hasil3 = cur.fetchone() 
        prop = str(hasil3[18])
        kab = str(hasil3[17])
        kec = str(hasil3[16])
        des = str(hasil3[15])
        
        fig = plt.figure()
        plt.axis('equal')
        plt.suptitle('GRAFIK JUMLAH PENDUDUK BERDASARKAN JENIS KELAMIN', fontsize=14, fontweight='bold')
        plt.title('Desa '+des+', Kecamatan '+kec+', Kabupaten '+kab+', Provinsi '+prop, fontsize=10,fontweight='bold')
                
        labels = 'Laki-laki', 'Perempuan'
        sizes = [hasil, hasil1]
        colors = ['blue', 'red']
        explode = (0, 0.1)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1f%%', shadow=True, startangle=90)
        plt.text(-2,-1.1, 'Jumlah Perempuan='+has1+' Jiwa',fontweight='bold')
        plt.text(-2,-1.2, 'Jumlah Laki-laki='+has+' Jiwa',fontweight='bold')
        
        plt.show()


    def OnTombol_perbandinganButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE jk='L' OR jk='Laki-laki'  AND kematian='Tidak' AND shdk='Kepala Keluarga'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0]
        has=str(hasil)
        
        sql1 = "SELECT COUNT(*) FROM penduduk WHERE jk='P' OR jk='Perempuan' AND kematian='Tidak' AND shdk='Kepala Keluarga'"
        cur.execute(sql1) 
        hasil1 = cur.fetchone()[0]
        has1=str(hasil1)
        
        sql2="SELECT * FROM identitas WHERE no=1"
        cur.execute(sql2)
        hasil3 = cur.fetchone() 
        prop = str(hasil3[18])
        kab = str(hasil3[17])
        kec = str(hasil3[16])
        des = str(hasil3[15])
        
        fig = plt.figure()
        plt.axis('equal')
        plt.suptitle('GRAFIK JUMLAH KK BERDASARKAN JENIS KELAMIN', fontsize=14, fontweight='bold')
        plt.title('Desa '+des+', Kecamatan '+kec+', Kabupaten '+kab+', Provinsi '+prop, fontsize=10,fontweight='bold')
                
        labels = 'Laki-laki', 'Perempuan'
        sizes = [hasil, hasil1]
        colors = ['blue', 'red']
        explode = (0, 0.1)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1f%%', shadow=True, startangle=90)
        plt.text(-2,-1.1, 'Jumlah Perempuan='+has1+' Jiwa',fontweight='bold')
        plt.text(-2,-1.2, 'Jumlah Laki-laki='+has+' Jiwa',fontweight='bold')
        
        plt.show()


    def OnTombol_pendidikan_akhirButton(self, event):
        event.Skip()

    def OnTombol_pendidikan_sedangButton(self, event):
        event.Skip()

    def OnTombol_kehamilanButton(self, event):
        event.Skip()

    def OnTombol_kontrasepsiButton(self, event):
        event.Skip()

    def OnTombol_giziButton(self, event):
        event.Skip()

    def OnTombol_kepemilikan_dokumenButton(self, event):
        event.Skip()

    def OnTombol_menuButton(self, event):
        self.Close()
