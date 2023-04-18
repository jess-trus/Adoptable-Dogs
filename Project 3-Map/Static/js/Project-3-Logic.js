// Create a map object.
let myMap = L.map("map", {
    center: [40.057347,-74.414532],
    zoom: 8
});

// Add a tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

function markerSize(population) {
    return Math.sqrt(population) * 500;
}

let cities = [
    {
        name:"Lambertville",
        location: [40.3659,-74.9429],
        population:82
    },
    {
        name:"Ringwood",
        location: [41.1134,-74.2454],
        population:67  
    },
    {
        name:"Bridgeton",
        location: [39.4273,-75.2340],
        population:63
    },
    {
        name:"Oak Ridge",
        location: [41.047,-74.485],
        population:44
    },
    {
        name:"Berkely Heights",
        location: [40.6808,-74.4310],
        population:82
    },
    {
        name:"Brick",
        location: [40.0602,-74.1393],
        population:34
    },
    {
        name:"Bridgewater",
        location: [40.6206,-74.6006],
        population:31
    },
    {
        name:"Red Bank",
        location: [40.3474,-74.0670],
        population:27
    },
    {
        name:"Toms River",
        location: [39.9546,-74.1984],
        population:27
    },
    {
        name:"Warren",
        location: [40.8560,-74.9917],
        population:26
    }
];

for (let i = 0; i < cities.length; i++) {
    L.circle(cities[i].location, {
        fillOpacity: 0.75,
        color: "white",
        fillColor: "red",
        radius: markerSize(cities[i].population)
    }).bindPopup(`<h1>${cities[i].name}</h1> <hr> <h3>Adoptable Dogs: ${cities[i].population.toLocaleString()}</h3>`).addTo(myMap);
}
