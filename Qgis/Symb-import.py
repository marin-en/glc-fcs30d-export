import xml.etree.ElementTree as ET
from qgis.core import QgsPalettedRasterRenderer, QgsColorRampShader
from PyQt5.QtGui import QColor

# 1. Imposta il percorso del tuo file QML originale
qml_path = "/home/enza/Documents/WBG-GDBM/GIS/Agriculture/Afghanistan_GLC_FCS30D_2022/glc_fcs30d.qml" 

layer = iface.activeLayer()

if layer and layer.type() == layer.RasterLayer:
    # 2. Parsifica il QML per estrarre i valori, i colori e i label originali
    tree = ET.parse(qml_path)
    root = tree.getroot()
    
    classes = []
    # Cerchiamo gli item della legenda nel file XML
    for item in root.findall(".//item"):
        val = int(float(item.get('value')))
        label = item.get('label')
        color_hex = item.get('color')
        
        # Convertiamo il colore esadecimale in QColor
        color = QColor(color_hex)
        
        # Creiamo la classe per il generatore Paletted di QGIS
        classes.append(QgsPalettedRasterRenderer.Class(val, color, label))
    
    # 3. Applichiamo forzatamente il renderer a Valori Unici (Paletted)
    band = 1
    renderer = QgsPalettedRasterRenderer(layer.dataProvider(), band, classes)
    layer.setRenderer(renderer)
    
    # 4. Aggiorna la vista e la legenda
    layer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(layer.id())
    print(f"Applicate con successo {len(classes)} classi con relativi label testuali!")
else:
    print("Seleziona il layer raster corretto nel pannello dei Layer prima di avviare lo script.")