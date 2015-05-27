#Boa:Frame:pecah_keluarga

import os
import wx
import wx.lib.buttons
import data_penduduk
import sqlite3
import string
import gettext
import peringatan
import input_profil


db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return pecah_keluarga(parent)

[wxID_PECAH_KELUARGA, wxID_PECAH_KELUARGAALAMAT_BARU, 
 wxID_PECAH_KELUARGACARI_KK, wxID_PECAH_KELUARGADOKUMEN, 
 wxID_PECAH_KELUARGADUSUN_BARU, wxID_PECAH_KELUARGAINPUT_ALAMAT, 
 wxID_PECAH_KELUARGAINPUT_AYAH, wxID_PECAH_KELUARGAINPUT_DUSUN, 
 wxID_PECAH_KELUARGAINPUT_IBU, wxID_PECAH_KELUARGAINPUT_NAMA, 
 wxID_PECAH_KELUARGAINPUT_NIK, wxID_PECAH_KELUARGAINPUT_NO, 
 wxID_PECAH_KELUARGAINPUT_NO_KK, wxID_PECAH_KELUARGAINPUT_RT, 
 wxID_PECAH_KELUARGAINPUT_RW, wxID_PECAH_KELUARGAINPUT_TEMPAT_LAHIR, 
 wxID_PECAH_KELUARGAISIPENDUDUK, wxID_PECAH_KELUARGAKEMBALI, 
 wxID_PECAH_KELUARGAKK_BARU, wxID_PECAH_KELUARGALABEL_AGAMA, 
 wxID_PECAH_KELUARGALABEL_ALAMAT, wxID_PECAH_KELUARGALABEL_DATA_PENDUDUK, 
 wxID_PECAH_KELUARGALABEL_DIFABELITAS, wxID_PECAH_KELUARGALABEL_DUSUN, 
 wxID_PECAH_KELUARGALABEL_GOLONGAN_DARAH, 
 wxID_PECAH_KELUARGALABEL_JENIS_KELAMIN, 
 wxID_PECAH_KELUARGALABEL_KEWARGANEGARAAN, 
 wxID_PECAH_KELUARGALABEL_KONTRASEPSI, wxID_PECAH_KELUARGALABEL_NAMA_AYAH, 
 wxID_PECAH_KELUARGALABEL_NAMA_IBU, wxID_PECAH_KELUARGALABEL_NAMA_LENGKAP, 
 wxID_PECAH_KELUARGALABEL_NOMOR_KK, wxID_PECAH_KELUARGALABEL_PEKERJAAN, 
 wxID_PECAH_KELUARGALABEL_PEKERJAAN_LAINNYA, 
 wxID_PECAH_KELUARGALABEL_PENDIDIKAN_TEMPUH, 
 wxID_PECAH_KELUARGALABEL_PENDIDIKAN_TERAKHIR, 
 wxID_PECAH_KELUARGALABEL_RESIKO_KEHAMILAN, wxID_PECAH_KELUARGALABEL_SHDK, 
 wxID_PECAH_KELUARGALABEL_STATUS_KEPENDUDUKAN, 
 wxID_PECAH_KELUARGALABEL_STATUS_PERKAWINAN, 
 wxID_PECAH_KELUARGALABEL_STATUS_TINGGAL, 
 wxID_PECAH_KELUARGALABEL_TANGGAL_LAHIR, 
 wxID_PECAH_KELUARGALABEL_TEMPAT_LAHIR, wxID_PECAH_KELUARGALEBEL_NIK, 
 wxID_PECAH_KELUARGANAMA_KK, wxID_PECAH_KELUARGAPILIHAN_AGAMA, 
 wxID_PECAH_KELUARGAPILIHAN_DIFABELITAS, 
 wxID_PECAH_KELUARGAPILIHAN_GOLONGAN_DARAH, 
 wxID_PECAH_KELUARGAPILIHAN_JENIS_KELAMIN, 
 wxID_PECAH_KELUARGAPILIHAN_KEHAMILAN, wxID_PECAH_KELUARGAPILIHAN_KONTRASEPSI, 
 wxID_PECAH_KELUARGAPILIHAN_PEKERJAAN, 
 wxID_PECAH_KELUARGAPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_PECAH_KELUARGAPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_PECAH_KELUARGAPILIHAN_PENDIDIKAN_TERAKHIR, 
 wxID_PECAH_KELUARGAPILIHAN_SHDK, wxID_PECAH_KELUARGAPILIHAN_STATUS, 
 wxID_PECAH_KELUARGAPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_PECAH_KELUARGAPILIHAN_STATUS_TINGGAL, 
 wxID_PECAH_KELUARGAPILIHAN_WARGANEGARA, wxID_PECAH_KELUARGART_BARU, 
 wxID_PECAH_KELUARGARW_BARU, wxID_PECAH_KELUARGASIMPANGAMBAR, 
 wxID_PECAH_KELUARGASTATICTEXT1, wxID_PECAH_KELUARGASTATICTEXT2, 
 wxID_PECAH_KELUARGASTATICTEXT3, wxID_PECAH_KELUARGASTATICTEXT4, 
 wxID_PECAH_KELUARGASTATICTEXT5, wxID_PECAH_KELUARGASTATICTEXT6, 
 wxID_PECAH_KELUARGASTATICTEXT7, wxID_PECAH_KELUARGASTATICTEXT8, 
 wxID_PECAH_KELUARGASTATICTEXT9, wxID_PECAH_KELUARGATANGGAL_LAHIR, 
 wxID_PECAH_KELUARGATGLLAHIR, wxID_PECAH_KELUARGATOMBOL_CARI, 
 wxID_PECAH_KELUARGATOMBOL_TAMBAH_DATA, 
] = [wx.NewId() for _init_ctrls in range(76)]

