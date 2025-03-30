class JadwalKonsultasi:
    def __init__(self):
        self.jadwal = []

    def tambah_jadwal(self, tanggal, waktu, nama_pasien):
        self.jadwal.append({
            'tanggal': tanggal,
            'waktu': waktu,
            'nama_pasien': nama_pasien
        })
        print(f"Jadwal konsultasi untuk {nama_pasien} pada {tanggal} pukul {waktu} telah ditambahkan.")

    def lihat_jadwal(self):
        if not self.jadwal:
            print("Tidak ada jadwal konsultasi.")
            return
        print("Jadwal Konsultasi:")
        for index, item in enumerate(self.jadwal):
            print(f"{index + 1}. Tanggal: {item['tanggal']}, Waktu: {item['waktu']}, Nama Pasien: {item['nama_pasien']}")

    def hapus_jadwal(self, index):
        if 0 <= index < len(self.jadwal):
            removed = self.jadwal.pop(index)
            print(f"Jadwal konsultasi untuk {removed['nama_pasien']} pada {removed['tanggal']} pukul {removed['waktu']} telah dihapus.")
        else:
            print("Index tidak valid.")

def main():
    jadwal_konsultasi = JadwalKonsultasi()

    while True:
        print("\nMenu:")
        print("1. Tambah Jadwal")
        print("2. Lihat Jadwal")
        print("3. Hapus Jadwal")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
            waktu = input("Masukkan waktu (HH:MM): ")
            nama_pasien = input("Masukkan nama pasien: ")
            jadwal_konsultasi.tambah_jadwal(tanggal, waktu, nama_pasien)
        elif pilihan == '2':
            jadwal_konsultasi.lihat_jadwal()
        elif pilihan == '3':
            jadwal_konsultasi.lihat_jadwal()
            index = int(input("Masukkan nomor jadwal yang ingin dihapus: ")) - 1
            jadwal_konsultasi.hapus_jadwal(index)
        elif pilihan == '4':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()