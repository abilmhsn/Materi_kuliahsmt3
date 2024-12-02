function fetchData(callback){
    setTimeout(function(){
        const data = 'Fetcthed Data';
        callback(data);
    },5000)
}
fetchData(function(data){
    console.log(data);
});