#Boa:Dialog:edit_kk

import os
import wx
import wx.lib.buttons
import edit_data_penduduk
import sqlite3
import string
import gettext
import peringatan
import shutil


db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return edit_kk(parent)

[wxID_EDIT_KK, wxID_EDIT_KKBUTTON1, wxID_EDIT_KKCARI_KK, wxID_EDIT_KKDESA, 
 wxID_EDIT_KKDOKUMEN, wxID_EDIT_KKDOKUMEN1, wxID_EDIT_KKDOKUMEN2, 
 wxID_EDIT_KKDOKUMEN3, wxID_EDIT_KKDOKUMEN4, wxID_EDIT_KKDOKUMEN5, 
 wxID_EDIT_KKDOKUMEN6, wxID_EDIT_KKDOKUMEN7, wxID_EDIT_KKDOKUMEN8, 
 wxID_EDIT_KKGAMBAR, wxID_EDIT_KKINPUT_ALAMAT, wxID_EDIT_KKINPUT_AYAH, 
 wxID_EDIT_KKINPUT_DUSUN, wxID_EDIT_KKINPUT_IBU, wxID_EDIT_KKINPUT_NAMA, 
 wxID_EDIT_KKINPUT_NIK, wxID_EDIT_KKINPUT_NO_KK, wxID_EDIT_KKINPUT_RT, 
 wxID_EDIT_KKINPUT_RW, wxID_EDIT_KKINPUT_TEMPAT_LAHIR, 
 wxID_EDIT_KKISIPENDUDUK, wxID_EDIT_KKKABUPATEN, wxID_EDIT_KKKECAMATAN, 
 wxID_EDIT_KKKEMBALI, wxID_EDIT_KKLABEL_AGAMA, wxID_EDIT_KKLABEL_ALAMAT, 
 wxID_EDIT_KKLABEL_DATA_PENDUDUK, wxID_EDIT_KKLABEL_DIFABELITAS, 
 wxID_EDIT_KKLABEL_DUSUN, wxID_EDIT_KKLABEL_GOLONGAN_DARAH, 
 wxID_EDIT_KKLABEL_JENIS_KELAMIN, wxID_EDIT_KKLABEL_KEWARGANEGARAAN, 
 wxID_EDIT_KKLABEL_KONTRASEPSI, wxID_EDIT_KKLABEL_NAMA_AYAH, 
 wxID_EDIT_KKLABEL_NAMA_IBU, wxID_EDIT_KKLABEL_NAMA_LENGKAP, 
 wxID_EDIT_KKLABEL_NOMOR_KK, wxID_EDIT_KKLABEL_PEKERJAAN, 
 wxID_EDIT_KKLABEL_PEKERJAAN_LAINNYA, wxID_EDIT_KKLABEL_PENDIDIKAN_TEMPUH, 
 wxID_EDIT_KKLABEL_PENDIDIKAN_TERAKHIR, wxID_EDIT_KKLABEL_RESIKO_KEHAMILAN, 
 wxID_EDIT_KKLABEL_SHDK, wxID_EDIT_KKLABEL_STATUS_KEPENDUDUKAN, 
 wxID_EDIT_KKLABEL_STATUS_PERKAWINAN, wxID_EDIT_KKLABEL_STATUS_TINGGAL, 
 wxID_EDIT_KKLABEL_TANGGAL_LAHIR, wxID_EDIT_KKLABEL_TEMPAT_LAHIR, 
 wxID_EDIT_KKLEBEL_NIK, wxID_EDIT_KKNAMA_KK, wxID_EDIT_KKNO, 
 wxID_EDIT_KKPILIHAN_AGAMA, wxID_EDIT_KKPILIHAN_DIFABELITAS, 
 wxID_EDIT_KKPILIHAN_GOLONGAN_DARAH, wxID_EDIT_KKPILIHAN_JENIS_KELAMIN, 
 wxID_EDIT_KKPILIHAN_KEHAMILAN, wxID_EDIT_KKPILIHAN_KONTRASEPSI, 
 wxID_EDIT_KKPILIHAN_PEKERJAAN, wxID_EDIT_KKPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_EDIT_KKPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_EDIT_KKPILIHAN_PENDIDIKAN_TERAKHIR, wxID_EDIT_KKPILIHAN_SHDK, 
 wxID_EDIT_KKPILIHAN_STATUS, wxID_EDIT_KKPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_EDIT_KKPILIHAN_STATUS_TINGGAL, wxID_EDIT_KKPILIHAN_WARGANEGARA, 
 wxID_EDIT_KKPROPINSI, wxID_EDIT_KKSIMPANGAMBAR, wxID_EDIT_KKSTATICTEXT1, 
 wxID_EDIT_KKSTATICTEXT2, wxID_EDIT_KKSTATICTEXT3, wxID_EDIT_KKSTATICTEXT4, 
 wxID_EDIT_KKSTATICTEXT5, wxID_EDIT_KKTANGGAL_LAHIR, wxID_EDIT_KKTGLLAHIR, 
 wxID_EDIT_KKTOMBOL_CARI, wxID_EDIT_KKTOMBOL_TAMBAH_DATA, 
] = [wx.NewId() for _init_ctrls in range(81)]

