🎬 FilmApp - Film ve Dizi Servisi
FilmApp, film severler için tasarlanmış, modern ve kullanıcı dostu bir masaüstü uygulamasıdır. Python ve Tkinter ile geliştirilen bu uygulama, favori filmlerinizi keşfetmenizi, detaylarını görüntülemenizi ve fragmanlarını izlemenizi sağlar. Neon esintili, genç ve enerjik arayüzüyle (morumsu #12032b, mavi #007bff, yeşil #28a745) film keyfinizi bir üst seviyeye taşır! 😎
Bu proje, basit bir kullanıcı giriş sistemi, film arama özelliği ve YouTube fragman bağlantıları ile donatılmıştır. Film kapak görselleri ve hata yakalama mekanizmalarıyla profesyonel bir deneyim sunar. Kanka, hadi filmlere dalalım! 🎥
📋 Özellikler

Kullanıcı Girişi ve Kayıt: Güvenli kullanıcı yönetimi (kullanicilar.txt ile).
Film Listesi: 5 kült film (Inception, Interstellar, The Matrix, Pulp Fiction, La La Land) ile başlangıç.
Arama: Film adına veya türe göre hızlı arama.
Detay Ekranı: Film başlığı, yönetmen, tür, süre, açıklama ve kapak görseli.
YouTube Fragmanları: “İzle” butonuyla filmin fragmanına direkt geçiş.
Neon Arayüz: Morumsu (#12032b), mavi (#007bff), yeşil (#28a745), kırmızı (#dc3545) tonlarla modern tasarım.
Hata Yönetimi: Loglama (film_app.log) ve kullanıcı dostu hata mesajları.
Emoji Desteği: 🎬🔍 ile samimi ve eğlenceli vibe.

📸 Ekran Görüntüleri



Giriş Ekranı
Ana Ekran
Film Detay Ekranı








Görsel Ekleme Talimatları:

Ekran görüntülerini screenshots/ klasörüne yükleyin (ör. login_screen.png, main_screen.png, detail_screen.png).
Yukarıdaki Markdown bağlantılarında dosya adlarını kendi görsellerinizle eşleştirin.
Logo için screenshots/filmapp_logo.png’yi ekleyin veya bağlantıyı kaldırın.

🚀 Kurulum
FilmApp’i çalıştırmak için aşağıdaki adımları izleyin:
Gereksinimler

Python 3.8 veya üstü
Tkinter (genellikle Python ile gelir)
İşletim sistemi: Windows, macOS veya Linux

Adımlar

Depoyu Klonlayın:
git clone https://github.com/kullanici/filmapp.git
cd filmapp


Kapak Görsellerini Ekleyin (Opsiyonel):

inception.png, interstellar.png, matrix.png, pulp_fiction.png, lalaland.png dosyalarını proje kök dizinine ekleyin.
Görseller yoksa uygulama çalışır, ancak “Kapak resmi bulunamadı” uyarısı gösterir.


Uygulamayı Çalıştırın:
python film_app.py


Sorun Giderme:

Tkinter yüklü değilse: pip install tk
Hata alırsanız, film_app.log dosyasını kontrol edin.



🎮 Kullanım

Giriş veya Kayıt:

Giriş Yap: Kullanıcı adı ve şifrenizi girin (ör. kullanicilar.txt’ten).
Kayıt Ol: Yeni bir kullanıcı adı ve şifre oluşturun, bilgiler kullanicilar.txt’e kaydedilir.
Hata alırsanız, “Kullanıcı adı veya şifre hatalı” gibi mesajlar görürsünüz.


Ana Ekran:

Üstteki arama çubuğuna film adı veya tür yazın (ör. “Inception” veya “Bilim Kurgu”).
Film listesinde istediğiniz filme tıklayın.


Film Detayı:

Film başlığı, yönetmen, tür, süre ve açıklamayı görün.
Kapak görseli (varsa) yüklenir, yoksa uyarı gösterilir.
“İzle” butonuna tıklayarak YouTube fragmanına gidin.
“Geri” ile ana ekrana dönün.


Çıkış:

“Çıkış Yap” butonuyla giriş ekranına dönün.



Örnek Kullanım

Kayıt ol: Kullanıcı adı “filmsever”, şifre “12345”.
Giriş yap, arama çubuğuna “Matrix” yaz.
“The Matrix” filmine tıkla, detayları gör.
“İzle”ye bas, fragmanı YouTube’da izle.
Geri dön, “Çıkış Yap” ile çık.


📬 İletişim
Soruların mı var, kanka? Bize ulaş:

E-posta: rojatkirtay21@gmail.com
GitHub: github.com/rojatkrty

Hadi, popcorn’u kap ve film keyfine başla! 🍿
