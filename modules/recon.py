import os
import webbrowser
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import folium  

FILENAME = "recon_map.html"

def convertir_dms_a_decimal(dms, referencia):
    try:
        grd = dms[0]
        mins = dms[1]
        seg = dms[2]
        
        resultado = grd + (mins / 60.0) + (seg / 3600.0)
        
        if referencia == 'S' or referencia == 'W':
            resultado = -resultado
            
        return resultado
    
    except:
        return 0.0

#Cogemos los metadatos
def obtener_coordenadas_imagen(ruta_imagen):
    try:
        # 1. Abrimos la imagen con Pillow
        imagen = Image.open(ruta_imagen)
        
        # 2. Extraemos los metadatos crudos en data numerica
        exif_data = imagen._getexif()
        
        if not exif_data:
            return None 

        # Buscamos la etiqueta específica de GPS
        # Recorremos todos los tags hasta encontrar el que se llama 'GPSInfo'
        gps_info = {}
        for tag_id, value in exif_data.items():
            name_tag = TAGS.get(tag_id, tag_id)
            if name_tag == "GPSInfo":
                # Encontramos el GPS, pero sus datos internos también están codificados --> GPSTAGS los decodifica
                for t in value:# Recorremos los datos DENTRO del GPS (1, 2, 3, 4...)
                    type_name = GPSTAGS.get(t, t) #Cogemos los campos especificos denttro de GPS, lat,lon,etc
                    gps_info[type_name] = value[t] #Los metemos en un mapa para asociar por el nombre y o por susn numeros internos
                break
        
        # Si después de buscar no tenemos datos GPS, salimos.
        if not gps_info:
            return None

        # 4. Extraemos los datos crudos necesarios
        latitud_dms = gps_info.get('GPSLatitude')
        latitud_ref = gps_info.get('GPSLatitudeRef')
        longitud_dms = gps_info.get('GPSLongitude')
        longitud_ref = gps_info.get('GPSLongitudeRef')

        # Validamos que existan todos los datos
        if latitud_dms and latitud_ref and longitud_dms and longitud_ref:
            lat = convertir_dms_a_decimal(latitud_dms, latitud_ref)
            lon = convertir_dms_a_decimal(longitud_dms, longitud_ref)
            return [lat, lon]
        
        return None

    except Exception as e:
        return None


#GENERAR EL MAPA
def analizar_directorio(carpeta_objetivo):    
    # Coordenadas por defecto para inicializar el mapa
    mapa = folium.Map(location=[40.416, -3.703], zoom_start=6)
    
    imagenes_encontradas = 0
    coordenadas_validas = []
    
    print(f"[*] Iniciando análisis forense en: {carpeta_objetivo}")

    # Recorremos la carpeta
    for root, dirs, files in os.walk(carpeta_objetivo):
        for file in files:
            #Comprobamos formatos
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
                path = os.path.join(root, file)
                
                coordenadas = obtener_coordenadas_imagen(path)
                
                if coordenadas:
                    lat, lon = coordenadas
                    
                    # Añadimos un marcador al mapa
                    folium.Marker(
                        location=[lat, lon],
                        popup=f"<b>Archivo:</b> {file}<br><b>Lat:</b> {lat:.4f}<br><b>Lon:</b> {lon:.4f}",
                        tooltip="Ver Evidencia",
                        icon=folium.Icon(color="red", icon="info-sign")
                    ).add_to(mapa)
                    
                    coordenadas_validas.append([lat, lon])
                    imagenes_encontradas += 1

    if imagenes_encontradas > 0:
       
        if len(coordenadas_validas) > 1: # Comprobamos que haya cordenadas vaidas mayor que uno para unirlas con puntos
            folium.PolyLine(
                coordenadas_validas, # Lista de puntos 
                color="blue",        # Color de la línea
                weight=2.5,          # Grosor
                opacity=1            # Opacidad
            ).add_to(mapa)
        
        mapa.location = coordenadas_validas[0]
        mapa.fit_bounds(coordenadas_validas)
        
        
        mapa.save(FILENAME)
        
        mensaje = f"¡ÉXITO! {imagenes_encontradas} fotos geolocalizadas.\nMapa guardado como '{FILENAME}'."
        return mensaje, FILENAME
    else:
        return "No se encontraron datos GPS en ninguna imagen", None

def abrir_mapa(ruta_mapa):
    if ruta_mapa:
        webbrowser.open('file://' + os.path.realpath(ruta_mapa))