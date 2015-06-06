#Boa:Frame:laporan_penduduk

import wx
import wx.calendar
import sqlite3

db = sqlite3.connect('/opt/sidesa/sidesa')
cur = db.cursor()

def create(parent):
    return laporan_penduduk(parent)

[wxID_LAPORAN_PENDUDUK, wxID_LAPORAN_PENDUDUKAGAMA, 
 wxID_LAPORAN_PENDUDUKBUTTON15, wxID_LAPORAN_PENDUDUKCBAGAMA, 
 wxID_LAPORAN_PENDUDUKCBDIF, wxID_LAPORAN_PENDUDUKCBDOK, 
 wxID_LAPORAN_PENDUDUKCBHAMIL, wxID_LAPORAN_PENDUDUKCBPDDK, 
 wxID_LAPORAN_PENDUDUKCBPEK, wxID_LAPORAN_PENDUDUKCBPENDUDUK, 
 wxID_LAPORAN_PENDUDUKCBSAAT, wxID_LAPORAN_PENDUDUKCBSTAT, 
 wxID_LAPORAN_PENDUDUKCBTINGGAL, wxID_LAPORAN_PENDUDUKCBWARGA, 
 wxID_LAPORAN_PENDUDUKDIFABEL, wxID_LAPORAN_PENDUDUKDOK, 
 wxID_LAPORAN_PENDUDUKHAMIL, wxID_LAPORAN_PENDUDUKISIAGAMA, 
 wxID_LAPORAN_PENDUDUKISIDIFABEL, wxID_LAPORAN_PENDUDUKISIDOKUMEN, 
 wxID_LAPORAN_PENDUDUKISIPEKERJAAN, wxID_LAPORAN_PENDUDUKISIPENDUDUK, 
 wxID_LAPORAN_PENDUDUKISIRESIKO, wxID_LAPORAN_PENDUDUKISISTATUS, 
 wxID_LAPORAN_PENDUDUKISISTATUSPENDUDUK, 
 wxID_LAPORAN_PENDUDUKISISTATUSTINGGAL, wxID_LAPORAN_PENDUDUKISIWARGANEGARA, 
 wxID_LAPORAN_PENDUDUKJMLKK, wxID_LAPORAN_PENDUDUKJMLPENDIDIKANAKHIR, 
 wxID_LAPORAN_PENDUDUKJMLPENDIDIKANSAATINI, wxID_LAPORAN_PENDUDUKKK, 
 wxID_LAPORAN_PENDUDUKKKLAKI, wxID_LAPORAN_PENDUDUKKKLK, 
 wxID_LAPORAN_PENDUDUKKKPEREMPUAN, wxID_LAPORAN_PENDUDUKKKPR, 
 wxID_LAPORAN_PENDUDUKLK, wxID_LAPORAN_PENDUDUKPEKERJAAN, 
 wxID_LAPORAN_PENDUDUKPENDAKHIR, wxID_LAPORAN_PENDUDUKPENDSAAT, 
 wxID_LAPORAN_PENDUDUKPENDUDUK, wxID_LAPORAN_PENDUDUKPENDUDUKLAKI, 
 wxID_LAPORAN_PENDUDUKPENDUDUKPEREMPUAN, wxID_LAPORAN_PENDUDUKPR, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT1, wxID_LAPORAN_PENDUDUKSTATICTEXT10, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT11, wxID_LAPORAN_PENDUDUKSTATICTEXT12, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT13, wxID_LAPORAN_PENDUDUKSTATICTEXT14, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT15, wxID_LAPORAN_PENDUDUKSTATICTEXT16, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT17, wxID_LAPORAN_PENDUDUKSTATICTEXT18, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT19, wxID_LAPORAN_PENDUDUKSTATICTEXT2, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT20, wxID_LAPORAN_PENDUDUKSTATICTEXT21, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT22, wxID_LAPORAN_PENDUDUKSTATICTEXT23, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT24, wxID_LAPORAN_PENDUDUKSTATICTEXT25, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT26, wxID_LAPORAN_PENDUDUKSTATICTEXT27, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT28, wxID_LAPORAN_PENDUDUKSTATICTEXT29, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT3, wxID_LAPORAN_PENDUDUKSTATICTEXT30, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT31, wxID_LAPORAN_PENDUDUKSTATICTEXT32, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT4, wxID_LAPORAN_PENDUDUKSTATICTEXT5, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT6, wxID_LAPORAN_PENDUDUKSTATICTEXT7, 
 wxID_LAPORAN_PENDUDUKSTATICTEXT8, wxID_LAPORAN_PENDUDUKSTATICTEXT9, 
 wxID_LAPORAN_PENDUDUKSTATUS, wxID_LAPORAN_PENDUDUKTINGGAL, 
 wxID_LAPORAN_PENDUDUKWARGA, 
] = [wx.NewId() for _init_ctrls in range(78)]

