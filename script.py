from PIL import Image
import os

def riduci_dimensioni(file_input, file_output, percentuale_diminuzione):
    # Apri l'immagine
    with Image.open(file_input) as img:
        # Calcola le nuove dimensioni
        nuova_larghezza = int(img.width * percentuale_diminuzione / 100)
        nuova_altezza = int(img.height * percentuale_diminuzione / 100)

        # Riduci le dimensioni dell'immagine
        nuova_immagine = img.resize((nuova_larghezza, nuova_altezza), Image.LANCZOS)

        # Salva l'immagine ridotta
        nuova_immagine.save(file_output)

def riduci_dimensioni_cartella(cartella_input, cartella_output, percentuale_diminuzione):
    # Assicurati che le cartelle di output esistano
    if not os.path.exists(cartella_output):
        os.makedirs(cartella_output)

    # Scansiona tutti i file nella cartella di input
    for file_name in os.listdir(cartella_input):
        if file_name.lower().endswith(".png"):
            # Costruisci i percorsi completi dei file di input e output
            file_input_path = os.path.join(cartella_input, file_name)
            file_output_path = os.path.join(cartella_output, file_name)

            # Riduci le dimensioni dell'immagine e salva il risultato
            riduci_dimensioni(file_input_path, file_output_path, percentuale_diminuzione)

# CONFIG
cartella_input = "C:/Users/black/Desktop/resize-file" # INSERIRE LA CARTELLA IN CUI CI SONO LE IMMAGINI DA RIDIMENSIONARE
cartella_output = "C:/Users/black/Desktop/resize-file" # INSERIRE LA CARTELLA IN CUI CI SONO LE IMMAGINI RIDIMENSIONATE (PUO ESSERE UGUALE A QUELLA DI INPUT)
percentuale_diminuzione = 50 # VALORE DI RESIZE (50 = -50%, ESEMPIO DA 1024X1024 A 512X512)

# Riduci le dimensioni di tutte le immagini PNG nella cartella di input
riduci_dimensioni_cartella(cartella_input, cartella_output, percentuale_diminuzione)