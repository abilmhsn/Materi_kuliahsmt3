#menghapus transaksi penjualan jika 
#jumlah > dari stok di tbl trasaksi
DELETE FROM tbl_detailtransaksi 
WHERE qty >(
SELECT stok  FROM tbl_barang )