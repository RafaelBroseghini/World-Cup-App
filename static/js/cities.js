let year = document.querySelector("#year").textContent;
let cities = document.querySelector(".hosts");
let stat = document.querySelector(".cities");
let clicker = document.querySelector(".clicker");

function get_cities(){
    fetch("/get_cities?y=" + year)
    .then(function(response){
        return response.json();
    }).then(function(data){
        create_items(data)
    })
}

function create_items(data){
    clicker.style.display = "none";
    for (const c in data) {
        let city = document.createElement("div");
        city.className = "item";
        let cont = document.createElement("div");
        cont.className = "content";
        let header = document.createElement("div");
        header.className = "header text-center";
        let atag = document.createElement("a");
        atag.textContent= data[c];
        atag.href = "https://en.wikipedia.org/wiki/"+data[c];
        atag.className = "ui fluid black button";
        atag.target = "_blank";
        header.appendChild(atag);
        cont.appendChild(header);
        city.appendChild(cont);
        cities.appendChild(city);
        
    }
    let label = document.createElement("div");
    label.className = "label";
    label.textContent = year + " World Cup Host Cities";
    console.log(label);
    stat.appendChild(label);
    console.log(stat);
    
}
