# update stok tbl_barang berdasar 
#tbl_detail_pengadan 
UPDATE tbl_barang 
SET stok = stok +(
SELECT IFNULL(SUM(jumlah),0)
FROM tbl_detail_pengadaan WHERE
tbl_detail_pengadaan.kode_barang =
tbl_barang.kode_barang)
