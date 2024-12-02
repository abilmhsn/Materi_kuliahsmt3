function proses1(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Hello")
        }, 1000);
    });
}
function proses2(greetings) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(`${greetings} Word`);
        }, 1000);
    });
}
function proses3(pesan) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(`${pesan} have a great day`);
        }, 1000);
    });
}
//memanggil cheaning proses
proses1()
 .then((greetings) => {
    return proses3(pesan);
 })
 .then((pesan) =>{
    return proses3(pesan)
 })
 .then((result)=> {
console.log(result);
})
catch((error) => {
    console.error(`Error; ${error}`);
});