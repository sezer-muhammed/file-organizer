from pathlib import Path
import datetime
import glob
import os
import shutil

months = {1: "1_Ocak", 2:"2_Subat", 3:"3_Mart", 4:"4_Nisan", 5:"5_Mayis", 6:"6_Haziran", 7:"7_Temmuz", 8:"8_Agustos", 9:"9_Eylul", 10:"10_Ekim", 11:"11_Kasim", 12:"12_Aralik"}

source_folder = "__NEW__"

all_files = glob.glob(source_folder + "/**/*.*", recursive=True)
files_num = len(all_files)

for i, file in enumerate(all_files):

    stats = os.stat(file)
    time = stats.st_mtime
    dt_m = datetime.datetime.fromtimestamp(time)

    year = dt_m.year
    month = dt_m.month
    day = dt_m.day

    month_name = months[month]

    save_path = Path(f"{year}/{month_name}")
    save_path.mkdir(exist_ok=True, parents=True)
    
    base_name = os.path.basename(file)
    destination = os.path.join(save_path, base_name)

    print(f"{i+1}/{files_num} moved.".ljust(20) + f"{year}/{month}/{day} - {base_name}".ljust(80) + f"File size is: {round(stats.st_size / (1024 * 1024), 3)} MB")

    shutil.move(file, destination)