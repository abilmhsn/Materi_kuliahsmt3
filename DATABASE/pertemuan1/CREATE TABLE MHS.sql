/*membuat tabel matakuliah*/
CREATE TABLE mahasiswa(
id_mahasiswa INT PRIMARY KEY auto_increment,
nama VARCHAR(100),performance_schemasys
nim VARCHAR(15) UNIQUE,
jurusan VARCHAR(50),
ankatan YEAR )