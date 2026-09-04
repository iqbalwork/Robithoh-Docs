# 📖 Robithoh Docs (Content Repository)

Repositori ini menyimpan seluruh dokumen amaliyah, dzikir, manaqib, sholat sunnah, dan liturgi TQN untuk aplikasi **Robithoh App**.

Setiap perubahan atau penambahan dokumen pada repositori ini akan langsung disinkronisasi ke aplikasi mobile pengguna secara *over-the-air* (tanpa rilis ulang APK/IPA).

---

## 📁 Struktur Repositori

```text
Robithoh-Docs/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions: auto-generate manifest & deploy Pages
├── documents/                  # Seluruh berkas naskah format Markdown (.md)
│   ├── DZIKIR_TQN.md
│   ├── KHOTAMAN_TQN.md
│   ├── MANQOBAH_INDONESIA.md
│   └── ... (48 berkas liturgi)
├── scripts/
│   └── generate_manifest.py    # Generator manifest.json & kalkulasi hash SHA-256
├── manifest.json               # Manifest metadata berkas & versi untuk mobile app
└── README.md
```

---

## ✍️ Cara Menyesuaikan atau Mengedit Dokumen

1. Buka folder `documents/` dan pilih berkas Markdown yang ingin diedit (misal: `DZIKIR_TQN.md`).
2. Edit teks, koreksi harakat, atau perbaiki terjemahan langsung di GitHub (atau via Git lokal).
3. Commit dan push ke branch `main`.
4. **GitHub Action** akan otomatis:
   * Menghitung ulang hash SHA-256 dokumen yang berubah.
   * Menaikkan nomor versi di `manifest.json`.
   * Meng-*deploy* ke CDN / GitHub Pages.
5. Aplikasi **Robithoh App** pada perangkat pengguna akan mendeteksi perbedaan hash SHA-256 dan memperbarui naskah lokal secara otomatis.

---

## ⚙️ Menjalankan Generator Manifest Secara Lokal (Opsional)

Jika ingin memperbarui `manifest.json` di komputer lokal sebelum push:

```bash
python3 scripts/generate_manifest.py
```

---

## 🌐 Endpoint Akses untuk Mobile App

* **Manifest:**
  * GitHub Pages: `https://iqbalwork.github.io/Robithoh-Docs/manifest.json`
  * jsDelivr CDN: `https://cdn.jsdelivr.net/gh/iqbalwork/Robithoh-Docs@main/manifest.json`
* **Dokumen:**
  * GitHub Pages: `https://iqbalwork.github.io/Robithoh-Docs/documents/{fileName}`
  * jsDelivr CDN: `https://cdn.jsdelivr.net/gh/iqbalwork/Robithoh-Docs@main/documents/{fileName}`

> **Catatan Pengaturan GitHub Pages:**
> Pastikan di tab **Settings** -> **Pages** pada repositori GitHub ini, opsi **Source** diatur ke **GitHub Actions**.
