# 💰 Harcama Takipçisi

Modern ve kullanıcı dostu bir Django tabanlı kişisel harcama takip uygulaması.

## ✨ Özellikler

### 🎯 Temel Özellikler
- **Harcama Yönetimi**: Harcamalarınızı kolayca ekleyin, düzenleyin ve silin
- **Kategorize Etme**: Harcamalarınızı 10 farklı kategoride organize edin
- **Tarih Seçimi**: İstediğiniz tarihe harcama ekleyin
- **Açıklama Desteği**: Her harcamaya detaylı açıklama ekleyin

### 📊 Analiz ve Raporlama
- **Görsel Grafikler**: Chart.js ile interaktif pasta ve çizgi grafikleri
- **Zaman Bazlı İstatistikler**: Günlük, haftalık, aylık ve yıllık harcama özetleri
- **Kategori Analizi**: Hangi kategorilerde ne kadar harcadığınızı görün
- **Trend Analizi**: Son 30 günün harcama trendini takip edin

### 🎨 Kullanıcı Arayüzü
- **Modern Tasarım**: Tailwind CSS ile responsive ve modern arayüz
- **Türkçe Dil Desteği**: Tamamen Türkçe arayüz
- **Mobil Uyumlu**: Tüm cihazlarda mükemmel görünüm
- **Koyu/Açık Tema**: Kullanıcı tercihine göre tema seçimi

### 🔒 Güvenlik
- **CSRF Koruması**: Güvenli form işlemleri
- **XSS Koruması**: Güvenli veri girişi ve çıkışı
- **Güvenli Oturumlar**: Gelişmiş oturum yönetimi

## 🚀 Kurulum

### Ön Gereksinimler
- Python 3.8+
- Node.js (Tailwind CSS için)
- Git

### Adım Adım Kurulum

1. **Projeyi klonlayın:**
```bash
git clone <repo-url>
cd expensetracker/tracker
```

2. **Sanal ortam oluşturun ve aktifleştirin:**
```bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# macOS/Linux için:
source venv/bin/activate
```

3. **Python bağımlılıklarını yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Node.js bağımlılıklarını yükleyin:**
```bash
npm install
```

5. **Tailwind CSS'i derleyin:**
```bash
npm run build
```

6. **Veritabanı migrasyonlarını çalıştırın:**
```bash
make mm
make mig
```

7. **Süper kullanıcı oluşturun:**
```bash
make createsuperuser
```

8. **Geliştirme sunucusunu başlatın:**
```bash
make run
```

## 🛠️ Kullanılabilir Komutlar

Projede kolaylık için Makefile komutları mevcuttur:

```bash
make run              # Django geliştirme sunucusunu başlat
make mig              # Veritabanı migrasyonlarını uygula
make mm               # Migration dosyalarını oluştur
make shell            # Django shell'i aç
make createsuperuser  # Süper kullanıcı oluştur
make test             # Testleri çalıştır
make collect-static   # Statik dosyaları topla
```

## 📱 Kullanım

### Harcama Ekleme
1. Ana sayfada "Yeni Harcama Ekle" formunu doldurun
2. Harcama adı, tutar, kategori ve tarihi girin
3. İsteğe bağlı olarak açıklama ekleyin
4. "Harcama Ekle" butonuna tıklayın

### Harcama Düzenleme
1. Harcama listesinde düzenlemek istediğiniz harcamanın yanındaki ✏️ ikonuna tıklayın
2. Bilgileri güncelleyin
3. "Değişiklikleri Kaydet" butonuna tıklayın

### Harcama Silme
1. Düzenleme sayfasında "Sil" butonuna tıklayın veya
2. Harcama listesinde 🗑️ ikonuna tıklayın
3. Onay verin

### Raporları İnceleme
- Ana sayfada otomatik olarak gösterilen istatistikleri inceleyin
- Kategori dağılımı pasta grafiğini görüntüleyin
- Günlük harcama trendini çizgi grafikte takip edin

## 🏗️ Proje Yapısı

```
tracker/
├── app/                    # Ana Django uygulaması
│   ├── models.py          # Veritabanı modelleri
│   ├── views.py           # View fonksiyonları
│   ├── forms.py           # Django formları
│   ├── admin.py           # Yönetici paneli konfigürasyonu
│   ├── urls.py            # URL yönlendirmeleri
│   ├── templates/         # HTML şablonları
│   └── static/            # CSS, JS ve görsel dosyalar
├── tracker/               # Django proje ayarları
│   ├── settings.py        # Proje konfigürasyonu
│   ├── urls.py            # Ana URL konfigürasyonu
│   └── wsgi.py            # WSGI konfigürasyonu
├── requirements.txt       # Python bağımlılıkları
├── package.json          # Node.js bağımlılıkları
├── Makefile              # Kısayol komutları
└── README.md             # Bu dosya
```

## 🎨 Teknolojiler

### Backend
- **Django 4.2.23**: Web framework
- **SQLite**: Veritabanı
- **Python 3.8+**: Programlama dili

### Frontend
- **Tailwind CSS 2.2.16**: CSS framework
- **Chart.js**: Grafik kütüphanesi
- **Font Awesome**: İkon kütüphanesi
- **HTML5/CSS3/JavaScript**: Web teknolojileri

### Geliştirme Araçları
- **Django Debug Toolbar**: Debug yardımcısı
- **Django Extensions**: Geliştirme araçları
- **Whitenoise**: Statik dosya sunumu

## 🔧 Konfigürasyon

### Ortam Değişkenleri
Üretim ortamı için `.env` dosyası oluşturun:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
```

### Güvenlik Ayarları
Üretim ortamında aşağıdaki ayarları güncelleyin:
- `DEBUG = False`
- `SECURE_SSL_REDIRECT = True`
- `SESSION_COOKIE_SECURE = True`
- `CSRF_COOKIE_SECURE = True`

## 📊 Kategoriler

Uygulama aşağıdaki harcama kategorilerini destekler:
- 🍽️ Yiyecek & İçecek
- 🚗 Ulaşım
- 🎬 Eğlence
- 💡 Faturalar
- 🛍️ Alışveriş
- 🏥 Sağlık
- 📚 Eğitim
- 🏠 Konut
- 👔 Giyim
- 📦 Diğer

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 📞 Destek

Sorularınız veya önerileriniz için:
- Issue açın
- E-posta gönderin
- Dokumentasyonu inceleyin

## 🚀 Gelecek Özellikler

- [ ] Kullanıcı hesapları ve kimlik doğrulama
- [ ] Çoklu para birimi desteği
- [ ] Excel/PDF export
- [ ] Bütçe belirleme ve uyarılar
- [ ] Gelir takibi
- [ ] Mobil uygulama
- [ ] REST API
- [ ] Çoklu dil desteği

---

**Geliştirici**: Ahmet Resul KURU  
**Versiyon**: 2.0.0  
**Son Güncelleme**: 2024 