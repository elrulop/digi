import ffmpeg
import os
import re

def get_mins(file_path):
    
    # Data del archivo
    probe = ffmpeg.probe(file_path, v='error', select_streams='v:0', show_entries='format=duration')
    segs = float(probe['format']['duration'])
    mins = int(segs/60)

    return mins



def file_mins(main_path=str):

    walker = os.walk(main_path)

    for root, _, files in walker:
        for file in files:
            if file.endswith('.mp4') and '[' not in file:

                # Características del archivo
                file_path = os.path.join(root, file)
                file_name = os.path.splitext(file)[0]
                file_mins = get_mins(file_path)
                
                # Nuevas características
                new_name = f"{file_name} [{file_mins}].mp4"
                new_path = os.path.join(root, new_name)
                
                # Renombración archivo
                os.rename(file_path, new_path)



def mins_counter(main_path=str):
    
    # El patron
    pattern = r'\[(\d+)\]'
    walker = os.walk(main_path)

    # Explorador de archivos
    for root, dirs, files in walker:
        for dir in dirs:
            if "[" not in dir:

                mins_count = 0

                # Explorador de archivos
                for file in files:
                    match = re.search(pattern, file)
                    mins = int(match.group(1))
                    mins_count += mins
                
                # Nombre de la carpeta
                dir_name   = f"{root}/{dir}"
                dir_rename = f"{dir_name} [{mins_count}]"

                # Renombre
                os.rename(dir_name, dir_rename)



if __name__ == "__main__":

    main_path = r'/home/digi/Escritorio/Digitalización/Clientes'
    file_mins(main_path)
    mins_counter(main_path)
