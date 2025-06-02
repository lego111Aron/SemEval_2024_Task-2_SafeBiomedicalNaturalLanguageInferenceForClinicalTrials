import zipfile
import os

zip_path = "Task-2-SemEval-2024/training_data.zip"
extract_path = "Task-2-SemEval-2024/"

# Ellenőrizzük, ki van-e már csomagolva
if not os.path.exists(os.path.join(extract_path, "train.json")):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("Fájlok sikeresen kicsomagolva.")
else:
    print("A fájlok már ki vannak csomagolva.")
