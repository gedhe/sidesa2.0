#Boa:Frame:tambah_anggota_keluarga

import os
import wx
import wx.lib.buttons
import data_penduduk
import sqlite3
import string
import gettext
import peringatan
import shutil


db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return tambah_anggota_keluarga(parent)

[wxID_TAMBAH_ANGGOTA_KELUARGA, wxID_TAMBAH_ANGGOTA_KELUARGABUTTON1, 
 wxID_TAMBAH_ANGGOTA_KELUARGACARI_KK, wxID_TAMBAH_ANGGOTA_KELUARGADESA, 
 wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN, wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN1, 
 wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN2, wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN3, 
 wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN4, wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN5, 
 wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN6, wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN7, 
 wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN8, wxID_TAMBAH_ANGGOTA_KELUARGAGAMBAR, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_ALAMAT, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_AYAH, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_DUSUN, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_IBU, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_NAMA, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_NIK, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_NO_KK, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_RT, wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_RW, 
 wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_TEMPAT_LAHIR, 
 wxID_TAMBAH_ANGGOTA_KELUARGAISIPENDUDUK, 
 wxID_TAMBAH_ANGGOTA_KELUARGAKABUPATEN, wxID_TAMBAH_ANGGOTA_KELUARGAKECAMATAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGAKEMBALI, wxID_TAMBAH_ANGGOTA_KELUARGALABEL_AGAMA, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_ALAMAT, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_DATA_PENDUDUK, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_DIFABELITAS, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_DUSUN, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_GOLONGAN_DARAH, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_JENIS_KELAMIN, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_KEWARGANEGARAAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_KONTRASEPSI, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_NAMA_AYAH, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_NAMA_IBU, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_NAMA_LENGKAP, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_NOMOR_KK, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_PEKERJAAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_PEKERJAAN_LAINNYA, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_PENDIDIKAN_TEMPUH, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_PENDIDIKAN_TERAKHIR, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_RESIKO_KEHAMILAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_SHDK, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_STATUS_KEPENDUDUKAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_STATUS_PERKAWINAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_STATUS_TINGGAL, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_TANGGAL_LAHIR, 
 wxID_TAMBAH_ANGGOTA_KELUARGALABEL_TEMPAT_LAHIR, 
 wxID_TAMBAH_ANGGOTA_KELUARGALEBEL_NIK, wxID_TAMBAH_ANGGOTA_KELUARGANAMA_KK, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_AGAMA, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_DIFABELITAS, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_GOLONGAN_DARAH, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_JENIS_KELAMIN, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_KEHAMILAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_KONTRASEPSI, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_PEKERJAAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_PEKERJAAN_LAINNYA, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_PENDIDIKAN_DITEMPUH, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_PENDIDIKAN_TERAKHIR, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_SHDK, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_STATUS, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_STATUS_KEPENDUDUKAN, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_STATUS_TINGGAL, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_WARGANEGARA, 
 wxID_TAMBAH_ANGGOTA_KELUARGAPROPINSI, 
 wxID_TAMBAH_ANGGOTA_KELUARGASIMPANGAMBAR, 
 wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT1, 
 wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT2, 
 wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT3, 
 wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT4, 
 wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT5, 
 wxID_TAMBAH_ANGGOTA_KELUARGATANGGAL_LAHIR, 
 wxID_TAMBAH_ANGGOTA_KELUARGATGLLAHIR, 
 wxID_TAMBAH_ANGGOTA_KELUARGATOMBOL_CARI, 
 wxID_TAMBAH_ANGGOTA_KELUARGATOMBOL_TAMBAH_DATA, 
] = [wx.NewId() for _init_ctrls in range(80)]

