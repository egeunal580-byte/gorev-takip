# Görev Takipçisi

Günlük görevleri eklemeye, tamamlandı olarak işaretlemeye ve silmeye yarayan basit bir web uygulaması. Arayüz HTML ve CSS ile hazırlandı; Flask uygulaması görevleri SQLite veritabanında saklıyor.

## Özellikler

- Görev ekleme
- Görevi tamamlandı veya bekliyor olarak işaretleme
- Görev silme
- SQLite ile kalıcı kayıt
- Telefon ve masaüstü ekranlarına uyumlu arayüz

## Kullanılan teknolojiler

- Python 3
- Flask
- SQLite
- HTML ve CSS

## Bilgisayarında çalıştırma

1. Python 3'ü yükle.
2. Bu klasörde bir terminal aç.
3. Sanal ortam oluşturup etkinleştir:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   macOS veya Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Gerekli paketi yükle:

   ```bash
   pip install -r requirements.txt
   ```

5. Uygulamayı başlat:

   ```bash
   python app.py
   ```

6. Tarayıcıda `http://127.0.0.1:5000` adresini aç.

İlk çalıştırmada `tasks.db` dosyası otomatik oluşturulur. Bu dosya `.gitignore` içinde olduğu için kişisel görevlerin GitHub'a yüklenmez.

## Proje yapısı

```text
gorev-takip/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Öğrenme notu

Bu proje Flask'ta sayfa gösterme ve form alma, Python ile SQLite sorguları çalıştırma ve HTML şablonlarını dinamik içerikle doldurma konularını pratik etmek için hazırlanmıştır.
