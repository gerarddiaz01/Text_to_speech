import os
from newspaper import Article
from gtts import gTTS
import pygame
import time

def procesar_articulo(url):
    '''
    Descarga y procesa el contenido de un artículo desde una URL.

    Parámetros:
    url (str): La URL del artículo a procesar.

    Retorna:
    list: Una lista de párrafos extraídos del texto del artículo.
    '''
    articulo = Article(url)
    articulo.download()
    articulo.parse()
    return [parrafo.strip() for parrafo in articulo.text.split("\n") if parrafo.strip()]

def generar_audios(parrafos):
    '''
    Convierte los párrafos de texto en archivos de audio en formato MP3.

    Parámetros:
    parrafos (list): Lista de párrafos de texto a convertir en audio.

    Retorna:
    int: El número total de archivos de audio generados.
    '''
    contador = 1
    for parrafo in parrafos:
        if parrafo.strip():
            archivo = f"parrafo_{contador}.mp3"
            if not os.path.exists(archivo):
                tts = gTTS(parrafo, lang="es")
                tts.save(archivo)
                print(f"El párrafo {contador} se ha guardado como '{archivo}'")
            else:
                print(f"El archivo '{archivo}' ya existe. No se generará de nuevo.")
            contador += 1
    return contador - 1  # Retorna el número total de párrafos generados

def reproducir_audio(archivo):
    '''
    Reproduce un archivo de audio en formato MP3.

    Parámetros:
    filename (str): El nombre del archivo de audio a reproducir.

    Retorna:
    None
    '''
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        print(f"Error al reproducir el archivo: {e}")
    finally:
        pygame.mixer.quit()

def mostrar_descripciones(descripciones):
    '''
    Muestra una lista numerada de los párrafos disponibles, indicando si alguno es un pie de foto.

    Parámetros:
    descripciones (list): Lista de descripciones de los párrafos.

    Retorna:
    None
    '''
    print("\nPárrafos disponibles:")
    for descripcion in descripciones:
        print(descripcion)
        time.sleep(0.5)

def main():
    '''
    Función principal que coordina la descarga, procesamiento, generación de audios
    y reproducción de los párrafos de un artículo.

    Retorna:
    None
    '''
    # URL del artículo
    url = "https://elpais.com/ciencia/2024-11-29/la-ingeniosa-tecnica-de-moctezuma-y-su-banda-de-orcas-para-cazar-tiburones-ballena-en-mexico.html"
    
    print("Procesando el artículo...")
    parrafos = procesar_articulo(url)
    
    if not parrafos or all(not p.strip() for p in parrafos):
        print("El artículo no contiene texto válido para procesar.")
        return

    total_parrafos = generar_audios(parrafos)
    print("\nEl artículo ha sido procesado y dividido en párrafos.")
    time.sleep(1)

    # Lista de descripciones de los párrafos
    descripciones = [
        "1. Párrafo 1: Una orca llamada Moctezuma lidera cacerías de tiburones ballena en el Golfo de California.",
        "2. Párrafo 2: Un estudio documenta detalladamente estas cacerías en el Golfo de California entre 2018 y 2024.",
        "3. Párrafo 3: Las orcas son identificadas por marcas únicas como cicatrices y patrones en su piel.",
        "4. Párrafo 4: La manada, liderada por una matriarca, voltea al tiburón ballena para inmovilizarlo y mantenerlo en la superficie.",
        "5. Párrafo 5: Las orcas cazan en grupo, coordinando tácticas específicas transmitidas por la hembra más vieja.",
        "6. Pie de foto: Descripción del pie de foto de una de las fotos del articulo.",
        "7. Párrafo 7: Su gran cerebro, sociabilidad y memoria explican su éxito en la caza.",
        "8. Párrafo 8: El tráfico marítimo rápido amenaza la vida marina en el golfo.",
        "9. Párrafo 9: Ponerles nombre a las orcas genera empatía y fomenta la conservación.",
        "10. Párrafo 10: Otra orca macho fue nombrada Cuitláhuac y también es reconocida por los científicos."
    ]

    respuesta = input("¿Te gustaría escuchar los audios generados? (si/no): ").strip().lower()
    if respuesta not in ["sí", "si", "s"]:
        print("\n¡Gracias por usar el programa!")
        return

    mostrar_descripciones(descripciones)

    # Bucle para permitir al usuario escuchar varios audios
    while True:
        try:
            seleccion = int(input("\nSelecciona el número del párrafo que deseas escuchar (1-10): "))
            if 1 <= seleccion <= total_parrafos:
                archivo = f"parrafo_{seleccion}.mp3"
                if os.path.exists(archivo):
                    # Mostrar el contenido del párrafo en la terminal
                    print(f"\nReproduciendo el párrafo {seleccion}...")
                    print(f"Contenido del párrafo {seleccion}:")
                    print(parrafos[seleccion - 1])  # Mostrar el párrafo correspondiente
                    reproducir_audio(archivo)
                else:
                    print(f"El archivo '{archivo}' no existe. Por favor, selecciona otro párrafo.")
            else:
                print("Por favor, selecciona un número válido entre 1 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entre 1 y 10.")

        # Preguntamos si desea escuchar otro audio o salir
        continuar = input("\n¿Deseas escuchar otro párrafo? (si/no): ").strip().lower()
        if continuar not in ["sí", "si", "s"]:
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break

# Ejecutamos el programa
if __name__ == "__main__":
    main()