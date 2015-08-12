#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import frm_sideka_menu
modules ={u'bantuan': [0, u'bantuan', u'bantuan.py'],
 u'cari_administrasi': [0, '', u'cari_administrasi.py'],
 u'cari_kemiskinan': [0, '', u'cari_kemiskinan.py'],
 u'cari_penduduk': [0, '', u'cari_penduduk.py'],
 u'data_penduduk': [0, '', u'data_penduduk.py'],
 u'edir_surat_masuk': [0, '', u'edir_surat_masuk.py'],
 u'edit_anggota': [0, '', u'edit_anggota.py'],
 u'edit_data_kemiskinan': [0, '', u'edit_data_kemiskinan.py'],
 u'edit_data_penduduk': [0, '', u'edit_data_penduduk.py'],
 u'edit_kejadian_kelahiran': [0, '', u'edit_kejadian_kelahiran.py'],
 u'edit_kejadian_kematian': [0, '', u'edit_kejadian_kematian.py'],
 u'edit_kejadian_lain': [0, '', u'edit_kejadian_lain.py'],
 u'edit_kejadian_pindah': [0, '', u'edit_kejadian_pindah.py'],
 u'edit_kk': [0, '', u'edit_kk.py'],
 u'edit_profil': [0, '', u'edit_profil.py'],
 u'edit_surat_keluar': [0, '', u'edit_surat_keluar.py'],
 u'frm_sideka_menu': [1, 'Main frame of Application', u'frm_sideka_menu.py'],
 u'importdisdukcapil': [0, '', u'importdisdukcapil.py'],
 u'importmitradesa': [0, '', u'importmitradesa.py'],
 u'input_administrasi_surat': [0, '', u'input_administrasi_surat.py'],
 u'input_data_kemiskinan': [0, '', u'input_data_kemiskinan.py'],
 u'input_edit_surat': [0, '', u'input_edit_surat.py'],
 u'input_indikator_kemiskinan': [0, '', u'input_indikator_kemiskinan.py'],
 u'input_profil': [0, '', u'input_profil.py'],
 u'kejadian_kelahiran': [0, '', u'kejadian_kelahiran.py'],
 u'kejadian_kematian': [0, '', u'kejadian_kematian.py'],
 u'kejadian_lain': [0, '', u'kejadian_lain.py'],
 u'kejadian_pindah': [0, '', u'kejadian_pindah.py'],
 u'keuangan': [0, '', u'keuangan.py'],
 u'kk_sementara': [0, '', u'kk_sementara.py'],
 u'kk_tetap': [0, '', u'kk_tetap.py'],
 u'kunci': [0, '', u'kunci.py'],
 u'laporan_administrasi': [0, '', u'laporan_administrasi.py'],
 u'laporan_kemiskinan': [0, '', u'laporan_kemiskinan.py'],
 u'laporan_penduduk': [0, '', u'laporan_penduduk.py'],
 u'laporan_potensi': [0, '', u'laporan_potensi.py'],
 u'laporan_profil': [0, '', u'laporan_profil.py'],
 u'laporan_statistik': [0, '', u'laporan_statistik.py'],
 u'pecah_keluarga': [0, '', u'pecah_keluarga.py'],
 u'pembuatan_surat_keluar': [0, '', u'pembuatan_surat_keluar.py'],
 u'penyusunan': [0, '', u'penyusunan.py'],
 u'pilihanimport': [0, '', u'pilihanimport.py'],
 u'piramidapenduduk': [0, '', u'piramidapenduduk.py'],
 u'potensi_ekonomi': [0, '', u'potensi_ekonomi.py'],
 u'potensi_lahan': [0, '', u'potensi_lahan.py'],
 u'potensi_pariwisata': [0, '', u'potensi_pariwisata.py'],
 u'potensi_tambak': [0, '', u'potensi_tambak.py'],
 u'sinkron_data': [0, '', u'sinkron_data.py'],
 u'statistik_administrasi': [0, '', u'statistik_administrasi.py'],
 u'statistik_kemiskinan': [0, '', u'statistik_kemiskinan.py'],
 u'statistik_penduduk': [0, '', u'statistik_penduduk.py'],
 u'statistik_potensi': [0, '', u'statistik_potensi.py'],
 u'surat_masuk': [0, '', u'surat_masuk.py'],
 u'tambah_anggota_keluarga': [0, '', u'tambah_anggota_keluarga.py']}

class MySplashScreen(wx.SplashScreen):
    """
Create a splash screen widget.
    """
    def __init__(self, parent=None):
        aBitmap = wx.Image(name = "/opt/sidesa/png/1.png").ConvertToBitmap()
        aBitmap1 = wx.Image(name = "/opt/sidesa/png/1.png").ConvertToBitmap()
        splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT
        splashDuration = 2000 # milliseconds
        wx.SplashScreen.__init__(self, aBitmap1, splashStyle,
                                 splashDuration, parent)
                
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        wx.Yield()

    def OnExit(self, evt):
        self.Hide()
        self.main = frm_sideka_menu.create(None)
        self.main.Show()
        evt.Skip()  # Make sure the default handler runs too...

class BoaApp(wx.App):
    def OnInit(self):
        #self.main = frm_sideka_menu.create(None)
        #self.main.Show()
        #self.SetTopWindow(self.main)
        MySplash = MySplashScreen()
        MySplash.Show()
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()

