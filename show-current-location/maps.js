function initMap(){
    const argCoords = {lat: -34.0, lng: -64.0}
    const map = new google.maps.Map(mapDiv, {
        center: argCoords,
        zoom: 6,
    });
    const marker = new google.maps.Marker({
        position: argCoords,
        map,
    });

    GamepadButton.addEventListener('click', () =>{
        if (navigator.geolocation){
            navigator.geolocation.getCurrentPosition(
               ({coords: {latitude, longitude}}) =>{
                   const coords = {
                       lat: latitude,
                       lng: longitude,
                   };
                   map.setCenter(coords)
                   map.setZoom(8)
                   marker.setPosition(coords)
            }, () =>{
               alert("El navegador esta bien, pero ocurrio un error")}
            );
           }else{
               alert("Tu navegador no consta de geolocalizacion, actualizalo para continuar");
           } 
    });
}