class edit_kk(wx.Dialog):
    def _init_coll_isipenduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor KK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Kepala Keluarga', width=250)
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
        wx.Dialog.__init__(self, id=wxID_EDIT_KK, name=u'edit_kk', parent=prnt,
              pos=wx.Point(406, 79), size=wx.Size(888, 639),
              style=wx.FRAME_NO_TASKBAR, title=u'Edit Kepala Keluarga')
        self.SetClientSize(wx.Size(888, 639))
        self.Center(wx.BOTH)

        self.label_nomor_kk = wx.StaticText(id=wxID_EDIT_KKLABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(8, 152), size=wx.Size(168, 17), style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_EDIT_KKINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(8, 168),
              size=wx.Size(240, 25), style=wx.TE_READONLY, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_EDIT_KKINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(256, 168),
              size=wx.Size(288, 25), style=wx.TE_READONLY, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_EDIT_KKINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(552, 168),
              size=wx.Size(192, 25), style=wx.TE_READONLY, value=u'')

        self.label_alamat = wx.StaticText(id=wxID_EDIT_KKLABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(256, 152), size=wx.Size(47, 17), style=0)

        self.label_dusun = wx.StaticText(id=wxID_EDIT_KKLABEL_DUSUN,
              label=u'Dusun', name=u'label_dusun', parent=self,
              pos=wx.Point(552, 152), size=wx.Size(144, 17), style=0)

        self.input_nik = wx.TextCtrl(id=wxID_EDIT_KKINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(192, 208),
              size=wx.Size(200, 25), style=0, value=u'')

        self.lebel_nik = wx.StaticText(id=wxID_EDIT_KKLEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(192, 192), size=wx.Size(40, 17), style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_EDIT_KKLABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(192, 232), size=wx.Size(98, 17), style=0)

        self.input_nama = wx.TextCtrl(id=wxID_EDIT_KKINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(192, 248),
              size=wx.Size(200, 25), style=0, value=u'')

        self.label_jenis_kelamin = wx.StaticText(id=wxID_EDIT_KKLABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(152, 17), style=0)

        self.pilihan_jenis_kelamin = wx.ComboBox(choices=['L',
              'P'], id=wxID_EDIT_KKPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(192,
              288), size=wx.Size(200, 27), style=0)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_EDIT_KKINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(192, 328),
              size=wx.Size(200, 25), style=0, value=u'')

        self.label_tempat_lahir = wx.StaticText(id=wxID_EDIT_KKLABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(192, 312), size=wx.Size(176, 17), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_EDIT_KKLABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(192, 352), size=wx.Size(152, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_EDIT_KKLABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(192, 392), size=wx.Size(200, 17),
              style=0)

        self.tanggal_lahir = wx.TextCtrl(id=wxID_EDIT_KKTANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(192, 368),
              size=wx.Size(200, 26), style=0, value=u'')

        self.pilihan_golongan_darah = wx.ComboBox(choices=['A', 'AB', 'B', 'O',
              'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-', 'Tidak tahu'],
              id=wxID_EDIT_KKPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(192,
              408), size=wx.Size(80, 25), style=0)

        self.label_agama = wx.StaticText(id=wxID_EDIT_KKLABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 192), size=wx.Size(120, 17), style=0)

        self.pilihan_agama = wx.ComboBox(choices=['Islam', 'Kristen Protestan',
              'Kristen Katolik', 'Hindu', 'Budha', 'Konghuchu',
              'Aliran Kepercayaan', 'Agama Lainnya'],
              id=wxID_EDIT_KKPILIHAN_AGAMA, name=u'pilihan_agama', parent=self,
              pos=wx.Point(400, 208), size=wx.Size(216, 25), style=0)

        self.label_kewarganegaraan = wx.StaticText(id=wxID_EDIT_KKLABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 232), size=wx.Size(168, 17),
              style=0)

        self.pilihan_warganegara = wx.ComboBox(choices=['WNI', 'WNA'],
              id=wxID_EDIT_KKPILIHAN_WARGANEGARA, name=u'pilihan_warganegara',
              parent=self, pos=wx.Point(400, 248), size=wx.Size(216, 25),
              style=0)

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_EDIT_KKLABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 272), size=wx.Size(184, 17),
              style=0)

        self.pilihan_pendidikan_terakhir = wx.ComboBox(choices=['Tidak/Belum Sekolah',
              'Tidak Tamat SD/Sederajat', 'Tamat SD/Sederajat',
              'SLTP/Sederajat', 'SLTA/Sederajat',
              'Diploma I/II',
              'Akademi/Diploma III/S. Muda',
              'Diploma IV/Strata I', 'Strata II', 'Strata III',
              'Pendidikan Non Formal'],
              id=wxID_EDIT_KKPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(400, 288), size=wx.Size(216, 25), style=0)

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_EDIT_KKLABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini Ditempuh',
              name=u'label_pendidikan_tempuh', parent=self, pos=wx.Point(400,
              312), size=wx.Size(264, 17), style=0)

        self.pilihan_pendidikan_ditempuh = wx.ComboBox(choices=['PAUD sederajat',
              'TK Sederajat', 'SD Sederajat', 'SLTP Sederajat',
              'SLTA Sederajat', 'D1 Sederajat', 'D2 Sederajat',
              'D3 Sederajat' , 'S1 Sederajat' , 'S2 Sederajat' ,
              'S3 Sederajat' , 'Pendidikan Non Formal'],
              id=wxID_EDIT_KKPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(400, 328), size=wx.Size(216, 25), style=0)

        self.label_pekerjaan = wx.StaticText(id=wxID_EDIT_KKLABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 352), size=wx.Size(200, 17), style=0)

        self.pilihan_pekerjaan = wx.ComboBox(choices=['Belum/Tidak Bekerja',
              'Mengurus Rumah Tangga', 'Pelajar/Mahasiswa', 'Pensiunan',
              'Pegawai Negeri Sipil', 'Tentara Nasional Indonesia',
              'Kepolisian RI', 'Perdagangan', 'Petani/Pekebun', 'Peternak',
              'Nelayan/Perikanan', 'Industri', 'Konstruksi', 'Transportasi',
              'Karyawan Swasta', 'Karyawan BUMN', 'Karyawan BUMD',
              'Karyawan Honorer', 'Buruh Harian Lepas',
              'Buruh Tani/Perkebunan', 'Buruh Nelayan/Perikanan',
              'Buruh Peternakan', 'Pembantu Rumah Tangga', 'Tukang Cukur',
              'Tukang Listrik', 'Tukang Batu', 'Tukang Kayu',
              'Tukang Sol Sepatu', 'Tukang Las/Pandai Besi', 'Tukang Jahit',
              'Penata Rambut', 'Penata Rias', 'Penata Busana', 'Mekanik',
              'Tukang Gigi', 'Seniman', 'Tabib', 'Paraji', 'Perancang Busana',
              'Penterjemah', 'Imam Masjid', 'Pendeta', 'Pastur', 'Wartawan',
              'Ustadz/Mubaligh', 'Juru Masak', 'Promotor Acara',
              'Anggota DPR-RI', 'Anggota DPD', 'Anggota BPK', 'Presiden',
              'Wakil Presiden', 'Anggota Mahkamah Konstitusi',
              'Anggota Kabinet/Kementerian', 'Duta Besar', 'Gubernur',
              'Wakil Gubernur', 'Bupati', 'Wakil Bupati', 'Walikota',
              'Wakil Walikota', 'Anggota DPRD Propinsi',
              'Anggota DPRD Kabupaten/Kota', 'Dosen', 'Guru', 'Pilot',
              'Pengacara', 'Notaris', 'Arsitek', 'Akuntan', 'Konsultan',
              'Dokter', 'Bidan', 'Perawat', 'Apoteker', 'Psikiater/Psikolog',
              'Penyiar Televisi', 'Penyiar Radio', 'Pelaut', 'Peneliti',
              'Sopir', 'Pialang', 'Paranormal', 'Pedagang', 'Perangkat Desa',
              'Kepala Desa', 'Biarawati', 'Wiraswasta', 'Buruh Migran'],
              id=wxID_EDIT_KKPILIHAN_PEKERJAAN, name=u'pilihan_pekerjaan',
              parent=self, pos=wx.Point(400, 370), size=wx.Size(216, 25),
              style=0)

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_EDIT_KKLABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(400, 392), size=wx.Size(168, 17),
              style=0)

        self.pilihan_pekerjaan_lainnya = wx.ComboBox(choices=['Berdagang',
              'Bertani', 'Berkebun', 'Jasa  profesional  tukang', 'Seniman',
              'Lainnya'], id=wxID_EDIT_KKPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(400,
              408), size=wx.Size(216, 25), style=0)

        self.label_status_perkawinan = wx.StaticText(id=wxID_EDIT_KKLABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(624, 192), size=wx.Size(176, 17),
              style=0)

        self.pilihan_status = wx.ComboBox(choices=['Belum Kawin', 'Kawin', 'Cerai Mati', 'Cerai Hidup'],
              id=wxID_EDIT_KKPILIHAN_STATUS, name=u'pilihan_status',
              parent=self, pos=wx.Point(624, 208), size=wx.Size(248, 25),
              style=0)

        self.label_status_kependudukan = wx.StaticText(id=wxID_EDIT_KKLABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(624, 232), size=wx.Size(184, 17),
              style=0)

        self.pilihan_status_kependudukan = wx.ComboBox(choices=['Penduduk Tetap',
              'Penduduk Sementara', 'Penduduk Pindah/Pindahan'],
              id=wxID_EDIT_KKPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(248, 25), style=0)

        self.label_status_tinggal = wx.StaticText(id=wxID_EDIT_KKLABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(624, 272), size=wx.Size(152, 17),
              style=0)

        self.pilihan_status_tinggal = wx.ComboBox(choices=['Tinggal Tetap',
              'Tinggal Di Luar Desa*', 'Tinggal Di Luar Kota/Kabupaten',
              'Tinggal Di Luar Propinsi', 'Tinggal Di Luar Negeri'],
              id=wxID_EDIT_KKPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(624,
              288), size=wx.Size(248, 25), style=0)

        self.label_difabelitas = wx.StaticText(id=wxID_EDIT_KKLABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(624, 312), size=wx.Size(184, 17),
              style=0)

        self.pilihan_difabelitas = wx.ComboBox(choices=['Tidak cacat',
              'Cacat Fisik', 'Cacat Netra/Buta', 'Cacat Rungu/Wicara',
              'Cacat Mental/Jiwa', 'Cacat Fisik/Mental', 'Cacat Lainnya'],
              id=wxID_EDIT_KKPILIHAN_DIFABELITAS, name=u'pilihan_difabelitas',
              parent=self, pos=wx.Point(624, 328), size=wx.Size(248, 25),
              style=0)

        self.label_kontrasepsi = wx.StaticText(id=wxID_EDIT_KKLABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(624, 352), size=wx.Size(192, 17),
              style=0)

        self.pilihan_kontrasepsi = wx.ComboBox(choices=['Pil', 'Suntik', 'IUD',
              'Kondom', 'Implant', 'MOP'], id=wxID_EDIT_KKPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(624, 368),
              size=wx.Size(248, 25), style=0)

        self.label_shdk = wx.StaticText(id=wxID_EDIT_KKLABEL_SHDK,
              label=u'Status Hubungan Dalam Keluarga', name=u'label_shdk',
              parent=self, pos=wx.Point(24, 536), size=wx.Size(320, 17),
              style=0)

        self.pilihan_shdk = wx.ComboBox(choices=['Anak', 'Istri', 'Suami',
              'Mertua', 'Menantu', 'Famili lain', 'Lainnya'],
              id=wxID_EDIT_KKPILIHAN_SHDK, name=u'pilihan_shdk', parent=self,
              pos=wx.Point(24, 560), size=wx.Size(304, 25), style=0)

        self.label_nama_ayah = wx.StaticText(id=wxID_EDIT_KKLABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(344, 536), size=wx.Size(152, 17), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_EDIT_KKINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(344, 560),
              size=wx.Size(280, 25), style=0, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_EDIT_KKLABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(632, 536), size=wx.Size(160, 17), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_EDIT_KKINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(632, 560),
              size=wx.Size(240, 25), style=0, value=u'')

        self.label_resiko_kehamilan = wx.StaticText(id=wxID_EDIT_KKLABEL_RESIKO_KEHAMILAN,
              label=u'Resiko Kehamilan', name=u'label_resiko_kehamilan',
              parent=self, pos=wx.Point(624, 392), size=wx.Size(176, 17),
              style=0)

        self.pilihan_kehamilan = wx.ComboBox(choices=['Resiko Tinggi',
              'Tidak Resiko Tinggi'], id=wxID_EDIT_KKPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(624, 408),
              size=wx.Size(248, 25), style=0)

        self.tombol_tambah_data = wx.Button(id=wxID_EDIT_KKTOMBOL_TAMBAH_DATA,
              label=u'Tambah Data', name=u'tombol_tambah_data', parent=self,
              pos=wx.Point(232, 600), size=wx.Size(200, 32), style=0)
        self.tombol_tambah_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_dataButton,
              id=wxID_EDIT_KKTOMBOL_TAMBAH_DATA)

        self.kembali = wx.Button(id=wxID_EDIT_KKKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(456, 600), size=wx.Size(208, 32), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_EDIT_KKKEMBALI)

        self.dokumen = wx.StaticText(id=wxID_EDIT_KKDOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'dokumen', parent=self,
              pos=wx.Point(24, 440), size=wx.Size(304, 17), style=0)

        self.label_data_penduduk = wx.StaticText(id=wxID_EDIT_KKLABEL_DATA_PENDUDUK,
              label=u'FORM DATA PENDUDUK', name=u'label_data_penduduk',
              parent=self, pos=wx.Point(336, 0), size=wx.Size(216, 17),
              style=0)

        self.isipenduduk = wx.ListCtrl(id=wxID_EDIT_KKISIPENDUDUK,
              name=u'isipenduduk', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(856, 104), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)
        self.isipenduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected, id=wxID_EDIT_KKISIPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_EDIT_KKSTATICTEXT1,
              label=u'Nomor Kartu Keluarga', name='staticText1', parent=self,
              pos=wx.Point(400, 128), size=wx.Size(145, 15), style=0)

        self.cari_kk = wx.TextCtrl(id=wxID_EDIT_KKCARI_KK, name=u'cari_kk',
              parent=self, pos=wx.Point(552, 128), size=wx.Size(224, 24),
              style=0, value='')

        self.tombol_cari = wx.Button(id=wxID_EDIT_KKTOMBOL_CARI, label=u'Cari',
              name=u'tombol_cari', parent=self, pos=wx.Point(784, 128),
              size=wx.Size(85, 24), style=0)
        self.tombol_cari.Bind(wx.EVT_BUTTON, self.OnTombol_cariButton,
              id=wxID_EDIT_KKTOMBOL_CARI)

        self.input_rt = wx.TextCtrl(id=wxID_EDIT_KKINPUT_RT, name=u'input_rt',
              parent=self, pos=wx.Point(752, 168), size=wx.Size(56, 27),
              style=0, value=u'')

        self.input_rw = wx.TextCtrl(id=wxID_EDIT_KKINPUT_RW, name=u'input_rw',
              parent=self, pos=wx.Point(816, 168), size=wx.Size(56, 27),
              style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_EDIT_KKSTATICTEXT2,
              label=u'RT', name='staticText2', parent=self, pos=wx.Point(760,
              152), size=wx.Size(24, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_EDIT_KKSTATICTEXT3,
              label=u'RW', name='staticText3', parent=self, pos=wx.Point(824,
              152), size=wx.Size(19, 17), style=0)

        self.dokumen1 = wx.ComboBox(choices=['Akta Kelahiran'], id=wxID_EDIT_KKDOKUMEN1, name=u'dokumen1', parent=self,
              pos=wx.Point(24, 464), size=wx.Size(187, 27), style=0, value='')

        self.dokumen3 = wx.ComboBox(choices=['Akta Cerai'], id=wxID_EDIT_KKDOKUMEN3, name=u'dokumen3', parent=self,
              pos=wx.Point(224, 464), size=wx.Size(187, 27), style=0, value='')

        self.dokumen5 = wx.ComboBox(choices=['KTP Sementara'], id=wxID_EDIT_KKDOKUMEN5, name=u'dokumen5', parent=self,
              pos=wx.Point(424, 464), size=wx.Size(187, 27), style=0, value='')

        self.dokumen7 = wx.ComboBox(choices=['VISA'], id=wxID_EDIT_KKDOKUMEN7, name=u'dokumen7', parent=self,
              pos=wx.Point(632, 464), size=wx.Size(187, 27), style=0, value='')

        self.dokumen2 = wx.ComboBox(choices=['Akta Nikah'], id=wxID_EDIT_KKDOKUMEN2, name=u'dokumen2', parent=self,
              pos=wx.Point(24, 504), size=wx.Size(187, 27), style=0, value='')

        self.dokumen4 = wx.ComboBox(choices=['Akta Kematian'], id=wxID_EDIT_KKDOKUMEN4, name=u'dokumen4', parent=self,
              pos=wx.Point(224, 504), size=wx.Size(187, 27), style=0, value='')

        self.dokumen6 = wx.ComboBox(choices=['KITAS'], id=wxID_EDIT_KKDOKUMEN6, name=u'dokumen6', parent=self,
              pos=wx.Point(424, 504), size=wx.Size(187, 27), style=0, value='')

        self.dokumen8 = wx.ComboBox(choices=['Paspor'], id=wxID_EDIT_KKDOKUMEN8, name=u'dokumen8', parent=self,
              pos=wx.Point(632, 504), size=wx.Size(187, 27), style=0, value='')

        self.staticText4 = wx.StaticText(id=wxID_EDIT_KKSTATICTEXT4,
              label=u'Kode KK SMT- adalah NoKK Sementara', name='staticText4',
              parent=self, pos=wx.Point(16, 128), size=wx.Size(248, 17),
              style=0)

        self.tgllahir = wx.TextCtrl(id=wxID_EDIT_KKTGLLAHIR, name=u'tgllahir',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(112, 27),
              style=0, value=u'')

        self.nama_kk = wx.TextCtrl(id=wxID_EDIT_KKNAMA_KK, name=u'nama_kk',
              parent=self, pos=wx.Point(8, 208), size=wx.Size(176, 24),
              style=wx.TE_READONLY, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_EDIT_KKSTATICTEXT5,
              label=u'Nama Kepala Keluarga', name='staticText5', parent=self,
              pos=wx.Point(8, 192), size=wx.Size(135, 17), style=0)

        self.gambar = wx.TextCtrl(id=wxID_EDIT_KKGAMBAR, name=u'gambar',
              parent=self, pos=wx.Point(24, 368), size=wx.Size(152, 24),
              style=0, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_EDIT_KKSIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'/opt/sidesa/penduduk')

        self.button1 = wx.Button(id=wxID_EDIT_KKBUTTON1, label=u'Upload Photo',
              name='button1', parent=self, pos=wx.Point(24, 392),
              size=wx.Size(152, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_EDIT_KKBUTTON1)

        self.propinsi = wx.TextCtrl(id=wxID_EDIT_KKPROPINSI, name=u'propinsi',
              parent=self, pos=wx.Point(-100, -100), size=wx.Size(152, 24),
              style=0, value=u'')

        self.kabupaten = wx.TextCtrl(id=wxID_EDIT_KKKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kecamatan = wx.TextCtrl(id=wxID_EDIT_KKKECAMATAN,
              name=u'kecamatan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.desa = wx.TextCtrl(id=wxID_EDIT_KKDESA, name=u'desa', parent=self,
              pos=wx.Point(-100, -100), size=wx.Size(152, 24), style=0,
              value=u'')

        self.no = wx.TextCtrl(id=wxID_EDIT_KKNO, name=u'no', parent=self,
              pos=wx.Point(-100, -100), size=wx.Size(152, 24), style=0,
              value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.dataprofil()
        self.awal()  
    
    def awal(self):
        self.IsiList()
        self.loadgambar()
        self.input_no_kk.SetValue('')
        self.input_alamat.SetValue('')
        self.input_dusun.SetValue('')
        self.input_rt.SetValue('')
        self.input_rw.SetValue('')
        self.input_nik.SetValue('')
        self.input_nama.SetValue('')
        self.pilihan_jenis_kelamin.SetValue('')
        self.input_tempat_lahir.SetValue('')
        self.tgllahir.SetValue('')
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
        self.pilihan_shdk.SetValue('')
        self.input_ayah.SetValue('')
        self.input_ibu.SetValue('')
        self.dokumen1.SetValue('')
        self.dokumen2.SetValue('')
        self.dokumen3.SetValue('')
        self.dokumen4.SetValue('')
        self.dokumen5.SetValue('')
        self.dokumen6.SetValue('')
        self.dokumen7.SetValue('')
        self.dokumen8.SetValue('')
        self.gambar.SetValue('')
        self.cari_kk.SetValue('')
        self.nama_kk.SetValue('')
        self.simpangambar.SetValue('/opt/sidesa/penduduk/')    
        
    def OnGetDate(self, event):
        selected = self.tanggal_lahir.GetValue()
        month = selected.Month + 1
        day = selected.Day
        year = selected.Year
        date_str = "%02d/%02d/%4d" % (month, day, year)
        self.tgllahir.SetValue("{}".format(date_str))
                    
    def IsiList(self):
        self.isipenduduk.DeleteAllItems()      
        sql = "SELECT * FROM penduduk WHERE shdk='Kepala Keluarga' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[16]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[29])
            self.isipenduduk.SetStringItem(nokk,4,"%s"%i[26]) 
            self.isipenduduk.SetStringItem(nokk,5,"%s"%i[27])
            nokk = nokk + 1
     
    
    def Isi_Object(self) : 
        carikk=str(self.cari_kk.GetValue())
        sql="SELECT * FROM penduduk WHERE no_kk='%s' AND kematian='Tidak' AND shdk='Kepala Keluarga'"%(carikk)
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
            self.pilihan_shdk.SetValue(str(hasil[10]))
            self.input_ayah.SetValue(str(hasil[15]))
            self.input_ibu.SetValue(str(hasil[14]))
            self.gambar.SetValue(str(hasil[57]))
            self.dokumen1.SetValue(str(hasil[41]))
            self.dokumen2.SetValue(str(hasil[42]))
            self.dokumen3.SetValue(str(hasil[43]))
            self.dokumen4.SetValue(str(hasil[44]))
            self.dokumen5.SetValue(str(hasil[45]))
            self.dokumen6.SetValue(str(hasil[46]))
            self.dokumen7.SetValue(str(hasil[47]))
            self.dokumen8.SetValue(str(hasil[48]))
            self.no.SetValue(str(hasil[0]))
            self.viewgambar()
            
        else : 
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
            self.cari_kk.Clear()
            self.cari_kk.SetFocus()
        
   
    def OnTombol_kembali_kemenuButton(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()
        self.Destroy()
    
    def loadgambar(self):
        self.PhotoMaxSize = 100
        img = wx.EmptyImage(100,100)
        self.imageCtrl = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img),wx.Point(52, 251))
  
    def dataprofil(self) : 
        sql="SELECT * FROM identitas WHERE no=1"
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.propinsi.SetValue(str(hasil[18]))
            self.kabupaten.SetValue(str(hasil[17])) 
            self.kecamatan.SetValue(str(hasil[16]))
            self.desa.SetValue(str(hasil[15]))
            
        else : 
            self.pesan = wx.MessageDialog(self,"Cek Data Profil","Konfirmasi",wx.OK) 
            self.pesan.ShowModal() 
                

    def OnTombol_tambah_dataButton(self, event):
    
        nokk = str(self.input_no_kk.GetValue())
        nik = str(self.input_nik.GetValue())
        nama = str(self.input_nama.GetValue())
        tmplahir = str(self.input_tempat_lahir.GetValue())
        jk = str(self.pilihan_jenis_kelamin.GetValue())
        tgllahir = str(self.tanggal_lahir.GetValue())
        gdr = str(self.pilihan_golongan_darah.GetValue())
        agama = str(self.pilihan_agama.GetValue())
        warganegara = str(self.pilihan_warganegara.GetValue())
        pddkakhir = str(self.pilihan_pendidikan_terakhir.GetValue())
        pddktempuh = str(self.pilihan_pendidikan_ditempuh.GetValue())
        pekerjaan = str(self.pilihan_pekerjaan.GetValue())
        pekerjaanlain = str(self.pilihan_pekerjaan_lainnya.GetValue())
        status = str(self.pilihan_status.GetValue())
        statuskependudukan = str(self.pilihan_status_kependudukan.GetValue())
        statustinggal = str(self.pilihan_status_tinggal.GetValue())
        difabelitas = str(self.pilihan_difabelitas.GetValue())
        kontrasepsi = str(self.pilihan_kontrasepsi.GetValue())
        shdk = str(self.pilihan_shdk.GetValue())
        namakk = str(self.nama_kk.GetValue())
        ayah = str(self.input_ayah.GetValue())
        ibu = str(self.input_ibu.GetValue())
        kehamilan = str(self.pilihan_kehamilan.GetValue())
        alamat = str(self.input_alamat.GetValue())
        dusun = str(self.input_dusun.GetValue())
        rt = str(self.input_rt.GetValue())
        rw = str(self.input_rw.GetValue())
        dok1 = str(self.dokumen1.GetValue())
        dok2 = str(self.dokumen2.GetValue())
        dok3 = str(self.dokumen3.GetValue())
        dok4 = str(self.dokumen4.GetValue())
        dok5 = str(self.dokumen5.GetValue())
        dok6 = str(self.dokumen6.GetValue())
        dok7 = str(self.dokumen7.GetValue())
        dok8 = str(self.dokumen8.GetValue())
        nomor = str(self.no.GetValue())
        gbr = str(self.simpangambar.GetValue())
        filepath = str(self.gambar.GetValue())
        
        #dataprofilget
        propinsi = str(self.propinsi.GetValue())
        kabupaten = str(self.kabupaten.GetValue())
        kecamatan = str(self.kecamatan.GetValue())
        desa = str(self.desa.GetValue())
        
        if nokk == '':
            self.pesan = wx.MessageDialog(self,"Nomor Kartu Keluarga Jangan Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif nik == '':
            self.pesan = wx.MessageDialog(self,"NIK Tidak Boleh Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()
        elif nama == '':
            self.pesan = wx.MessageDialog(self,"Nama Tidak Boleh Kosong","Peringatan",wx.OK) 
            self.pesan.ShowModal()    
        
        elif filepath == '':
            add_keluarga="UPDATE penduduk SET nik='"+nik+"' , nama='"+nama+"' , jk='"+jk+"', tmpt_lahir='"+tmplahir+"', tgl_lahir='"+tgllahir+"', umur='', gdr='"+gdr+"', agama='"+agama+"', status='"+status+"', shdk='"+shdk+"', shdrt='', pddk_akhir='"+pddkakhir+"', pekerjaan='"+pekerjaan+"', nama_ibu='"+ibu+"', nama_ayah='"+ayah+"', no_kk='"+nokk+"', nama_kep_kel='"+namakk+"', petugas='"+''+"', pekerjaan_lain='"+pekerjaanlain+"', nama_petugas='"+''+"', alamat='"+alamat+"', nama_prop='"+propinsi+"', nama_kab='"+kabupaten+"', nama_kec='"+kecamatan+"', nama_kel='"+desa+"', rt='"+rt+"', rw='"+rw+"', warganegara='"+warganegara+"', nama_dusun='"+dusun+"', kemiskinan='Tidak Miskin', pddk_saat_ini='"+pddktempuh+"', status_pddk='"+statuskependudukan+"', status_tgl='"+statustinggal+"', difabelitas='"+difabelitas+"', kontrasepsi='"+kontrasepsi+"', resiko='"+kehamilan+"', kelahiran='', kematian='Tidak', kejadianlain='', pindah='', dok1='"+dok1+"', dok2='"+dok2+"', dok3='"+dok3+"', dok4='"+dok4+"', dok5='"+dok5+"', dok6='"+dok6+"', dok7='"+dok7+"', dok8='"+dok8+"', promis1='', promis2='',promis3='', promis4='', promis5='', promis6='', promis7='', promis8='', photo='"+gbr+"blank.jpg', keterangan='' WHERE no = '"+nomor+"'" 
            cur.execute(add_keluarga)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
        
        elif filepath == gbr+nik+'.jpg':
            add_keluarga="UPDATE penduduk SET nik='"+nik+"' , nama='"+nama+"' , jk='"+jk+"', tmpt_lahir='"+tmplahir+"', tgl_lahir='"+tgllahir+"', umur='', gdr='"+gdr+"', agama='"+agama+"', status='"+status+"', shdk='"+shdk+"', shdrt='', pddk_akhir='"+pddkakhir+"', pekerjaan='"+pekerjaan+"', nama_ibu='"+ibu+"', nama_ayah='"+ayah+"', no_kk='"+nokk+"', nama_kep_kel='"+namakk+"', petugas='"+''+"', pekerjaan_lain='"+pekerjaanlain+"', nama_petugas='"+''+"', alamat='"+alamat+"', nama_prop='"+propinsi+"', nama_kab='"+kabupaten+"', nama_kec='"+kecamatan+"', nama_kel='"+desa+"', rt='"+rt+"', rw='"+rw+"', warganegara='"+warganegara+"', nama_dusun='"+dusun+"', kemiskinan='Tidak Miskin', pddk_saat_ini='"+pddktempuh+"', status_pddk='"+statuskependudukan+"', status_tgl='"+statustinggal+"', difabelitas='"+difabelitas+"', kontrasepsi='"+kontrasepsi+"', resiko='"+kehamilan+"', kelahiran='', kematian='Tidak', kejadianlain='', pindah='', dok1='"+dok1+"', dok2='"+dok2+"', dok3='"+dok3+"', dok4='"+dok4+"', dok5='"+dok5+"', dok6='"+dok6+"', dok7='"+dok7+"', dok8='"+dok8+"', promis1='', promis2='',promis3='', promis4='', promis5='', promis6='', promis7='', promis8='', photo='"+gbr+nik+".jpg', keterangan='' WHERE no = '"+nomor+"'"        
            cur.execute(add_keluarga)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal() 
        
        elif filepath == gbr+'blank.jpg':
            add_keluarga="UPDATE penduduk SET nik='"+nik+"' , nama='"+nama+"' , jk='"+jk+"', tmpt_lahir='"+tmplahir+"', tgl_lahir='"+tgllahir+"', umur='', gdr='"+gdr+"', agama='"+agama+"', status='"+status+"', shdk='"+shdk+"', shdrt='', pddk_akhir='"+pddkakhir+"', pekerjaan='"+pekerjaan+"', nama_ibu='"+ibu+"', nama_ayah='"+ayah+"', no_kk='"+nokk+"', nama_kep_kel='"+namakk+"', petugas='"+''+"', pekerjaan_lain='"+pekerjaanlain+"', nama_petugas='"+''+"', alamat='"+alamat+"', nama_prop='"+propinsi+"', nama_kab='"+kabupaten+"', nama_kec='"+kecamatan+"', nama_kel='"+desa+"', rt='"+rt+"', rw='"+rw+"', warganegara='"+warganegara+"', nama_dusun='"+dusun+"', kemiskinan='Tidak Miskin', pddk_saat_ini='"+pddktempuh+"', status_pddk='"+statuskependudukan+"', status_tgl='"+statustinggal+"', difabelitas='"+difabelitas+"', kontrasepsi='"+kontrasepsi+"', resiko='"+kehamilan+"', kelahiran='', kematian='Tidak', kejadianlain='', pindah='', dok1='"+dok1+"', dok2='"+dok2+"', dok3='"+dok3+"', dok4='"+dok4+"', dok5='"+dok5+"', dok6='"+dok6+"', dok7='"+dok7+"', dok8='"+dok8+"', promis1='', promis2='',promis3='', promis4='', promis5='', promis6='', promis7='', promis8='', photo='"+gbr+"blank.jpg', keterangan='' WHERE no = '"+nomor+"'"        
            cur.execute(add_keluarga)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()       
            
        else:
            shutil.copy2(filepath, gbr+nik+'.jpg')
            add_keluarga="UPDATE penduduk SET nik='"+nik+"' , nama='"+nama+"' , jk='"+jk+"', tmpt_lahir='"+tmplahir+"', tgl_lahir='"+tgllahir+"', umur='', gdr='"+gdr+"', agama='"+agama+"', status='"+status+"', shdk='"+shdk+"', shdrt='', pddk_akhir='"+pddkakhir+"', pekerjaan='"+pekerjaan+"', nama_ibu='"+ibu+"', nama_ayah='"+ayah+"', no_kk='"+nokk+"', nama_kep_kel='"+namakk+"', petugas='"+''+"', pekerjaan_lain='"+pekerjaanlain+"', nama_petugas='"+''+"', alamat='"+alamat+"', nama_prop='"+propinsi+"', nama_kab='"+kabupaten+"', nama_kec='"+kecamatan+"', nama_kel='"+desa+"', rt='"+rt+"', rw='"+rw+"', warganegara='"+warganegara+"', nama_dusun='"+dusun+"', kemiskinan='Tidak Miskin', pddk_saat_ini='"+pddktempuh+"', status_pddk='"+statuskependudukan+"', status_tgl='"+statustinggal+"', difabelitas='"+difabelitas+"', kontrasepsi='"+kontrasepsi+"', resiko='"+kehamilan+"', kelahiran='', kematian='Tidak', kejadianlain='', pindah='', dok1='"+dok1+"', dok2='"+dok2+"', dok3='"+dok3+"', dok4='"+dok4+"', dok5='"+dok5+"', dok6='"+dok6+"', dok7='"+dok7+"', dok8='"+dok8+"', promis1='', promis2='',promis3='', promis4='', promis5='', promis6='', promis7='', promis8='', photo='"+gbr+nik+".jpg', keterangan='' WHERE no = '"+nomor+"'"         
            cur.execute(add_keluarga)
            db.commit()
            self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
            self.pesan.ShowModal()
            self.awal()
            
    def OnKembaliButton(self, event):
        self.main=edit_data_penduduk.create(None)
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

    def OnButton1Button(self, event):
        wildcard = "JPG PNG BMP File (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Ambil File",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.gambar.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.viewgambar()
        
    def viewgambar(self):
        filepath = self.gambar.GetValue()
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
