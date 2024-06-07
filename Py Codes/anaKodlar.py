import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas ayarlarını değiştir
pd.options.display.float_format = '{:,.2f}'.format

# Dosya yolunu belirle
file_path = 'C:/Users/salim/Desktop/Projeler/BüyükVeriProjesi/x.csv'

# CSV dosyasını oku, hatalı satırları atlayarak
data = pd.read_csv(file_path, on_bad_lines='skip')


# Oyun türlerine göre toplam kazançları hesapla
total_earnings_by_genre = data.groupby('Genre')['TotalEarnings'].sum()

# Toplam kazançlara göre sıralama yap
total_earnings_by_genre = total_earnings_by_genre.sort_values(ascending=False)

# Grafik oluştur
plt.figure(figsize=(10, 6))
total_earnings_by_genre.plot(kind='bar', color='purple')
plt.title('Oyun Türlerine Göre Toplam Kazançlar')
plt.xlabel('Oyun Türü')
plt.ylabel('Toplam Kazanç')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


filtered_data2016 = data[data['ReleaseDate'] > 2016]
filtered_data2019 = data[data['ReleaseDate'] > 2019]


# Oyun türlerine göre toplam kazanç ve toplam oyuncu sayısını hesapla
total_earnings_players_by_genre = data.groupby('Genre').agg({'TotalEarnings': 'sum', 'TotalPlayers': 'sum'}).reset_index()

# Grafik oluştur
plt.figure(figsize=(12, 8))
sns.barplot(x='TotalPlayers', y='TotalEarnings', hue='Genre', data=total_earnings_players_by_genre, palette='viridis')
plt.title('Oyun Türlerine Göre Toplam Oyuncu Sayısı ve Toplam Kazanç')
plt.xlabel('Toplam Oyuncu Sayısı')
plt.ylabel('Toplam Kazanç')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Oyun Türü', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


total_earnings_players_by_genre = filtered_data2016.groupby('Genre').agg({'TotalEarnings': 'sum', 'TotalPlayers': 'sum'}).reset_index()

# Grafik oluştur
plt.figure(figsize=(12, 8))
sns.barplot(x='TotalPlayers', y='TotalEarnings', hue='Genre', data=total_earnings_players_by_genre, palette='viridis')
plt.title('Oyun Türlerine Göre Toplam Oyuncu Sayısı ve Toplam Kazanç 2017-2023')
plt.xlabel('Toplam Oyuncu Sayısı')
plt.ylabel('Toplam Kazanç')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Oyun Türü', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


total_earnings_players_by_genre = filtered_data2019.groupby('Genre').agg({'TotalEarnings': 'sum', 'TotalPlayers': 'sum'}).reset_index()

# Grafik oluştur
plt.figure(figsize=(12, 8))
sns.barplot(x='TotalPlayers', y='TotalEarnings', hue='Genre', data=total_earnings_players_by_genre, palette='viridis')
plt.title('Oyun Türlerine Göre Toplam Oyuncu Sayısı ve Toplam Kazanç 2020-2023')
plt.xlabel('Toplam Oyuncu Sayısı')
plt.ylabel('Toplam Kazanç')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Oyun Türü', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



filtered_data2016 = data[data['ReleaseDate'] > 2016]
filtered_data2019 = data[data['ReleaseDate'] > 2019]

# Oyun türlerine göre toplam kazanç ve toplam turnuva sayısını hesapla
total_earnings_tournaments_by_genre = data.groupby('Genre').agg({'TotalEarnings': 'sum', 'TotalTournaments': 'sum'}).reset_index()

# Grafik oluştur
plt.figure(figsize=(12, 8))
sns.set_palette('bright')  # Her kategori için net farklı renkler kullan
sns.barplot(x='TotalTournaments', y='TotalEarnings', hue='Genre', data=total_earnings_tournaments_by_genre)
plt.title('Oyun Türlerine Göre Toplam Turnuva Sayısı ve Toplam Kazanç')
plt.xlabel('Toplam Turnuva Sayısı')
plt.ylabel('Toplam Kazanç')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Oyun Türü', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# Oyun türlerine göre toplam kazanç, toplam oyuncu sayısı ve toplam turnuva sayısını hesapla
# Oyun türlerine göre toplam kazanç ve toplam turnuva sayısını hesapla
total_earnings_tournaments_by_genre = filtered_data2016.groupby('Genre').agg({'TotalEarnings': 'sum', 'TotalTournaments': 'sum'}).reset_index()

