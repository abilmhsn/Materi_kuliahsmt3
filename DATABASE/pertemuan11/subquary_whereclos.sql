#menampilkan stok baranag yang jumlahnya
#sudah di bawah rata rata
SELECT nama_barang, stok FROM tbl_barang 
WHERE stok <
(SELECT AVG(stok) FROM tbl_barang)