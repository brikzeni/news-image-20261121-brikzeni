# Competitive Intel — news-image-20261121 (@brikzeni)

**Dibuat:** 22 Nov 2026 ~15:35 UTC (cek langsung hari itu)
**Sumber:** leaderboard https://make.fun/bounty/news-image-20261121/leaderboard,
API https://make.fun/api/competitions/news-image-20261121,
halaman profil tiap handle top 10, halaman entri `/s/<id>`,
dan pencarian berita (vertikal news) untuk verifikasi peristiwa 21 Nov 2026.
**Status brikzeni:** tidak ada entri `brikzeni` yang ditemukan di teks API kompetisi
saat pengecekan ini (pencarian `brikzeni` di dump API = 0 hasil) — entri kita
belum ada / belum ter-submit saat intel ini dibuat.

## ⚠️ Batasan metode — baca dulu

**Gambar para entri TIDAK bisa dilihat lewat `browser.open`.** Halaman entri
(`/s/<id>`, contoh: `01a20295-848f-75d9-a078-0c935496a24a` milik @akun-fft)
dan tampilan feed (`?post=<id>#feed`) dalam bentuk teks hanya mengembalikan
judul + handle — tanpa data gambar, tanpa footnote `Images:`. API kompetisi
juga hanya berisi judul/handle/`score`, bukan URL gambar.

**Konsekuensi:** semua analisis visual di bawah ini (jumlah cerita, wilayah,
peta, timeline, kartu ilustrasi, klaim verifikasi) berasal dari **judul entri,
profil handle, dan pola judul di API** — bukan dari inspeksi piksel.
Yang TIDAK teramati dan TIDAK boleh diklaim: warna/kontras spesifik,
keterbacaan huruf, hierarki visual, dan komposisi persis entri mana pun.
Bagian "Tidak teramati" di bawah merinci ini. Jangan ada yang meniru
artwork, kode, atau komposisi persis entri mana pun — intel ini hanya analisis.

## Fakta kompetisi (terverifikasi dari API + halaman bounty)

- Judul: "Sum up 21 November's world news in one image" — Sabtu 21 Nov 2026.
- Deadline: **23 Nov 2026 00:00 UTC**. Hadiah $100 (1st $20, 2nd $12, 3rd $6,
  4th–10th $2, 11th–50th $1,20). Escrow $100 USDC terkunci sejak 21 Nov 01:56 UTC.
- **21.888 submission** (submissionCount di API) — jauh lebih ramai dari
  news-image-20261119/20261120.
- Juri: AI yang bisa melihat gambar, **z-ai/glm-5.3-flash** (OpenRouter),
  pairwise — dua gambar dibandingkan per call, margin 1–5, tiap pasangan
  diuji dua arah, **3 ronde Swiss + playoff top 52**. Juri TIDAK punya feed
  berita: ia menilai dari apa yang terlihat di gambar itu sendiri.
- Ranking leaderboard saat ini **"Live ranking, unofficial"** — ranking resmi
  ditetapkan final run setelah deadline.
- Gambar: PNG/JPEG utuh, maks 1 MiB, maks 1024×1024 px, program tanpa network,
  dua run harus menghasilkan byte identik (deterministik).
- Dev phase: tiap entri valid langsung di-judge melawan 4 gambar house +
  8 gambar house terdekat — jadi win rate profil adalah hasil dev, bukan final.

## Top 10 — tabel utama (per 22 Nov 2026 ~15:20 UTC)

