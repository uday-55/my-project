// Check map div visibility
setTimeout(() => {
    const mapDiv = document.getElementById('map');
    if (mapDiv) {
        console.log('Map div found');
        console.log('Height:', mapDiv.offsetHeight);
        console.log('Width:', mapDiv.offsetWidth);
        console.log('Display:', window.getComputedStyle(mapDiv).display);
        console.log('Visibility:', window.getComputedStyle(mapDiv).visibility);
    } else {
        console.error('Map div not found!');
    }
}, 3000);