# Grafik oluştur
plt.figure(figsize=(12, 8))
sns.set_palette('bright')  # Her kategori için net farklı renkler kullan
sns.barplot(x='TotalTournaments', y='TotalEarnings', hue='Genre', data=total_earnings_tournaments_by_genre)
plt.title('Oyun Türlerine Göre Toplam Turnuva Sayısı ve Toplam Kazanç 2017-2023')
plt.xlabel('Toplam Turnuva Sayısı')
plt.ylabel('Toplam Kazanç')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Oyun Türü', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

total_earnings_tournaments_by_genre = filtered_data2019.groupby('Genre').agg({'TotalEarnings': 'sum', 'TotalTournaments': 'sum'}).reset_index()

# Grafik oluştur
plt.figure(figsize=(12, 8))
sns.set_palette('bright')  # Her kategori için net farklı renkler kullan
sns.barplot(x='TotalTournaments', y='TotalEarnings', hue='Genre', data=total_earnings_tournaments_by_genre)
plt.title('Oyun Türlerine Göre Toplam Turnuva Sayısı ve Toplam Kazanç 2020-2023')
plt.xlabel('Toplam Turnuva Sayısı')
plt.ylabel('Toplam Kazanç')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Oyun Türü', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Oyun türlerine göre ortalama kazanç ve ortalama oyuncu sayısını hesapla
average_earnings_players_by_genre = data.groupby('Genre').agg({'TotalEarnings': 'mean', 'TotalPlayers': 'mean'}).reset_index()

# Grafik oluştur
plt.figure(figsize=(12, 8))

# Ortalama Kazanç Grafik
plt.subplot(2, 1, 1)
sns.barplot(x='Genre', y='TotalEarnings', data=average_earnings_players_by_genre, palette='viridis')
plt.title('Oyun Türlerine Göre Ortalama Kazanç')
plt.xlabel('Oyun Türü')
plt.ylabel('Ortalama Kazanç')
plt.xticks(rotation=45)

# Ortalama Oyuncu Sayısı Grafik
plt.subplot(2, 1, 2)
sns.barplot(x='Genre', y='TotalPlayers', data=average_earnings_players_by_genre, palette='viridis')
plt.title('Oyun Türlerine Göre Ortalama Oyuncu Sayısı')
plt.xlabel('Oyun Türü')
plt.ylabel('Ortalama Oyuncu Sayısı')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


player_counts = data.groupby(['ReleaseDate', 'Genre'])['TotalPlayers'].sum().reset_index()
player_counts_pivot = player_counts.pivot(index='ReleaseDate', columns='Genre', values='TotalPlayers')

# Grafiği çizelim
plt.figure(figsize=(12, 8))
player_counts_pivot.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12,8))
plt.title('Yıllara ve Oyun Türlerine Göre Toplam Oyuncu Sayısı')
plt.xlabel('Yıl')
plt.ylabel('Toplam Oyuncu Sayısı')
plt.xticks(rotation=45)
plt.legend(title='Oyun Türü', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# Oyun türlerine göre toplam kazançları hesapla
total_earnings_by_genre = data.groupby('Genre')['TotalEarnings'].sum().reset_index()

# Seaborn 'bright' paletini kullanarak renkleri ayarla
sns.set_palette('bright')
colors = sns.color_palette('bright', len(total_earnings_by_genre))

# Pasta grafik oluştur
plt.figure(figsize=(10, 8))
patches, texts, autotexts = plt.pie(total_earnings_by_genre['TotalEarnings'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Oyun Türlerine Göre Toplam Kazançlar')

# Legend ekle
plt.legend(patches, total_earnings_by_genre['Genre'], title="Oyun Türü", loc="center left", bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()
