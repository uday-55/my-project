// Test script to verify translation and map
window.addEventListener('load', function() {
    console.log('=== FARMER DASHBOARD TEST ===');
    console.log('1. Current language:', currentLanguage || 'not set');
    console.log('2. Map object:', typeof map !== 'undefined' ? 'initialized' : 'not initialized');
    console.log('3. Leaflet loaded:', typeof L !== 'undefined' ? 'yes' : 'no');
    console.log('4. Map div exists:', document.getElementById('map') ? 'yes' : 'no');
    console.log('5. Map div height:', document.getElementById('map')?.offsetHeight + 'px');
    console.log('6. Translations object:', typeof translations !== 'undefined' ? 'loaded' : 'not loaded');
    
    setTimeout(function() {
        console.log('7. Map after delay:', typeof map !== 'undefined' && map ? 'ready' : 'not ready');
        if (map && map._layers) {
            console.log('8. Map layers count:', Object.keys(map._layers).length);
        }
    }, 2000);
});
