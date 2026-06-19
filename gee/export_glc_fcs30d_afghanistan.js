// =========================================================================
// 1. DEFINE REGION OF INTEREST (ROI) - USING STABLE LSIB BOUNDARIES
// =========================================================================
// Load United States Department of State Large Scale International Boundary dataset
var countries = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017");

// Filter explicitly for Afghanistan using its standardized country name
var afghanistan = countries.filter(ee.Filter.eq('country_na', 'Afghanistan'));

// Center the map viewport over Afghanistan to verify the geometry loaded
Map.centerObject(afghanistan, 6);
Map.addLayer(afghanistan, {color: 'grey'}, 'Afghanistan Boundary Outline', false);

// =========================================================================
// 2. LOAD GLC_FCS30D DATASET
// =========================================================================
var annualCollection = ee.ImageCollection("projects/sat-io/open-datasets/GLC-FCS30D/annual");
var globalMosaiced = annualCollection.mosaic();

// =========================================================================
// 3. EXTRACT TARGET YEAR AND CLIP
// =========================================================================
// Select 'b23' which corresponds to the year 2022
var targetYearMap = globalMosaiced.select('b23');

// Quick inspections to help verify band mapping and content
print('GLC image band names:', globalMosaiced.bandNames());
print('Sample image from collection:', annualCollection.first());
print('Selected band image (targetYearMap):', targetYearMap);

// Clip the image to the verified non-empty geometry
var afghanistanLC = targetYearMap.clip(afghanistan);

// =========================================================================
// 4. VISUALIZE THE LAND COVER
// =========================================================================
var visParams = {
    min: 10,
    max: 210,
    palette: [
        '003300', '006600', '33cc33', '99ff99', // Forests
        '808000', 'a52a2a', 'eedd82',          // Shrublands / Grasslands
        '0000ff', '33ccff',                     // Waterbodies / Wetlands
        'ff0000',                               // Built-up / Urban
        'ffffff', 'd3d3d3'                      // Barren / Snow and Ice
    ]
};

Map.addLayer(afghanistanLC, visParams, 'Afghanistan Land Cover 2022');

// =========================================================================
// 5. EXPORT LAND COVER MAP TO GOOGLE DRIVE
// =========================================================================
// Check for non-empty pixels in the AOI before exporting. If zero, abort.
var pixelCountDict = targetYearMap.reduceRegion({
    reducer: ee.Reducer.count(),
                                                geometry: afghanistan.geometry(),
                                                scale: 30,
                                                maxPixels: 1e13
});

print('Pixel count (server-side object):', pixelCountDict);

// Evaluate on the client to decide whether to export
pixelCountDict.values().get(0).evaluate(function(count) {
    if (!count || count === 0) {
        print('Export aborted: no valid pixels found in AOI for the selected band.');
    } else {
        Export.image.toDrive({
            image: afghanistanLC,
            description: 'Afghanistan_GLC_FCS30D_2022',
            folder: 'GEE_LandCover_Exports',
            fileNamePrefix: 'afghanistan_lc_2022_30m',
            scale: 30,
            region: afghanistan.geometry(),
                             maxPixels: 1e13,
                             crs: 'EPSG:4326'
        });
        print('Export started: Afghanistan_GLC_FCS30D_2022');
    }
});
