# LiteLang

LiteLang, yapım aşamasında Türkçe sade bir sözdizimine sahip minimal ChatGPT ile üretilen, Phyton ile yazılan bir programlama dilidir. Eğlencelik, öğretici ve tamamen açık kaynak.

---

## 🖥️ Özellikler

- `show "merhaba"` gibi basit komutlarla çıktı alma  
- Toplama, çıkarma, çarpma, bölme işlemleri  
- String + sayı birleştirme desteği  
- `.lite` uzantılı dosya desteği
- Daha fazlası yok çünkü demo versiyonu

---

## 🔧 Kurulum

Releases Kısmında Demo'ya git Aşağı indir ve LiteLangDemo.zip dosyasını indir (tıkla) Sonra zip dosyasını klasöre çıkart LiteLangDemo.exe yi çalıştır.

---

## 📘 LiteLang Programlama Dili Tanıtımı

**LiteLang**, firelowq tarafından, öğrenmesi kolay ve sade yapılı bir dil olarak geliştirilmiştir. Pek gelişmiş değildir fakat şu anda yapım aşamasındadır.
Python’un yorumlayıcı mantığıyla çalışır ama kendi sözdizimini sunar.
Yani basitçe göster, gösterirken hesapla, hata varsa net bir şekilde söyle.

---

### 🧩 Temel Sözdizimi

LiteLang’de tek temel komut şudur:

```
show "bir şey"
```

Bu `print` gibidir. Ama Python’daki gibi parantez, virgül, modül derdi yok.

---

### 🧮 Matematik İşlemleri

Aritmetik direkt desteklenir. `show` komutu içinde yazarsın, sonucu basar:

```lite
show 3 + 4
show "Toplam: " + 2 + 5
show 10 / 2
```

* Toplama (`+`)
* Çıkarma (`-`)
* Çarpma (`*`)
* Bölme (`/`)
* Sayıyla yazı da toplanabilir: `"Sonuç: " + 3 + 2`

---

### ⚠️ Hatalar

Dilin mantığı dışına çıkarsan kırmızı hatayı alırsın:

```lite
show 5 + "elma"
```

🟥 Çıktı: `Hata: Toplama işlemi sayı ve yazı arasında geçersizdir.`

---

### 🎯 Amacımız nedir?

* Kodlama öğrenmeye başlarken bunalmamak
* Yeni başlamak için süper bir yol yapmak
* Türkçe destekli bir sistemle öğrenmek

---

`Bunu bile ChatGPT yazdı :D`
