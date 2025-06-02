Természetesen! Itt egy **tömör, érthető összefoglaló** a projekt céljáról, az eddigi megvalósítási lépésekről, valamint arról, hogyan lehet a projektet leállítani és újraindítani.

---

# 🔍 **Projektösszefoglaló: SemEval 2024 Task 2 – Szövegközi következtetés klinikai kontextusban**

## 🎯 **Cél és feladat**

A projekt célja egy mesterséges intelligencia modell fejlesztése, amely képes megérteni klinikai szövegeket és logikailag következtetni rájuk.

**Konkrét feladat:**
Adott egy **klinikai dokumentum szakasza** (pl. "Diagnosis") és egy **állítás** (pl. "The patient has diabetes."). A modell feladata, hogy eldöntse:

* **Entailment** – az állítás igaz a szöveg alapján,
* **Contradiction** – az állítás ellentmond a szövegnek,
* **Neutral** – a szöveg nem utal egyértelműen az állítás igazságtartalmára.

---

## 🧱 **A megvalósítás főbb lépései**

### 1. ✅ **Könyvtárak telepítése**

Telepítettük a szükséges könyvtárakat:
`transformers`, `datasets`, `torch`, `pandas`, `sklearn`, `tqdm` stb.

### 2. 📦 **Adatok letöltése és előkészítése**

* Letöltöttük a hivatalos adatcsomagot GitHub-ról.
* Kinyertük a `train.json`, `dev.json`, `test.json` fájlokat.
* Ezeket kiegészítettük a kapcsolódó CTR fájlokkal, amelyek a klinikai dokumentumokat tartalmazzák.

### 3. 🔄 **Adatok feldolgozása**

* Összefűztük a CTR fájlokból származó szövegrészeket az állításokkal.
* Egy új mezőt hoztunk létre: `input_text`, amely ezt az összeillesztett szöveget tartalmazza.
* Az adatokat Pandas DataFrame-be rendeztük és opcionálisan CSV-be is elmentettük.

### 4. 🧠 **HuggingFace Dataset és tokenizálás**

* A feldolgozott adatokat `Dataset` objektummá alakítottuk.
* Használtunk egy BERT típusú nyelvi modellt (`bert-base-uncased`).
* Tokenizáltuk az adatokat, hogy a modell be tudja fogadni őket.

### 5. 🏷️ **Címkék (label-ek) kódolása**

* A három kategóriát számmá alakítottuk:

  * Entailment → 0
  * Neutral → 1
  * Contradiction → 2

### 6. 🏋️ **Fine-tuning / tanítás**

* Beállítottuk a tanítási paramétereket (`TrainingArguments`).
* A modellt finomhangoltuk (fine-tune) a tanító és validáló adathalmazon `Trainer` segítségével.
* A tanítás 3 epoch alatt zajlott le.

### 7. 📊 **Értékelés és predikció**

* A modell értékelése `eval_accuracy = 52%`, `f1_macro ≈ 44%`.
* Lefuttattuk a predikciót a címkézetlen teszthalmazon.
* Az eredményeket elmentettük CSV fájlba (`test_predictions.csv`).

---

## 🛑 **Projekt leállítása**

1. **Virtuális környezet leállítása**:
   A terminálban:

   ```bash
   deactivate
   ```
2. **VS Code vagy terminál bezárása** (opcionális)

---

## 🔁 **Projekt újraindítása a jövőben**

1. Navigálj a projekt mappába:

   ```bash
   cd C:\Projektek\semeval2024
   ```

2. Aktiváld a virtuális környezetet:

   ```bash
   .\venv\Scripts\Activate.ps1
   ```

3. (Opcionális) Indítsd el VS Code-ot:

   ```bash
   code .
   ```

4. Futtasd a tanítást vagy predikciót újra a meglévő `.py` fájlokon keresztül.

---

## 🧩 Hasznos fájlok és kimenetek

* `train.json`, `dev.json`, `test.json` – kiinduló adatok
* `processed_*.csv` – feldolgozott, összefűzött szövegállományok
* `test_predictions.csv` – predikált címkék a teszthalmazra
* `trainer.evaluate()` – teljesítmény metrikák (pontosság, F1)

---

Szeretnél hozzá egy `.py` scriptet vagy `.ipynb` verziót is a jövőbeli gyorsabb használathoz? Szívesen összefoglalom abban is!