| # | Handle | Judul entri (leaderboard) | Cerita | Wilayah | Win rate* | Catatan |
|---|--------|---------------------------|--------|---------|-----------|---------|
| 1 | @akun-fft | Saturday 21 November 2026: 37 stories, 9 regions | 37 | 9 | **99,3%** | Win rate tertinggi yang terverifikasi di profil. 8x placed dari 22 entry, $0 dibayar. |
| 2 | @y-cat33 | Saturday 21 November 2026: 37 date-checked stories, 9 regions — Bahrain says Iran struck it, Mexico captures 'El Chapo Isidro', COP31 overtime | 37 | 9 | tidak terverifikasi | Profilnya hanya menampilkan 2 solusi 19 Nov (99,1% di sana); entri 21 Nov tidak muncul di profil saat dicek. |
| 3 | @skyscrapperr | Saturday 21 November 2026: 35 dated stories, 9 regions — Iran hits Bahrain bases, deep Peru quake, COP31 overtime | 35 | 9 | **99,2%** | 5x submit judul identik (iterasi/resubmit). Juga 1st-place-calibre di GTA 6 (99,1%). |
| 4 | @f22r | Saturday 21 November 2026: 35 verified stories, 7 regions, Natural Earth map, UTC strip & strict date check | 35 | 7 | 97,7%† | †97,7% adalah varian saudaranya ("35 verified stories … COP31 Day 13, Bahrain & Hormuz strikes, El Chapo Isidro, BepiColombo"); varian peta Natural Earth sendiri tidak menampilkan win rate di profil. 6 varian 35 cerita diajukan. |
| 5 | @superskie | Saturday 21 November 2026 in one picture | — | — | **99,2%** | **Tanpa angka cerita di judul.** Pemenang 1st 19 Nov ($50, 86,4% final), total 5 kemenangan / $476,15 dibayar. Bukti rute "satu gambar kuat" bisa menembus top 5. |
| 6 | @vivid-walrus-44-2678 | Saturday 21 November 2026: 36 dated stories across seven regions | 36 | 7 | **98,9%** | 10 versi diajukan (31→36 cerita); versi final = jumlah tertinggi. Akun baru, hanya ikut kompetisi ini. |
| 7 | @quiet-panda-11 | Saturday 21 November 2026: 49 stories, 7 regions, 41 fields, each tagged by how sure it is, with UTC strip, pin map and date check | 49 | 7 | tidak terverifikasi | Profil menampilkan 0 solusi. Klaim terbanyak di top 10 + **tag keyakinan per cerita** (differentiator unik). |
| 8 | @kakek-zeus | Certain Mirror | — | — | **99,1%** | **Tanpa angka/tanggal di judul** — judul abstrak dua kata, tetap 99,1%. Juga 98,6% di news-20. |
| 9 | @lively-pika-72-4981 | World news front page: 39 dated stories, UTC timeline, Gulf map, illustrated cards, 21 Nov 2026 | 39 | — | **99,1%** | Iterasi 27→44 cerita dalam 11 solusi; versi leaderboard (39) BUKAN yang terbanyak (44) — jumlah maks ≠ terbaik. Format: front page + timeline UTC + peta Teluk + kartu ilustrasi. |
| 10 | @asell | Saturday 21 November 2026 — The World's News in One Picture (Round 2) | — | — | **99,1%** | "Round 2" = iterasi kedua. Veteran (36 entry, 11 placed, $27 dibayar); di 17 Nov 48 cerita hanya 209th (70,7%), di 18 Nov 39 cerita 446th (72,1%) — jumlah besar saja tidak menjamin. |

\* Win rate = dev-phase judge win rate dari halaman profil handle, per 22 Nov 2026.
Bukan ranking final. Selisih top 10 sangat rapat (97,7–99,3%): perbedaan
peringkat lebih ditentukan playoff Swiss nanti daripada selisih win rate dev.

## Top 11–50 — pola yang menguatkan

- **#12 @danza-gyporct:** 42 cerita, 7 wilayah, "every panel drawn" — COP31
  overtime, Riyadh missiles, Peru quake.
- **#13 @ijeawele-harold-odili:** "Russian ship ablaze off Finland, Iran strike
  hits Bahrain, M6.7 Peru quake and 43 more date-checked stories" (~46 total).
- **#14 @ulinnuha-eth:** 34 cerita, 7 wilayah — Iran–Bahrain, COP31, El Chapo Isidro.
- **#15 @sipa:** 33 cerita, satu front page.
- **#18 @semogaudinjp:** v3, "Bahrain leads, 36 stories".
- **#19 @myhanni:** 36 cerita, 7 wilayah, **13 illustrated cards**, satu front page.
- **#20 @ryanp1632-netizen:** 35 cerita, 7 wilayah — Riyadh missiles, Peru M6.7,
  COP31 deadlock, Iran drone claim.
- **#21 @guy-sensei:** 36 cerita, 6 wilayah — Riyadh intercepts, COP31 overtime,
  BepiColombo at Mercury.
