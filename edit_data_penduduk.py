#Boa:Frame:edit_penduduk

import wx
import wx.lib.buttons
import frm_sideka_menu
import edit_kejadian_kelahiran
import edit_kejadian_kematian
import edit_kejadian_lain
import edit_kejadian_pindah
import edit_kk
import edit_anggota

def create(parent):
    return edit_penduduk(parent)

[wxID_EDIT_PENDUDUK, wxID_EDIT_PENDUDUKKOTAK_PERISTIWA, 
 wxID_EDIT_PENDUDUKTBL_EDIT_ANGGOTA, wxID_EDIT_PENDUDUKTBL_EDIT_KK, 
 wxID_EDIT_PENDUDUKTOMBOL_KELAHIRAN, wxID_EDIT_PENDUDUKTOMBOL_KEMATIAN, 
 wxID_EDIT_PENDUDUKTOMBOL_KE_MENU_UTAMA, 
 wxID_EDIT_PENDUDUKTOMBOL_PERISTIWA_LAIN, wxID_EDIT_PENDUDUKTOMBOL_PINDAH, 
] = [wx.NewId() for _init_ctrls in range(9)]

class edit_penduduk(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_EDIT_PENDUDUK, name=u'edit_penduduk',
              parent=prnt, pos=wx.Point(624, 300), size=wx.Size(455, 213),
              style=wx.FRAME_NO_TASKBAR, title=u'Edit Data Penduduk')
        self.SetClientSize(wx.Size(455, 213))
        self.Center(wx.BOTH)

        self.kotak_peristiwa = wx.StaticBox(id=wxID_EDIT_PENDUDUKKOTAK_PERISTIWA,
              label=u'Data Yang Di Edit', name=u'kotak_peristiwa', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(416, 150), style=0)

        self.tbl_edit_kk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTBL_EDIT_KK, label=u'Edit Kartu Keluarga',
              name=u'tbl_edit_kk', parent=self, pos=wx.Point(24, 40),
              size=wx.Size(184, 31), style=0)
        self.tbl_edit_kk.Bind(wx.EVT_BUTTON, self.OnTbl_edit_kkButton,
              id=wxID_EDIT_PENDUDUKTBL_EDIT_KK)

        self.tbl_edit_anggota = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTBL_EDIT_ANGGOTA,
              label=u'Edit Anggota Keluarga', name=u'tbl_edit_anggota',
              parent=self, pos=wx.Point(24, 80), size=wx.Size(184, 31),
              style=0)
        self.tbl_edit_anggota.Bind(wx.EVT_BUTTON, self.OnTbl_edit_anggotaButton,
              id=wxID_EDIT_PENDUDUKTBL_EDIT_ANGGOTA)

        self.tombol_kelahiran = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_KELAHIRAN, label=u'Edit Kelahiran',
              name=u'tombol_kelahiran', parent=self, pos=wx.Point(24, 120),
              size=wx.Size(184, 31), style=0)
        self.tombol_kelahiran.Bind(wx.EVT_BUTTON, self.OnTombol_kelahiranButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_KELAHIRAN)

        self.tombol_kematian = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_KEMATIAN, label=u'Edit Kematian',
              name=u'tombol_kematian', parent=self, pos=wx.Point(240, 40),
              size=wx.Size(184, 31), style=0)
        self.tombol_kematian.Bind(wx.EVT_BUTTON, self.OnTombol_kematianButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_KEMATIAN)

        self.tombol_pindah = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_PINDAH, label=u'Edit Pindah',
              name=u'tombol_pindah', parent=self, pos=wx.Point(240, 80),
              size=wx.Size(184, 31), style=0)
        self.tombol_pindah.Bind(wx.EVT_BUTTON, self.OnTombol_pindahButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_PINDAH)

        self.tombol_peristiwa_lain = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_PERISTIWA_LAIN,
              label=u'Edit Peristiwa Lain', name=u'tombol_peristiwa_lain',
              parent=self, pos=wx.Point(240, 118), size=wx.Size(184, 31),
              style=0)
        self.tombol_peristiwa_lain.Bind(wx.EVT_BUTTON,
              self.OnTombol_peristiwa_lainButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_PERISTIWA_LAIN)

        self.tombol_ke_menu_utama = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_EDIT_PENDUDUKTOMBOL_KE_MENU_UTAMA,
              label=u'Kembali Ke Menu Utama', name=u'tombol_ke_menu_utama',
              parent=self, pos=wx.Point(136, 176), size=wx.Size(208, 31),
              style=0)
        self.tombol_ke_menu_utama.Bind(wx.EVT_BUTTON,
              self.OnTombol_ke_menu_utamaButton,
              id=wxID_EDIT_PENDUDUKTOMBOL_KE_MENU_UTAMA)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_kelahiranButton(self, event):
        self.main=edit_kejadian_kelahiran.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_kematianButton(self, event):
        self.main=edit_kejadian_kematian.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_pindahButton(self, event):
        self.main=edit_kejadian_pindah.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_peristiwa_lainButton(self, event):
        self.main=edit_kejadian_lain.create(None)
        self.main.Show()
        self.Close()


    def OnTombol_ke_menu_utamaButton(self, event):
        self.Close()
        event.Skip()

    

    def OnTbl_edit_kkButton(self, event):
        self.main=edit_kk.create(None)
        self.main.Show()
        self.Close()

    def OnTbl_edit_anggotaButton(self, event):
        self.main=edit_anggota.create(None)
        self.main.Show()
        self.Close()

   
