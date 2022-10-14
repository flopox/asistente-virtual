function initMap() {                                        //creamos la funcion de mapeo
    const argCoords = { lat: -34.0, lng: -64.0 };           //Al iniciar la aplicación, se mostrara primero el pais de Argentina
    const map = new google.maps.Map(mapDiv, {               //Determina el zoom utilizado al iniciar la app
        zoom: 5,
        center: argCoords,
    });

    const marker = new google.maps.Marker({                 //Determina el marcador que se va a utilizar al buscar o selecionar alguna ubicacion
        position: { lat: -34.0, lng: -64.0 },               //Nuevamente se señalan las coordenadas de Argentina
        map,
    });

    const autocomplete = new google.maps.places.Autocomplete(place_input, {
       strictBounds: true,
    });                                                     //Lineas de codigo relacionado al autocompletar una busqueda en la barra superior(la funcion "strictBounds" cumple la funcion de autocompletar con zonas dentro del area que se muestra en pantalla)
    
    activateBtn.addEventListener("click", () => {
        autocomplete.bindTo("bounds", map);
    });
    desactivateBtn.addEventListener("click", () => {
        autocomplete.unbind("bounds");
    });

    autocomplete.bindTo("bounds", map);                     //Delimita el área en el que se busca, si alguien no se encuentra en Argentina y busca Cordoba, el autocompletado no deberia mostrar a Cordoba, Argentina como primera opcion
    autocomplete.addListener("place_changed", ()=>{         //Funciones de autcompletado que cambian la ubicacion y el zoom a la sona seleccionada(previamente solo marcaba el lugar que se buscaba, ahora ademas te dirige hacia alli)
        const place = autocomplete.getPlace();
        const { geometry } = place;
        const { viewport, location } = geometry;

        //map.center(location);
        //map.setZoom(8);
        marker.setPosition(location)
        map.fitBound(viewport);
    });
}  