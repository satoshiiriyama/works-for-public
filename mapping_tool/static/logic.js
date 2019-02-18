// JSON URL
var bbySellthruUrl = ***Confidential;
var faultUrl = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";


// Colors
function colorCategory(performance) {
  if (performance >= 150) {
    return '#00FF00'
  } else if (performance >= 125) {
    return '#4169E1'
  } else if (performance >= 100) {
    return '#00BFFF'
  } else if (performance >= 75) {
    return '#FFC0CB'
  } else if (performance >= 50) {
    return '#FF1493'
  } else {
    return '#FF0000'
  }
}

// Getting data
d3.json("/datageojsonformat", function(data) {
  makingMarkers(data.features);
});

// making markers (https://leafletjs.com/examples/geojson/)
function makingMarkers(data) {       
  var bbyMarkers = L.geoJson(data, {
      onEachFeature: function (feature, layer){
      layer.bindPopup(`<h3><b><u>Store# ${feature.properties.storenumber}</u></b>&nbsp &nbsp &nbsp &nbsp Last week : ${feature.properties.lastwknumber}</h3>
      <b>Last Week: Sell-thru ${feature.properties.lastwkst} units</b>,  Share ${feature.properties.lastwkshare}%
      <br><b>L. 5 Wks Ave: Sell-thru ${feature.properties.last5wkavest} units</b>,  Share ${feature.properties.last5wkshare}%
      <br><b>L. 10 Wks Ave: Sell-thru ${feature.properties.last10wkavest} units</b>,  Share ${feature.properties.last10wkshare}%
      <br><b>L. 20 Wks Ave: Sell-thru ${feature.properties.last20wkavest} units</b>,  Share ${feature.properties.last20wkshare}%
      <br><b><font color="#FF0000">Recent Performance</font></b> (5w Share/20w Share): <b><font color="#FF0000">${feature.properties.last5wkperformance}%</font></b>
      <br><b>Premium 10wk Ave: Sell-thru ${feature.properties.premium_10wk} units</b>,  Share ${feature.properties.premium_10wk_share}%
      <br>Table Display: ${feature.properties.tabledisplay}
      <br>End Cap: ${feature.properties.endcap}
      <br>Address: ${feature.properties.address1}, ${feature.properties.city} ${feature.properties.zipcode.slice(0, 5)}, ${feature.properties.state.slice(0, 2)}
      <br>Phone Number: ${feature.properties.telephonenumber}
      <br><br>-----------------Last Store Visit-----------------
      <br><b>Last Visit: ${feature.properties.last_visit}</b> by ${feature.properties.who_visited} 
      <br>Issue Status: ${feature.properties.status}
      <br><a href="${feature.properties.photo_1}" target="_blank">Photo 1</a>  
      <a href="${feature.properties.photo_2}" target="_blank">Photo 2</a>  
      <a href="${feature.properties.photo_3}" target="_blank">Photo 3</a>  
      <a href="${feature.properties.photo_4}" target="_blank">Photo 4</a>
      <a href="${feature.properties.photo_5}" target="_blank">Photo 5</a>    
      <br><b>Comment: </b>${feature.properties.comment}
      <br><b>Memo: </b>${feature.properties.memo}`
      
      );},

      //creating a circlemarker
      pointToLayer: function (feature, latlng) {
      return new L.circle(latlng,
      {radius: Math.sqrt(Number(feature.properties.lastwkst))*4500 + 2000, 
      fillColor: colorCategory(feature.properties.last5wkperformance),
      fillOpacity: .8,
      stroke: true,
      color: "black",
      weight: .5
      })
      }
  });

  // Same Mark Size MarkerLayer Small
  var smallbbyMarkers = L.geoJson(data, {
    onEachFeature: function (feature, layer){
    layer.bindPopup(`<h3><b><u>Store# ${feature.properties.storenumber}</u></b>&nbsp &nbsp &nbsp &nbsp Last week : ${feature.properties.lastwknumber}</h3>
    <b>Last Week: Sell-thru ${feature.properties.lastwkst} units</b>,  Share ${feature.properties.lastwkshare}%
    <br><b>L. 5 Wks Ave: Sell-thru ${feature.properties.last5wkavest} units</b>,  Share ${feature.properties.last5wkshare}%
    <br><b>L. 10 Wks Ave: Sell-thru ${feature.properties.last10wkavest} units</b>,  Share ${feature.properties.last10wkshare}%
    <br><b>L. 20 Wks Ave: Sell-thru ${feature.properties.last20wkavest} units</b>,  Share ${feature.properties.last20wkshare}%
    <br><b><font color="#FF0000">Recent Performance</font></b> (5w Share/20w Share): <b><font color="#FF0000">${feature.properties.last5wkperformance}%</font></b>
    <br><b>Premium 10wk Ave: Sell-thru ${feature.properties.premium_10wk} units</b>,  Share ${feature.properties.premium_10wk_share}%
    <br>Table Display: ${feature.properties.tabledisplay}
    <br>End Cap: ${feature.properties.endcap}
    <br>Address: ${feature.properties.address1}, ${feature.properties.city} ${feature.properties.zipcode.slice(0, 5)}, ${feature.properties.state.slice(0, 2)}
    <br>Phone Number: ${feature.properties.telephonenumber}
    <br><br>-----------------Last Store Visit-----------------
    <br><b>Last Visit: ${feature.properties.last_visit}</b> by ${feature.properties.who_visited} 
    <br>Issue Status: ${feature.properties.status}
    <br><a href="${feature.properties.photo_1}" target="_blank">Photo 1</a>  
    <a href="${feature.properties.photo_2}" target="_blank">Photo 2</a>  
    <a href="${feature.properties.photo_3}" target="_blank">Photo 3</a>  
    <a href="${feature.properties.photo_4}" target="_blank">Photo 4</a>
    <a href="${feature.properties.photo_5}" target="_blank">Photo 5</a>   
    <br><b>Comment: </b>${feature.properties.comment}
    <br><b>Memo: </b>${feature.properties.memo}`);
    },

    //creating a circlemarker
    pointToLayer: function (feature, latlng) {
    return new L.circle(latlng,
    {radius: 800, 
    fillColor: colorCategory(feature.properties.last5wkperformance),
    fillOpacity: .9,
    stroke: true,
    color: "black",
    weight: .5
    })
    }
});


  // Big Size MarkerLayer
  var bigbbyMarkers = L.geoJson(data, {
    onEachFeature: function (feature, layer){
    layer.bindPopup(`<h3><b><u>Store# ${feature.properties.storenumber}</u></b>&nbsp &nbsp &nbsp &nbsp Last week : ${feature.properties.lastwknumber}</h3>
    <b>Last Week: Sell-thru ${feature.properties.lastwkst} units</b>,  Share ${feature.properties.lastwkshare}%
    <br><b>L. 5 Wks Ave: Sell-thru ${feature.properties.last5wkavest} units</b>,  Share ${feature.properties.last5wkshare}%
    <br><b>L. 10 Wks Ave: Sell-thru ${feature.properties.last10wkavest} units</b>,  Share ${feature.properties.last10wkshare}%
    <br><b>L. 20 Wks Ave: Sell-thru ${feature.properties.last20wkavest} units</b>,  Share ${feature.properties.last20wkshare}%
    <br><b><font color="#FF0000">Recent Performance</font></b> (5w Share/20w Share): <b><font color="#FF0000">${feature.properties.last5wkperformance}%</font></b>
    <br><b>Premium 10wk Ave: Sell-thru ${feature.properties.premium_10wk} units</b>,  Share ${feature.properties.premium_10wk_share}%
    <br>Table Display: ${feature.properties.tabledisplay}
    <br>End Cap: ${feature.properties.endcap}
    <br>Address: ${feature.properties.address1}, ${feature.properties.city} ${feature.properties.zipcode.slice(0, 5)}, ${feature.properties.state.slice(0, 2)}
    <br>Phone Number: ${feature.properties.telephonenumber}
    <br><br>-----------------Last Store Visit-----------------
    <br><b>Last Visit: ${feature.properties.last_visit}</b> by ${feature.properties.who_visited} 
    <br>Issue Status: ${feature.properties.status}
    <br><a href="${feature.properties.photo_1}" target="_blank">Photo 1</a>  
    <a href="${feature.properties.photo_2}" target="_blank">Photo 2</a>  
    <a href="${feature.properties.photo_3}" target="_blank">Photo 3</a>  
    <a href="${feature.properties.photo_4}" target="_blank">Photo 4</a>
    <a href="${feature.properties.photo_5}" target="_blank">Photo 5</a>   
    <br><b>Comment: </b>${feature.properties.comment}
    <br><b>Memo: </b>${feature.properties.memo}`);
    },

    //creating a circlemarker
    pointToLayer: function (feature, latlng) {
    return new L.circle(latlng,
    {radius: Math.sqrt(Number(feature.properties.lastwkst))*25000 + 2000, 
    fillColor: colorCategory(feature.properties.last5wkperformance),
    fillOpacity: 0.4,
    stroke: true,
    color: "black",
    weight: .5
    })
    }
});


  // Making Premium Medium Markers
  var premiumMarkersMedium = L.geoJson(data, {
    onEachFeature: function (feature, layer){
    layer.bindPopup(`<h3><b><u>Store# ${feature.properties.storenumber}</u></b>&nbsp &nbsp &nbsp &nbsp Last week : ${feature.properties.lastwknumber}</h3>
    <b>Last Week: Sell-thru ${feature.properties.lastwkst} units</b>,  Share ${feature.properties.lastwkshare}%
    <br><b>L. 5 Wks Ave: Sell-thru ${feature.properties.last5wkavest} units</b>,  Share ${feature.properties.last5wkshare}%
    <br><b>L. 10 Wks Ave: Sell-thru ${feature.properties.last10wkavest} units</b>,  Share ${feature.properties.last10wkshare}%
    <br><b>L. 20 Wks Ave: Sell-thru ${feature.properties.last20wkavest} units</b>,  Share ${feature.properties.last20wkshare}%
    <br><b><font color="#FF0000">Recent Performance</font></b> (5w Share/20w Share): <b><font color="#FF0000">${feature.properties.last5wkperformance}%</font></b>
    <br><b>Premium 10wk Ave: Sell-thru ${feature.properties.premium_10wk} units</b>,  Share ${feature.properties.premium_10wk_share}%
    <br>Table Display: ${feature.properties.tabledisplay}
    <br>End Cap: ${feature.properties.endcap}
    <br>Address: ${feature.properties.address1}, ${feature.properties.city} ${feature.properties.zipcode.slice(0, 5)}, ${feature.properties.state.slice(0, 2)}
    <br>Phone Number: ${feature.properties.telephonenumber}
    <br><br>-----------------Last Store Visit-----------------
    <br><b>Last Visit: ${feature.properties.last_visit}</b> by ${feature.properties.who_visited} 
    <br>Issue Status: ${feature.properties.status}
    <br><a href="${feature.properties.photo_1}" target="_blank">Photo 1</a>  
    <a href="${feature.properties.photo_2}" target="_blank">Photo 2</a>  
    <a href="${feature.properties.photo_3}" target="_blank">Photo 3</a>  
    <a href="${feature.properties.photo_4}" target="_blank">Photo 4</a>
    <a href="${feature.properties.photo_5}" target="_blank">Photo 5</a>   
    <br><b>Comment: </b>${feature.properties.comment}
    <br><b>Memo: </b>${feature.properties.memo}`
    
    );},

    //creating a circlemarker
    pointToLayer: function (feature, latlng) {
    return new L.circle(latlng,
    {radius: Math.sqrt(Number(feature.properties.premium_10wk))*4500 + 600, 
    fillColor: colorCategory(feature.properties.last5wkperformance),
    fillOpacity: .8,
    stroke: true,
    color: "black",
    weight: .5
    })
    }
  });


  // Making Premium Big Markers
  var premiumMarkersBig = L.geoJson(data, {
    onEachFeature: function (feature, layer){
    layer.bindPopup(`<h3><b><u>Store# ${feature.properties.storenumber}</u></b>&nbsp &nbsp &nbsp &nbsp Last week : ${feature.properties.lastwknumber}</h3>
    <b>Last Week: Sell-thru ${feature.properties.lastwkst} units</b>,  Share ${feature.properties.lastwkshare}%
    <br><b>L. 5 Wks Ave: Sell-thru ${feature.properties.last5wkavest} units</b>,  Share ${feature.properties.last5wkshare}%
    <br><b>L. 10 Wks Ave: Sell-thru ${feature.properties.last10wkavest} units</b>,  Share ${feature.properties.last10wkshare}%
    <br><b>L. 20 Wks Ave: Sell-thru ${feature.properties.last20wkavest} units</b>,  Share ${feature.properties.last20wkshare}%
    <br><b><font color="#FF0000">Recent Performance</font></b> (5w Share/20w Share): <b><font color="#FF0000">${feature.properties.last5wkperformance}%</font></b>
    <br><b>Premium 10wk Ave: Sell-thru ${feature.properties.premium_10wk} units</b>,  Share ${feature.properties.premium_10wk_share}%
    <br>Table Display: ${feature.properties.tabledisplay}
    <br>End Cap: ${feature.properties.endcap}
    <br>Address: ${feature.properties.address1}, ${feature.properties.city} ${feature.properties.zipcode.slice(0, 5)}, ${feature.properties.state.slice(0, 2)}
    <br>Phone Number: ${feature.properties.telephonenumber}
    <br><br>-----------------Last Store Visit-----------------
    <br><b>Last Visit: ${feature.properties.last_visit}</b> by ${feature.properties.who_visited} 
    <br>Issue Status: ${feature.properties.status}
    <br><a href="${feature.properties.photo_1}" target="_blank">Photo 1</a>  
    <a href="${feature.properties.photo_2}" target="_blank">Photo 2</a>  
    <a href="${feature.properties.photo_3}" target="_blank">Photo 3</a>  
    <a href="${feature.properties.photo_4}" target="_blank">Photo 4</a>
    <a href="${feature.properties.photo_5}" target="_blank">Photo 5</a>   
    <br><b>Comment: </b>${feature.properties.comment}
    <br><b>Memo: </b>${feature.properties.memo}`);
    },

    //creating a circlemarker
    pointToLayer: function (feature, latlng) {
    return new L.circle(latlng,
    {radius: Math.sqrt(Number(feature.properties.premium_10wk))*25000 + 600, 
    fillColor: colorCategory(feature.properties.last5wkperformance),
    fillOpacity: 0.4,
    stroke: true,
    color: "black",
    weight: .5
    })
    }
});


  // Making All 10wks Medium Markers
  var all10wksMarkersMedium = L.geoJson(data, {
    onEachFeature: function (feature, layer){
    layer.bindPopup(`<h3><b><u>Store# ${feature.properties.storenumber}</u></b>&nbsp &nbsp &nbsp &nbsp Last week : ${feature.properties.lastwknumber}</h3>
    <b>Last Week: Sell-thru ${feature.properties.lastwkst} units</b>,  Share ${feature.properties.lastwkshare}%
    <br><b>L. 5 Wks Ave: Sell-thru ${feature.properties.last5wkavest} units</b>,  Share ${feature.properties.last5wkshare}%
    <br><b>L. 10 Wks Ave: Sell-thru ${feature.properties.last10wkavest} units</b>,  Share ${feature.properties.last10wkshare}%
    <br><b>L. 20 Wks Ave: Sell-thru ${feature.properties.last20wkavest} units</b>,  Share ${feature.properties.last20wkshare}%
    <br><b><font color="#FF0000">Recent Performance</font></b> (5w Share/20w Share): <b><font color="#FF0000">${feature.properties.last5wkperformance}%</font></b>
    <br><b>Premium 10wk Ave: Sell-thru ${feature.properties.premium_10wk} units</b>,  Share ${feature.properties.premium_10wk_share}%
    <br>Table Display: ${feature.properties.tabledisplay}
    <br>End Cap: ${feature.properties.endcap}
    <br>Address: ${feature.properties.address1}, ${feature.properties.city} ${feature.properties.zipcode.slice(0, 5)}, ${feature.properties.state.slice(0, 2)}
    <br>Phone Number: ${feature.properties.telephonenumber}
    <br><br>-----------------Last Store Visit-----------------
    <br><b>Last Visit: ${feature.properties.last_visit}</b> by ${feature.properties.who_visited} 
    <br>Issue Status: ${feature.properties.status}
    <br><a href="${feature.properties.photo_1}" target="_blank">Photo 1</a>  
    <a href="${feature.properties.photo_2}" target="_blank">Photo 2</a>  
    <a href="${feature.properties.photo_3}" target="_blank">Photo 3</a>  
    <a href="${feature.properties.photo_4}" target="_blank">Photo 4</a>
    <a href="${feature.properties.photo_5}" target="_blank">Photo 5</a>   
    <br><b>Comment: </b>${feature.properties.comment}
    <br><b>Memo: </b>${feature.properties.memo}`
    
    );},

    //creating a circlemarker
    pointToLayer: function (feature, latlng) {
    return new L.circle(latlng,
    {radius: Math.sqrt(Number(feature.properties.last10wkavest))*4500 + 600, 
    fillColor: colorCategory(feature.properties.last5wkperformance),
    fillOpacity: .4,
    stroke: true,
    color: "black",
    weight: .5
    })
    }
  });
  

    // Making All 10wks Big Markers
  var all10wksMarkersBig = L.geoJson(data, {
    onEachFeature: function (feature, layer){
    layer.bindPopup(`<h3><b><u>Store# ${feature.properties.storenumber}</u></b>&nbsp &nbsp &nbsp &nbsp Last week : ${feature.properties.lastwknumber}</h3>
    <b>Last Week: Sell-thru ${feature.properties.lastwkst} units</b>,  Share ${feature.properties.lastwkshare}%
    <br><b>L. 5 Wks Ave: Sell-thru ${feature.properties.last5wkavest} units</b>,  Share ${feature.properties.last5wkshare}%
    <br><b>L. 10 Wks Ave: Sell-thru ${feature.properties.last10wkavest} units</b>,  Share ${feature.properties.last10wkshare}%
    <br><b>L. 20 Wks Ave: Sell-thru ${feature.properties.last20wkavest} units</b>,  Share ${feature.properties.last20wkshare}%
    <br><b><font color="#FF0000">Recent Performance</font></b> (5w Share/20w Share): <b><font color="#FF0000">${feature.properties.last5wkperformance}%</font></b>
    <br><b>Premium 10wk Ave: Sell-thru ${feature.properties.premium_10wk} units</b>,  Share ${feature.properties.premium_10wk_share}%
    <br>Table Display: ${feature.properties.tabledisplay}
    <br>End Cap: ${feature.properties.endcap}
    <br>Address: ${feature.properties.address1}, ${feature.properties.city} ${feature.properties.zipcode.slice(0, 5)}, ${feature.properties.state.slice(0, 2)}
    <br>Phone Number: ${feature.properties.telephonenumber}
    <br><br>-----------------Last Store Visit-----------------
    <br><b>Last Visit: ${feature.properties.last_visit}</b> by ${feature.properties.who_visited} 
    <br>Issue Status: ${feature.properties.status}
    <br><a href="${feature.properties.photo_1}" target="_blank">Photo 1</a>  
    <a href="${feature.properties.photo_2}" target="_blank">Photo 2</a>  
    <a href="${feature.properties.photo_3}" target="_blank">Photo 3</a>  
    <a href="${feature.properties.photo_4}" target="_blank">Photo 4</a>
    <a href="${feature.properties.photo_5}" target="_blank">Photo 5</a>   
    <br><b>Comment: </b>${feature.properties.comment}
    <br><b>Memo: </b>${feature.properties.memo}`);
    },

    //creating a circlemarker
    pointToLayer: function (feature, latlng) {
    return new L.circle(latlng,
    {radius: Math.sqrt(Number(feature.properties.last10wkavest))*25000 + 600, 
    fillColor: colorCategory(feature.properties.last5wkperformance),
    fillOpacity: 0.4,
    stroke: true,
    color: "black",
    weight: .5
    })
    }
});




   //call the plotMap function
  plotMap(bbyMarkers, smallbbyMarkers, bigbbyMarkers, premiumMarkersMedium, premiumMarkersBig, all10wksMarkersMedium, all10wksMarkersBig)
}


