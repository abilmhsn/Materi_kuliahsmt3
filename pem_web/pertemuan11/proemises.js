function fetchData(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = "";
            resolve(data);
            if (data){
                resolve(data);
            }else{
            reject("data tidak ada");
            }
        }, 1000);
    };
}
// memanggil Promise
fetchData()
   .then((data) => {
    console.log(data);
   })
   .catch((error) => {
    console.error(`Error; Unable to fetch data: ${error}`);
   });