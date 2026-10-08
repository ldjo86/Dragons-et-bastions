# Audit technique — Dragons et Bastions 0.27.12-candidate

## Artefact étudié

- Fichier : `ballista-fabric-0.27.12-candidate+mc26.1-26.3-test.jar`
- SHA-256 : `5cb0158c309bd38fad9bfe090bee32eac43ee70996607625dd640f88ec72c284`
- Mod externe `ballista_bundle` / titre `Dragons et Bastions` ; licence déclarée `All-Rights-Reserved`.
- **5 JAR imbriqués** (un par version Minecraft) avec Java >=25, Fabric Loader >=0.19.3, Fabric API ; JAR externe dépend aussi du mod-id `ballista` >=`0.27.12-candidate`, fourni à l'intérieur sous forme imbriquée.
- `mc26.1` : 685 fichiers internes ; mod-id `ballista`, version `0.27.12-candidate+mc26.1`.
- `mc26.1.1` : 685 fichiers internes ; mod-id `ballista`, version `0.27.12-candidate+mc26.1.1`.
- `mc26.1.2` : 685 fichiers internes ; mod-id `ballista`, version `0.27.12-candidate+mc26.1.2`.
- `mc26.2` : 684 fichiers internes ; mod-id `ballista`, version `0.27.12-candidate+mc26.2`.
- `mc26.3` : 686 fichiers internes ; mod-id `ballista`, version `0.27.12-candidate+mc26.3`.

La métadonnée `Fabric-Minecraft-Version` du manifeste des JAR internes indique `26.2` même dans les variantes 26.1 et 26.3. **Il ne s'agit pas de la contrainte `fabric.mod.json`**, qui est bien spécifique à chaque variante. Vérifier en lançant le mod sur chacune des cinq versions avant d'annoncer une compatibilité garantie.

## Ressources du module 26.3

| Type | Nombre validé |
|---|---:|
| Classes Java | 244 |
| Recettes JSON | 32 |
| Avancements JSON | 33 |
| Tables de butin JSON | 28 |
| Fichiers `data/ballista/worldgen/**` | 16 |
| Modèles NBT | 23 |
| Images PNG | 90 |
| Clés de langue françaises/anglaises | 160 / 160 |
| Enchantements JSON propres au mod | 1 : `savoir` |

- Archives ZIP externe et imbriquées : **CRC sans erreur**.
- Fichiers JSON de chaque module : **analyse syntaxique valide** (0 échec).
- 23 structures NBT : **décompression GZIP valide**, et racine TAG_Compound vérifiée ; aucune simulation de placement en monde.
- Les différentes variantes n'ont **pas** un bytecode identique : elles incluent des adaptations de rendu et de génération du monde. `Outline261` ne se trouve que dans les variantes 26.1.x ; `World263` est propre à la 26.3. Ne pas déclarer leur comportement strictement équivalent.

## Changements documentés ici et éléments contrôlés

1. `ballista:bone_pile` — vrai modèle de 82 cuboïdes, loot `7` os, collision vide, sons de squelette au mouvement, présence dans `LairRules`.
2. `ballista:fish_trap` — bloc et entité bloc, GUI à 5 emplacements, appât en graines de blé, délai prévu de 120 à 240 secondes, sélection de poissons par biome et modèles de capture.
3. `ballista:savoir` — niveaux I–III, aimant XP (`8+2×rang cumulé` blocs), bonus calculé par `gain` et mixins d'orbes, XP à la mort et commerces.
4. `NightThreats` — événements nocturnes, invasion zombie en vagues jusqu'à 200 et spawns ponctuels ; règles et difficulté prises en compte.
5. `DraconicRaids` — gestion des fioles I–V et **appel de montage réel** (`startRiding`/`startRidingExtended`) pour l'illager sur le dragon.
6. **32 recettes** au lieu des 31 documentées pour la 0.27.10 ; la nasse est la nouvelle recette standard additionnelle.

## Anomalies / réserves constatées

- **Chaînes UTF-8 mal affichées dans `fr_fr.json`** : `block.ballista.black_dragon_egg` = `Å’uf de dragon corrompu`, `item.ballista.black_dragon_heart` = `CÅ“ur de dragon noir`. À corriger dans les ressources du **mod** lors d'une prochaine compilation ; le présent travail ne modifie pas le JAR.
- **Métadonnées du manifeste** : voir la mention `Fabric-Minecraft-Version: 26.2` ci-dessus. Les contraintes déclarées dans `fabric.mod.json` diffèrent et semblent prévues pour leurs versions respectives, mais aucun lancement n'a été effectué.
- `savoir.json` contient `effects: {}` mais les effets sont implémentés dans le code Java ; une inspection des JSON seuls donnerait une information erronée.
- Le nouveau tas d'ossements n'a pas de recette standard ; il sert à la construction de tanières par le mod. Ne pas lui attribuer un craft fictif.
- Le paquet est marqué **candidate / test**. Les comportements d'IA, butin, génération, raids et commandes doivent être validés en jeu avant une sortie stable.
- Aucune conclusion sur Minecraft 1.21.x : ce JAR ne comprend **aucun** module 1.21 ; analyser séparément les fichiers concernés.

## Scénarios conseillés pour la validation en jeu

- Lancement client et serveur sous les cinq versions ; création monde/chargement sans crash ; contrôler les mappings et la génération différée.
- Tester nasse avec/dehors eau, graines absentes, sorties remplies, rivière vs océan et sauvegarde/rechargement.
- Vérifier le tas d'ossements : hauteur 3D, collisions, son de pas, 7 os à la casse, rendu des 82 éléments.
- Tester Savoir I, II, III, cumul sur pièces équipées, récupération d'XP, commerce bibliothécaire et compatibilité avec d'autres enchantements.
- Tester les quatre dragons et les ordres, l'incubation/ponte, les cœurs et les tanières, y compris les ossements.
- Déclencher les fioles I–V, vérifier l'illageois réellement **sur** un dragon noir, suivi du raid et remise des avancements.
- Nuit paisible vs difficulté avec monstres, invasion 200 zombies (impact serveur), barres de boss et disparition des entités.
- Vérifier les 32 recettes, 28 loot tables et worldgen, avec et sans autres datapacks.

**Statut :** audit approfondi de l'archive, des JSON et d'une sélection ciblée du bytecode ; **pas** un test d'intégration en client Minecraft, pas une décompilation source exhaustive de chaque instruction Java.
