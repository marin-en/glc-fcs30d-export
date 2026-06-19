"""
GLC-FCS30D QGIS Symbology Import

Reads a GLC-FCS30D QML style file and applies a Paletted Raster Renderer
to the active raster layer while preserving the original class labels.

Tested with QGIS 3.40.6
"""
import xml.etree.ElementTree as ET
from qgis.core import QgsPalettedRasterRenderer, QgsColorRampShader
from PyQt5.QtGui import QColor

# 1. Set the path to your original QML file
qml_path = "/your_path/glc_fcs30d.qml"

layer = iface.activeLayer()

if layer and layer.type() == layer.RasterLayer:
    # 2. Parse the QML file to extract the original values, colors, and labels
    tree = ET.parse(qml_path)
    root = tree.getroot()

    classes = []

    # Search for legend items in the XML file
    for item in root.findall(".//item"):
        val = int(float(item.get('value')))
        label = item.get('label')
        color_hex = item.get('color')

        # Convert the hexadecimal color string to a QColor object
        color = QColor(color_hex)

        # Create a QGIS Paletted renderer class with value, color, and label
        classes.append(QgsPalettedRasterRenderer.Class(val, color, label))

    # 3. Force the raster to use a Paletted (Unique Values) renderer
    band = 1
    renderer = QgsPalettedRasterRenderer(layer.dataProvider(), band, classes)
    layer.setRenderer(renderer)

    # 4. Refresh the map canvas and legend
    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())

    print(f"Successfully applied {len(classes)} classes with their corresponding labels!")

else:
    print("Please select the correct raster layer in the Layers panel before running the script.")
