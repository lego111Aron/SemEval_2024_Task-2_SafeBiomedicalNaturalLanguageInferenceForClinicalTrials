Természetesen! Itt egy részletes **összefoglaló**, lépésről lépésre, arról, hogyan sikerült a SemEval 2024 Task 2 projektet **lokálisan** futtatni Windows rendszeren, CUDA-s GPU-val, és hogyan tudod ugyanezt megismételni más projektekkel is.

---

## 🔧 Lokális fejlesztési környezet beállítása transformer alapú NLP projekthez

### 📁 1. Projekt mappa létrehozása

Hozz létre egy külön mappát a projekthez, például:

```powershell
mkdir C:\Projektek\semeval2024
cd C:\Projektek\semeval2024
```

---

### 🐍 2. Virtuális környezet létrehozása és aktiválása

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

> Ha hibát kapsz a PowerShell-ben az `Activate.ps1` miatt, futtasd előtte:
>
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

---

### 📦 3. Legfontosabb csomagok telepítése

Aktív `venv` esetén telepítsd a következő csomagokat:

```powershell
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate datasets
pip install accelerate
pip install transformers
pip install --quiet transformers datasets torch scikit-learn pandas tqdm
pip install -U transformers
```

(Ez a `torch` verzió az NVIDIA RTX 2070-hez és CUDA 11.8-hoz passzol.)

---

### 🧪 4. Kód futtatása VS Code-ból

1. Indítsd el a VS Code-ot a projekt mappából:

```powershell
code .
```

2. A bal alsó sarokban válaszd ki a `venv` Python környezetet.

3. Írd meg vagy másold be a `test.py`, `train.py` vagy más fájlt.

4. Futtasd a kódot (pl. `Run Python File` vagy F5).

---

### 📁 5. (Opcionális) `requirements.txt` létrehozása

Ha másik gépen vagy kollégának is be akarod állítani, futtasd:

```bash
pip freeze > requirements.txt
```

Majd másik gépen:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 🛑 Projekt leállítása

Ha már nem dolgozol a projekten:

1. A terminálban írd be:

   ```powershell
   deactivate
   ```
2. A VS Code-ot vagy a terminált bezárhatod.

---

## ▶️ Projekt újraindítása később

1. Nyisd meg a mappát PowerShellben:

   ```powershell
   cd C:\Projektek\semeval2024
   ```

2. Aktiváld a virtuális környezetet:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. Indítsd el a VS Code-ot (vagy futtasd a fájlt közvetlenül):

   ```powershell
   code .
   ```

4. Futtasd a `train.py`, `test.py` vagy egyéb fájlokat.

---

## 📌 Gyors emlékeztető: parancslista

```powershell
# Első alkalommal:
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate datasets
pip install accelerate
pip install transformers
pip install --quiet transformers datasets torch scikit-learn pandas tqdm
pip install -U transformers

# Projekt újraindítása:
cd C:\Projektek\semeval2024
.\venv\Scripts\Activate.ps1
code .

# Projekt leállítása:
deactivate
```

---

Szükség esetén szívesen készítek neked ehhez egy `.bat` fájlt vagy VS Code `tasks.json` beállítást is az automatikus indításhoz!
