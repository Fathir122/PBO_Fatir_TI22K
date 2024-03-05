from db import DBConnection as mydb


class Warnet:

    """Kelas untuk mengelola data penggunaan internet di warnet."""

    def __init__(self):
        """Menginisialisasi objek Warnet."""
        self.__id = None
        self.__id_komputer = None
        self.__nama = None
        self.__tanggal = None
        self.__waktu = None
        self.__status_pembayaran = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        """Mengembalikan ID penggunaan internet."""
        return self.__id

    @property
    def id_komputer(self):
        """Mengembalikan ID komputer yang digunakan."""
        return self.__id_komputer

    @id_komputer.setter
    def id_komputer(self, value):
        """Menentukan ID komputer yang digunakan."""
        self.__id_komputer = value

    @property
    def nama(self):
        """Mengembalikan nama pelanggan."""
        return self.__nama

    @nama.setter
    def nama(self, value):
        """Menentukan nama pelanggan."""
        self.__nama = value

    @property
    def tanggal(self):
        """Mengembalikan tanggal penggunaan internet."""
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, value):
        """Menentukan tanggal penggunaan internet."""
        self.__tanggal = value

    @property
    def waktu(self):
        """Mengembalikan waktu penggunaan internet."""
        return self.__waktu

    @waktu.setter
    def waktu(self, value):
        """Menentukan waktu penggunaan internet."""
        self.__waktu = value

    @property
    def status_pembayaran(self):
        """Mengembalikan status pembayaran internet."""
        return self.__status_pembayaran

    @status_pembayaran.setter
    def status_pembayaran(self, value):
        """Menentukan status pembayaran internet."""
        self.__status_pembayaran = value

    def simpan(self, id_komputer, nama, tanggal, waktu, status_pembayaran):
        self.conn = mydb()
        try:
        # Validasi data
            if not isinstance(id_komputer, int):
                raise ValueError("id_komputer harus bertipe integer")
            if not nama or not isinstance(nama, str):
                raise ValueError("nama harus string yang tidak kosong")
            if not tanggal or not isinstance(tanggal, str):
                raise ValueError("tanggal harus string yang tidak kosong")
            if not waktu or not isinstance(waktu, str):
                raise ValueError("waktu harus string yang tidak kosong")
            if not status_pembayaran or not isinstance(status_pembayaran, str):
                raise ValueError("status_pembayaran harus string yang tidak kosong")

        # Menyiapkan data
            val = (id_komputer, nama, tanggal, waktu, status_pembayaran)
            sql = "INSERT INTO warnet (id_komputer, nama, tanggal, waktu, status_pembayaran) VALUES (%s, %s, %s, %s, %s)"

        # Menjalankan query
            self.affected = self.conn.insert(sql, val)

        # Mengambil ID yang baru saja dimasukkan
            self.__id = self.conn.lastrowid

        except Exception as e:
            print(f"Terjadi kesalahan saat menyimpan data: {e}")
        finally:
            self.conn.disconnect()
        return self.__id
    
    def update(self, id):
        self.conn = mydb()
        try:
        # Validasi data
            if not isinstance(id, int):
                raise ValueError("id harus bertipe integer")

        # Menyiapkan data
            val = (self.__nama, self.__tanggal, self.__waktu, self.__status_pembayaran, id)
            sql = "UPDATE warnet SET nama = %s, tanggal = %s, waktu = %s, status_pembayaran = %s WHERE id = %s"

        # Menjalankan query
            self.affected = self.conn.update(sql, val)

        except Exception as e:
            print(f"Terjadi kesalahan saat memperbarui data: {e}")
        finally:
            self.conn.disconnect()
        return self.affected


    def delete(self, id):
        """
        Menghapus data penggunaan internet di database berdasarkan ID.

        Args:
            id (int): ID penggunaan internet yang ingin dihapus.

        Returns:
            int: Jumlah baris yang terpengaruh (1 jika berhasil).
        """
        self.conn = mydb()
        try:
            # Validasi data
            if not isinstance(id, int):
                raise ValueError("id harus bertipe integer")

            # Menyiapkan data
            sql = "DELETE FROM warnet WHERE id = %s"

            # Menjalankan query
            self.affected = self.conn.delete(sql, str(id))

        except Exception as e:
            print(f"Terjadi kesalahan saat menghapus data: {e}")
        finally:
            self.conn.disconnect()
        return self.affected
    
    def get_all_data(self):
        """
        Mengambil semua data penggunaan internet dari database.

        Returns:
            list: Daftar dictionary berisi data penggunaan internet.
        """
        self.conn = mydb()
        try:
            # Menyiapkan data
            sql = "SELECT * FROM warnet"

            # Menjalankan query
            self.result = self.conn.findAll(sql)

            # Mengubah hasil menjadi list dictionary
            data = []
            for row in self.result:
                data.append({
                    "id": row[0],
                    "id_komputer": row[1],
                    "nama": row[2],
                    "tanggal": row[3],
                    "waktu": row[4],
                    "status_pembayaran": row[5],
                })

        except Exception as e:
            print(f"Terjadi kesalahan saat mengambil data: {e}")
        finally:
            self.conn.disconnect()
        return data
    
    def get_by_nama(self, nama):
        """
        Mengambil data penggunaan internet di database berdasarkan nama.

        Args:
            nama (str): Nama pelanggan yang ingin dicari.

        Returns:
            list: Daftar dictionary berisi data penggunaan internet.
        """
        self.conn = mydb()
        try:
            # Validasi data
            if not nama or not isinstance(nama, str):
                raise ValueError("nama harus string yang tidak kosong")

            # Menyiapkan data
            sql = "SELECT * FROM warnet WHERE nama LIKE %s"
            val = ("%" + nama + "%",)

            # Menjalankan query
            self.result = self.conn.findAll(sql, val)

            # Mengubah hasil menjadi list dictionary
            data = []
            for row in self.result:
                data.append({
                    "id": row[0],
                    "id_komputer": row[1],
                    "nama": row[2],
                    "tanggal": row[3],
                    "waktu": row[4],
                    "status_pembayaran": row[5],
                })

        except Exception as e:
            print(f"Terjadi kesalahan saat mengambil data: {e}")
        finally:
            self.conn.disconnect()
        return data


    def get_by_id(self, id):
        """
        Mengambil data penggunaan internet di database berdasarkan ID.

        Args:
            id (int): ID penggunaan internet yang ingin dicari.

        Returns:
            dict: Data penggunaan internet dengan ID yang diberikan.
        """
        self.conn = mydb()
        try:
            # Validasi data
            if not isinstance(id, int):
                raise ValueError("id harus bertipe integer")

            # Menyiapkan data
            sql = "SELECT * FROM warnet WHERE id = %s"

            # Menjalankan query
            self.result = self.conn.findOne(sql, str(id))

            # Mengubah hasil menjadi dictionary
            if self.result is not None:
                data = {
                    "id": self.result[0],
                    "id_komputer": self.result[1],
                    "nama": self.result[2],
                    "tanggal": self.result[3],
                    "waktu": self.result[4],
                    "status_pembayaran": self.result[5],
                }
            else:
                data = None

        except Exception as e:
            print(f"Terjadi kesalahan saat mengambil data: {e}")
        finally:
            self.conn.disconnect()
        return data
    
    def update_by_nama(self, nama, id_komputer, tanggal, waktu, status_pembayaran):
        """
        Memperbarui data penggunaan internet di database berdasarkan nama.

        Args:
            nama (str): Nama pelanggan yang ingin diubah.
            id_komputer (int): ID komputer yang digunakan.
            tanggal (str): Tanggal penggunaan internet.
            waktu (str): Waktu penggunaan internet.
            status_pembayaran (str): Status pembayaran internet.

        Returns:
            int: Jumlah baris yang terpengaruh (1 jika berhasil).
        """
        self.conn = mydb()
        try:
            # Validasi data
            if not nama or not isinstance(nama, str):
                raise ValueError("nama harus string yang tidak kosong")

            # Menyiapkan data
            val = (id_komputer, tanggal, waktu, status_pembayaran, nama)
            sql = "UPDATE warnet SET id_komputer = %s, tanggal = %s, waktu = %s, status_pembayaran = %s WHERE nama = %s"

            # Menjalankan query
            self.affected = self.conn.update(sql, val)

        except Exception as e:
            print(f"Terjadi kesalahan saat memperbarui data: {e}")
        finally:
            self.conn.disconnect()
        return self.affected
    
    def delete_by_nama(self, nama):
        """
        Menghapus data penggunaan internet di database berdasarkan nama.

        Args:
            nama (str): Nama pelanggan yang ingin dihapus.

        Returns:
            int: Jumlah baris yang terpengaruh (1 jika berhasil).
        """
        self.conn = mydb()
        try:
            # Validasi data
            if not nama or not isinstance(nama, str):
                raise ValueError("nama harus string yang tidak kosong")

            # Menyiapkan data
            sql = "DELETE FROM warnet WHERE nama = %s"

            # Menjalankan query
            self.affected = self.conn.delete(sql, nama)

        except Exception as e:
            print(f"Terjadi kesalahan saat menghapus data: {e}")
        finally:
            self.conn.disconnect()
        return self.affected