function plotMap(bbyLayer, smallbbyLayer, bigbbyLayer, premiumMarkersMediumLayer, premiumMarkersBigLayer, all10wksMarkersMediumLayer, all10wksMarkersBigLayer) {

   // Create a base tile layer (satellite)
   var satellite = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.satellite",
    accessToken: API_KEY
  });


  // Create a base tile layer (grayscale)
  var grayscale = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.light",
      accessToken: API_KEY
  });

  // Create a base tile layer (outdoor)
  var outdoor = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.streets",
      accessToken: API_KEY
    });

  //base layer with three tile maps
  var baseMaps = {
    "Street Map": outdoor,
    "Grayscale": grayscale,
    "Satellite Map": satellite,
  };
  
  // overlay layer with the fault line and cirle markers layer
  var overlayMaps = {
    "Lask Wk All Products (Big Markers)": bigbbyLayer,
    "Last Wk All Products (Mid Markers)": bbyLayer,
    "Premium 10wk Ave (Big Markers)": premiumMarkersBigLayer,
    "Premium 10wk Ave (Mid Markers)": premiumMarkersMediumLayer,
    "All Prod 10wk Ave (Big Markers)": all10wksMarkersBigLayer,
    "All Prod 10wk Ave (Mid Markers)": all10wksMarkersMediumLayer,
    "Small Markers": smallbbyLayer
  };


  // Define a map object with layers (grayscale, earthquakes, fault)
  var myMap = L.map("map", {
    center: [36.7, -90.7],
    zoom: 4,
    layers: [outdoor, bigbbyLayer]
  });


  // Layer control
  L.control.layers(baseMaps,overlayMaps,{
    collapsed: false
  }).addTo(myMap);


  // Adding Legend (https://leafletjs.com/examples/choropleth/)
  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function (map) {
      var div = L.DomUtil.create('div', 'info legend'),
          grades = [0, 50, 75, 100, 125, 150],
          labels = [];

      // loop through our density intervals and generate a label with a colored square for each interval
      for (var i = 0; i < grades.length; i++) {
          div.innerHTML +=
              '<i style="background:' + colorCategory(grades[i] + 1) + '"></i> ' +
              grades[i] + '%' + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '%' + '<br>' : '+');
      }
      return div;
  };
  legend.addTo(myMap);
}

