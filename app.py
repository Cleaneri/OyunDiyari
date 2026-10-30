import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Dosyaların barınacağı klasör yolu
DOWNLOAD_FOLDER = os.path.join(app.root_path, 'downloads')

# Dosya isimleri
WINDOWS_DOSYA = 'Oyun_Diyari_v1.0.exe'
ANDROID_DOSYA = 'Oyun_Diyari_v1.0.apk'

@app.route('/')
def ana_sayfa():
    # Artık doğrudan butonların olduğu ana sayfayı yüklüyoruz
    return render_template('index.html')

@app.route('/download/windows')
def download_windows():
    # Klasör veya dosya yoksa hata vermemesi için geçici dosya oluşturur
    if not os.path.exists(os.path.join(DOWNLOAD_FOLDER, WINDOWS_DOSYA)):
        os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
        with open(os.path.join(DOWNLOAD_FOLDER, WINDOWS_DOSYA), 'w') as f:
            f.write("Oyun Diyari v1.0 Windows Kurulum Dosyasi")

    return send_from_directory(DOWNLOAD_FOLDER, WINDOWS_DOSYA, as_attachment=True)

@app.route('/download/android')
def download_android():
    # Klasör veya dosya yoksa hata vermemesi için geçici dosya oluşturur
    if not os.path.exists(os.path.join(DOWNLOAD_FOLDER, ANDROID_DOSYA)):
        os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
        with open(os.path.join(DOWNLOAD_FOLDER, ANDROID_DOSYA), 'w') as f:
            f.write("Oyun Diyari v1.0 Android Kurulum Dosyasi")
            
@app.route('/google63dd5220789c7bff.html')
def google_verify():
    return render_template('google63dd5220789c7bff.html')

    return send_from_directory(DOWNLOAD_FOLDER, ANDROID_DOSYA, as_attachment=True)
