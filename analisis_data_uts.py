import pandas as pd

# Membuat DataFrame dari dataset
data = {
    "Tanggal": [
        "1/10/2025", "2/10/2025", "3/10/2025", "4/10/2025", "5/10/2025",
        "6/10/2025", "7/10/2025", "8/10/2025", "9/10/2025", "11/10/2025",
        "12/10/2025", "20/10/2025", "21/10/2025", "22/10/2025", "23/10/2025",
        "24/10/2025", "25/10/2025", "26/10/2025", "27/10/2025", "28/10/2025",
        "31/10/2025"
    ],
    "Produk": [
        "Kebab Maknyus", "Mozarella Sosis", "Burger Mini", "Nutrijel Dark Cocho", "Susu Full Cream",
        "Puding Lumer", "Jus Alpukat", "Teh Leci", "Hot Dog", "Sosis Mozarella",
        "Bakpau", "Puding Coklat", "Kebab Maknyus", "Mozarella Sosis", "Burger Mini",
        "Teh Tarik", "Puding Lumer", "Jelly Shake", "Teh Leci", "Jus Alpukat",
        "Puding Coklat"
    ],
    "Kategori": [
        "Makanan", "Makanan", "Makanan", "Minuman", "Minuman",
        "Makanan", "Minuman", "Minuman", "Makanan", "Makanan",
        "Makanan", "Makanan", "Makanan", "Makanan", "Makanan",
        "Minuman", "Makanan", "Minuman", "Minuman", "Minuman",
        "Makanan"
    ],
    "Wilayah": [
        "Lenteng", "Bluto", "Sumenep", "Guluk-guluk", "Lenteng",
        "Bluto", "Sumenep", "Guluk-guluk", "Lenteng", "Bluto",
        "Sumenep", "Guluk-guluk", "Lenteng", "Bluto", "Sumenep",
        "Guluk-guluk", "Lenteng", "Bluto", "Sumenep", "Guluk-guluk",
        "Sumenep"
    ],
    "Jumlah Terjual": [
        25, 18, 22, 30, 27,
        19, 24, 28, 24, 30,
        27, 25, 28, 25, 30,
        32, 20, 35, 25, 22,
        27
    ],
    "Harga Satuan (Rp)": [
        13000, 10000, 12000, 8000, 9000,
        11000, 7000, 6000, 8000, 10000,
        8000, 10000, 13000, 10000, 12000,
        9000, 11000, 8000, 6000, 7000,
        10000
    ],
    "Total Penjualan (Rp)": [
        325000, 180000, 264000, 240000, 243000,
        209000, 168000, 168000, 192000, 300000,
        216000, 250000, 364000, 250000, 360000,
        288000, 220000, 280000, 150000, 154000,
        270000
    ],
    "Keuntungan (Rp)": [
        65000, 36000, 52800, 48000, 48600,
        41800, 33600, 33600, 38400, 60000,
        43200, 50000, 72800, 50000, 72000,
        57600, 44000, 56000, 30000, 30800,
        54000
    ]
}

df = pd.DataFrame(data)

# Tampilkan data awal
print("=== DATASET PENJUALAN OKTOBER 2025 ===")
print(df)

# Ringkasan statistik
print("\n=== RINGKASAN DATA ===")
print(df.describe())

# Total penjualan keseluruhan
total_penjualan = df["Total Penjualan (Rp)"].sum()
total_keuntungan = df["Keuntungan (Rp)"].sum()
print(f"\nTotal Penjualan Keseluruhan : Rp{total_penjualan:,}")
print(f"Total Keuntungan Keseluruhan : Rp{total_keuntungan:,}")

# Analisis per kategori
print("\n=== PENJUALAN BERDASARKAN KATEGORI ===")
kategori = df.groupby("Kategori")[["Total Penjualan (Rp)", "Keuntungan (Rp)"]].sum()
print(kategori)

# Analisis per wilayah
print("\n=== PENJUALAN BERDASARKAN WILAYAH ===")
wilayah = df.groupby("Wilayah")[["Total Penjualan (Rp)", "Keuntungan (Rp)"]].sum()
print(wilayah)

# Produk dengan penjualan tertinggi
produk_tertinggi = df.loc[df["Total Penjualan (Rp)"].idxmax()]
print("\n=== PRODUK DENGAN PENJUALAN TERTINGGI ===")
print(produk_tertinggi)
