meme_dict = {
}
"char" : "karakter",
"skin" : "kaplama",
"skill":"yetenek",
"gg": "iyi oyun",
"drop": "almak",
"nt": "iyi deneme"
} 

kelimemiz = input("öğrenmek istediğiniz kelimeyi yazın")

if kelimemiz in mene_dict.keys():
   print(meme_dict[kelimemiz])
else:
    print("Böyle bir kelime yok")