class laporan_penduduk(wx.Frame):
    
    def _init_coll_isipenduduk_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nomor NIK', width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Lengkap', width=250)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Jenis Kelamin', width=100)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=260)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_LAPORAN_PENDUDUK,
              name=u'laporan_penduduk', parent=prnt, pos=wx.Point(387, 154),
              size=wx.Size(928, 506), style=wx.FRAME_NO_TASKBAR,
              title=u'Sistem Laporan Penduduk')
        self.SetClientSize(wx.Size(928, 506))
        self.Center(wx.BOTH)

        self.staticText1 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT1,
              label=u'Jumlah Kepala Keluarga', name='staticText1', parent=self,
              pos=wx.Point(16, 184), size=wx.Size(216, 17), style=0)

        self.staticText2 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT2,
              label=u'Jumlah KK Lak-laki', name='staticText2', parent=self,
              pos=wx.Point(16, 216), size=wx.Size(200, 17), style=0)

        self.staticText3 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT3,
              label=u'Jumlah Penduduk Laki - Laki', name='staticText3',
              parent=self, pos=wx.Point(16, 280), size=wx.Size(224, 15),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT4,
              label=u'Jumlah Penduduk Perempuan', name='staticText4',
              parent=self, pos=wx.Point(16, 312), size=wx.Size(224, 15),
              style=0)

        self.jmlkk = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKJMLKK, name=u'jmlkk',
              parent=self, pos=wx.Point(248, 184), size=wx.Size(50, 25),
              style=0, value='')

        self.kklaki = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKKKLAKI,
              name=u'kklaki', parent=self, pos=wx.Point(248, 216),
              size=wx.Size(50, 25), style=0, value='')

        self.kkperempuan = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKKKPEREMPUAN,
              name=u'kkperempuan', parent=self, pos=wx.Point(248, 248),
              size=wx.Size(50, 25), style=0, value='')

        self.penduduklaki = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKPENDUDUKLAKI,
              name=u'penduduklaki', parent=self, pos=wx.Point(248, 280),
              size=wx.Size(50, 25), style=0, value='')

        self.kklk = wx.Button(id=wxID_LAPORAN_PENDUDUKKKLK, label=u'Lihat Data',
              name=u'kklk', parent=self, pos=wx.Point(336, 216),
              size=wx.Size(96, 24), style=0)
        self.kklk.Bind(wx.EVT_BUTTON, self.OnKklkButton,
              id=wxID_LAPORAN_PENDUDUKKKLK)

        self.kkpr = wx.Button(id=wxID_LAPORAN_PENDUDUKKKPR, label=u'Lihat Data',
              name=u'kkpr', parent=self, pos=wx.Point(336, 248),
              size=wx.Size(96, 24), style=0)
        self.kkpr.Bind(wx.EVT_BUTTON, self.OnKkprButton,
              id=wxID_LAPORAN_PENDUDUKKKPR)

        self.difabel = wx.Button(id=wxID_LAPORAN_PENDUDUKDIFABEL,
              label=u'Lihat Data', name=u'difabel', parent=self,
              pos=wx.Point(816, 312), size=wx.Size(96, 24), style=0)
        self.difabel.Bind(wx.EVT_BUTTON, self.OnDifabelButton,
              id=wxID_LAPORAN_PENDUDUKDIFABEL)

        self.pendakhir = wx.Button(id=wxID_LAPORAN_PENDUDUKPENDAKHIR,
              label=u'Lihat Data', name=u'pendakhir', parent=self,
              pos=wx.Point(816, 184), size=wx.Size(96, 24), style=0)
        self.pendakhir.Bind(wx.EVT_BUTTON, self.OnPendakhirButton,
              id=wxID_LAPORAN_PENDUDUKPENDAKHIR)

        self.staticText7 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT7,
              label=u'Jumlah Pendidikan Akhir', name='staticText7', parent=self,
              pos=wx.Point(448, 192), size=wx.Size(176, 15), style=0)

        self.cbpddk = wx.ComboBox(choices=['Tidak/Belum Sekolah',
              'Tidak Tamat SD/Sederajat', 'Tamat SD/Sederajat',
              'SLTP/Sederajat', 'SLTA/Sederajat', 'Diploma I/II',
              'Akademi/Diploma III/S. Muda', 'Diploma IV/Strata I',
              'Tamat Strata II', 'Tamat Strata III', 'Pendidikan Non Formal'],
              id=wxID_LAPORAN_PENDUDUKCBPDDK, name=u'cbpddk', parent=self,
              pos=wx.Point(624, 184), size=wx.Size(96, 25), style=0, value='')

        self.jmlpendidikanakhir = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKJMLPENDIDIKANAKHIR,
              name=u'jmlpendidikanakhir', parent=self, pos=wx.Point(728, 184),
              size=wx.Size(50, 25), style=0, value='')

        self.staticText8 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT8,
              label=u'Jumlah Saat Ini Pendidikan', name='staticText8',
              parent=self, pos=wx.Point(448, 224), size=wx.Size(200, 15),
              style=0)

        self.cbsaat = wx.ComboBox(choices=['PAUD Sederajat', 'TK Sederajat',
              'SD Sederajat', 'SLTP Sederajat', 'SLTA Sederajat',
              'D1 Sederajat', 'D2 Sederajat', 'D3 Sederajat' , 'S1 Sederajat' ,
              'S2 Sederajat' , 'S3 Sederajat' , 'Pendidikan Non Formal'],
              id=wxID_LAPORAN_PENDUDUKCBSAAT, name=u'cbsaat', parent=self,
              pos=wx.Point(624, 216), size=wx.Size(96, 25), style=0, value='')

        self.jmlpendidikansaatini = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKJMLPENDIDIKANSAATINI,
              name=u'jmlpendidikansaatini', parent=self, pos=wx.Point(728, 216),
              size=wx.Size(50, 25), style=0, value='')

        self.staticText9 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT9,
              label=u'Status Perkawinan', name='staticText9', parent=self,
              pos=wx.Point(448, 288), size=wx.Size(152, 17), style=0)

        self.cbpek = wx.ComboBox(choices=['Belum/Tidak Bekerja',
              'Mengurus Rumah Tangga', 'Pelajar/Mahasiswa', 'Pensiunan',
              'Pegawai Negeri Sipil', 'Tentara Nasional Indonesia',
              'Kepolisian RI', 'Perdagangan', 'Petani/Pekebun', 'Peternak',
              'Nelayan/Perikanan', 'Industri', 'Konstruksi', 'Transportasi',
              'Karyawan Swasta', 'Karyawan BUMN', 'Karyawan BUMD',
              'Karyawan Honorer', 'Buruh Harian Lepas', 'Buruh Tani/Perkebunan',
              'Buruh Nelayan/Perikanan', 'Buruh Peternakan',
              'Pembantu Rumah Tangga', 'Tukang Cukur', 'Tukang Listrik',
              'Tukang Batu', 'Tukang Kayu', 'Tukang Sol Sepatu',
              'Tukang Las/Pandai Besi', 'Tukang Jahit', 'Penata Rambut',
              'Penata Rias', 'Penata Busana', 'Mekanik', 'Tukang Gigi',
              'Seniman', 'Tabib', 'Paraji', 'Perancang Busana', 'Penterjemah',
              'Imam Masjid', 'Pendeta', 'Pastur', 'Wartawan', 'Ustadz/Mubaligh',
              'Juru Masak', 'Promotor Acara', 'Anggota DPR-RI', 'Anggota DPD',
              'Anggota BPK', 'Presiden', 'Wakil Presiden',
              'Anggota Mahkamah Konstitusi', 'Anggota Kabinet/Kementerian',
              'Duta Besar', 'Gubernur', 'Wakil Gubernur', 'Bupati',
              'Wakil Bupati', 'Walikota', 'Wakil Walikota',
              'Anggota DPRD Propinsi', 'Anggota DPRD Kabupaten/Kota', 'Dosen',
              'Guru', 'Pilot', 'Pengacara', 'Notaris', 'Arsitek', 'Akuntan',
              'Konsultan', 'Dokter', 'Bidan', 'Perawat', 'Apoteker',
              'Psikiater/Psikolog', 'Penyiar Televisi', 'Penyiar Radio',
              'Pelaut', 'Peneliti', 'Sopir', 'Pialang', 'Paranormal',
              'Pedagang', 'Perangkat Desa', 'Kepala Desa', 'Biarawati',
              'Wiraswasta', 'Buruh Migran'], id=wxID_LAPORAN_PENDUDUKCBPEK,
              name=u'cbpek', parent=self, pos=wx.Point(624, 248),
              size=wx.Size(96, 25), style=0, value='')

        self.pendsaat = wx.Button(id=wxID_LAPORAN_PENDUDUKPENDSAAT,
              label=u'Lihat Data', name=u'pendsaat', parent=self,
              pos=wx.Point(816, 216), size=wx.Size(96, 24), style=0)
        self.pendsaat.Bind(wx.EVT_BUTTON, self.OnPendsaatButton,
              id=wxID_LAPORAN_PENDUDUKPENDSAAT)

        self.kk = wx.Button(id=wxID_LAPORAN_PENDUDUKKK, label=u'Lihat Data',
              name=u'kk', parent=self, pos=wx.Point(336, 184), size=wx.Size(96,
              24), style=0)
        self.kk.Bind(wx.EVT_BUTTON, self.OnKkButton, id=wxID_LAPORAN_PENDUDUKKK)

        self.staticText10 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT10,
              label=u'Difabelitas', name='staticText10', parent=self,
              pos=wx.Point(448, 320), size=wx.Size(120, 15), style=0)

        self.cbstat = wx.ComboBox(choices=['Belum Kawin', 'Kawin', 'Cerai Mati',
              'Cerai Hidup'], id=wxID_LAPORAN_PENDUDUKCBSTAT, name=u'cbstat',
              parent=self, pos=wx.Point(624, 280), size=wx.Size(96, 25),
              style=0, value='')

        self.staticText11 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT11,
              label=u'Status Tinggal', name='staticText11', parent=self,
              pos=wx.Point(448, 352), size=wx.Size(152, 15), style=0)

        self.cbdif = wx.ComboBox(choices=['Tidak cacat', 'Cacat Fisik',
              'Cacat Netra/Buta', 'Cacat Rungu/Wicara', 'Cacat Mental/Jiwa',
              'Cacat Fisik/Mental', 'Cacat Lainnya'],
              id=wxID_LAPORAN_PENDUDUKCBDIF, name=u'cbdif', parent=self,
              pos=wx.Point(624, 312), size=wx.Size(96, 25), style=0, value='')

        self.staticText12 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT12,
              label=u'Pekerjaan', name='staticText12', parent=self,
              pos=wx.Point(448, 256), size=wx.Size(120, 15), style=0)

        self.pendudukperempuan = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKPENDUDUKPEREMPUAN,
              name=u'pendudukperempuan', parent=self, pos=wx.Point(248, 312),
              size=wx.Size(50, 25), style=0, value='')

        self.isiagama = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISIAGAMA,
              name=u'isiagama', parent=self, pos=wx.Point(248, 344),
              size=wx.Size(50, 25), style=0, value='')

        self.staticText13 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT13,
              label=u'Status Penduduk', name='staticText13', parent=self,
              pos=wx.Point(448, 384), size=wx.Size(144, 15), style=0)

        self.cbtinggal = wx.ComboBox(choices=['Tinggal Tetap',
              'Tinggal Di Luar Desa*', 'Tinggal Di Luar Kota/Kabupaten',
              'Tinggal Di Luar Propinsi', 'Tinggal Di Luar Negeri'],
              id=wxID_LAPORAN_PENDUDUKCBTINGGAL, name=u'cbtinggal', parent=self,
              pos=wx.Point(624, 344), size=wx.Size(96, 25), style=0, value='')

        self.cbpenduduk = wx.ComboBox(choices=['Penduduk Tetap',
              'Penduduk Sementara', 'Penduduk Pindah/Pindahan', 'Meninggal'],
              id=wxID_LAPORAN_PENDUDUKCBPENDUDUK, name=u'cbpenduduk',
              parent=self, pos=wx.Point(624, 376), size=wx.Size(96, 25),
              style=0, value='')

        self.staticText14 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT14,
              label=u'Resiko Kehamilan', name='staticText14', parent=self,
              pos=wx.Point(448, 416), size=wx.Size(160, 15), style=0)

        self.cbhamil = wx.ComboBox(choices=['Resiko Tinggi',
              'Tidak Resiko Tinggi'], id=wxID_LAPORAN_PENDUDUKCBHAMIL,
              name=u'cbhamil', parent=self, pos=wx.Point(624, 408),
              size=wx.Size(96, 25), style=0, value='')

        self.isipekerjaan = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISIPEKERJAAN,
              name=u'isipekerjaan', parent=self, pos=wx.Point(728, 248),
              size=wx.Size(50, 25), style=0, value='')

        self.isistatus = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISISTATUS,
              name=u'isistatus', parent=self, pos=wx.Point(728, 280),
              size=wx.Size(50, 25), style=0, value='')

        self.isistatustinggal = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISISTATUSTINGGAL,
              name=u'isistatustinggal', parent=self, pos=wx.Point(728, 344),
              size=wx.Size(50, 25), style=0, value='')

        self.isidifabel = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISIDIFABEL,
              name=u'isidifabel', parent=self, pos=wx.Point(728, 312),
              size=wx.Size(50, 25), style=0, value='')

        self.isistatuspenduduk = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISISTATUSPENDUDUK,
              name=u'isistatuspenduduk', parent=self, pos=wx.Point(728, 376),
              size=wx.Size(50, 25), style=0, value='')

        self.isiresiko = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISIRESIKO,
              name=u'isiresiko', parent=self, pos=wx.Point(728, 408),
              size=wx.Size(50, 25), style=0, value='')

        self.warga = wx.Button(id=wxID_LAPORAN_PENDUDUKWARGA,
              label=u'Lihat Data', name=u'warga', parent=self, pos=wx.Point(336,
              376), size=wx.Size(96, 24), style=0)
        self.warga.Bind(wx.EVT_BUTTON, self.OnWargaButton,
              id=wxID_LAPORAN_PENDUDUKWARGA)

        self.pekerjaan = wx.Button(id=wxID_LAPORAN_PENDUDUKPEKERJAAN,
              label=u'Lihat Data', name=u'pekerjaan', parent=self,
              pos=wx.Point(816, 248), size=wx.Size(96, 24), style=0)
        self.pekerjaan.Bind(wx.EVT_BUTTON, self.OnPekerjaanButton,
              id=wxID_LAPORAN_PENDUDUKPEKERJAAN)

        self.status = wx.Button(id=wxID_LAPORAN_PENDUDUKSTATUS,
              label=u'Lihat Data', name=u'status', parent=self,
              pos=wx.Point(816, 280), size=wx.Size(96, 24), style=0)
        self.status.Bind(wx.EVT_BUTTON, self.OnStatusButton,
              id=wxID_LAPORAN_PENDUDUKSTATUS)

        self.pr = wx.Button(id=wxID_LAPORAN_PENDUDUKPR, label=u'Lihat Data',
              name=u'pr', parent=self, pos=wx.Point(336, 312), size=wx.Size(96,
              24), style=0)
        self.pr.Bind(wx.EVT_BUTTON, self.OnPrButton, id=wxID_LAPORAN_PENDUDUKPR)

        self.tinggal = wx.Button(id=wxID_LAPORAN_PENDUDUKTINGGAL,
              label=u'Lihat Data', name=u'tinggal', parent=self,
              pos=wx.Point(816, 344), size=wx.Size(96, 24), style=0)
        self.tinggal.Bind(wx.EVT_BUTTON, self.OnTinggalButton,
              id=wxID_LAPORAN_PENDUDUKTINGGAL)

        self.penduduk = wx.Button(id=wxID_LAPORAN_PENDUDUKPENDUDUK,
              label=u'Lihat Data', name=u'penduduk', parent=self,
              pos=wx.Point(816, 376), size=wx.Size(96, 24), style=0)
        self.penduduk.Bind(wx.EVT_BUTTON, self.OnPendudukButton,
              id=wxID_LAPORAN_PENDUDUKPENDUDUK)

        self.hamil = wx.Button(id=wxID_LAPORAN_PENDUDUKHAMIL,
              label=u'Lihat Data', name=u'hamil', parent=self, pos=wx.Point(816,
              408), size=wx.Size(96, 24), style=0)
        self.hamil.Bind(wx.EVT_BUTTON, self.OnHamilButton,
              id=wxID_LAPORAN_PENDUDUKHAMIL)

        self.lk = wx.Button(id=wxID_LAPORAN_PENDUDUKLK, label=u'Lihat Data',
              name=u'lk', parent=self, pos=wx.Point(336, 280), size=wx.Size(96,
              24), style=0)
        self.lk.Bind(wx.EVT_BUTTON, self.OnLkButton, id=wxID_LAPORAN_PENDUDUKLK)

        self.button15 = wx.Button(id=wxID_LAPORAN_PENDUDUKBUTTON15,
              label=u'Kembali Ke Menu', name='button15', parent=self,
              pos=wx.Point(360, 448), size=wx.Size(224, 30), style=0)
        self.button15.Bind(wx.EVT_BUTTON, self.OnButton15Button,
              id=wxID_LAPORAN_PENDUDUKBUTTON15)

        self.staticText5 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT5,
              label=u'Agama', name='staticText5', parent=self, pos=wx.Point(16,
              344), size=wx.Size(42, 17), style=0)

        self.staticText6 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT6,
              label=u'Kewarganegaraan', name='staticText6', parent=self,
              pos=wx.Point(16, 376), size=wx.Size(108, 17), style=0)

        self.cbagama = wx.ComboBox(choices=['Islam', 'Kristen Protestan',
              'Kristen Katolik', 'Hindu', 'Budha', 'Konghuchu',
              'Aliran Kepercayaan', 'Agama Lainnya'],
              id=wxID_LAPORAN_PENDUDUKCBAGAMA, name=u'cbagama', parent=self,
              pos=wx.Point(144, 344), size=wx.Size(96, 24), style=0, value=u'')
        self.cbagama.SetLabel(u'')

        self.isipenduduk = wx.ListCtrl(id=wxID_LAPORAN_PENDUDUKISIPENDUDUK,
              name='isipenduduk', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(888, 168), style=wx.LC_REPORT)
        self._init_coll_isipenduduk_Columns(self.isipenduduk)
        self.isipenduduk.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnIsipendudukListItemSelected,
              id=wxID_LAPORAN_PENDUDUKISIPENDUDUK)

        self.staticText15 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT15,
              label=u'KK', name='staticText15', parent=self, pos=wx.Point(304,
              224), size=wx.Size(17, 17), style=0)

        self.staticText16 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT16,
              label=u'KK', name='staticText16', parent=self, pos=wx.Point(304,
              192), size=wx.Size(17, 17), style=0)

        self.staticText17 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT17,
              label=u'Jiwa', name='staticText17', parent=self, pos=wx.Point(304,
              288), size=wx.Size(25, 17), style=0)

        self.staticText18 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT18,
              label=u'Jiwa', name='staticText18', parent=self, pos=wx.Point(304,
              320), size=wx.Size(25, 17), style=0)

        self.staticText19 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT19,
              label=u'Jiwa', name='staticText19', parent=self, pos=wx.Point(304,
              384), size=wx.Size(25, 17), style=0)

        self.staticText20 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT20,
              label=u'Jiwa', name='staticText20', parent=self, pos=wx.Point(784,
              192), size=wx.Size(25, 17), style=0)

        self.staticText21 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT21,
              label=u'Jiwa', name='staticText21', parent=self, pos=wx.Point(784,
              224), size=wx.Size(25, 17), style=0)

        self.staticText22 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT22,
              label=u'Jiwa', name='staticText22', parent=self, pos=wx.Point(784,
              256), size=wx.Size(25, 17), style=0)

        self.staticText23 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT23,
              label=u'Jiwa', name='staticText23', parent=self, pos=wx.Point(784,
              288), size=wx.Size(25, 17), style=0)

        self.staticText24 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT24,
              label=u'Jiwa', name='staticText24', parent=self, pos=wx.Point(784,
              352), size=wx.Size(25, 17), style=0)

        self.staticText25 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT25,
              label=u'KK', name='staticText25', parent=self, pos=wx.Point(304,
              256), size=wx.Size(25, 17), style=0)

        self.staticText26 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT26,
              label=u'Jiwa', name='staticText26', parent=self, pos=wx.Point(784,
              384), size=wx.Size(25, 17), style=0)

        self.staticText27 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT27,
              label=u'Jiwa', name='staticText27', parent=self, pos=wx.Point(784,
              416), size=wx.Size(25, 17), style=0)

        self.staticText28 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT28,
              label=u'Jiwa', name='staticText28', parent=self, pos=wx.Point(784,
              320), size=wx.Size(25, 17), style=0)

        self.dok = wx.Button(id=wxID_LAPORAN_PENDUDUKDOK, label=u'Lihat Data',
              name=u'dok', parent=self, pos=wx.Point(336, 408), size=wx.Size(96,
              24), style=0)
        self.dok.Bind(wx.EVT_BUTTON, self.OnDokButton,
              id=wxID_LAPORAN_PENDUDUKDOK)

        self.agama = wx.Button(id=wxID_LAPORAN_PENDUDUKAGAMA,
              label=u'Lihat Data', name=u'agama', parent=self, pos=wx.Point(336,
              344), size=wx.Size(96, 24), style=0)
        self.agama.Bind(wx.EVT_BUTTON, self.OnAgamaButton,
              id=wxID_LAPORAN_PENDUDUKAGAMA)

        self.isiwarganegara = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISIWARGANEGARA,
              name=u'isiwarganegara', parent=self, pos=wx.Point(248, 376),
              size=wx.Size(50, 25), style=0, value='')

        self.isidokumen = wx.TextCtrl(id=wxID_LAPORAN_PENDUDUKISIDOKUMEN,
              name=u'isidokumen', parent=self, pos=wx.Point(248, 408),
              size=wx.Size(50, 25), style=0, value='')

        self.staticText29 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT29,
              label=u'Jiwa', name='staticText29', parent=self, pos=wx.Point(304,
              416), size=wx.Size(25, 17), style=0)

        self.staticText30 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT30,
              label=u'Jiwa', name='staticText30', parent=self, pos=wx.Point(304,
              352), size=wx.Size(25, 17), style=0)

        self.cbwarga = wx.ComboBox(choices=['WNI', 'WNA'],
              id=wxID_LAPORAN_PENDUDUKCBWARGA, name=u'cbwarga', parent=self,
              pos=wx.Point(144, 376), size=wx.Size(96, 24), style=0, value=u'')
        self.cbwarga.SetLabel(u'')

        self.cbdok = wx.ComboBox(choices=['Akta Kelahiran', 'Akta Nikah',
              'Akta Cerai', 'Akta Kematian', 'KTP Sementara', 'KITAS', 'VISA',
              'Paspor'], id=wxID_LAPORAN_PENDUDUKCBDOK, name=u'cbdok',
              parent=self, pos=wx.Point(144, 408), size=wx.Size(96, 24),
              style=0, value=u'')
        self.cbdok.SetLabel(u'')

        self.staticText31 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT31,
              label=u'Jumlah KK Perempuan', name='staticText31', parent=self,
              pos=wx.Point(16, 248), size=wx.Size(131, 17), style=0)

        self.staticText32 = wx.StaticText(id=wxID_LAPORAN_PENDUDUKSTATICTEXT32,
              label=u'Dokumen', name='staticText32', parent=self,
              pos=wx.Point(16, 408), size=wx.Size(58, 17), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton15Button(self, event):
        
        self.Close()

    
    def lihatmiskin(self):
        self.isipenduduk.DeleteAllItems()    
        sql = "SELECT * FROM penduduk WHERE kemiskinan='Miskin' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchall() 
        nokk = self.isipenduduk.GetItemCount() 
        for i in hasil : 
            self.isipenduduk.InsertStringItem(nokk, "%s"%i[1]) 
            self.isipenduduk.SetStringItem(nokk,1,"%s"%i[2]) 
            self.isipenduduk.SetStringItem(nokk,2,"%s"%i[21])
            self.isipenduduk.SetStringItem(nokk,3,"%s"%i[30])
            
            nokk = nokk + 1    

    def OnIsipendudukListItemSelected(self, event):
        
        event.Skip()  

    def OnKklkButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE jk='L' AND shdk='Kepala Keluarga' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.kklaki.SetValue(str(hasil))
        event.Skip()

    def OnKkprButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE jk='P' AND shdk='Kepala Keluarga' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.kkperempuan.SetValue(str(hasil))
        event.Skip()

    def OnDifabelButton(self, event):
        event.Skip()

    def OnPendakhirButton(self, event):
        pdka = str(self.cbpddk.GetValue())
        if pdka == 'Tidak/Belum Sekolah':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Tidak/Belum Sekolah' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'Tidak Tamat SD/Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Tidak Tamat SD/Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'Tamat SD/Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Tamat SD/Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'SLTP/Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='SLTP/Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'SLTA/Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='SLTA/Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'Diploma I/II':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Diploma I/II' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'Akademi/Diploma III/S. Muda':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Akademi/Diploma III/S. Muda' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'Diploma IV/Strata I':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Diploma IV/Strata I' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'Strata II':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Strata II' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'Strata III':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Strata III' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        elif pdka == 'Pendidikan Non Formal':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='Pendidikan Non Formal' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))

        else :
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_akhir='' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikanakhir.SetValue(str(hasil))
            
        event.Skip()

    def OnPendsaatButton(self, event):
        pdks = str(self.cbsaat.GetValue())
        if pdks == 'PAUD Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='PAUD Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil)) 
            
        elif pdks == 'TK Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='TK Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        elif pdks == 'SD Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='SD Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        elif pdks == 'SLTP Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='SLTP Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        elif pdks == 'SLTA Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='SLTA Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        elif pdks == 'D1 Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='D1 Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        elif pdks == 'D2 Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='D2 Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        elif pdks == 'D3 Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='D3 Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        elif pdks == 'S1 Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='S1 Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        elif pdks == 'S2 Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='S2 Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
            
        elif pdks == 'S3 Sederajat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='S3 Sederajat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
            
        elif pdks == 'Pendidikan Non Formal':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='Pendidikan Non Formal' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))
        else :
            sql = "SELECT COUNT(*) FROM penduduk WHERE pddk_saat_ini='' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.jmlpendidikansaatini.SetValue(str(hasil))    
        
        event.Skip()

    def OnKkButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE shdk='Kepala Keluarga' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.jmlkk.SetValue(str(hasil))
        event.Skip()
       

    def OnWargaButton(self, event):
        wrg = str(self.cbwarga.GetValue())
        if wrg == 'WNI':
            sql = "SELECT COUNT(*) FROM penduduk WHERE warganegara='WNI' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiwarganegara.SetValue(str(hasil))
        elif wrg == 'WNA':
            sql = "SELECT COUNT(*) FROM penduduk WHERE warganegara='WNA' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiwarganegara.SetValue(str(hasil))
        else :
            sql = "SELECT COUNT(*) FROM penduduk WHERE warganegara='' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiwarganegara.SetValue(str(hasil))        
        event.Skip()

    def OnPekerjaanButton(self, event):
        pek = str(self.cbpek.GetValue())
        if pek == 'Belum/Tidak Bekerja':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Belum/Tidak Bekerja' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Mengurus Rumah Tangga':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Mengurus Rumah Tangga' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pelajar/Mahasiswa':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pelajar/Mahasiswa' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pensiunan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pensiunan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pegawai Negeri Sipil':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pegawai Negeri Sipil' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Tentara Nasional Indonesia':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tentara Nasional Indonesia' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Kepolisian RI':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Kepolisian RI' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Perdagangan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Perdagangan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Petani/Pekebun':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Petani/Pekebun' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Peternak':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Peternak' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Nelayan/Perikanan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Nelayan/Perikanan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Industri':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Industri' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Konstruksi':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Konstruksi' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Transportasi':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Transportasi' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Karyawan Swasta':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Karyawan Swasta' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Karyawan BUMN':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Karyawan BUMN' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Karyawan BUMD':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Karyawan BUMD' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Karyawan Honorer':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Karyawan Honorer' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Buruh Harian Lepas':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Buruh Harian Lepas' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Buruh Tani/Perkebunan':           
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Buruh Tani/Perkebunan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Buruh Nelayan/Perikanan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Buruh Nelayan/Perikanan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Buruh Peternakan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Buruh Peternakan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pembantu Rumah Tangga':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pembantu Rumah Tangga' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Tukang Cukur':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tukang Cukur' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Tukang Listrik':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tukang Listrik' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Tukang Batu':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tukang Batu' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Tukang Kayu':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tukang Kayu' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Tukang Sol Sepatu':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tukang Sol Sepatu' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Tukang Las/Pandai Besi':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tukang Las/Pandai Besi' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Tukang Jahit':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tukang Jahit' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Penata Rambut':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Penata Rambut' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Penata Rias':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Penata Rias' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Penata Busana':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Penata Busana' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Mekanik':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Mekanik' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Tukang Gigi':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tukang Gigi' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Seniman':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Seniman' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Tabib':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Tabib' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Paraji':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Paraji' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Perancang Busana':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Perancang Busana' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Penterjemah':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Penterjemah' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Imam Masjid':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Imam Masjid' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pendeta':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pendeta' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pastur':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pastur' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Wartawan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Wartawan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Ustadz/Mubaligh':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Ustadz/Mubaligh' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Juru Masak':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Juru Masak' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Promotor Acara':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Promotor Acara' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Anggota DPR-RI':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Anggota DPR-RI' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Anggota DPD':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Anggota DPD' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Anggota BPK':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Anggota BPK' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Presiden':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Presiden' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Wakil Presiden':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Wakil Presiden' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Anggota Mahkamah Konstitusi':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Anggota Mahkamah Konstitusi' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Anggota Kabinet/Kementerian':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Anggota Kabinet/Kementerian' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Duta Besar':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Duta Besar' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Gubernur':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Gubernur' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Wakil Gubernur':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Wakil Gubernur' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Bupati':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Bupati' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Wakil Bupati':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Wakil Bupati' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Walikota':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Walikota' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Wakil Walikota':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Wakil Walikota' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Anggota DPRD Propinsi':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Anggota DPRD Propinsi' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Anggota DPRD Kabupaten/Kota':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Anggota DPRD Kabupaten/Kota' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Dosen':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Dosen' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Guru':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Guru' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pilot':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pilot' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pengacara':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pengacara' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Notaris':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Notaris' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Arsitek':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Arsitek' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Akuntan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Akuntan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Konsultan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Konsultan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Dokter':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Dokter' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Bidan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Bidan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Perawat':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Perawat' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Apoteker':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Apoteker' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Psikiater/Psikolog':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Psikiater/Psikolog' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Penyiar Televisi':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Penyiar Televisi' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Penyiar Radio':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Penyiar Radio' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pelaut':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pelaut' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Peneliti':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Peneliti' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Sopir':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Sopir' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Pialang':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pialang' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Paranormal':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Paranormal' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Pedagang':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Pedagang' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
             
        elif pek == 'Perangkat Desa':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Perangkat Desa' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Kepala Desa':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Kepala Desa' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Biarawati':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Biarawati' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Wiraswasta':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Wiraswasta' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
            
        elif pek == 'Buruh Migran':
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='Buruh Migran' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
        else :
            sql = "SELECT COUNT(*) FROM penduduk WHERE pekerjaan='' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isipekerjaan.SetValue(str(hasil))
        event.Skip()

    def OnStatusButton(self, event):
        sta = str(self.cbstat.GetValue())
        if sta == 'Kawin':
            sql = "SELECT COUNT(*) FROM penduduk WHERE status='Kawin' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isistatus.SetValue(str(hasil))
            
        elif sta == 'Belum Kawin':
            sql = "SELECT COUNT(*) FROM penduduk WHERE status='Belum Kawin' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isistatus.SetValue(str(hasil))
            
        elif sta == 'Cerai Mati':
            sql = "SELECT COUNT(*) FROM penduduk WHERE status='Cerai Mati' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isistatus.SetValue(str(hasil))
            
        elif sta == 'Cerai Hidup':
            sql = "SELECT COUNT(*) FROM penduduk WHERE status='Cerai Hidup' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isistatus.SetValue(str(hasil))
        
        else :
            sql = "SELECT COUNT(*) FROM penduduk WHERE status='' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isistatus.SetValue(str(hasil))
                    
        event.Skip()

    def OnPrButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE jk='P' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.pendudukperempuan.SetValue(str(hasil))
        event.Skip()

    def OnTinggalButton(self, event):
        event.Skip()

    def OnPendudukButton(self, event):
        event.Skip()

    def OnHamilButton(self, event):
        event.Skip()

    def OnLkButton(self, event):
        sql = "SELECT COUNT(*) FROM penduduk WHERE jk='L' AND kematian='Tidak'"
        cur.execute(sql) 
        hasil = cur.fetchone()[0] 
        self.penduduklaki.SetValue(str(hasil))
        event.Skip()
        
    def OnDokButton(self, event):
        dok = str(self.cbdok.GetValue())
        if dok == 'Akta Kelahiran':
           sql = "SELECT COUNT(*) FROM penduduk WHERE dok1='Akta Kelahiran' AND kematian='Tidak'"
           cur.execute(sql) 
           hasil = cur.fetchone()[0] 
           self.isidokumen.SetValue(str(hasil)) 
        
        elif dok == 'Akta Nikah':
           sql = "SELECT COUNT(*) FROM penduduk WHERE dok2='Akta Nikah' AND kematian='Tidak'"
           cur.execute(sql) 
           hasil = cur.fetchone()[0] 
           self.isidokumen.SetValue(str(hasil))
           
        elif dok == 'Akta Cerai':
            sql = "SELECT COUNT(*) FROM penduduk WHERE dok3='Akta Cerai' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isidokumen.SetValue(str(hasil))
            
        elif dok == 'Akta Kematian':
            sql = "SELECT COUNT(*) FROM penduduk WHERE dok4='Akta Kematian' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isidokumen.SetValue(str(hasil))
            
        elif dok == 'KTP Sementara':
            sql = "SELECT COUNT(*) FROM penduduk WHERE dok5='KTP Sementara' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isidokumen.SetValue(str(hasil))
            
        elif dok == 'KITAS':
            sql = "SELECT COUNT(*) FROM penduduk WHERE dok6='KITAS' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isidokumen.SetValue(str(hasil))
            
        elif dok == 'VISA':
            sql = "SELECT COUNT(*) FROM penduduk WHERE dok7='VISA' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isidokumen.SetValue(str(hasil))
            
        elif dok == 'Paspor':
            sql = "SELECT COUNT(*) FROM penduduk WHERE dok8='Paspor' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isidokumen.SetValue(str(hasil))
            
        else :
            sql = "SELECT COUNT(*) FROM penduduk WHERE dok1='' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isidokumen.SetValue(str(hasil))
            
        event.Skip()

    def OnAgamaButton(self, event):
        aga = str(self.cbagama.GetValue())
        if aga == 'Islam':
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='Islam' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))
            
                
        elif aga == 'Kristen Protestan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='Kristen Protestan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))
                        
        elif aga == 'Kristen Katolik':
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='Kristen Katolik' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))
                        
        elif aga == 'Hindu':
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='Hindu' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))
            
        elif aga == 'Budha':
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='Budha' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))
            
        elif aga == 'Konghuchu':
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='Konghuchu' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))
            
        elif aga == 'Aliran Kepercayaan':
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='Aliran Kepercayaan' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))
            
        elif aga == 'Agama Lainnya':
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='Agama Lainnya' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))
            
        else :
            sql = "SELECT COUNT(*) FROM penduduk WHERE agama='' AND kematian='Tidak'"
            cur.execute(sql) 
            hasil = cur.fetchone()[0] 
            self.isiagama.SetValue(str(hasil))    
        
        event.Skip()