class tambah_anggota_keluarga(wx.Dialog):
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
        wx.Dialog.__init__(self, id=wxID_TAMBAH_ANGGOTA_KELUARGA,
              name=u'tambah_anggota_keluarga', parent=prnt, pos=wx.Point(406,
              79), size=wx.Size(888, 639), style=wx.FRAME_NO_TASKBAR,
              title=u'Tambah Anggota Keluarga')
        self.SetClientSize(wx.Size(888, 639))
        self.Center(wx.BOTH)

        self.label_nomor_kk = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_NOMOR_KK,
              label=u'Nomor KK', name=u'label_nomor_kk', parent=self,
              pos=wx.Point(8, 152), size=wx.Size(168, 17), style=0)

        self.input_no_kk = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_NO_KK,
              name=u'input_no_kk', parent=self, pos=wx.Point(8, 168),
              size=wx.Size(240, 25), style=wx.TE_READONLY, value=u'')

        self.input_alamat = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_ALAMAT,
              name=u'input_alamat', parent=self, pos=wx.Point(256, 168),
              size=wx.Size(288, 25), style=wx.TE_READONLY, value=u'')

        self.input_dusun = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_DUSUN,
              name=u'input_dusun', parent=self, pos=wx.Point(552, 168),
              size=wx.Size(192, 25), style=wx.TE_READONLY, value=u'')

        self.label_alamat = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_ALAMAT,
              label=u'Alamat', name=u'label_alamat', parent=self,
              pos=wx.Point(256, 152), size=wx.Size(47, 17), style=0)

        self.label_dusun = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_DUSUN,
              label=u'Dusun', name=u'label_dusun', parent=self,
              pos=wx.Point(552, 152), size=wx.Size(144, 17), style=0)

        self.input_nik = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_NIK,
              name=u'input_nik', parent=self, pos=wx.Point(192, 208),
              size=wx.Size(200, 25), style=0, value=u'')

        self.lebel_nik = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALEBEL_NIK,
              label=u'N I K *', name=u'lebel_nik', parent=self,
              pos=wx.Point(192, 192), size=wx.Size(40, 17), style=0)

        self.label_nama_lengkap = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_NAMA_LENGKAP,
              label=u'Nama Lengkap', name=u'label_nama_lengkap', parent=self,
              pos=wx.Point(192, 232), size=wx.Size(98, 17), style=0)

        self.input_nama = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_NAMA,
              name=u'input_nama', parent=self, pos=wx.Point(192, 248),
              size=wx.Size(200, 25), style=0, value=u'')

        self.label_jenis_kelamin = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_JENIS_KELAMIN,
              label=u'Jenis Kelamin', name=u'label_jenis_kelamin', parent=self,
              pos=wx.Point(192, 272), size=wx.Size(152, 17), style=0)

        self.pilihan_jenis_kelamin = wx.ComboBox(choices=['Laki-laki',
              'Perempuan'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_JENIS_KELAMIN,
              name=u'pilihan_jenis_kelamin', parent=self, pos=wx.Point(192,
              288), size=wx.Size(200, 27), style=0)

        self.input_tempat_lahir = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_TEMPAT_LAHIR,
              name=u'input_tempat_lahir', parent=self, pos=wx.Point(192, 328),
              size=wx.Size(200, 25), style=0, value=u'')

        self.label_tempat_lahir = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_TEMPAT_LAHIR,
              label=u'Tempat Lahir', name=u'label_tempat_lahir', parent=self,
              pos=wx.Point(192, 312), size=wx.Size(176, 17), style=0)

        self.label_tanggal_lahir = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_TANGGAL_LAHIR,
              label=u'Tanggal Lahir', name=u'label_tanggal_lahir', parent=self,
              pos=wx.Point(192, 352), size=wx.Size(152, 17), style=0)

        self.label_golongan_darah = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_GOLONGAN_DARAH,
              label=u'Golongan Darah', name=u'label_golongan_darah',
              parent=self, pos=wx.Point(192, 392), size=wx.Size(200, 17),
              style=0)

        self.tanggal_lahir = wx.DatePickerCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGATANGGAL_LAHIR,
              name=u'tanggal_lahir', parent=self, pos=wx.Point(192, 368),
              size=wx.Size(200, 26), style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
        self.tanggal_lahir.Bind(wx.EVT_DATE_CHANGED, self.OnGetDate)

        self.pilihan_golongan_darah = wx.ComboBox(choices=['A', 'AB', 'B', 'O',
              'A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-', 'Tidak tahu'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_GOLONGAN_DARAH,
              name=u'pilihan_golongan_darah', parent=self, pos=wx.Point(192,
              408), size=wx.Size(80, 25), style=0)

        self.label_agama = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_AGAMA,
              label=u'Agama', name=u'label_agama', parent=self,
              pos=wx.Point(400, 192), size=wx.Size(120, 17), style=0)

        self.pilihan_agama = wx.ComboBox(choices=['Islam', 'Kristen Protestan',
              'Kristen Katolik', 'Hindu', 'Budha', 'Konghuchu',
              'Aliran Kepercayaan', 'Agama Lainnya'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_AGAMA,
              name=u'pilihan_agama', parent=self, pos=wx.Point(400, 208),
              size=wx.Size(216, 25), style=0)

        self.label_kewarganegaraan = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_KEWARGANEGARAAN,
              label=u'Kewarganegaraan', name=u'label_kewarganegaraan',
              parent=self, pos=wx.Point(400, 232), size=wx.Size(168, 17),
              style=0)

        self.pilihan_warganegara = wx.ComboBox(choices=['WNI', 'WNA'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_WARGANEGARA,
              name=u'pilihan_warganegara', parent=self, pos=wx.Point(400, 248),
              size=wx.Size(216, 25), style=0)

        self.label_pendidikan_terakhir = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_PENDIDIKAN_TERAKHIR,
              label=u'Pendidikan Terakhir', name=u'label_pendidikan_terakhir',
              parent=self, pos=wx.Point(400, 272), size=wx.Size(184, 17),
              style=0)

        self.pilihan_pendidikan_terakhir = wx.ComboBox(choices=['Tidak / Belum Sekolah',
              'Tidak tamat SD / sederajat', 'Tamat SD / sederajat',
              'Tamat SLTP / sederajat', 'Tamat SLTA / sederajat',
              'Tamat Diploma I / II',
              'Tamat Akademi / Diploma III / Sarjana Muda',
              'Tamat D IV / Strata I', 'Tamat Strata II', 'Tamat Strata III',
              'Pendidikan Non Formal'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_PENDIDIKAN_TERAKHIR,
              name=u'pilihan_pendidikan_terakhir', parent=self,
              pos=wx.Point(400, 288), size=wx.Size(216, 25), style=0)

        self.label_pendidikan_tempuh = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_PENDIDIKAN_TEMPUH,
              label=u'Pendidikan Saat Ini Ditempuh',
              name=u'label_pendidikan_tempuh', parent=self, pos=wx.Point(400,
              312), size=wx.Size(264, 17), style=0)

        self.pilihan_pendidikan_ditempuh = wx.ComboBox(choices=['PAUD sederajat',
              'TK sederajat', 'SD  sederajat', 'SLTP  sederajat',
              'SLTA  sederajat', 'D1  sederajat', 'D2  sederajat',
              'D3  sederajat' , 'S1 sederajat' , 'S2  sederajat' ,
              'S3  sederajat' , 'Pendidikan Non Formal'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_PENDIDIKAN_DITEMPUH,
              name=u'pilihan_pendidikan_ditempuh', parent=self,
              pos=wx.Point(400, 328), size=wx.Size(216, 25), style=0)

        self.label_pekerjaan = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_PEKERJAAN,
              label=u'Pekerjaan Utama', name=u'label_pekerjaan', parent=self,
              pos=wx.Point(400, 352), size=wx.Size(200, 17), style=0)

        self.pilihan_pekerjaan = wx.ComboBox(choices=['Belum / Tidak Bekerja',
              'Mengurus Rumah Tangga', 'Pelajar / Mahasiswa', 'Pensiunan',
              'Pegawai Negeri Sipil', 'Tentara Nasional Indonesia',
              'Kepolisian RI', 'Perdagangan', 'Petani / Pekebun', 'Peternak',
              'Nelayan / Perikanan', 'Industri', 'Konstruksi', 'Transportasi',
              'Karyawan Swasta', 'Karyawan BUMN', 'Karyawan BUMD',
              'Karyawan Honorer', 'Buruh Harian Lepas',
              'Buruh Tani / Perkebunan', 'Buruh Nelayan / Perikanan',
              'Buruh Peternakan', 'Pembantu Rumah Tangga', 'Tukang Cukur',
              'Tukang Listrik', 'Tukang Batu', 'Tukang Kayu',
              'Tukang Sol Sepatu', 'Tukang Las / Pandai Besi', 'Tukang Jahit',
              'Penata Rambut', 'Penata Rias', 'Penata Busana', 'Mekanik',
              'Tukang Gigi', 'Seniman', 'Tabib', 'Paraji', 'Perancang Busana',
              'Penterjemah', 'Imam Masjid', 'Pendeta', 'Pastur', 'Wartawan',
              'Ustadz / Mubaligh', 'Juru Masak', 'Promotor Acara',
              'Anggota DPR-RI', 'Anggota DPD', 'Anggota BPK', 'Presiden',
              'Wakil Presiden', 'Anggota Mahkamah Konstitusi',
              'Anggota Kabinet / Kementerian', 'Duta Besar', 'Gubernur',
              'Wakil Gubernur', 'Bupati', 'Wakil Bupati', 'Walikota',
              'Wakil Walikota', 'Anggota DPRD Propinsi',
              'Anggota DPRD Kabupaten / Kota', 'Dosen', 'Guru', 'Pilot',
              'Pengacara', 'Notaris', 'Arsitek', 'Akuntan', 'Konsultan',
              'Dokter', 'Bidan', 'Perawat', 'Apoteker', 'Psikiater / Psikolog',
              'Penyiar Televisi', 'Penyiar Radio', 'Pelaut', 'Peneliti',
              'Sopir', 'Pialang', 'Paranormal', 'Pedagang', 'Perangkat Desa',
              'Kepala Desa', 'Biarawati', 'Wiraswasta', 'Buruh Migran'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_PEKERJAAN,
              name=u'pilihan_pekerjaan', parent=self, pos=wx.Point(400, 370),
              size=wx.Size(216, 25), style=0)

        self.label_pekerjaan_lainnya = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_PEKERJAAN_LAINNYA,
              label=u'Pekerjaan Lainnya', name=u'label_pekerjaan_lainnya',
              parent=self, pos=wx.Point(400, 392), size=wx.Size(168, 17),
              style=0)

        self.pilihan_pekerjaan_lainnya = wx.ComboBox(choices=['Berdagang',
              'Bertani', 'Berkebun', 'Jasa  profesional  tukang', 'Seniman',
              'Lainnya'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_PEKERJAAN_LAINNYA,
              name=u'pilihan_pekerjaan_lainnya', parent=self, pos=wx.Point(400,
              408), size=wx.Size(216, 25), style=0)

        self.label_status_perkawinan = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_STATUS_PERKAWINAN,
              label=u'Status Perkawinan', name=u'label_status_perkawinan',
              parent=self, pos=wx.Point(624, 192), size=wx.Size(176, 17),
              style=0)

        self.pilihan_status = wx.ComboBox(choices=['Belum Kawin', 'Kawin'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_STATUS,
              name=u'pilihan_status', parent=self, pos=wx.Point(624, 208),
              size=wx.Size(248, 25), style=0)

        self.label_status_kependudukan = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_STATUS_KEPENDUDUKAN,
              label=u'Status Kependudukan', name=u'label_status_kependudukan',
              parent=self, pos=wx.Point(624, 232), size=wx.Size(184, 17),
              style=0)

        self.pilihan_status_kependudukan = wx.ComboBox(choices=['Penduduk Tetap',
              'Penduduk Sementara', 'Penduduk Pindah / Pindahan', 'Meninggal'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_STATUS_KEPENDUDUKAN,
              name=u'pilihan_status_kependudukan', parent=self,
              pos=wx.Point(624, 248), size=wx.Size(248, 25), style=0)

        self.label_status_tinggal = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_STATUS_TINGGAL,
              label=u'Status Tinggal', name=u'label_status_tinggal',
              parent=self, pos=wx.Point(624, 272), size=wx.Size(152, 17),
              style=0)

        self.pilihan_status_tinggal = wx.ComboBox(choices=['Tinggal Tetap',
              'Tinggal di Luar Desa*', 'Tinggal di Luar Kota / Kabupaten',
              'Tinggal di Luar Propinsi', 'Tinggal di Luar Negeri'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_STATUS_TINGGAL,
              name=u'pilihan_status_tinggal', parent=self, pos=wx.Point(624,
              288), size=wx.Size(248, 25), style=0)

        self.label_difabelitas = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_DIFABELITAS,
              label=u'Penyandang Difabelitas', name=u'label_difabelitas',
              parent=self, pos=wx.Point(624, 312), size=wx.Size(184, 17),
              style=0)

        self.pilihan_difabelitas = wx.ComboBox(choices=['Tidak cacat',
              'Cacat Fisik', 'Cacat Netra / Buta', 'Cacat Rungu / Wicara',
              'Cacat Mental / Jiwa', 'Cacat Fisik / Mental', 'Cacat Lainnya'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_DIFABELITAS,
              name=u'pilihan_difabelitas', parent=self, pos=wx.Point(624, 328),
              size=wx.Size(248, 25), style=0)

        self.label_kontrasepsi = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_KONTRASEPSI,
              label=u'Penggunaan Kontrasepsi', name=u'label_kontrasepsi',
              parent=self, pos=wx.Point(624, 352), size=wx.Size(192, 17),
              style=0)

        self.pilihan_kontrasepsi = wx.ComboBox(choices=['Pil', 'Suntik', 'IUD',
              'Kondom', 'Implant', 'MOP'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_KONTRASEPSI,
              name=u'pilihan_kontrasepsi', parent=self, pos=wx.Point(624, 368),
              size=wx.Size(248, 25), style=0)

        self.label_shdk = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_SHDK,
              label=u'Status Hubungan Dalam Keluarga', name=u'label_shdk',
              parent=self, pos=wx.Point(24, 536), size=wx.Size(320, 17),
              style=0)

        self.pilihan_shdk = wx.ComboBox(choices=['Anak', 'Istri', 'Suami',
              'Mertua', 'Menantu', 'Famili lain', 'Lainnya'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_SHDK, name=u'pilihan_shdk',
              parent=self, pos=wx.Point(24, 560), size=wx.Size(304, 25),
              style=0)

        self.label_nama_ayah = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_NAMA_AYAH,
              label=u'Nama Ayah', name=u'label_nama_ayah', parent=self,
              pos=wx.Point(344, 536), size=wx.Size(152, 17), style=0)

        self.input_ayah = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_AYAH,
              name=u'input_ayah', parent=self, pos=wx.Point(344, 560),
              size=wx.Size(280, 25), style=0, value=u'')

        self.label_nama_ibu = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_NAMA_IBU,
              label=u'Nama Ibu', name=u'label_nama_ibu', parent=self,
              pos=wx.Point(632, 536), size=wx.Size(160, 17), style=0)

        self.input_ibu = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_IBU,
              name=u'input_ibu', parent=self, pos=wx.Point(632, 560),
              size=wx.Size(240, 25), style=0, value=u'')

        self.label_resiko_kehamilan = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_RESIKO_KEHAMILAN,
              label=u'Resiko Kehamilan', name=u'label_resiko_kehamilan',
              parent=self, pos=wx.Point(624, 392), size=wx.Size(176, 17),
              style=0)

        self.pilihan_kehamilan = wx.ComboBox(choices=['Resiko Tinggi',
              'Tidak Resiko Tinggi'],
              id=wxID_TAMBAH_ANGGOTA_KELUARGAPILIHAN_KEHAMILAN,
              name=u'pilihan_kehamilan', parent=self, pos=wx.Point(624, 408),
              size=wx.Size(248, 25), style=0)

        self.tombol_tambah_data = wx.Button(id=wxID_TAMBAH_ANGGOTA_KELUARGATOMBOL_TAMBAH_DATA,
              label=u'Tambah Data', name=u'tombol_tambah_data', parent=self,
              pos=wx.Point(232, 600), size=wx.Size(200, 32), style=0)
        self.tombol_tambah_data.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_dataButton,
              id=wxID_TAMBAH_ANGGOTA_KELUARGATOMBOL_TAMBAH_DATA)

        self.kembali = wx.Button(id=wxID_TAMBAH_ANGGOTA_KELUARGAKEMBALI,
              label=u'Kembali Ke Menu', name=u'kembali', parent=self,
              pos=wx.Point(456, 600), size=wx.Size(208, 32), style=0)
        self.kembali.Bind(wx.EVT_BUTTON, self.OnKembaliButton,
              id=wxID_TAMBAH_ANGGOTA_KELUARGAKEMBALI)

        self.dokumen = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN,
              label=u'Kepemilikan Dokumen', name=u'dokumen', parent=self,
              pos=wx.Point(24, 440), size=wx.Size(304, 17), style=0)

        self.label_data_penduduk = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGALABEL_DATA_PENDUDUK,
              label=u'FORM DATA PENDUDUK', name=u'label_data_penduduk',
              parent=self, pos=wx.Point(336, 0), size=wx.Size(216, 17),
              style=0)

        self.isipenduduk = wx.ListCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAISIPENDUDUK,
              name=u'isipenduduk', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(856, 104), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)
        self.isipenduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected,
              id=wxID_TAMBAH_ANGGOTA_KELUARGAISIPENDUDUK)

        self.staticText1 = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT1,
              label=u'Nomor Kartu Keluarga', name='staticText1', parent=self,
              pos=wx.Point(400, 128), size=wx.Size(145, 15), style=0)

        self.cari_kk = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGACARI_KK,
              name=u'cari_kk', parent=self, pos=wx.Point(552, 128),
              size=wx.Size(224, 24), style=0, value='')

        self.tombol_cari = wx.Button(id=wxID_TAMBAH_ANGGOTA_KELUARGATOMBOL_CARI,
              label=u'Cari', name=u'tombol_cari', parent=self, pos=wx.Point(784,
              128), size=wx.Size(85, 24), style=0)
        self.tombol_cari.Bind(wx.EVT_BUTTON, self.OnTombol_cariButton,
              id=wxID_TAMBAH_ANGGOTA_KELUARGATOMBOL_CARI)

        self.input_rt = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_RT,
              name=u'input_rt', parent=self, pos=wx.Point(752, 168),
              size=wx.Size(56, 27), style=0, value=u'')

        self.input_rw = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAINPUT_RW,
              name=u'input_rw', parent=self, pos=wx.Point(816, 168),
              size=wx.Size(56, 27), style=0, value=u'')

        self.staticText2 = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT2,
              label=u'RT', name='staticText2', parent=self, pos=wx.Point(760,
              152), size=wx.Size(24, 16), style=0)

        self.staticText3 = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT3,
              label=u'RW', name='staticText3', parent=self, pos=wx.Point(824,
              152), size=wx.Size(19, 17), style=0)

        self.dokumen1 = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN1,
              name=u'dokumen1', parent=self, pos=wx.Point(24, 464),
              size=wx.Size(187, 27), style=0, value='')

        self.dokumen3 = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN3,
              name=u'dokumen3', parent=self, pos=wx.Point(224, 464),
              size=wx.Size(187, 27), style=0, value='')

        self.dokumen5 = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN5,
              name=u'dokumen5', parent=self, pos=wx.Point(424, 464),
              size=wx.Size(187, 27), style=0, value='')

        self.dokumen7 = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN7,
              name=u'dokumen7', parent=self, pos=wx.Point(632, 464),
              size=wx.Size(187, 27), style=0, value='')

        self.dokumen2 = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN2,
              name=u'dokumen2', parent=self, pos=wx.Point(24, 504),
              size=wx.Size(187, 27), style=0, value='')

        self.dokumen4 = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN4,
              name=u'dokumen4', parent=self, pos=wx.Point(224, 504),
              size=wx.Size(187, 27), style=0, value='')

        self.dokumen6 = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN6,
              name=u'dokumen6', parent=self, pos=wx.Point(424, 504),
              size=wx.Size(187, 27), style=0, value='')

        self.dokumen8 = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_TAMBAH_ANGGOTA_KELUARGADOKUMEN8,
              name=u'dokumen8', parent=self, pos=wx.Point(632, 504),
              size=wx.Size(187, 27), style=0, value='')

        self.staticText4 = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT4,
              label=u'Kode KK SMT- adalah NoKK Sementara', name='staticText4',
              parent=self, pos=wx.Point(16, 128), size=wx.Size(248, 17),
              style=0)

        self.tgllahir = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGATGLLAHIR,
              name=u'tgllahir', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(112, 27), style=0, value=u'')

        self.nama_kk = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGANAMA_KK,
              name=u'nama_kk', parent=self, pos=wx.Point(8, 208),
              size=wx.Size(176, 24), style=wx.TE_READONLY, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_TAMBAH_ANGGOTA_KELUARGASTATICTEXT5,
              label=u'Nama Kepala Keluarga', name='staticText5', parent=self,
              pos=wx.Point(8, 192), size=wx.Size(135, 17), style=0)

        self.gambar = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAGAMBAR,
              name=u'gambar', parent=self, pos=wx.Point(24, 368),
              size=wx.Size(152, 24), style=0, value=u'')

        self.simpangambar = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGASIMPANGAMBAR,
              name=u'simpangambar', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'/opt/sidesa/penduduk')

        self.button1 = wx.Button(id=wxID_TAMBAH_ANGGOTA_KELUARGABUTTON1,
              label=u'Upload Photo', name='button1', parent=self,
              pos=wx.Point(24, 392), size=wx.Size(152, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_TAMBAH_ANGGOTA_KELUARGABUTTON1)

        self.propinsi = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAPROPINSI,
              name=u'propinsi', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kabupaten = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAKABUPATEN,
              name=u'kabupaten', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.kecamatan = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGAKECAMATAN,
              name=u'kecamatan', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

        self.desa = wx.TextCtrl(id=wxID_TAMBAH_ANGGOTA_KELUARGADESA,
              name=u'desa', parent=self, pos=wx.Point(-100, -100),
              size=wx.Size(152, 24), style=0, value=u'')

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
        sql = "SELECT * FROM penduduk WHERE shdk='Kepala Keluarga' AND kematian='Tidak' "
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[16]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[17]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[29])
            self.isipenduduk.SetStringItem(nokk,4,"%s"%i[26]) 
            self.isipenduduk.SetStringItem(nokk,5,"%s"%i[27])
            nokk = nokk + 1
     
    
    def Isi_Object(self) : 
        carikk=str(self.cari_kk.GetValue())
        sql="SELECT * FROM penduduk WHERE no_kk='%s'"%(carikk)
        cur.execute(sql)
        hasil = cur.fetchone()  
        if hasil : 
            self.nama_kk.SetValue(str(hasil[17]))
            self.input_no_kk.SetValue(str(hasil[16])) 
            self.input_alamat.SetValue(str(hasil[21]))
            self.input_dusun.SetValue(str(hasil[29]))
            self.input_rt.SetValue(str(hasil[26]))
            self.input_rw.SetValue(str(hasil[27]))
            
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
        tgllahir = str(self.tgllahir.GetValue())
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
            sql="SELECT * FROM penduduk WHERE nik='"+(nik)+"'"
            cur.execute(sql)
            hasil = cur.fetchone()  
            if hasil:
                self.pesan = wx.MessageDialog(self,"Nomor NIK  Sudah Ada","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
            else:
                add_keluarga="INSERT INTO penduduk (nik , nama , jk, tmpt_lahir, tgl_lahir, umur, gdr, agama, status, shdk, shdrt, pddk_akhir, pekerjaan, nama_ibu, nama_ayah, no_kk, nama_kep_kel, petugas, pekerjaan_lain, nama_petugas, alamat, nama_prop, nama_kab, nama_kec, nama_kel, rt, rw, warganegara, nama_dusun, kemiskinan, pddk_saat_ini, status_pddk, status_tgl, difabelitas, kontrasepsi, resiko, kelahiran, kematian, kejadianlain, pindah, dok1, dok2, dok3, dok4, dok5, dok6, dok7, dok8, promis1, promis2,promis3, promis4, promis5, promis6, promis7, promis8, photo, keterangan) VALUES('"+(nik)+"', '"+(nama)+"', '"+(jk)+"','"+(tmplahir)+"','"+(tgllahir)+"','"+''+"','"+(gdr)+"','"+(agama)+"','"+(status)+"','"+(shdk)+"','"+''+"','"+(pddkakhir)+"','"+(pekerjaan)+"','"+(ibu)+"','"+(ayah)+"','"+(nokk)+"','"+(namakk)+"','"+''+"','"+(pekerjaanlain)+"','"+''+"','"+(alamat)+"','"+(propinsi)+"','"+(kabupaten)+"','"+(kecamatan)+"','"+(desa)+"','"+(rt)+"','"+(rw)+"','"+(warganegara)+"','"+(dusun)+"','Tidak Miskin','"+(pddktempuh)+"','"+(statuskependudukan)+"','"+(statustinggal)+"','"+(difabelitas)+"','"+(kontrasepsi)+"','"+(kehamilan)+"', '"+''+"', 'Tidak', '"+''+"', '"+''+"', '"+(dok1)+"', '"+(dok2)+"', '"+(dok3)+"', '"+(dok4)+"', '"+(dok5)+"', '"+(dok6)+"', '"+(dok7)+"', '"+(dok8)+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+(gbr)+"blank.jpg', '"+''+"')"        
                cur.execute(add_keluarga)
                db.commit()
                self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
                self.awal()
            
        else:
            sql="SELECT * FROM penduduk WHERE nik='"+(nik)+"'"
            cur.execute(sql)
            hasil = cur.fetchone()  
            if hasil:
                self.pesan = wx.MessageDialog(self,"Nomor NIK Sudah Ada","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
            else:
                shutil.copy2(filepath, gbr+nik+'.jpg')
                add_keluarga="INSERT INTO penduduk (nik , nama , jk, tmpt_lahir, tgl_lahir, umur, gdr, agama, status, shdk, shdrt, pddk_akhir, pekerjaan, nama_ibu, nama_ayah, no_kk, nama_kep_kel, petugas, pekerjaan_lain, nama_petugas, alamat, nama_prop, nama_kab, nama_kec, nama_kel, rt, rw, warganegara, nama_dusun,  kemiskinan, pddk_saat_ini, status_pddk, status_tgl, difabelitas, kontrasepsi, resiko, kelahiran, kematian, kejadianlain, pindah, dok1, dok2, dok3, dok4, dok5, dok6, dok7, dok8, promis1, promis2,promis3, promis4, promis5, promis6, promis7, promis8, photo, keterangan) VALUES('"+(nik)+"', '"+(nama)+"', '"+(jk)+"','"+(tmplahir)+"','"+(tgllahir)+"','"+''+"','"+(gdr)+"','"+(agama)+"','"+(status)+"','"+(shdk)+"','"+''+"','"+(pddkakhir)+"','"+(pekerjaan)+"','"+(ibu)+"','"+(ayah)+"','"+(nokk)+"','"+(namakk)+"','"+''+"','"+(pekerjaanlain)+"','"+''+"','"+(alamat)+"','"+(propinsi)+"','"+(kabupaten)+"','"+(kecamatan)+"','"+(desa)+"','"+(rt)+"','"+(rw)+"','"+(warganegara)+"','"+(dusun)+"','Tidak Miskin','"+(pddktempuh)+"','"+(statuskependudukan)+"','"+(statustinggal)+"','"+(difabelitas)+"','"+(kontrasepsi)+"','"+(kehamilan)+"', '"+''+"', 'Tidak', '"+''+"', '"+''+"', '"+(dok1)+"', '"+(dok2)+"', '"+(dok3)+"', '"+(dok4)+"', '"+(dok5)+"', '"+(dok6)+"', '"+(dok7)+"', '"+(dok8)+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+''+"', '"+(gbr)+(nik)+".jpg', '"+''+"')"        
                cur.execute(add_keluarga)
                db.commit()
                self.pesan = wx.MessageDialog(self,"Data Sudah Tersimpan","Konfirmasi",wx.OK) 
                self.pesan.ShowModal()
                self.awal()
            
    def OnKembaliButton(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()

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
        self.onView()
        
    def onView(self):
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
      

  
