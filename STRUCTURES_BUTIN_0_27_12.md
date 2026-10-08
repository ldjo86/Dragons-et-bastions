# Structures, génération et butin — JAR 0.27.12

## Structures configurées

Les placements ci-dessous sont **des réglages JSON**, non une promesse de trouver une structure à une distance fixe. Les biomes, reliefs, graines et autres règles de Minecraft continuent de conditionner la génération. « Espacement / séparation » donne les valeurs techniques entre régions de placement.

| Ensemble | Structures du tirage | Espacement / séparation | Source |
|---|---|---|---|
| `large_dragon_lair` | `ballista:large_dragon_lair` (poids 1) | 40 / 12 | `data/ballista/worldgen/structure_set/large_dragon_lair.json` |
| `mountain_dragon_lairs` | `ballista:mountain_lair_red` (poids 1) ; `ballista:mountain_lair_green` (poids 1) ; `ballista:mountain_lair_blue` (poids 1) | 28 / 8 | `data/ballista/worldgen/structure_set/mountain_dragon_lairs.json` |
| `pillager_den` | `ballista:pillager_den` (poids 1) | 28 / 8 | `data/ballista/worldgen/structure_set/pillager_den.json` |

Le mod contient **23 modèles de structures NBT compressés**, tous décodés sans erreur lors de l'audit, couvrant grottes, grandes cavernes, tanières de montagne et refuges de pillards :

- `caverne_glace.nbt`
- `caverne_rouge.nbt`
- `caverne_verte.nbt`
- `grande_caverne_glace.nbt`
- `grande_caverne_rouge.nbt`
- `grande_caverne_verte.nbt`
- `mountain_lairs/caverne_glace.nbt`
- `mountain_lairs/caverne_glace_aiguille.nbt`
- `mountain_lairs/caverne_glace_cirque.nbt`
- `mountain_lairs/caverne_glace_falaise.nbt`
- `mountain_lairs/caverne_rouge.nbt`
- `mountain_lairs/caverne_rouge_aiguille.nbt`
- `mountain_lairs/caverne_rouge_cratere.nbt`
- `mountain_lairs/caverne_rouge_falaise.nbt`
- `mountain_lairs/caverne_verte.nbt`
- `mountain_lairs/caverne_verte_arche.nbt`
- `mountain_lairs/caverne_verte_balcon.nbt`
- `mountain_lairs/caverne_verte_sommet.nbt`
- `relief_glace.nbt`
- `relief_rouge.nbt`
- `relief_verte.nbt`
- `taniere_pillards_1.nbt`
- `taniere_pillards_2.nbt`

## Coffres, entités et blocs avec tables de butin (28)

- `blocks/black_dragon_egg.json`
- `blocks/blue_dragon_egg.json`
- `blocks/bone_pile.json`
- `blocks/dragon_hunter_table.json`
- `blocks/echo_fletching_table.json`
- `blocks/fish_trap.json`
- `blocks/green_dragon_egg.json`
- `blocks/heavy_ballista_wreck.json`
- `blocks/infernal_fletching_table.json`
- `blocks/iron_spikes.json`
- `blocks/light_ballista_wreck.json`
- `blocks/medium_ballista_wreck.json`
- `blocks/obsidian_fletching_table.json`
- `blocks/red_dragon_egg.json`
- `blocks/wooden_spikes.json`
- `chests/dragon_lair.json`
- `chests/dragon_lair_blue.json`
- `chests/dragon_lair_green.json`
- `chests/dragon_lair_red.json`
- `chests/large_lair_gems.json`
- `chests/large_lair_relics.json`
- `chests/pillager_armory.json`
- `chests/pillager_den.json`
- `chests/pillager_den_tower.json`
- `entities/blue_dragon.json`
- `entities/dragon_hunter.json`
- `entities/green_dragon.json`
- `entities/red_dragon.json`

**Nouveauté utile :** la table `blocks/bone_pile.json` prévoit exactement **7 os** après destruction normale du tas d'ossements (sous la condition standard de survie à une explosion). La nasse (`blocks/fish_trap.json`) redonne le bloc nasse. Les coffres des camps incluent de l'équipement et des matériaux selon leurs tirages ; les probabilités ne sont pas garanties à l'unité.

## Limites

Aucun monde Minecraft n'a été généré pour confirmer la fréquence réelle ou l'emplacement visuel de chaque structure. La génération Java supplémentaire des tanières et des camps peut modifier le résultat. [Audit technique](ANALYSE_JAR_0_27_12.md).
