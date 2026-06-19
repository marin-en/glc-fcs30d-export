# QGIS Styling Utilities
/glc-fcs30d-export/Qgis/symbology_import.py
/glc-fcs30d-export/Qgis/glc_fcs30d.qml

This folder contains QGIS resources for visualizing GLC-FCS30D land cover maps.

## Contents

### QML Style

`Qgis/glc_fcs30d.qml`

QGIS style file containing the GLC-FCS30D land cover classes, colors, and labels.

### Symbology Import Script

`Qgis/symbology_import.py`

Python script for QGIS that reads the QML file and rebuilds a paletted raster renderer while preserving class labels.

This can be useful when QGIS imports raster classes correctly but does not display the expected legend labels.

## Usage

1. Load the exported GLC-FCS30D raster in QGIS.
2. Open the Python Console.
3. Update the `qml_path` variable in the script if necessary.
4. Run the script.
5. The active raster layer will be styled using the predefined GLC-FCS30D classes and labels.

## Notes

The script must be executed with the target raster selected as the active layer in QGIS.
