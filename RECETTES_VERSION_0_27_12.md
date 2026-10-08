# Dragons et Bastions — Les 32 recettes du JAR 0.27.12-candidate

> **Version étudiée :** archive `ballista-fabric-0.27.12-candidate+mc26.1-26.3-test.jar`. Cet inventaire est extrait des JSON du module 26.3. Les modules 26.1, 26.1.1, 26.1.2 et 26.2 contiennent les mêmes 32 fichiers de recettes. Aucun essai sur un client Minecraft n'a été réalisé.

Les **29 illustrations de fabrication de la version historique 0.27.1** sont conservées dans [le README](README.md) et sur [la page de recettes illustrées](site/recettes.html). La version 0.27.10 avait 31 fichiers de recette ; **la version 0.27.12 en contient 32**, dont la nouvelle `fish_trap`. Les recettes dont le champ `type` commence par `ballista:` ne doivent pas être interprétées comme de simples crafts classiques : elles utilisent les sérialiseurs Java du mod (cœur noir, cœur gelé, cœur de dragon, renfort d'armure).

[→ Guide complet 0.27.12](GUIDE_VERSION_0_27_12.md) · [→ Nouvelle nasse et tas d'ossements](BLOCS_ET_MECANIQUES_0_27_12.md)

## Liste et ingrédients vérifiés

### `apply_scale_boots_lining`

- **Type de recette :** `ballista:scale_armor`.
- **Recette spéciale propre au mod :** les règles complètes et les composants supplémentaires sont implémentés dans la classe Java de ce type, pas dans une grille vanilla.
- **Paramètres déclarés :** `base=#minecraft:foot_armor` ; `addition=ballista:scale_boots_lining`.
- **Source :** `data/ballista/recipe/apply_scale_boots_lining.json`.

### `apply_scale_chest_lining`

- **Type de recette :** `ballista:scale_armor`.
- **Recette spéciale propre au mod :** les règles complètes et les composants supplémentaires sont implémentés dans la classe Java de ce type, pas dans une grille vanilla.
- **Paramètres déclarés :** `base=#minecraft:chest_armor` ; `addition=ballista:scale_chest_lining`.
- **Source :** `data/ballista/recipe/apply_scale_chest_lining.json`.

### `apply_scale_helmet_lining`

- **Type de recette :** `ballista:scale_armor`.
- **Recette spéciale propre au mod :** les règles complètes et les composants supplémentaires sont implémentés dans la classe Java de ce type, pas dans une grille vanilla.
- **Paramètres déclarés :** `base=#minecraft:head_armor` ; `addition=ballista:scale_helmet_lining`.
- **Source :** `data/ballista/recipe/apply_scale_helmet_lining.json`.

### `apply_scale_leggings_lining`

- **Type de recette :** `ballista:scale_armor`.
- **Recette spéciale propre au mod :** les règles complètes et les composants supplémentaires sont implémentés dans la classe Java de ce type, pas dans une grille vanilla.
- **Paramètres déclarés :** `base=#minecraft:leg_armor` ; `addition=ballista:scale_leggings_lining`.
- **Source :** `data/ballista/recipe/apply_scale_leggings_lining.json`.

### `ballista`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:ballista`.
- **Ingrédients :** 1 × `minecraft:crossbow` ; 3 × `minecraft:iron_ingot` ; 3 × `#minecraft:logs` ; 2 × `minecraft:string`.
- **Disposition (espaces = cases vides) :**

```text
SIS
LCL
ILI
```
- **Source :** `data/ballista/recipe/ballista.json`.

### `black_dragon_heart`

- **Type de recette :** `ballista:black_dragon_heart`.
- **Recette spéciale propre au mod :** les règles complètes et les composants supplémentaires sont implémentés dans la classe Java de ce type, pas dans une grille vanilla.
- **Paramètres déclarés :** `base=#ballista:black_heart_equipment`.
- **Source :** `data/ballista/recipe/black_dragon_heart.json`.

### `bolt_primer`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 4 × `ballista:bolt_primer`.
- **Ingrédients sans forme :** 1 × `minecraft:feather` ; 1 × `minecraft:iron_nugget` ; 1 × `minecraft:stick`.
- **Source :** `data/ballista/recipe/bolt_primer.json`.

### `diamond_dragon_armor`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:diamond_dragon_armor`.
- **Ingrédients :** 6 × `minecraft:diamond` ; 1 × `ballista:dragon_scale`.
- **Disposition (espaces = cases vides) :**

```text
M M
MSM
M M
```
- **Source :** `data/ballista/recipe/diamond_dragon_armor.json`.

### `draconic_staff`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:draconic_staff`.
- **Ingrédients :** 1 × `minecraft:emerald` ; 1 × `minecraft:gold_ingot` ; 2 × `ballista:dragon_scale` ; 1 × `minecraft:stick`.
- **Disposition (espaces = cases vides) :**

```text
 G 
SES
 T 
```
- **Source :** `data/ballista/recipe/draconic_staff.json`.

### `dragon_heart`

- **Type de recette :** `ballista:dragon_heart`.
- **Recette spéciale propre au mod :** les règles complètes et les composants supplémentaires sont implémentés dans la classe Java de ce type, pas dans une grille vanilla.
- **Paramètres déclarés :** `base=#ballista:heart_equipment`.
- **Source :** `data/ballista/recipe/dragon_heart.json`.

### `dragon_hunter_table`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:dragon_hunter_table`.
- **Ingrédients :** 2 × `#minecraft:planks` ; 1 × `minecraft:map` ; 4 × `minecraft:gold_ingot` ; 2 × `minecraft:smooth_stone`.
- **Disposition (espaces = cases vides) :**

```text
BCB
OPO
OPO
```
- **Source :** `data/ballista/recipe/dragon_hunter_table.json`.

### `dragon_pack_saddle`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:dragon_pack_saddle`.
- **Ingrédients sans forme :** 1 × `ballista:dragon_saddle` ; 4 × `minecraft:chest`.
- **Source :** `data/ballista/recipe/dragon_pack_saddle.json`.

### `dragon_saddle`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:dragon_saddle`.
- **Ingrédients :** 2 × `minecraft:iron_ingot` ; 3 × `minecraft:leather` ; 2 × `ballista:dragon_scale`.
- **Disposition (espaces = cases vides) :**

```text
LLL
ISI
 S 
```
- **Source :** `data/ballista/recipe/dragon_saddle.json`.

### `echo_fletching_table`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:echo_fletching_table`.
- **Ingrédients sans forme :** 4 × `minecraft:echo_shard` ; 1 × `minecraft:fletching_table`.
- **Source :** `data/ballista/recipe/echo_fletching_table.json`.

### `fish_trap`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:fish_trap`.
- **Ingrédients :** 2 × `minecraft:stick` ; 3 × `#minecraft:planks` ; 3 × `minecraft:string`.
- **Disposition (espaces = cases vides) :**

```text
BSB
S S
PPP
```
- **Source :** `data/ballista/recipe/fish_trap.json`.

### `frozen_dragon_heart`

- **Type de recette :** `ballista:frozen_dragon_heart`.
- **Recette spéciale propre au mod :** les règles complètes et les composants supplémentaires sont implémentés dans la classe Java de ce type, pas dans une grille vanilla.
- **Paramètres déclarés :** `base=#minecraft:enchantable/armor`.
- **Source :** `data/ballista/recipe/frozen_dragon_heart.json`.

### `gold_dragon_armor`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:gold_dragon_armor`.
- **Ingrédients :** 6 × `minecraft:gold_ingot` ; 1 × `ballista:dragon_scale`.
- **Disposition (espaces = cases vides) :**

```text
M M
MSM
M M
```
- **Source :** `data/ballista/recipe/gold_dragon_armor.json`.

### `infernal_fletching_table`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:infernal_fletching_table`.
- **Ingrédients sans forme :** 2 × `minecraft:blaze_powder` ; 1 × `minecraft:fletching_table` ; 2 × `minecraft:nether_brick`.
- **Source :** `data/ballista/recipe/infernal_fletching_table.json`.

### `iron_dragon_armor`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:iron_dragon_armor`.
- **Ingrédients :** 6 × `minecraft:iron_ingot` ; 1 × `ballista:dragon_scale`.
- **Disposition (espaces = cases vides) :**

```text
M M
MSM
M M
```
- **Source :** `data/ballista/recipe/iron_dragon_armor.json`.

### `iron_spikes`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:iron_spikes`.
- **Ingrédients sans forme :** 1 × `ballista:wooden_spikes` ; 3 × `minecraft:iron_ingot`.
- **Source :** `data/ballista/recipe/iron_spikes.json`.

### `light_ballista`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:light_ballista`.
- **Ingrédients :** 1 × `minecraft:bow` ; 1 × `#minecraft:planks` ; 2 × `minecraft:string` ; 4 × `minecraft:stick`.
- **Disposition (espaces = cases vides) :**

```text
S S
TCT
TPT
```
- **Source :** `data/ballista/recipe/light_ballista.json`.

### `medium_ballista`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:medium_ballista`.
- **Ingrédients :** 1 × `minecraft:crossbow` ; 1 × `minecraft:iron_ingot` ; 3 × `#minecraft:planks` ; 2 × `minecraft:string` ; 2 × `minecraft:stick`.
- **Disposition (espaces = cases vides) :**

```text
SIS
PCP
TPT
```
- **Source :** `data/ballista/recipe/medium_ballista.json`.

### `netherite_dragon_armor`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:netherite_dragon_armor`.
- **Ingrédients sans forme :** 1 × `ballista:diamond_dragon_armor` ; 1 × `ballista:dragon_scale` ; 1 × `minecraft:netherite_ingot`.
- **Source :** `data/ballista/recipe/netherite_dragon_armor.json`.

### `obsidian_fletching_table`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:obsidian_fletching_table`.
- **Ingrédients sans forme :** 1 × `minecraft:fletching_table` ; 4 × `minecraft:obsidian`.
- **Source :** `data/ballista/recipe/obsidian_fletching_table.json`.

### `repair_heavy_ballista`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:ballista`.
- **Ingrédients sans forme :** 1 × `ballista:heavy_ballista_wreck` ; 1 × `minecraft:crossbow` ; 3 × `minecraft:iron_ingot`.
- **Source :** `data/ballista/recipe/repair_heavy_ballista.json`.

### `repair_light_ballista`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:light_ballista`.
- **Ingrédients sans forme :** 1 × `ballista:light_ballista_wreck` ; 2 × `minecraft:stick` ; 2 × `minecraft:string`.
- **Source :** `data/ballista/recipe/repair_light_ballista.json`.

### `repair_medium_ballista`

- **Type de recette :** `minecraft:crafting_shapeless`.
- **Résultat :** 1 × `ballista:medium_ballista`.
- **Ingrédients sans forme :** 1 × `#minecraft:logs` ; 1 × `ballista:medium_ballista_wreck` ; 2 × `minecraft:iron_ingot`.
- **Source :** `data/ballista/recipe/repair_medium_ballista.json`.

### `scale_boots_lining`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:scale_boots_lining`.
- **Ingrédients :** 4 × `ballista:dragon_scale`.
- **Disposition (espaces = cases vides) :**

```text
S S
S S
```
- **Source :** `data/ballista/recipe/scale_boots_lining.json`.

### `scale_chest_lining`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:scale_chest_lining`.
- **Ingrédients :** 8 × `ballista:dragon_scale`.
- **Disposition (espaces = cases vides) :**

```text
S S
SSS
SSS
```
- **Source :** `data/ballista/recipe/scale_chest_lining.json`.

### `scale_helmet_lining`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:scale_helmet_lining`.
- **Ingrédients :** 5 × `ballista:dragon_scale`.
- **Disposition (espaces = cases vides) :**

```text
SSS
S S
```
- **Source :** `data/ballista/recipe/scale_helmet_lining.json`.

### `scale_leggings_lining`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:scale_leggings_lining`.
- **Ingrédients :** 7 × `ballista:dragon_scale`.
- **Disposition (espaces = cases vides) :**

```text
SSS
S S
S S
```
- **Source :** `data/ballista/recipe/scale_leggings_lining.json`.

### `wooden_spikes`

- **Type de recette :** `minecraft:crafting_shaped`.
- **Résultat :** 1 × `ballista:wooden_spikes`.
- **Ingrédients :** 3 × `minecraft:stone_slab` ; 3 × `minecraft:stick`.
- **Disposition (espaces = cases vides) :**

```text
TTT
   
SSS
```
- **Source :** `data/ballista/recipe/wooden_spikes.json`.
