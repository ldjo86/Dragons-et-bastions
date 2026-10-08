# Dragon noir, chasseur illageois et fioles de mauvais présage draconique

> **🆕 Wiki 0.27.12-candidate (JAR analysé le 08/10/2026) :** [guide complet](GUIDE_VERSION_0_27_12.md) · [32 recettes](RECETTES_VERSION_0_27_12.md) · [tas d'ossements et nasse](BLOCS_ET_MECANIQUES_0_27_12.md) · [Savoir I–III](ENCHANTEMENT_SAVOIR_0_27_12.md) · [audit technique](ANALYSE_JAR_0_27_12.md). Les explications historiques ci-dessous concernent des JAR plus anciens et ne remplacent pas le guide 0.27.12.

**Guide du JAR `ballista-fabric-0.27.10-candidate+mc26.1-26.3-test.jar`**, variante Minecraft 26.3 inspectée le 8 octobre 2026. Les mécanismes ci-dessous sont lus dans les classes et les ressources du mod ; les apparitions effectives restent conditionnées au monde, au chargement des zones et au bon fonctionnement de Minecraft.

[← Accueil du wiki](README.md) · [Guide général 0.27.10](GUIDE_VERSION_0_27_10.md) · [Page illustrée consacrée aux raids](site/raids-draconiques.html) · [Page illustrée du dragon noir](site/dragon-noir.html)

## 1. Le dragon noir : un quatrième dragon, allié des illageois

![Texture de l'œuf noir](site/generated/icons/black_dragon_egg_0.png) ![Œuf d'apparition noir](site/generated/icons/black_dragon_spawn_egg.png)

Le **dragon noir** est une véritable entité enregistrée sous **`ballista:black_dragon`**, distincte des dragons rouge, vert et bleu. Il dispose d'un **œuf incubable** (`ballista:black_dragon_egg`), d'un **œuf d'apparition** et de textures propres, dont différentes apparences de corps/équipement. Son butin spécifique comprend le **cœur de dragon noir**.

Son système de faction est différent : un **dragon noir corrompu considère les autres dragons noirs et les illageois comme des alliés**. Son ciblage peut notamment prendre en compte joueurs non créatifs, villageois, gardes ou golems, tout en écartant les alliés de faction. Un dragon noir de raid n'est donc **pas un dragon de compagnie donné au joueur**.

### Santé, dégâts et croissance

| Âge | Santé maximale définie | Dégâts d'attaque de base définis |
|---|---:|---:|
| Nouveau-né | 24 PV (12 cœurs) | 3 |
| Adolescent | 60 PV (30 cœurs) | 7 |
| Adulte | 120 PV (60 cœurs) | 12 |

Ce sont des **attributs de base de l'entité**, pas le résultat garanti de chaque attaque (les souffles, projectiles, protections ou autres effets sont calculés séparément). Les raids de niveaux I et II font explicitement passer leur dragon noir au stade **adolescent** ; les niveaux III, IV et V utilisent la variante **adulte**.

**Sources du code :** `SiegeDragons.BLACK`, `DragonColor.BLACK`, `SiegeDragon.createAttributes/applyHatchlingAttributes/makeAdolescent`, `CorruptedRules.black/friendly/hostile`, `DraconicRaidState.adolescent`, `SiegeDragon.dropCustomDeathLoot`.

## 2. Le chasseur de dragons illageois est réellement un CAVALIER

L'**œuf d'apparition du chasseur illageois** est enregistré par le mod ; son icône est rendue par Minecraft et aucun PNG autonome correspondant n'est présent dans les ressources extraites du JAR.

Le **chasseur de dragons illageois**, identifiant **`ballista:illager_dragon_hunter`**, est un ennemi dérivé du **Vindicateur**. Lors du renfort draconique final, à partir du **présage III**, le code :

1. Crée un **dragon noir adulte**.
2. Insère une **selle draconique** dans son emplacement d'équipement.
3. Crée un **chasseur de dragons illageois** et lui attribue son équipement.
4. Place le chasseur à la position du dragon, puis appelle **`startRiding`** pour lui faire **monter ce dragon**.
5. Ajoute le dragon et son passager au monde, si les opérations nécessaires réussissent.

Ce n'est **pas** la simple apparition côte à côte d'un dragon et d'un chasseur. La relation de **passager monté sur le dragon** est explicitement programmée.

Au niveau IV ou V, **trois dragons noirs** sont prévus dans ce renfort, mais **seul le premier porte un chasseur**. Le code ne génère pas trois cavaliers.

### Équipement et comportement du chasseur monté

| Propriété | Valeur constatée |
|---|---|
| Santé maximale | **60 PV** (30 cœurs) |
| Dégâts d'attaque de base | **3** |
| Portée de suivi | **24 blocs** |
| Vitesse de déplacement de base | **0,30** |
| Échelle du modèle | **1,3** |
| Armure | **Casque, plastron, jambières et bottes en diamant** |
| Arme finale en main | **Bâton draconique** (il remplace l'épée en diamant attribuée au début de l'équipement) |
| Attaque à distance programmée | **Boule de feu**, portée approximative de **3 à 24 blocs** avec ligne de vue |
| Cadence de cette attaque | **60 ticks**, soit environ **3 secondes**, quand un projectile a pu être généré |

Le chasseur **ne pilote pas le dragon comme un joueur** : le dragon suit son comportement de combat et le code du raid **transmet sa cible au chasseur passager**. Ils attaquent ainsi la même menace. Le chasseur évite de prendre pour cible un **illageois allié** ou un **dragon noir**.

À sa mort, le chasseur déclenche la chute d'**un cœur de dragon noir** dans sa logique de butin. Il tente aussi de fournir **une ou deux cartes de tanière illageoise éloignée**, uniquement lorsqu'il repère des structures adaptées : ces cartes ne sont **pas garanties**.

**Sources du code :** `DraconicRaids.ride/spawn/beforeTick`, `IllagerDragonHunter.attributes/equipHunter/equipDraconicStaff`, `HunterRules.combat/loot`, `DragonVillages.ILLAGER_HUNTER`.

## 3. Les cinq fioles de mauvais présage draconique

Les cinq fioles sont des **objets consommables** indépendants :

| Fiole | Identifiant dans le mod | Effet appliqué après consommation |
|---|---|---|
| ![I](site/generated/icons/draconic_omen_1.png) **I** | `ballista:draconic_omen_1` | Mauvais présage **I** |
| ![II](site/generated/icons/draconic_omen_2.png) **II** | `ballista:draconic_omen_2` | Mauvais présage **II** |
| ![III](site/generated/icons/draconic_omen_3.png) **III** | `ballista:draconic_omen_3` | Mauvais présage **III** |
| ![IV](site/generated/icons/draconic_omen_4.png) **IV** | `ballista:draconic_omen_4` | Mauvais présage **IV** |
| ![V](site/generated/icons/draconic_omen_5.png) **V** | `ballista:draconic_omen_5` | Mauvais présage **V** |

### Utilisation et durée

- **Tenir la fiole puis boire** : animation de boisson de **32 ticks** (environ **1,6 seconde** à 20 TPS).
- Elle retire d'abord l'ancien effet **Mauvais présage**, puis applique le niveau choisi ; les amplificateurs internes vont de **0 à 4** pour les niveaux I à V.
- **Durée de Mauvais présage : 120 000 ticks**, soit **100 minutes** de temps simulé à 20 TPS, tant que l'effet ne disparaît pas avant.
- La consommation utilise le comportement de contenant de Minecraft : **une bouteille de verre vide** est rendue, avec la gestion habituelle du mode créatif.
- **Il n'y a pas cinq effets de statut élémentaires différents dans la fiole** : les cinq fioles produisent le même type d'effet, **Mauvais présage**, à des puissances distinctes. Ce qui change ensuite, c'est le renfort draconique associé au niveau du raid.

L'objet est enregistré dans le mod et proposé dans sa collection d'objets, mais la **présence d'un objet dans le registre ne prouve pas une recette de survie**. Les 31 recettes analysées ne contiennent pas de fabrication 3×3 de ces fioles. Ne pas annoncer une recette inventée.

**Sources :** `DraconicOmenItem.use/getUseDuration/getUseAnimation/finishUsingItem`, `DraconicRaids.drink`, `SiegeDragons.draconicOmen1..5`.

## 4. Que se passe-t-il pendant un raid ?

Le mod **étend le système de raid des villages de Minecraft**. Boire une fiole confère le Mauvais présage correspondant ; l'entrée en situation de raid relève ensuite du déclenchement normal de Minecraft.

**Point capital : les dragons noirs ne sont PAS invoqués à chaque vague.** Le code `DraconicRaids.wave` attend **la dernière vague du raid** (ou sa vague supplémentaire selon les règles de mauvais présage) avant de déployer le renfort draconique. Il peut tenter à nouveau de générer les dragons tant que le raid est actif si un emplacement n'a pas été trouvé.

| Niveau de la fiole | Renfort draconique de fin de raid | Cavalier illageois | Modification du combat |
|---|---|---|---|
| **I** | **1 dragon noir adolescent** | Non | Premier combat contre un dragon noir plus jeune |
| **II** | **1 dragon noir adolescent** | Non | Même nombre et même âge dans la règle draconique ; raid vanilla de niveau plus élevé |
| **III** | **1 dragon noir adulte** | **Oui, monté** | Première apparition de l'ensemble **dragon + chasseur illageois** |
| **IV** | **3 dragons noirs adultes** | **Oui, sur le premier** | Renfort de trois dragons, dont un monté |
| **V** | **3 dragons noirs adultes** | **Oui, sur le premier** | Même effectif draconique que IV ; puissance du Mauvais présage et récompense de niveau V |

Attention : cette table donne les **effectifs programmés dans le renfort draconique final** et les différences d'âge/monture. Elle ne compte **pas tous les pillards, vindicateurs et autres créatures des vagues vanilla**. Les niveaux II/I et V/IV ne reçoivent pas automatiquement un dragon supplémentaire : la différence relève surtout du **niveau de présage/raid et de sa récompense**.

### Conditions qui peuvent empêcher l'apparition

Le mod cherche des positions de génération dans des chunks chargés, dans les limites du monde et sans collision bloquante, à différentes hauteurs autour de la zone du raid. Il sauvegarde les renforts créés, suit leur santé et les inclut dans le comptage et la barre de vie du raid.

Un renfort peut donc être **retardé** si aucun emplacement utilisable n'est trouvé. Le code prévoit aussi un abandon de la tentative de dragon monté si `startRiding` échoue. La **présence du mécanisme dans le JAR** est confirmée ; elle ne garantit pas que toutes les situations en jeu produisent un couple monté sans incident.

**Sources :** `DraconicRaids.absorb/wave/ride/spawn/beforeTick/count/health/bossbar`, `DraconicRaidState.dragons/adolescent/mounted/pending/remaining`, `DraconicRaidMixin`.

## 5. Récompenses : Héros légendaire I à V

Le raid n'est considéré réussi, pour cette mécanique supplémentaire, que si le **raid est gagné**, que les renforts draconiques ont bien été déclenchés, et que **tous les dragons du renfort ont été vaincus**. S'ils sont encore vivants, le système retarde la validation.

À la victoire :

- Le mod retient la progression des participants et enregistre **le meilleur rang obtenu**.
- Il attribue les avancements **Héros légendaire I à V** jusqu'au niveau remporté : remporter III permet d'obtenir les niveaux I, II et III si nécessaire.
- Il applique l'effet **Héros du village** du niveau correspondant avec une **durée infinie**, et le réapplique après reconnexion à partir des données persistantes du joueur.
- Un nouveau niveau inférieur ne doit **pas écraser** une récompense supérieure déjà enregistrée.

Les réductions commerciales restent dépendantes des règles de Minecraft et de la présence de villageois avec lesquels échanger. **Permanent** signifie ici que le mod conserve et réapplique la récompense ; cela ne signifie pas que chaque marchand offre des objets gratuits.

**Sources :** `DraconicRaids.afterTick/playerTick`, `DraconicRaidState.canReward`, `DraconicRaidState.Store.reward/save`, `data/ballista/advancement/legendary_hero/level_1.json` à `level_5.json`.

## 6. Œuf corrompu, cœur noir et autres objets associés

Le **dragon noir** et le **chasseur monté** constituent deux systèmes liés au combat. Ils sont distincts des nouvelles améliorations permanentes d'équipement :

- **Cœur noir** : applique jusqu'à deux stades à 18 types d'objets en diamant/netherite (armes, outils, armures). Les mécanismes incluent **vol de vie**, **réduction supplémentaire des dégâts** et **fonte automatique** activable pour la pioche. Voir [Guide 0.27.10 — section Cœur noir](GUIDE_VERSION_0_27_10.md#5-cœur-de-dragon-noir--outils-armes-et-armures).
- **Œuf noir incubable** : objet/bloc `ballista:black_dragon_egg` présentant trois aspects de texture ; distinct de l'**œuf d'apparition** noir utilisé pour invoquer directement le mob.
- **Carte de tanière illageoise** : le chasseur peut en lâcher si une tanière admissible est trouvée, mais ne garantit pas une carte à chaque mort.
- **Chasseur illageois** : une entité spécifique, pas une simple réutilisation du chasseur de dragons villageois.

## 7. Périmètre de validation

La documentation s'appuie sur le **JAR réellement fourni**, notamment le bytecode des classes citées et les traductions FR/EN. Les paramètres programmés sont identifiés précisément. Aucune partie Minecraft n'a été lancée pour mesurer les combats ni tester la compatibilité de la monture sur les cinq implémentations du bundle.

Les explications essentielles sont intégrées directement dans ces pages destinées aux joueurs.
