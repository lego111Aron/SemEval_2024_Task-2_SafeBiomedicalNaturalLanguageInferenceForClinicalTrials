# Futási eredmények

<hr style="border: 2px solid #333; margin: 24px 0;"/>

## bert-base-uncased

**Modell:** `bert-base-uncased`  
**Tanítási adathalmaz:** `clinical_trials_train.csv`  
**Paraméterek:**
- **Tanulási ráta:** `2e-5`
- **Batch méret:** `8`
- **Epochok száma:** `3`

<div style="display: flex; align-items: flex-start; gap: 32px;">

<div>

### Eredmények

| **Metrika**     | **Érték** |
|-----------------|-----------|
| Pontosság       | 0.53      |
| F1-macro        | 0.52      |
| Veszteség       | 0.69      |
| Epoch           | 3         |

- **Futtatási idő:** `6.00 mp`
- **Minták/másodperc:** `33.31`
- **Lépések/másodperc:** `4.16`

### Megjegyzések

- ...

</div>

<img src="bert-base-uncased.png" alt="bert-base-uncased eredmények" width="350" style="margin-top: 0;"/>

</div>

<hr style="border: 2px solid #333; margin: 24px 0;"/>

## emilyalsentzer/Bio_ClinicalBERT

**Modell:** `emilyalsentzer/Bio_ClinicalBERT`  
**Tanítási adathalmaz:** `clinical_trials_train.csv`  
**Paraméterek:**
- **Tanulási ráta:** `2e-5`
- **Batch méret:** `8`
- **Epochok száma:** `3`

<div style="display: flex; align-items: flex-start; gap: 32px;">

<div>

### Eredmények

| **Metrika**     | **Érték** |
|-----------------|-----------|
| Pontosság       | 0.52      |
| F1-macro        | 0.47      |
| Veszteség       | 0.69      |
| Epoch           | 3         |

- **Futtatási idő:** `5.34 mp`
- **Minták/másodperc:** `37.44`
- **Lépések/másodperc:** `4.68`

### Megjegyzések

- ...

</div>

<img src="emilyalsentzer-Bio_ClinicalBERT.png" alt="emilyalsentzer/Bio_ClinicalBERT eredmények" width="350" style="margin-top: 0;"/>

</div>

<hr style="border: 2px solid #333; margin: 24px 0;"/>