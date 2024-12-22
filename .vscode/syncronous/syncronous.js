function prosesData() {
    for(let i = 0; i < 5; i++) {
        console.log("Memproses item", i);
        // simulasi proses yang memakan waktu
        const result = i * i;
        console.log("Hasil:", result);
    }
}

console.log("Mulai proses");
prosesData();
console.log("Proses selesai");