import pandas as pd

# Pandas ayarlarını değiştir
pd.options.display.float_format = '{:,.2f}'.format

# Dosya yolunu belirle
file_path = 'C:/Users/salim/Desktop/Projeler/BüyükVeriProjesi/x.csv'

# CSV dosyasını oku, hatalı satırları atlayarak
data = pd.read_csv(file_path, on_bad_lines='skip')

# Toplam turnuva sayısı 0 olan tüm verileri sil
filtered_data = data[data['TotalTournaments'] > 0]

# PercentOffline ve OfflineEarnings sütunlarını sil (Kullanmıyoruz)
filtered_data = filtered_data.drop(columns=['PercentOffline', 'OfflineEarnings'])

# Null değer içeren verileri tespit et ve sil
filtered_data = filtered_data.dropna()

# Filtrelenmiş veriyi aynı dosyaya yaz
filtered_data.to_csv(file_path, index=False)

# Sonuçları göster
print(filtered_data.head())
print(filtered_data.shape)




