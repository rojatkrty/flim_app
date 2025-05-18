import tkinter as tk
from tkinter import messagebox
import webbrowser
import os
import logging

# Set up logging for debugging
logging.basicConfig(filename='film_app.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Film data with PNG cover images
FILMLER = [
    {
        "baslik": "Inception",
        "yonetmen": "Christopher Nolan",
        "tur": "Bilim Kurgu",
        "sure": 148,
        "aciklama": "Dom Cobb, rüyalarda bilinçaltına girip sırlar çalan bir hırsızdır. "
                    "Son görevinde bir fikri zihne yerleştirmesi gerekir, ancak bu görev "
                    "gerçeklik ve rüya arasındaki sınırları zorlar.",
        "kapak_dosya": "inception.png",
        "youtube_link": "https://www.youtube.com/watch?v=YoHD9XEInc0"
    },
    {
        "baslik": "Interstellar",
        "yonetmen": "Christopher Nolan",
        "tur": "Bilim Kurgu",
        "sure": 169,
        "aciklama": "Dünya'nın sonu yaklaşırken, bir grup kaşif insanlık için yeni bir "
                    "ev aramak üzere solucan deliğinden geçer. Zaman ve sevgi, evrenin sınırlarını aşar.",
        "kapak_dosya": "interstellar.png",
        "youtube_link": "https://www.youtube.com/watch?v=zSWdZVtXT7E"
    },
    {
        "baslik": "The Matrix",
        "yonetmen": "Lana Wachowski, Lilly Wachowski",
        "tur": "Bilim Kurgu",
        "sure": 136,
        "aciklama": "Neo, gerçekliğin bir simülasyon olduğunu öğrenir ve insanlığı özgürleştirmek "
                    "için Matrix'e karşı savaşır. Gerçeklik, sanal dünya ile çarpışır.",
        "kapak_dosya": "matrix.png",
        "youtube_link": "https://www.youtube.com/watch?v=m8e-FF8MsWU"
    },
    {
        "baslik": "Pulp Fiction",
        "yonetmen": "Quentin Tarantino",
        "tur": "Suç",
        "sure": 154,
        "aciklama": "Kesişen hikayeler, suç dünyasının kaotik ve mizahi yüzünü ortaya koyar. "
                    "Kült diyaloglar ve unutulmaz karakterlerle dolu bir macera.",
        "kapak_dosya": "pulp_fiction.png",
        "youtube_link": "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
    },
    {
        "baslik": "La La Land",
        "yonetmen": "Damien Chazelle",
        "tur": "Romantik",
        "sure": 128,
        "aciklama": "Bir müzisyen ve aktris, Los Angeles'ta hayallerini ve aşklarını yaşamaya çalışır. "
                    "Müzik ve tutkuyla dolu bir romantik yolculuk.",
        "kapak_dosya": "lalaland.png",
        "youtube_link": "https://www.youtube.com/watch?v=0pdqf4P9MB8"
    }
]

KULLANICI_DOSYA = "kullanicilar.txt"


class FilmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 Film ve Dizi Servisi")
        self.root.geometry("1000x900")
        self.root.configure(bg="#f0f2f5")
        self.filmler = FILMLER
        self.search_entry = None
        try:
            self.giris_ekrani()
        except Exception as e:
            logging.error(f"Init error: {str(e)}")
            messagebox.showerror("Hata", "Uygulama başlatılamadı. Lütfen log dosyasını kontrol edin.")
            self.root.quit()

    def temizle(self):
        try:
            for widget in self.root.winfo_children():
                widget.destroy()
        except Exception as e:
            logging.error(f"Temizle error: {str(e)}")

    def giris_ekrani(self):
        self.temizle()
        frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="flat")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400)

        tk.Label(frame, text="🎥 Film Servisi", font=("Helvetica", 28, "bold"), fg="#333", bg="#ffffff").pack(pady=30)

        tk.Label(frame, text="Kullanıcı Adı", font=("Helvetica", 12), bg="#ffffff").pack()
        self.giris_kadi = tk.Entry(frame, font=("Helvetica", 12), width=30, bd=1, relief="solid")
        self.giris_kadi.pack(pady=10, padx=20)

        tk.Label(frame, text="Şifre", font=("Helvetica", 12), bg="#ffffff").pack()
        self.giris_sifre = tk.Entry(frame, show="*", font=("Helvetica", 12), width=30, bd=1, relief="solid")
        self.giris_sifre.pack(pady=10, padx=20)

        tk.Button(frame, text="Giriş Yap", font=("Helvetica", 12, "bold"), bg="#007bff", fg="white",
                  command=self.giris_yap, relief="flat", width=20).pack(pady=15)

        tk.Button(frame, text="Kayıt Ol", font=("Helvetica", 12, "bold"), bg="#6c757d", fg="white",
                  command=self.kayit_ekrani, relief="flat", width=20).pack(pady=10)

    def kayit_ekrani(self):
        self.temizle()
        frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="flat")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400)

        tk.Label(frame, text="📝 Kayıt Ol", font=("Helvetica", 28, "bold"), fg="#333", bg="#ffffff").pack(pady=30)

        tk.Label(frame, text="Kullanıcı Adı", font=("Helvetica", 12), bg="#ffffff").pack()
        self.kayit_kadi = tk.Entry(frame, font=("Helvetica", 12), width=30, bd=1, relief="solid")
        self.kayit_kadi.pack(pady=10, padx=20)

        tk.Label(frame, text="Şifre", font=("Helvetica", 12), bg="#ffffff").pack()
        self.kayit_sifre = tk.Entry(frame, show="*", font=("Helvetica", 12), width=30, bd=1, relief="solid")
        self.kayit_sifre.pack(pady=10, padx=20)

        tk.Button(frame, text="Kayıt Ol", font=("Helvetica", 12, "bold"), bg="#28a745", fg="white",
                  command=self.kayit_ol, relief="flat", width=20).pack(pady=15)

        tk.Button(frame, text="← Geri", font=("Helvetica", 12, "bold"), bg="#6c757d", fg="white",
                  command=self.giris_ekrani, relief="flat", width=20).pack(pady=10)

    def kayit_ol(self):
        try:
            kullanici = self.kayit_kadi.get().strip()
            sifre = self.kayit_sifre.get().strip()
            if not kullanici or not sifre:
                messagebox.showwarning("Hata", "Lütfen tüm alanları doldurun.")
                return
            if os.path.exists(KULLANICI_DOSYA):
                with open(KULLANICI_DOSYA, "r") as f:
                    for satir in f:
                        kadi, _ = satir.strip().split(",")
                        if kadi == kullanici:
                            messagebox.showwarning("Hata", "Bu kullanıcı adı zaten alınmış.")
                            return
            with open(KULLANICI_DOSYA, "a") as f:
                f.write(f"{kullanici},{sifre}\n")
            messagebox.showinfo("Başarılı", "Kayıt başarılı! Giriş yapabilirsiniz.")
            self.giris_ekrani()
        except Exception as e:
            logging.error(f"Kayıt ol error: {str(e)}")
            messagebox.showerror("Hata", "Kayıt sırasında bir hata oluştu.")

    def giris_yap(self):
        try:
            kullanici = self.giris_kadi.get().strip()
            sifre = self.giris_sifre.get().strip()
            if os.path.exists(KULLANICI_DOSYA):
                with open(KULLANICI_DOSYA, "r") as f:
                    for satir in f:
                        kadi, ksifre = satir.strip().split(",")
                        if kadi == kullanici and ksifre == sifre:
                            self.ana_ekran()
                            return
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı.")
        except Exception as e:
            logging.error(f"Giriş yap error: {str(e)}")
            messagebox.showerror("Hata", "Giriş sırasında bir hata oluştu.")

    def ana_ekran(self):
        self.temizle()
        self.filmler = FILMLER
        frame = tk.Frame(self.root, bg="#f0f2f5")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(frame, text="🎬 Film Seç", font=("Helvetica", 24, "bold"), fg="#333", bg="#f0f2f5").pack(pady=10)

        search_frame = tk.Frame(frame, bg="#ffffff", bd=1, relief="solid")
        search_frame.pack(fill="x", pady=10)
        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 12), width=50)
        self.search_entry.pack(side="left", padx=5, pady=5)
        tk.Button(search_frame, text="🔍 Ara", font=("Helvetica", 12), bg="#007bff", fg="white",
                  command=self.ara, relief="flat").pack(side="left", padx=5)

        self.film_frame = tk.Frame(frame, bg="#f0f2f5")
        self.film_frame.pack(fill="both", expand=True)
        self.yenile_filmler()

        tk.Button(frame, text="Çıkış Yap", font=("Helvetica", 12, "bold"), bg="#dc3545", fg="white",
                  command=self.giris_ekrani, relief="flat").pack(pady=10)

    def ara(self):
        try:
            arama = self.search_entry.get().lower()
            self.filmler = [film for film in FILMLER if arama in film["baslik"].lower() or arama in film["tur"].lower()]
            self.yenile_filmler()
        except Exception as e:
            logging.error(f"Ara error: {str(e)}")
            messagebox.showerror("Hata", "Arama sırasında bir hata oluştu.")

    def yenile_filmler(self):
        try:
            for widget in self.film_frame.winfo_children():
                widget.destroy()
            for film in self.filmler:
                btn = tk.Button(
                    self.film_frame, text=film["baslik"], font=("Helvetica", 14, "bold"), bg="#343a40",
                    fg="white", width=50, relief="flat", command=lambda f=film: self.film_detay(f)
                )
                btn.pack(pady=8, padx=20)
        except Exception as e:
            logging.error(f"Yenile filmler error: {str(e)}")
            messagebox.showerror("Hata", "Film listesi yüklenirken bir hata oluştu.")

    def film_detay(self, film):
        self.temizle()
        frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="flat")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=800)

        tk.Label(frame, text=film["baslik"], font=("Helvetica", 28, "bold"), fg="#333", bg="#ffffff").pack(pady=20)

        info = f"Yönetmen: {film['yonetmen']} | Tür: {film['tur']} | Süre: {film['sure']} dk"
        tk.Label(frame, text=info, font=("Helvetica", 12), fg="#555", bg="#ffffff").pack()

        # Cover image
        try:
            if os.path.exists(film["kapak_dosya"]):
                img = tk.PhotoImage(file=film["kapak_dosya"])
                img_label = tk.Label(frame, image=img, bg="#ffffff")
                img_label.image = img  # Keep reference to prevent garbage collection
                img_label.pack(pady=20)
            else:
                tk.Label(frame, text="⚠️ Kapak resmi bulunamadı.", fg="#dc3545", bg="#ffffff").pack(pady=20)
        except Exception as e:
            logging.error(f"Image load error for {film['kapak_dosya']}: {str(e)}")
            tk.Label(frame, text="⚠️ Kapak resmi yüklenemedi.", fg="#dc3545", bg="#ffffff").pack(pady=20)

        tk.Button(
            frame, text="🎬 İzle", font=("Helvetica", 14, "bold"), bg="#007bff", fg="white",
            width=20, height=2, relief="flat", command=lambda: webbrowser.open(film["youtube_link"])
        ).pack(pady=20)

        tk.Label(
            frame, text=f"Açıklama:\n{film['aciklama']}", wraplength=700, justify="center",
            font=("Helvetica", 12), fg="#333", bg="#ffffff"
        ).pack(pady=20)

        tk.Button(
            frame, text="← Geri", font=("Helvetica", 12, "bold"), bg="#6c757d", fg="white",
            command=self.ana_ekran, relief="flat", width=15
        ).pack(pady=10)


if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = FilmApp(root)
        root.mainloop()
    except Exception as e:
        logging.error(f"Main loop error: {str(e)}")
        print(f"Uygulama başlatılamadı. Hata: {str(e)}. Lütfen film_app.log dosyasını kontrol edin.")