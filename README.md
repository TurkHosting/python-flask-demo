# python-flask-demo

TurkHosting Python Hosting testleri için basit Flask uygulaması. Müşteri belgelerinin ve ekran görüntülerinin dayanağıdır.

## Uç noktalar
- `/` Framework ve Python sürümü
- `/health` Sağlık kontrolü
- `/visits` Kalıcı SQLite dosyası testi (`data.db`)

## Plesk'e yükleme
1. Dosyaları `httpdocs` içine yükleyin.
2. Python sayfasında sırasıyla **Scan**, **Enable Python**, **Create Virtual Environment**, **Install Dependencies**.
3. Sanal ortamdan sonra sayfayı yenileyin: Python yolu `.venv/bin/python` olmalı.