class pecah_keluarga(wx.Dialog):
    def _init_coll_isipenduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor NIK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Lengkap', width=250)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=260)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Dusun',
              width=100)
        parent.InsertColumn(col=4, format=wx.LIST_FORMAT_LEFT, heading='RT',
              width=40)
        parent.InsertColumn(col=5, format=wx.LIST_FORMAT_LEFT, heading='RW',
              width=40)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_PECAH_KELUARGA, name=u'pecah_keluarga',
              parent=prnt, pos=wx.Point(406, 79), size=wx.Size(888, 639),
              style=wx.FRAME_NO_TASKBAR, title=u'Pecah Keluarga')
        self.SetClientSize(wx.Size(888, 639))
        self.Center(wx.BOTH)

        self.label_nomor_kk = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(8, 152), size=wx.Size(168, 17), style=0)

        self.label_alamat = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(256, 152), size=wx.Size(47, 17), style=0)

        self.label_dusun = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_DUSUN,
              label=u'Dusun', name=u'label_dusun', parent=self,
              pos=wx.Point(552, 152), size=wx.Size(144, 17), style=0)

        self.lebel_nik = wx.StaticText(id=wxID_PECAH_KELUARGALEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(192, 192), size=wx.Size(40, 17), style=0)

        self.label_tempat_lahir = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(192, 312), size=wx.Size(176, 17), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(192, 352), size=wx.Size(152, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(192, 392), size=wx.Size(200, 17),
              style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(192, 232), size=wx.Size(98, 17), style=0)

        self.label_jenis_kelamin = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(152, 17), style=0)

        self.label_agama = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 192), size=wx.Size(120, 17), style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(8, 168),
              size=wx.Size(240, 25), style=wx.TE_READONLY, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(256, 168),
              size=wx.Size(288, 25), style=wx.TE_READONLY, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(552, 168),
              size=wx.Size(192, 25), style=wx.TE_READONLY, value=u'')

        self.input_rt = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_RT,
              name=u'input_rt', parent=self, pos=wx.Point(752, 168),
              size=wx.Size(56, 27), style=0, value=u'')

        self.input_rw = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_RW,
              name=u'input_rw', parent=self, pos=wx.Point(816, 168),
              size=wx.Size(56, 27), style=0, value=u'')

        self.input_nik = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(192, 208),
              size=wx.Size(200, 25), style=0, value=u'')

        self.input_nama = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(192, 248),
              size=wx.Size(200, 25), style=0, value=u'')

        self.pilihan_jenis_kelamin = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(192,
              288), size=wx.Size(200, 27), style=wx.TE_READONLY)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(192, 328),
              size=wx.Size(200, 25), style=0, value=u'')

        self.tanggal_lahir = wx.TextCtrl(id=wxID_PECAH_KELUARGATANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(192, 368),
              size=wx.Size(200, 26), style=wx.TE_READONLY)

        self.pilihan_golongan_darah = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(192,
              408), size=wx.Size(80, 25), style=wx.TE_READONLY)

        self.pilihan_agama = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_AGAMA,
              name=u'pilihan_agama', parent=self, pos=wx.Point(400, 208),
              size=wx.Size(216, 25), style=wx.TE_READONLY)

        self.label_kewarganegaraan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 232), size=wx.Size(168, 17),
              style=0)

        self.pilihan_warganegara = wx.TextCtrl(name=u'pilihan_warganegara',
              parent=self, pos=wx.Point(400, 248), size=wx.Size(216, 25),
              style=wx.TE_READONLY)

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 272), size=wx.Size(184, 17),
              style=0)

        self.pilihan_pendidikan_terakhir = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(400, 288), size=wx.Size(216, 25),
              style=wx.TE_READONLY)

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini Ditempuh',
              name=u'label_pendidikan_tempuh', parent=self, pos=wx.Point(400,
              312), size=wx.Size(264, 17), style=0)

        self.pilihan_pendidikan_ditempuh = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(400, 328), size=wx.Size(216, 25),
              style=wx.TE_READONLY)

        self.label_pekerjaan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 352), size=wx.Size(200, 17), style=0)

        self.pilihan_pekerjaan = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_PEKERJAAN,
              name=u'pilihan_pekerjaan', parent=self, pos=wx.Point(400, 370),
              size=wx.Size(216, 25), style=wx.TE_READONLY)

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(400, 392), size=wx.Size(168, 17),
              style=0)

        self.pilihan_pekerjaan_lainnya = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(400,
              408), size=wx.Size(216, 25), style=wx.TE_READONLY)

        self.label_status_perkawinan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(624, 192), size=wx.Size(176, 17),
              style=0)

        self.pilihan_status = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_STATUS,
              name=u'pilihan_status', parent=self, pos=wx.Point(624, 208),
              size=wx.Size(248, 25), style=wx.TE_READONLY)

        self.label_status_kependudukan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(624, 232), size=wx.Size(184, 17),
              style=0)

        self.pilihan_status_kependudukan = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(248, 25),
              style=wx.TE_READONLY)

        self.label_status_tinggal = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(624, 272), size=wx.Size(152, 17),
              style=0)

        self.pilihan_status_tinggal = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(624,
              288), size=wx.Size(248, 25), style=wx.TE_READONLY)

        self.label_difabelitas = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(624, 312), size=wx.Size(184, 17),
              style=0)

        self.pilihan_difabelitas = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_DIFABELITAS,
              name=u'pilihan_difabelitas', parent=self, pos=wx.Point(624, 328),
              size=wx.Size(248, 25), style=wx.TE_READONLY)

        self.label_kontrasepsi = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(624, 352), size=wx.Size(192, 17),
              style=0)

        self.pilihan_kontrasepsi = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(624, 368),
              size=wx.Size(248, 25), style=wx.TE_READONLY)

        self.pilihan_kehamilan = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(624, 408),
              size=wx.Size(248, 25), style=wx.TE_READONLY)

        self.kk_baru = wx.TextCtrl(id=wxID_PECAH_KELUARGAKK_BARU,
              name=u'kk_baru', parent=self, pos=wx.Point(144, 480),
              size=wx.Size(192, 27), style=0, value=u'')

        self.alamat_baru = wx.TextCtrl(id=wxID_PECAH_KELUARGAALAMAT_BARU,
              name=u'alamat_baru', parent=self, pos=wx.Point(392, 480),
              size=wx.Size(136, 27), style=0, value=u'')

        self.dusun_baru = wx.TextCtrl(id=wxID_PECAH_KELUARGADUSUN_BARU,
              name=u'dusun_baru', parent=self, pos=wx.Point(584, 480),
              size=wx.Size(104, 27), style=0, value=u'')

        self.rt_baru = wx.TextCtrl(id=wxID_PECAH_KELUARGART_BARU,
              name=u'rt_baru', parent=self, pos=wx.Point(712, 480),
              size=wx.Size(48, 27), style=0, value=u'')

        self.rw_baru = wx.TextCtrl(id=wxID_PECAH_KELUARGARW_BARU,
              name=u'rw_baru', parent=self, pos=wx.Point(800, 480),
              size=wx.Size(40, 27), style=0, value=u'')

        self.label_shdk = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_SHDK,
              label=u'Status Hubungan Dalam Keluarga', name=u'label_shdk',
              parent=self, pos=wx.Point(24, 536), size=wx.Size(320, 17),
              style=0)

        self.pilihan_shdk = wx.TextCtrl(id=wxID_PECAH_KELUARGAPILIHAN_SHDK,
              name=u'pilihan_shdk', parent=self, pos=wx.Point(24, 560),
              size=wx.Size(304, 25), style=wx.TE_READONLY,
              value=u'Kepala Keluarga')

        self.label_nama_ayah = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(344, 536), size=wx.Size(152, 17), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(344, 560),
              size=wx.Size(280, 25), style=0, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(632, 536), size=wx.Size(160, 17), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(632, 560),
              size=wx.Size(240, 25), style=0, value=u'')

        self.label_resiko_kehamilan = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_RESIKO_KEHAMILAN,
              label=u'Resiko Kehamilan', name=u'label_resiko_kehamilan',
              parent=self, pos=wx.Point(624, 392), size=wx.Size(176, 17),
              style=0)

        self.tombol_tambah_data = wx.Button(id=wxID_PECAH_KELUARGATOMBOL_TAMBAH_DATA,
              label=u'Tambah Data', name=u'tombol_tambah_data', parent=self,
              pos=wx.Point(224, 600), size=wx.Size(200, 32), style=0)
        self.tombol_tambah_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_dataButton,
              id=wxID_PECAH_KELUARGATOMBOL_TAMBAH_DATA)

        self.kembali = wx.Button(id=wxID_PECAH_KELUARGAKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(440, 600), size=wx.Size(208, 32), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_PECAH_KELUARGAKEMBALI)

        self.dokumen = wx.StaticText(id=wxID_PECAH_KELUARGADOKUMEN,
              label=u'Perubahan Pecah KK', name=u'dokumen', parent=self,
              pos=wx.Point(24, 440), size=wx.Size(304, 17), style=0)

        self.label_data_penduduk = wx.StaticText(id=wxID_PECAH_KELUARGALABEL_DATA_PENDUDUK,
              label=u'FORM DATA PENDUDUK', name=u'label_data_penduduk',
              parent=self, pos=wx.Point(336, 0), size=wx.Size(216, 17),
              style=0)

        self.isipenduduk = wx.ListCtrl(id=wxID_PECAH_KELUARGAISIPENDUDUK,
              name=u'isipenduduk', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(856, 104), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)
        self.isipenduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected,
              id=wxID_PECAH_KELUARGAISIPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT1,
              label=u'Nomor NIK', name='staticText1', parent=self,
              pos=wx.Point(456, 128), size=wx.Size(145, 17), style=0)

        self.cari_kk = wx.TextCtrl(id=wxID_PECAH_KELUARGACARI_KK,
              name=u'cari_kk', parent=self, pos=wx.Point(552, 128),
              size=wx.Size(224, 24), style=0, value='')

        self.tombol_cari = wx.Button(id=wxID_PECAH_KELUARGATOMBOL_CARI,
              label=u'Cari', name=u'tombol_cari', parent=self, pos=wx.Point(784,
              128), size=wx.Size(85, 24), style=0)
        self.tombol_cari.Bind(wx.EVT_BUTTON, self.OnTombol_cariButton,
              id=wxID_PECAH_KELUARGATOMBOL_CARI)

        self.input_no = wx.TextCtrl(id=wxID_PECAH_KELUARGAINPUT_NO,
              name=u'input_no', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(56, 27), style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT2,
              label=u'RT', name='staticText2', parent=self, pos=wx.Point(760,
              152), size=wx.Size(24, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT3,
              label=u'RW', name='staticText3', parent=self, pos=wx.Point(824,
              152), size=wx.Size(19, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT4,
              label=u'Nomor KK Menjadi', name='staticText4', parent=self,
              pos=wx.Point(16, 488), size=wx.Size(118, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT5,
              label=u'Alamat', name='staticText5', parent=self,
              pos=wx.Point(344, 488), size=wx.Size(47, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT6,
              label=u'Dusun', name='staticText6', parent=self, pos=wx.Point(536,
              488), size=wx.Size(42, 17), style=0)

        self.staticText7 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT7,
              label=u'RT', name='staticText7', parent=self, pos=wx.Point(696,
              488), size=wx.Size(15, 17), style=0)

        self.staticText8 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT8,
              label=u'RW', name='staticText8', parent=self, pos=wx.Point(776,
              488), size=wx.Size(19, 17), style=0)

        self.tgllahir = wx.TextCtrl(id=wxID_PECAH_KELUARGATGLLAHIR,
              name=u'tgllahir', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(112, 27), style=0, value=u'')

        self.nama_kk = wx.TextCtrl(id=wxID_PECAH_KELUARGANAMA_KK,
              name=u'nama_kk', parent=self, pos=wx.Point(8, 208),
              size=wx.Size(176, 27), style=0, value=u'')

        self.staticText9 = wx.StaticText(id=wxID_PECAH_KELUARGASTATICTEXT9,
              label=u'Nama Kepala Keluarga', name='staticText9', parent=self,
              pos=wx.Point(8, 192), size=wx.Size(135, 17), style=0)

        self.simpangambar = wx.TextCtrl(id=wxID_PECAH_KELUARGASIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        self.awal()
    
   
    def awal(self):
        self.loadgambar()
        self.IsiDaftar()
        self.input_no_kk.SetValue('')
        self.input_alamat.SetValue('')
        self.input_dusun.SetValue('')
        self.input_rt.SetValue('')
        self.input_rw.SetValue('')
        self.input_nik.SetValue('')
        self.input_nama.SetValue('')
        self.pilihan_jenis_kelamin.SetValue('')
        self.input_tempat_lahir.SetValue('')
        self.tanggal_lahir.SetValue('')
        self.pilihan_golongan_darah.SetValue('')
        self.pilihan_agama.SetValue('')
        self.pilihan_warganegara.SetValue('')
        self.pilihan_pendidikan_terakhir.SetValue('')
        self.pilihan_pendidikan_ditempuh.SetValue('')
        self.pilihan_pekerjaan.SetValue('')
        self.pilihan_pekerjaan_lainnya.SetValue('')
        self.pilihan_status.SetValue('')
        self.pilihan_status_kependudukan.SetValue('')
        self.pilihan_status_tinggal.SetValue('')
        self.pilihan_difabelitas.SetValue('')
        self.pilihan_kontrasepsi.SetValue('')
        self.pilihan_kehamilan.SetValue('')
        self.pilihan_shdk.SetValue('Kepala Keluarga')
        self.input_ayah.SetValue('')
        self.input_ibu.SetValue('')
        self.kk_baru.SetValue('')
        self.alamat_baru.SetValue('')
        self.dusun_baru.SetValue('')
        self.rt_baru.SetValue('')
        self.rw_baru.SetValue('')
        self.input_no.SetValue('')
        self.cari_kk.SetValue('')
        self.nama_kk.SetValue('')
       
        
    def IsiDaftar(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE shdk<>'Kepala Keluarga' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[29])
            self.isipenduduk.SetStringItem(nokk,4,"%s"%i[26]) 
            self.isipenduduk.SetStringItem(nokk,5,"%s"%i[27])
            nokk = nokk + 1
                
    def Isi_Object(self) : 
        carikk=str(self.cari_kk.GetValue())
        sql="SELECT * FROM penduduk WHERE nik='%s'"%(carikk)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.input_no_kk.SetValue(str(hasil[16]))
            self.nama_kk.SetValue(str(hasil[17])) 
            self.input_alamat.SetValue(str(hasil[21]))
            self.input_dusun.SetValue(str(hasil[29]))
            self.input_rt.SetValue(str(hasil[26]))
            self.input_rw.SetValue(str(hasil[27]))
            self.input_nik.SetValue(str(hasil[1]))
            self.input_nama.SetValue(str(hasil[2]))
            self.pilihan_jenis_kelamin.SetValue(str(hasil[3]))
            self.input_tempat_lahir.SetValue(str(hasil[4]))
            self.tanggal_lahir.SetValue(str(hasil[5]))
            self.pilihan_golongan_darah.SetValue(str(hasil[7]))
            self.pilihan_agama.SetValue(str(hasil[8]))
            self.pilihan_warganegara.SetValue(str(hasil[28]))
            self.pilihan_pendidikan_terakhir.SetValue(str(hasil[12]))
            self.pilihan_pendidikan_ditempuh.SetValue(str(hasil[31]))
            self.pilihan_pekerjaan.SetValue(str(hasil[13]))
            self.pilihan_pekerjaan_lainnya.SetValue(str(hasil[19]))
            self.pilihan_status.SetValue(str(hasil[9]))
            self.pilihan_status_kependudukan.SetValue(str(hasil[32]))
            self.pilihan_status_tinggal.SetValue(str(hasil[33]))
            self.pilihan_difabelitas.SetValue(str(hasil[34]))
            self.pilihan_kontrasepsi.SetValue(str(hasil[35]))
            self.pilihan_kehamilan.SetValue(str(hasil[36]))
            self.input_ayah.SetValue(str(hasil[15]))
            self.input_ibu.SetValue(str(hasil[14]))
            self.simpangambar.SetValue(str(hasil[57]))
            self.input_no.SetValue(str(hasil[0]))
            self.viewgambar()
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.cari_kk.Clear()
            self.cari_kk.SetFocus()
        
    def loadgambar(self):
        self.PhotoMaxSize = 130
        img = wx.EmptyImage(120,130)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(52, 251))
    
    def OnTombol_kembali_kemenuButton(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()
        self.Destroy()

    def OnTombol_tambah_dataButton(self, event):
    
        nokk = str(self.kk_baru.GetValue())
        nama = str(self.input_nama.GetValue())
        alamat = str(self.alamat_baru.GetValue())
        dusun = str(self.dusun_baru.GetValue())
        rt = str(self.rt_baru.GetValue())
        rw = str(self.rw_baru.GetValue())
        inputno = str(self.input_no.GetValue())
        
        if  nokk == '':
            self.pesan = wx.MessageDialog(self,"Nomor Kartu Keluarga Baru Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        else:
            add_keluarga="UPDATE penduduk SET no_kk='"+(nokk)+"', nama_kep_kel='"+(nama)+"', alamat='"+(alamat)+"', nama_dusun='"+(dusun)+"', rt='"+(rt)+"', rw='"+(rw)+"', shdk='Kepala Keluarga'  WHERE no='"+(inputno)+"'"        
            cur.execute(add_keluarga)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.awal()

    def OnKembaliButton(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()
        self.Destroy()

    def OnTombol_cariButton(self, event):
        self.Isi_Object()
   
    def OnIsipendudukListItemSelected(self, event):
        self.currentItem = event.m_itemIndex
        b=self.isipenduduk.GetItem(self.currentItem).GetText()
        self.cari_kk.SetValue(b) 
        self.Isi_Object()
        event.Skip()
        
    def viewgambar(self):
        filepath=self.simpangambar.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
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
