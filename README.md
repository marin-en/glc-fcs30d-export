# Afghanistan GLC_FCS30D Export

Google Earth Engine script for extracting and exporting the GLC_FCS30D global land cover dataset for Afghanistan.

## Overview

The script:

1. Loads Afghanistan boundaries from the USDOS LSIB dataset.
2. Loads the GLC_FCS30D annual land cover collection.
3. Extracts the 2022 land cover layer.
4. Clips the raster to Afghanistan.
5. Visualizes the result in Google Earth Engine.
6. Exports the clipped raster to Google Drive.

## Dataset

GLC_FCS30D is a global 30 m land cover product providing annual land cover maps.

## Output

* Spatial resolution: 30 m
* Coordinate system: EPSG:4326
* Output format: GeoTIFF (Google Drive export)

## Usage

Open the script in the Google Earth Engine Code Editor and run the export task.

## Author

Enza Marino