- **#26 @quiet-puffin-39:** 35 cerita — BepiColombo, COP31, Hormuz tankers.
- **#28 @ryan-liu:** 36 cerita, "numbers strip 146" — Davao jet, Las Vegas GP,
  UK-EU reset (angka/statistik sebagai strip tersendiri).
- **#34 @calm-owl-82:** 41 cerita, 8 wilayah — Hormuz tankers, Baltic ship fire,
  Mexico cartel capture.
- **#38 @raiden-mei:** 53 cerita (terbanyak di top 50).
- **#40 @miku39-lab:** 35 cerita, "each with its source, from 7 regions;
  13 drawn; **10 left out by a date check**" — eksplisit menampilkan cerita
  yang DIBUANG karena gagal cek tanggal (sinyal ketelitian).
- **#29 @hazel-badger-33-1076:** 29 cerita, satu peta (terendah di top 50).

## Distribusi jumlah cerita (dihitung dari judul top 50)

Dari 50 judul leaderboard, **31 menyebut angka cerita secara eksplisit**:

- **Kisaran: 29–53 cerita. Modus: 35. Median: 35. Rata-rata: ~36,8.**
- 35 cerita muncul 11× — angka paling umum di top 50.
- Top 10 yang menyebut angka: 35–49 (37, 37, 35, 35, 36, 49, 39).
- Di bawah 30 hanya #29 (29 cerita, masih top 30); di atas 45 hanya #7 (49),
  #13 (~46), #38 (53) — jumlah ekstrem bukan jaminan peringkat 1
  (#38 dengan 53 cerita hanya peringkat 38; #1 menang dengan 37).
- **Wilayah: modus 7 region, maks 9.** Top 3 semuanya 9 region; #21 hanya
  6 region tapi tetap top 25. Klaim "9 regions" berkorelasi dengan top 3,
  tapi 7 region sudah cukup untuk top 10.

## Peristiwa dominan 21 Nov 2026 (dari judul top 50 + verifikasi berita)

Urutan kemunculan di judul-judul top 50 — ini yang dianggap "wajib ada"
oleh konsensus entri:

1. **Iran menyerang Bahrain / pangkalan AS di Bahrain** — hampir di semua
   judul top 10. Framing bervariasi: "Iran hits Bahrain bases" (#3),
   "Bahrain says Iran struck it" (#2 — atribusi hati-hati),
   "Bahrain & Hormuz strikes" (#4). Verifikasi berita: Iran menyerang
   pangkalan AS di Bahrain dengan rudal+drone 21–22 Nov; Bahrain menyebut
   fasilitas sipil kena dan 2 orang luka; Iran mengklaim menghancurkan
   2 radar Patriot AS. **Jebakan:** klaim korban/kerusakan berbeda antar
   sumber — tulis atribusi ("Bahrain says…", "Iran claims…"), jangan
   jadikan satu angka sebagai fakta mutlak.
2. **COP31 overtime / deadlock (Antalya)** — "COP31 overtime" di #2, #3,
   #12, #21; "deadlock" di #20, #26. Verifikasi: perundingan melewati
   deadline Jumat, buntu soal bahan bakar fosil. **Jebakan tanggal:**
   COP31 baru COLLAPSED (tanpa kesepakatan) pada 22 Nov — entri 21 Nov
   TIDAK boleh mengklaim "COP31 collapsed" sebagai peristiwa 21 Nov.
3. **Gempa Peru M6.7, Junín (dalam)** — "deep Peru quake" (#3), "Peru M6.7"
   (#13, #20). Verifikasi: AP/AFP 20 Nov — M6.7, 1 tewas, 16 luka,
   853 mengungsi; sebagian roundup menulis M6.9 dan "tanpa korban".
   **Jebakan:** magnitudo + tanggal (gempa terjadi Jumat malam 20 Nov
   waktu setempat, dilaporkan 21 Nov) + angka korban — pilih satu sumber
   konsisten dan beri tanggal.
4. **Saudi/Riyadh mencegat rudal Houthi** — "Riyadh missiles" (#12),
   "three missiles over Riyadh" (#37), "Saudi intercepts" (#21).
   Verifikasi: pertahanan Saudi mencegat 3 rudal balistik Houthi ke
   Riyadh Sabtu dini hari.
5. **Meksiko menangkap 'El Chapo Isidro'** (Fausto Isidro Meza Flores,
   Guasave, Sinaloa; 11 tewas dalam penangkapan, reward AS $5 juta) — #2, #4, #14.
6. **Ukraina: serangan ke Kryvyi Rih** (kota asal Zelenskyy; anak 7 thn +
   perempuan 20 thn tewas, 60+ luka) + **Kyiv strikes** — #27, dan
   disebut di banyak judul 35-cerita.
7. **BepiColombo tiba di Merkurius** — #4, #21, #26, #40. Cerita sains
   "ringan" yang konsisten muncul sebagai penyeimbang.
8. **Selat Hormuz / tanker terbakar dekat Khasab, Oman** — #4, #26, #34.
   Iran mengklaim ranjau laut; UKMTO melaporkan proyektil; tanpa korban.
9. **Kapal kargo Rusia Sparta II terbakar di Teluk Finlandia** (2 drone,
   16 kru dievakuasi) — #13, #34.
10. **Lapis kedua (penyeimbang geografis):** Davao jet, Las Vegas GP,
    UK-EU reset (#28), Ethiopia displacement (#37), EU-Indonesia trade deal,
    ICJ Rohingya (disebut di #40 konteks 19–20 Nov — hati-hati tanggal),
    AI sell-off / Nasdaq (S&P −3,7%, Nasdaq −5,3% Jumat).

**Cakupan geografis yang diharapkan juri:** Teluk/Middle East mendominasi
lead, lalu Eropa (Ukraina, Finlandia, COP31 Antalya), Amerika Latin
(Peru, Meksiko), Asia-Pasifik, sains/luar angkasa, pasar/ekonomi.
Entri yang hanya fokus satu kawasan akan kalah lawan yang 7–9 region.

## Pola format pemenang (dari judul + metadata, BUKAN dari piksel)

1. **Arsitektur "front page + daftar brief" dominan.** Judul-judul
   menyebut: front page, UTC timeline/strip, peta (Gulf map, Natural Earth
   map, pin map), kartu ilustrasi, numbers strip. Contoh arsitektur yang
   berulang: ~3 lead besar + ~12–15 kartu/panel ilustrasi + ~35 brief
   berlabel wilayah. Angka "13 illustrated cards" muncul berulang
   (#19: 13 kartu; #40: 13 drawn; #9: 12–15 kartu antar versi).
2. **Sinyal verifikasi dijual di judul.** Kata yang berulang di top 10:
   "date-checked", "dated stories", "verified stories", "strict date check",
   "each tagged by how sure it is" (#7), "each with its source" (#40),
   "10 left out by a date check" (#40). Juri tidak punya feed berita —
   sinyal ketelitian tanggal di DALAM gambar (strip UTC, cap tanggal,
   label sumber) adalah cara entri meyakinkan juri.
3. **Spesifisitas headline.** Judul entri top menamai peristiwa spesifik
   ("Iran hits Bahrain bases", "deep Peru quake", "COP31 overtime") bukan
   "World News Today" generik. Tiga lead spesifik di judul = pola top 3.
4. **Iterasi multi-varian adalah norma.** @skyscrapperr 5× judul identik,
   @f22r 6 varian, @vivid-walrus 10 versi, @lively-pika 11 solusi,
   @asell "Round 2". Pemenang bukan one-shot; mereka menguji varian dan
   membiarkan win rate dev memilih. Catatan: versi leaderboard belum tentu
   varian jumlah-terbanyak.
5. **Dua rute menuju top 10 — dan keduanya ada buktinya:**
   - Rute A (mayoritas, 7 dari top 10): digest padat 35–49 cerita,
     7–9 region, peta + timeline + kartu ilustrasi.
   - Rute B (minoritas tapi nyata): satu gambar editorial kuat tanpa angka
     di judul — #5 @superskie "in one picture" (99,2%; juara 1 di 19 Nov)
     dan #8 @kakek-zeus "Certain Mirror" (99,1%). Ini relevan dengan
     arahan user untuk news-image: poster/ilustrasi editorial yang kuat,
     bukan template koran ber-kotak-kotak. Rute B lebih berisiko (butuh
     konsep visual yang sangat kuat) tapi bukan tanpa preseden.
6. **Judul entri = ringkasan yang dibaca juri manusia? Tidak — tapi judul
   mencerminkan isi gambar.** Karena juri hanya melihat gambar, judul yang
   menyebut "37 stories, 9 regions" hampir pasti berarti gambarnya memang
   memuat hitungan itu secara terbaca. Judul adalah proksi isi yang cukup
   dapat dipercaya di kompetisi ini.

## Kekuatan & kelemahan per entri top 10 (inferensi dari judul/profil saja)

- **#1 @akun-fft (37/9, 99,3%):** Kekuatan — kombinasi jumlah + wilayah
  tertinggi di top 3, win rate tertinggi. Kelemahan (inferensi) — judul
  tidak menyebut peta/timeline/kartu ilustrasi; tidak ada diferensiator
  format yang terlihat dari judul. Pelajaran: fondasi "37 cerita, 9 region"
  yang bersih sudah cukup untuk #1.
- **#2 @y-cat33 (37/9):** Kekuatan — framing atribusi paling hati-hati
  ("Bahrain says…"). Kelemahan — profil tidak menampilkan entri 21 Nov-nya
  (tidak bisa diverifikasi win rate-nya dari profil).
- **#3 @skyscrapperr (35/9, 99,2%):** Kekuatan — 9 region + 3 lead spesifik
  di judul; iterasi agresif. Kelemahan — 35 cerita (bukan 37) tapi 9 region:
  wilayah lebih penting daripada +2 cerita.
- **#4 @f22r (35/7, peta Natural Earth + UTC strip + strict date check):**
  Kekuatan — diferensiasi teknis paling eksplisit (peta + strip UTC + cek
  tanggal). Kelemahan — 7 region (lebih sempit dari top 3) dan win rate
  varian terverifikasi 97,7%, terendah di top 10 yang terverifikasi.
- **#5 @superskie (tanpa angka, 99,2%):** Kekuatan — rekam jejak juara
  (5 kemenangan, $476); membuktikan gambar-tunggal bisa menang. Kelemahan —
  tanpa angka cerita, juri yang menghitung cakupan bisa menganggapnya
  kurang "merangkum hari itu" dibanding digest 35+ cerita.
- **#6 @vivid-walrus (36/7, 98,9%):** Kekuatan — iterasi 10 versi sampai
  36 cerita. Kelemahan — akun baru tanpa rekam jejak; tidak ada peta/
  timeline yang disebut di judul.
- **#7 @quiet-panda-11 (49/7, tag keyakinan, pin map, UTC strip):**
  Kekuatan — cerita terbanyak + satu-satunya tag keyakinan per cerita +
  41 fields. Kelemahan — risiko kepadatan/keterbacaan (49 cerita di
  1024×1024); profil 0 solusi = tidak terverifikasi.
- **#8 @kakek-zeus ("Certain Mirror", 99,1%):** Kekuatan — judul abstrak
  membuktikan juri menilai gambar, bukan judul. Kelemahan — tanpa sinyal
  jumlah/wilayah, sulit ditebak isinya; tidak bisa dipelajari polanya
  dari luar.
- **#9 @lively-pika (39, timeline UTC, peta Teluk, kartu ilustrasi, 99,1%):**
  Kekuatan — paket format paling lengkap di top 10. Kelemahan — versi
  44 cerita kalah dari versi 39 cerita: ada titik jenuh kepadatan.
- **#10 @asell (Round 2, 99,1%):** Kekuatan — iterasi round 2 + rekam
  jejak panjang. Kelemahan — riwayatnya menunjukkan jumlah besar saja
  tidak cukup (48 cerita → 209th di 17 Nov).

## Sinyal dari luar top 10 / dari API (konteks tambahan)

- Judul-judul di API menunjukkan para peserta sadar soal keterbacaan:
  "readable at 300px", "44px lead type", "High-Legibility Front Page",
  "hand-rolled PNG, own bitmap font" — keterbacaan adalah arena kompetisi,
  tapi tidak ada bukti piksel yang bisa dikutip di sini.
- Peringatan dari riwayat: @f22r di 19 Nov mengajukan "17 Verified Global
  Stories — High-Legibility Front Page" dan hanya 2301st (63,4%).
  **Terlalu sedikit cerita menghukum, betapa pun terbacanya.**
  Sebaliknya @asell 48 cerita di 17 Nov hanya 209th (70,7%) —
  **terlalu banyak tanpa hierarki juga menghukum.** Zona manis yang
  teramati: ~35–39 cerita.
- Contoh format dari postingan Threads yang terindeks (entri 21 Nov lain):
  front page "THE WORLD", 33 cerita, 3 lead utama, peta + 3 kolom +
  timeline di bawah — arsitektur yang sama dengan pola top 10.

## Yang TIDAK teramati (jangan diklaim)

- Warna, palet, kontras, tipografi, ukuran huruf aktual, dan hierarki
  visual entri mana pun — tidak ada piksel yang bisa diakses subagent ini.
- Apakah peta/timeline/kartu ilustrasi di gambar top 10 benar-benar
  terbaca atau justru berantakan.
- Skor mentah (`score` di API, mis. 920.628) bukan win rate dan tidak
  sebanding antar entri — jangan dipakai untuk ranking.
- Win rate @y-cat33 (#2) dan @quiet-panda-11 (#7) untuk entri 21 Nov
  tidak bisa diverifikasi dari profil mereka saat dicek.

## Pelajaran konkret untuk entri @brikzeni

1. **Target 35–39 cerita, 7–9 region — bukan 20, bukan 50.**
   Modus top 50 adalah 35; #1 menang dengan 37/9; 49–53 cerita tidak
   menang; 17 cerita pernah finis 2301st. Tulis angka cerita + wilayah
   secara terbaca di gambar (juri menghitung dari gambar).
2. **Lead dengan 3 peristiwa yang sama dengan konsensus, tapi dengan
   atribusi + tanggal yang disiplin.** Urutan lead: (1) Iran–Bahrain,
   (2) COP31 overtime, (3) gempa Peru M6.7 — lalu El Chapo Isidro,
   Riyadh, Kryvyi Rih, BepiColombo, Hormuz. Jangan klaim "COP31 collapsed"
   (itu 22 Nov), jangan campur M6.7/M6.9, jangan jadikan klaim sepihak
   (radar Patriot, korban) sebagai fakta tanpa "says/claims". Tambahkan
   strip UTC + cap "Saturday 21 November 2026" yang besar dan terbaca,
   dan (seperti #40) pertimbangkan menampilkan bahwa cerita yang gagal
   cek tanggal sengaja dibuang.
3. **Satu peta + satu timeline + ~13 kartu/panel ilustrasi, selebihnya
   brief singkat berlabel wilayah.** Ini paket format top 10 yang paling
   lengkap (#9) — peta Teluk untuk lead, timeline UTC di bawah, kartu
   ilustrasi untuk lead/kategori, daftar brief untuk sisanya. Sambil
   menjaga arahan user: poster/ilustrasi editorial yang kuat, satu konsep
   fokal, teks mendukung gambar — jangan jadi grid koran ber-kotak-kotak
   berisi teks. Jika rute B (satu gambar kuat ala #5/#8) yang dipilih,
   sadari risikonya: hanya 2 dari top 10 yang menempuhnya, dan keduanya
   punya rekam jejak juara; rute A (digest 35–39) adalah taruhan yang
   lebih aman secara statistik.
4. **Iterasi multi-varian, biarkan win rate dev memilih.** Top entrants
   mengajukan 5–11 varian. Jangan one-shot: siapkan 2–3 varian
   (mis. digest 37-cerita vs poster editorial) dan submit yang win
   rate-nya terbaik — tapi ingat batas 10 submit/hari, 20 total, dan
   submit terakhir sebelum deadline 23 Nov 00:00 UTC adalah final.
   Perhatian: "gas" setelah deadline tidak berlaku (pelajaran GTA 21 Nov).

## Larangan

Tidak ada artwork, kode, atau komposisi persis entri mana pun yang disalin
dalam intel ini — hanya judul publik, angka, dan pola yang dianalisis.
