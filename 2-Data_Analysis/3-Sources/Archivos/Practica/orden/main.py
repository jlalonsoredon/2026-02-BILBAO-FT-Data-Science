import variables as var
import funciones as fun
import os

if __name__ == '__main__':
    fun.create_backup_folder(var.download_dir, var.download_dir_backup)
    fun.create_folder(var.folders)
    result_generator = os.walk(var.download_dir_backup)
    fun.sort_files(result_generator)
