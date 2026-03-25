
import os
import shutil

def create_backup_folder(original_folder, backup_folder):
    if not os.path.exists(backup_folder):
        shutil.copytree(original_folder, backup_folder)
        if os.path.exists(backup_folder):
            print(f"Backup created at {backup_folder}") 
    else:
        print(f"Backup already exists at {backup_folder}")
        shutil.copytree(original_folder, backup_folder, dirs_exist_ok=True)
    os.chdir(backup_folder)
        
def create_folder(list_folders):
    print(os.getcwd())
    for folder in list_folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            if os.path.exists(folder):
                print(f"Folder '{folder}' created successfully.")
            else:                
                print(f"Failed to create folder '{folder}'.")
            
def get_extension(file_name):
    return os.path.splitext(file_name)[1].lower()

def move_file(root, file, folder):
    shutil.move(os.path.join(root, file), os.path.join(os.getcwd(), folder, file))

def sort_files(result_generator):
    for root, dirs, files in result_generator:
        for file in files:
            if '.' in file:
                extension = get_extension(file)
                match extension:
                    case ".exe" | ".msi" | ".bat" | ".sh" | ".py":
                        move_file(root, file, 'ejecutables')
                    case ".zip" | ".rar" | ".tar" | ".gz":
                        move_file(root, file, 'zips')
                    case ".jpg" | ".jpeg" | ".png" | ".svg" | ".gif" | ".bmp" | ".tiff" | ".webp":
                        move_file(root, file, 'imágenes')
                    case ".doc" | ".docx":
                        move_file(root, file, 'words')
                    case ".txt" | ".md":
                        move_file(root, file, 'txts')
                    case ".xls" | ".xlsx":
                        move_file(root, file, 'excels')
                    case ".ppt" | ".pptx" | ".pdf":
                        move_file(root, file, 'presentaciones')
                    case ".csv" | ".json" | ".xml":
                        move_file(root, file, 'dataset')
                    case ".ipynb":
                        move_file(root, file, 'Jupyter_Notebooks')
                    case _:
                        print(f"Archivo {file} con extensión {extension} no categorizado.")