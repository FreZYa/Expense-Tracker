# Harcama Takipçisi - Makefile
# Django proje yönetimi için kısayol komutları

.PHONY: help run mig mm shell createsuperuser test collect-static build-css watch-css clean install

# Varsayılan hedef
.DEFAULT_GOAL := help

help:  ## Bu yardım mesajını göster
	@echo "🚀 Harcama Takipçisi - Kullanılabilir Komutlar:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

run:  ## Django geliştirme sunucusunu başlat
	python manage.py runserver

mig:  ## Veritabanı migrasyonlarını uygula
	python manage.py migrate

mm:  ## Migration dosyalarını oluştur
	python manage.py makemigrations

shell:  ## Django shell'i aç
	python manage.py shell

createsuperuser:  ## Süper kullanıcı oluştur
	python manage.py createsuperuser

test:  ## Testleri çalıştır
	python manage.py test

collect-static:  ## Statik dosyaları topla
	python manage.py collectstatic --noinput

build-css:  ## Tailwind CSS'i derle
	npm run build

watch-css:  ## Tailwind CSS'i izle ve otomatik derle
	npx tailwindcss -i app/static/src.css -o app/static/styles.css --watch

clean:  ## Geçici dosyaları temizle
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".DS_Store" -delete

install:  ## Tüm bağımlılıkları yükle
	pip install -r requirements.txt
	npm install

setup:  ## Projeyi ilk kez kurun (full setup)
	pip install -r requirements.txt
	npm install
	npm run build
	python manage.py makemigrations
	python manage.py migrate
	@echo "🎉 Kurulum tamamlandı! 'make createsuperuser' ile admin kullanıcısı oluşturun."
	@echo "📝 Ardından 'make run' ile sunucuyu başlatın."

reset-db:  ## Veritabanını sıfırla (DİKKAT: Tüm veri silinir!)
	rm -f db.sqlite3
	python manage.py makemigrations
	python manage.py migrate
	@echo "⚠️  Veritabanı sıfırlandı! Yeni superuser oluşturmayı unutmayın."

backup:  ## Veritabanını yedekle
	cp db.sqlite3 backup_db_$(shell date +%Y%m%d_%H%M%S).sqlite3
	@echo "✅ Veritabanı yedeklendi!"

dev:  ## Geliştirme ortamını başlat (CSS watch + server)
	make watch-css &
	make run

check:  ## Kod kalitesi kontrolü
	python manage.py check
	python manage.py check --deploy

requirements:  ## requirements.txt güncelle
	pip freeze > requirements.txt

deploy-static:  ## Statik dosyaları hazırla ve topla
	npm run build
	python manage.py collectstatic --noinput
	@echo "📦 Statik dosyalar hazırlandı!"