#Boa:Frame:data_statistik

import wx
import wx.lib.buttons
import sqlite3
import matplotlib.pyplot as plt

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return data_statistik(parent)

[wxID_DATA_STATISTIK, wxID_DATA_STATISTIKLABEL_STATISTIKA_KEMISKINAN, 
 wxID_DATA_STATISTIKTOMBOL_DATA_MISKIN_DESA, 
 wxID_DATA_STATISTIKTOMBOL_KEMBALI_KEMENU, wxID_DATA_STATISTIKTOMBOL_PROG, 
] = [wx.NewId() for _init_ctrls in range(5)]

class data_statistik(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_DATA_STATISTIK, name=u'data_statistik',
              parent=prnt, pos=wx.Point(697, 320), size=wx.Size(306, 173),
              style=wx.FRAME_NO_TASKBAR, title=u'Data Statistik Kemiskinan')
        self.SetClientSize(wx.Size(306, 173))
        self.Center(wx.BOTH)

        self.label_statistika_kemiskinan = wx.StaticBox(id=wxID_DATA_STATISTIKLABEL_STATISTIKA_KEMISKINAN,
              label=u'Statistik Kemiskinan',
              name=u'label_statistika_kemiskinan', parent=self, pos=wx.Point(16,
              16), size=wx.Size(272, 105), style=0)

        self.tombol_data_miskin_desa = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIKTOMBOL_DATA_MISKIN_DESA,
              label=u'Data Miskin Desa', name=u'tombol_data_miskin_desa',
              parent=self, pos=wx.Point(32, 40), size=wx.Size(240, 31),
              style=0)
        self.tombol_data_miskin_desa.Bind(wx.EVT_BUTTON,
              self.OnTombol_data_miskin_desaButton,
              id=wxID_DATA_STATISTIKTOMBOL_DATA_MISKIN_DESA)

        self.tombol_prog = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIKTOMBOL_PROG,
              label=u'Perbandingan Prog. Perlindungan', name=u'tombol_prog',
              parent=self, pos=wx.Point(32, 80), size=wx.Size(240, 31),
              style=0)
        self.tombol_prog.Bind(wx.EVT_BUTTON, self.OnTombol_progButton,
              id=wxID_DATA_STATISTIKTOMBOL_PROG)

        self.tombol_kembali_kemenu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_DATA_STATISTIKTOMBOL_KEMBALI_KEMENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_kembali_kemenu',
              parent=self, pos=wx.Point(32, 128), size=wx.Size(240, 31),
              style=0)
        self.tombol_kembali_kemenu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_kemenuButton,
              id=wxID_DATA_STATISTIKTOMBOL_KEMBALI_KEMENU)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_data_miskin_desaButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE shdk='Kepala Keluarga'  AND kematian='Tidak' AND kemiskinan='Tidak Miskin'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0]
        has=str(hasil)
        
        sql1 = "SELECT COUNT(*) FROM penduduk WHERE shdk='Kepala Keluarga'  AND kematian='Tidak' AND kemiskinan='Miskin'"
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
        plt.suptitle('GRAFIK PERBANDINGAN PENDUDUK MISKIN', fontsize=14, fontweight='bold')
        plt.title('Desa '+des+', Kecamatan '+kec+', Kabupaten '+kab+', Provinsi '+prop, fontsize=10,fontweight='bold')
                
        labels = 'Tidak Miskin', 'Miskin'
        sizes = [hasil, hasil1]
        colors = ['blue', 'red']
        explode = (0, 0.1)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1f%%', shadow=True)
        plt.text(-2,-1.1, 'Jumlah KK Miskin='+has1+' KK',fontweight='bold')
        plt.text(-2,-1.2, 'Jumlah KK Tidak Miskin='+has+' KK',fontweight='bold')
        
        plt.show()


    def OnTombol_progButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE promis1='RASKIN'  AND kematian='Tidak' AND kemiskinan='Miskin'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0]
        has=str(hasil)
        
        sql1 = "SELECT COUNT(*) FROM penduduk WHERE promis2='JKN'  AND kematian='Tidak' AND kemiskinan='Miskin'"
        cur.execute(sql1) 
        hasil1 = cur.fetchone()[0]
        has1=str(hasil1)
        
        sql2 = "SELECT COUNT(*) FROM penduduk WHERE promis3='BLSM'  AND kematian='Tidak' AND kemiskinan='Miskin'"
        cur.execute(sql1) 
        hasil2 = cur.fetchone()[0]
        has2=str(hasil2)
        
        sql3 = "SELECT COUNT(*) FROM penduduk WHERE promis4='BSM'  AND kematian='Tidak' AND kemiskinan='Miskin'"
        cur.execute(sql1) 
        hasil3 = cur.fetchone()[0]
        has3=str(hasil3)
        
        sql4 = "SELECT COUNT(*) FROM penduduk WHERE promis5='PKH'  AND kematian='Tidak' AND kemiskinan='Miskin'"
        cur.execute(sql1) 
        hasil4 = cur.fetchone()[0]
        has1=str(hasil4)
        
        sql5 = "SELECT COUNT(*) FROM penduduk WHERE promis6='Prog. Kesehatan Daerah'  AND kematian='Tidak' AND kemiskinan='Miskin'"
        cur.execute(sql5) 
        hasil5 = cur.fetchone()[0]
        has5=str(hasil5)
        
        sql6 = "SELECT COUNT(*) FROM penduduk WHERE promis7='Prog. Pendidikan Daerah'  AND kematian='Tidak' AND kemiskinan='Miskin'"
        cur.execute(sql6) 
        hasil6 = cur.fetchone()[0]
        has6=str(hasil6)
        
        sql7 = "SELECT COUNT(*) FROM penduduk WHERE promis8='Prog. Lain'  AND kematian='Tidak' AND kemiskinan='Miskin'"
        cur.execute(sql7) 
        hasil7 = cur.fetchone()[0]
        has7=str(hasil7)
    
        sql2="SELECT * FROM identitas WHERE no=1"
        cur.execute(sql2)
        hasil8 = cur.fetchone() 
        prop = str(hasil8[18])
        kab = str(hasil8[17])
        kec = str(hasil8[16])
        des = str(hasil8[15])
        
        fig = plt.figure()
        plt.axis('equal')
        plt.suptitle('GRAFIK PENERIMA PROGRAM KEMISKINAN', fontsize=14, fontweight='bold')
        plt.title('Desa '+des+', Kecamatan '+kec+', Kabupaten '+kab+', Provinsi '+prop, fontsize=10,fontweight='bold')
                
        labels = 'RASKIN', 'JKN', 'BLSM', 'BSM', 'PKH', 'Prog. Kesehatan Daerah', 'Prog. Pendidikan Daerah', 'Prog. Lain'
        sizes = [hasil, hasil1, hasil2, hasil3, hasil4, hasil5, hasil6, hasil7]
        colors = ['blue', 'red', 'yellow', 'green', 'grey', 'red','white','black']
        
        
        explode = (0.1, 0.1, 0.1,0.1,0.1,0.1,0.1,0.1)
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1f%%', shadow=True)
        plt.text(-2,-1.1, 'Jumlah KK Miskin='+has1+' KK',fontweight='bold')
        plt.text(-2,-1.2, 'Jumlah KK Tidak Miskin='+has+' KK',fontweight='bold')
        
        plt.show()

    def OnTombol_kembali_kemenuButton(self, event):
        self.Close()
