import goslate


inserted_text = "Python progamming language is very good"
new_gs = goslate.Goslate()
print(new_gs.translate(inserted_text, 'de'))