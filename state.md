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

---
---

A jelenlegi megoldásod a SemEval2024_Task2_NLI.ipynb fájlban **alapvetően megfelel** a feladat fő követelményeinek, de néhány fontos szempontot érdemes figyelembe venni a teljes megfeleléshez:

---

## ✔️ Amit a notebookod már tud:
- **Input feldolgozás**: A CTR szakaszokat és állításokat összefűzi, előállítja az `input_text` mezőt.
- **Címkék**: A három címkét (Entailment, Neutral, Contradiction) kezeli.
- **Tokenizálás, modell betöltés**: HuggingFace BERT-alapú modell, tokenizálás, GPU támogatás.
- **Tanítás, értékelés**: Modell tanítása, validáció, F1 és accuracy metrikák számítása.
- **Predikció**: Teszthalmazra predikció, eredmények mentése CSV-be.

---

## ⚠️ Amit a feladat (és a hivatalos értékelés) még elvár(na):

1. **Kimeneti címkék**:  
   - A baseline notebookod három címkével dolgozik (`Entailment`, `Neutral`, `Contradiction`), de a *részletes összefoglaló* szerint a végső értékelés **bináris** (`Entailment` vagy `Contradiction`).  
   - Ha a végső értékelés bináris, a `Neutral` predikciókat át kell alakítani valamelyik osztályba (pl. `Contradiction`), vagy a modellt eleve binárisra kell tanítani.

2. **Faithfulness & Consistency metrikák**:  
   - A notebookod csak klasszikus F1-et és accuracy-t számol, de a versenyen **külön értékelik a Faithfulness és Consistency** mutatókat is, amelyek a perturbed példákra vonatkoznak.
   - Ezekhez szükséges lenne a predikciók utólagos elemzése az intervenció típusok szerint (preserving/altering), és a metrikák kiszámítása.

3. **Intervenció típusok kezelése**:  
   - A notebookod nem tartalmaz explicit logikát az intervenció típusok (paraphrase, contradiction, numerical, appended text stb.) felismerésére vagy kezelésére.
   - A Faithfulness/Consistency számításhoz szükséges, hogy a dev/test példákhoz tartozó intervenció típusokat ismerd (ez általában az adathalmazban szerepel).

4. **Baseline/Leaderboard kompatibilitás**:  
   - A végső predikciós fájl formátuma, elnevezése, és a mezők elnevezése feleljen meg a versenykiírásnak (pl. `results.json` vagy hasonló, ha azt várják el).

---

## 📝 **Mit kell(ene) még megvalósítanod?**

1. **Faithfulness és Consistency metrikák számítása**  
   - Implementáld a notebook végén a predikciók utólagos kiértékelését az intervenció típusok szerint.
   - Számold ki:  
     - **Faithfulness**: altering példákon, hogy a predikció változott-e.
     - **Consistency**: preserving példákon, hogy a predikció változatlan maradt-e.

2. **Bináris címkézés (ha szükséges)**  
   - Ha a végső értékelés bináris, módosítsd a címkézést és a modellt is binárisra (2 osztály), vagy a predikciókat konvertáld.

3. **Predikciós fájl formátum**  
   - Ellenőrizd, hogy a mentett predikciós fájl megfelel-e a verseny elvárásainak (pl. JSON formátum, megfelelő kulcsok).

4. **Intervenció típusok beolvasása**  
   - Ha az adathalmaz tartalmazza az intervenció típusát, olvasd be, és használd a Faithfulness/Consistency számításához.

---

## 📌 **Összefoglalva**

- **A fő pipeline helyes** (feldolgozás, tanítás, predikció, F1).
- **A hivatalos értékeléshez** szükséges a Faithfulness és Consistency metrikák implementálása, valamint a bináris címkézés ellenőrzése.
- **A predikciós fájl formátumát** igazítsd a versenykiíráshoz.

---

Ha szeretnéd, szívesen mutatok példát a Faithfulness/Consistency számítására vagy a bináris címkézésre a notebookod alapján!

----------------
----------------

Úgy látom a notebookodban megvannak az alapok (betöltöd az eredeti train/dev/test adatokat, finomhangolod a modellt és kiszámolod a Macro-F1-et az eredeti teszten), viszont **nem** találtam benne:

1. **Az NLI4CT-P kontrasztkészlet betöltését**

   * A teszt- és dev-állításokhoz tartozó perturbed változatok (paraphrase, contradiction, numerical paraphrase/contradiction, appended text) nincsenek beolvasva. Ezek nélkül nem tudod kiszámolni a 2. és 3. pontban szükséges metrikákat.

2. **Consistency metrika számítása**

   * Azokon a példákon, ahol a perturbáció *nem* változtatja az állítás jelentését (paraphrase, numerical paraphrase, appended text), ellenőrizned kell, hogy a predikció *azonos* marad-e az eredetivel.
   * Formális definíció:

     ```
     Consistency = (1/N_preserving) * Σ_i [ 1{f(original_i) == f(perturbed_i)} ]
     ```

3. **Faithfulness metrika számítása**

   * Azokon a példákon, ahol a perturbáció *megváltoztatja* az állítás jelentését (contradiction rephrasing, numerical contradiction), ellenőrizned kell, hogy a predikció *változik*-e az eredetihez képest.
   * Formális definíció:

     ```
     Faithfulness = (1/N_altering) * Σ_i [ 1{f(original_i) != f(perturbed_i)} ]
     ```

4. **Eredmények riportálása a két új metrikára**

   * A SemEval-feladatban nem elég csak a Macro-F1 a „control” eredeti adatokon, a kontrasztkészleten is mutatnod kell Consistency és Faithfulness értékeket, külön bontva perturbáció-típusok szerint (vagy legalább összesítve).

---

### Mit kell hozzáadnod a notebookhoz

* **Perturbed adatok betöltése**

  * A dev/test JSON-ek mellett beolvasod a `dev_perturbed.json` és `test_perturbed.json` fájlokat (vagy az azokból generált Pandas DataFrame-eket), ahol minden perturbed állításhoz megkapod az eredeti páros UUID-ját és a perturbáció típusát.

* **Predikciók generálása perturbed állításokra**

  * Ugyanazzal a finomhangolt modelleddel végigmész a perturbed set-en is, és elmented mind az eredeti, mind a perturbed predikciókat.

* **Consistency és Faithfulness kiszámítása**

  * Csoportosítod a perturbed példákat preserving vs altering típusokra, és az előbbi csoportnál nézed a predikció megegyezését, az utóbbinál az eltérést.

* **Összefoglaló táblázatot/plotot** készítesz, ahol látható:

  * Macro-F1 (eredeti adatokon)
  * Consistency (preserving perturbációkon)
  * Faithfulness (altering perturbációkon)

Ha ezeket a lépéseket beépíted a notebookodba, teljes lesz a feladatmegoldásod a SemEval-2024 Task 2 elvárásai alapján (az eredmények beküldése nélkül). Ha szeretnéd, megmutatom a konkrét kódvázlatot is a metrikákra.
