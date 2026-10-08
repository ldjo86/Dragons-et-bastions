# Dragons et Bastions — Guide de la version 0.27.10-candidate

> **🆕 Wiki 0.27.12-candidate (JAR analysé le 08/10/2026) :** [guide complet](GUIDE_VERSION_0_27_12.md) · [32 recettes](RECETTES_VERSION_0_27_12.md) · [tas d'ossements et nasse](BLOCS_ET_MECANIQUES_0_27_12.md) · [Savoir I–III](ENCHANTEMENT_SAVOIR_0_27_12.md) · [audit technique](ANALYSE_JAR_0_27_12.md). Les explications historiques ci-dessous concernent des JAR plus anciens et ne remplacent pas le guide 0.27.12.

> **Source vérifiée :** ballista-fabric-0.27.10-candidate+mc26.1-26.3-test.jar, analysé le 8 octobre 2026. Ce guide concerne **Dragons et Bastions / Baliste** (identifiant Fabric *ballista*), **pas Realms Reforged**. Il s'agit d'une **version candidate de test**, pas d'une validation de stabilité en jeu.
>
> **Navigation :** [Wiki et recettes illustrées](README.md) · [Dragons : guide historique](DRAGONS.md) · [Recettes](RECETTES.md) · [Inventaire du JAR](CONTENU_DU_JAR.md) · [Version HTML](site/maj-0-27-10.html) · [Dragon noir et fioles](DRAGON_NOIR_ET_RAIDS.md)

## 1. Compatibilité et contenu exact du paquet

L'archive extérieure est un **bundle Fabric**, identifiant **ballista_bundle**, version **0.27.10-candidate**, nom **Dragons et Bastions**. Elle charge des implémentations internes du mod **ballista**, une seule devant correspondre à la version exacte de Minecraft.

| Minecraft Java | Archive interne | Classes Java compilées | Recettes | Tables de butin | PNG |
|---|---|---:|---:|---:|---:|
| 26.1 | ballista-fabric-0.27.10-candidate+mc26.1.jar | 201 | 31 | 25 | 89 |
| 26.1.1 | ballista-fabric-0.27.10-candidate+mc26.1.1.jar | 201 | 31 | 25 | 89 |
| 26.1.2 | ballista-fabric-0.27.10-candidate+mc26.1.2.jar | 201 | 31 | 25 | 89 |
| 26.2 | ballista-fabric-0.27.10-candidate+mc26.2.jar | 200 | 31 | 25 | 89 |
| 26.3 | ballista-fabric-0.27.10-candidate+mc26.3.jar | 202 | 31 | 25 | 89 |

- Fabric Loader **0.19.3 minimum**, Java **25 minimum**, **Fabric API** requis.
- Les implémentations internes portent le même identifiant *ballista* et ciblent chacune **une seule version Minecraft** ; le bundle n'est ni un mod Forge/NeoForge, ni un addon Bedrock.
- Les 31 recettes comprennent **29 entrées héritées** et **2 recettes personnalisées ajoutées** (cœur gelé et cœur noir). Les 29 schémas illustrés de l'ancien wiki restent utiles pour les fabrications classiques ; les 2 nouvelles entrées ne sont **pas** des recettes 3×3.
- Les 258 fichiers JSON de la variante 26.3 ont été décodés sans erreur de syntaxe. Les tests de chargement, jeu multijoueur, générations de structures et forge restent à effectuer dans Minecraft.

**Sources internes :** manifestes fabric.mod.json de l'enveloppe et de chacun des cinq JAR, data/ballista/recipe/, data/ballista/loot_table/.

## 2. Les quatre dragons, leurs œufs et leurs cœurs

| Dragon | Identifiant de l'entité | Œuf incubable | Cœur spécifique |
|---|---|---|---|
| Rouge | ballista:red_dragon | ballista:red_dragon_egg | Cœur de dragon classique |
| Vert | ballista:green_dragon | ballista:green_dragon_egg | Cœur de dragon classique |
| Bleu | ballista:blue_dragon | ballista:blue_dragon_egg | **Cœur de dragon gelé** |
| Noir / corrompu | ballista:black_dragon | ballista:black_dragon_egg | **Cœur de dragon noir** |

Les **œufs incubables** sont des blocs distincts des **œufs d'apparition** utilisables en créatif. Le JAR fournit trois étapes de textures pour chacun des quatre œufs (suffixes _0, _1, _2), les textures des quatre dragons et des variantes de rendu liées à leur état.

Le dragon noir utilise des règles de **faction corrompue** spécifiques. Il ne faut donc pas supposer qu'un dragon noir hostile rencontré dans le monde se comporte exactement comme une monture rouge, verte ou bleue apprivoisée.

À sa mort, un dragon non nouveau-né lâche un cœur choisi en fonction de sa couleur : **noir → cœur noir**, **bleu → cœur gelé**, **rouge/vert → cœur classique**. Un dragon adulte peut également laisser un œuf de sa couleur ; les écailles sont également gérées par son code de butin. Ce comportement est lu dans la méthode de butin de *SiegeDragon*, indépendamment des tables de butin JSON des trois anciens dragons.

**Sources internes :** SiegeDragons.register, DragonColor, DragonEggs, SiegeDragon.dropCustomDeathLoot, FrozenHeartRules.heart, CorruptedRules, assets/ballista/textures/.

## 3. Ponte et cycle familial — nouveauté importante

Le code de reproduction distingue **deux minuteries d'un dragon adulte** :

| État du dragon | Intervalle de ponte du code | À 20 ticks/s |
|---|---:|---:|
| Sauvage / non domestiqué | 36 000 ticks | **30 minutes** |
| Domestiqué | 144 000 ticks | **2 heures** |

Le compteur n'avance pas chez les bébés/adolescents et évolue pendant la simulation active du monde. L'échéance n'est **pas** une garantie de ponte immédiate : la remise ou la pose de l'œuf dépend de vérifications de position, de propriétaire, d'ordre et d'espace disponible. Pour les dragons apprivoisés, le code de remise vérifie notamment la proximité du propriétaire (distance de 8 blocs lors de la vérification correspondante).

La famille ne se limite plus à un compteur : les classes *FamilyRules* et *EggRules* relient le parent, le jeune dragon, le suivi familial, la remise des œufs et la reprise de certaines tâches. La commande « Informations du dragon » permet de consulter **propriétaire, parent, ordre, tanière et prochaine ponte**. Il existe également une information contextuelle sur la **chaleur et la progression de l'œuf**.

**Attention :** ces 30 minutes / 2 heures désignent la **ponte d'un adulte**, et non les durées d'incubation ou de croissance. Les durées d'incubation de l'ancien guide ne doivent pas être confondues avec cette nouvelle minuterie.

**Sources internes :** EggCycle.interval/advance/due, EggRules.tick, FamilyRules, DragonInformation, EggDetails, lang/fr_fr.json.

## 4. Cœur de dragon gelé — amélioration d'armure

Le mod enregistre une **recette spéciale de forge** de type **ballista:frozen_dragon_heart** ; sa base doit correspondre au tag Minecraft **#minecraft:enchantable/armor**. Il ne s'agit pas d'un nouveau motif de table de craft.

- **Premier palier : 4 niveaux d'expérience**.
- **Second palier : 12 niveaux d'expérience**, avec des conditions plus strictes : armure en **netherite**, premier palier/provenance diamant enregistré et second palier pas encore appliqué.
- Le code utilise des composants persistants sur l'objet, ajoute des modificateurs d'armure et prévoit des **bonus d'enchantements** associés au cœur gelé.
- Les vérifications de niveau à la récupération du résultat et au transfert rapide sont traitées par les mixins de forge ; les joueurs créatifs peuvent contourner les coûts.

On ne doit **pas** annoncer un bonus universel identique sur n'importe quel objet : le type exact de pièce, son matériau et son historique d'amélioration modifient l'éligibilité et le résultat. La protection réelle et les interactions avec les autres enchantements nécessitent un test en jeu.

**Sources internes :** data/ballista/recipe/frozen_dragon_heart.json, FrozenHeartRecipe, FrozenHeartRules.canApply/cost/apply/pay, HiddenHeartEnchantments, FrozenPaymentMixin et FrozenQuickMoveMixin.

## 5. Cœur de dragon noir — outils, armes et armures

La recette spéciale de forge **ballista:black_dragon_heart** accepte les objets listés dans **#ballista:black_heart_equipment** :

- Épées, haches, pioches, pelles, houes et quatre pièces d'armure **en diamant**.
- Les **neuf équivalents en netherite** (soit **18 objets précis** dans le tag).

L'objet porte un **stade de cœur noir** (I puis II). Le deuxième stade demande une évolution vers la **netherite** et la preuve enregistrée d'une application antérieure sur **diamant** : ce n'est pas une répétition infinie du même craft sur n'importe quelle armure.

**Effets relevés dans le code :**

- **Armure** : la fonction de réduction multiplie les dégâts par *1 − 0,05 × min(8, total des stades équipés)*. Cela correspond au maximum théorique à **40 % de réduction supplémentaire** dans cette fonction avec 8 stades cumulés, avant les autres règles du jeu. Ce plafond ne garantit pas un résultat identique face à toutes les sources de dégâts.
- **Armes** : un mécanisme de **vol de vie** existe, borné par la formule *0,1 × min(2, stade) × dégâts effectivement infligés*.
- **Pioche** : une option de **fonte automatique** existe. Pour l'activer/désactiver, **tenir la pioche au cœur noir en main principale, s'accroupir et utiliser l'objet** : un message indique l'état. Les drops concernés dépendent de la logique de récolte, des types de blocs et des protections anti-duplication.

Le traitement des blocs posés par les joueurs, des pistons, des chutes, des cultures et des blocs appartenant aux tanières fait l'objet de vérifications spécifiques. Ne pas décrire la fonte automatique comme une duplication ou comme un effet appliqué à tous les objets du monde.

**Sources internes :** data/ballista/recipe/black_dragon_heart.json, tags/item/black_heart_equipment.json, BlackHeartRecipe, BlackHeartRules.canApply/reduced/stolen/toggle, BlackHarvestRules, mixins BlackCombat/BlackLoot/BlackToggle/BlackPiston.

## 6. Tanières, grandes cavernes et géographie

Le JAR inclut des **structures Minecraft 26.x** dédiées, avec plusieurs variantes par couleur.

| Ensemble de génération | Structures | Spacing / separation déclarés |
|---|---|---|
| Antres de montagne | mountain_lair_red, mountain_lair_green, mountain_lair_blue | **28 / 8** |
| Grandes cavernes | large_dragon_lair | **40 / 12** |
| Tanières de pillards | pillager_den | **28 / 8** |

Les fichiers d'antres de montagne prévoient des **variantes de relief**, dont falaises, arches, aiguilles, cirques et cratères. Les biomes sont filtrés par des tags : le **bleu** est surtout associé aux zones froides/montagneuses, le **vert** aux zones boisées, le **rouge** aux zones sèches ou escarpées. Les structures et tables de butin disposent de thèmes selon la couleur.

Les paramètres « spacing » et « separation » sont des **paramètres de placement**, **pas** des distances garanties entre deux structures visibles. La génération n'est pas rétroactive dans les chunks déjà explorés, sauf mécanisme distinct prévu par le mod.

Les tanières peuvent intégrer du **terrain excavé**, des **minerais préservés ou déplacés**, des **dragons gardiens**, et des **slimes liés aux tanières**, selon les règles et conditions de placement. Le code comprend des contrôles destinés à éviter certains volumes construits ou protégés ; cela ne constitue pas une garantie absolue de protection pour tous les mods de claims.

**Sources internes :** data/ballista/worldgen/structure/, structure_set/, template_pool/, tags/worldgen/, structure/*.nbt, LairRules, LairThemes, MountainLairs, DragonLairTerrain, LairSlimes, LairSpawnMixin.

## 7. Construire une tanière avec son dragon

Un nouvel ensemble de commandes permet à un **dragon apprivoisé et adulte** de **créer sa tanière** ou de **retourner à une tanière**. L'interface prévoit un **aperçu de construction** avec rotation et hauteur réglables :

- « Aménager une tanière » : lance une demande de construction.
- « Retourner à la tanière » : ordonne le retour.
- Dans l'aperçu, les clics règlent la **rotation**, la molette ajuste la **hauteur**, une touche autre que le déplacement confirme et **Échap** annule.
- Un emplacement trop risqué ou inadapté peut être refusé (relief insuffisant, obstacles, construction à protéger, autre tâche en cours).
- L'exécution se poursuit progressivement, avec des données d'avancement conservées par le dragon ; charger les zones concernées et protéger la zone de chantier restent importants.

Le système de génération naturelle et le système de construction par un dragon sont **distincts**.

**Sources internes :** DomesticLairs.valid/start/command/tick, DragonCommandRequest, LairPreview, MountainLairs, lang/fr_fr.json.

## 8. Chasseurs illageois, camps et alarmes

La variante contient désormais une entité **ballista:illager_dragon_hunter**, dotée d'une configuration d'équipement et d'attaque spécifique, distincte du **chasseur de dragons villageois** existant.

Les **tanières de pillards** sont des structures de génération à part entière (deux modèles principaux dans le JAR), avec leurs propres coffres **pillager_den** et **pillager_den_tower**. Le code prévoit une **alerte de camp**, des gardes, des relations d'hostilité et des contrôles liés aux zones de prison/camp.

Les trésors possibles comprennent notamment arbalètes, émeraudes, diamants et ressources rares, suivant la table de butin correspondante : **aucun objet n'est garanti à chaque coffre**.

**Sources internes :** IllagerDragonHunter, HunterRules, CampAlarm, CampPrisonRules, CorruptedRules, worldgen/structure/pillager_den.json, structure/taniere_pillards_*.nbt, loot_table/chests/pillager_den*.json.

## 9. FIOLES DE MAUVAIS PRÉSAGE DRACONIQUE et chasseur monté

![Présage I](site/generated/icons/draconic_omen_1.png) ![Présage II](site/generated/icons/draconic_omen_2.png) ![Présage III](site/generated/icons/draconic_omen_3.png) ![Présage IV](site/generated/icons/draconic_omen_4.png) ![Présage V](site/generated/icons/draconic_omen_5.png)

Le mod enregistre cinq fioles à boire (`ballista:draconic_omen_1` à `ballista:draconic_omen_5`). Leur utilisation dure **32 ticks** (1,6 seconde) et applique **Mauvais présage I à V** pendant **120 000 ticks**, soit **100 minutes** à 20 TPS. L'ancien Mauvais présage est retiré, puis l'effet de la fiole est appliqué. Le contenant rendu est une bouteille de verre ordinaire.

**L'effet de potion est le même pour les cinq fioles : Mauvais présage.** Leur niveau détermine la puissance du présage, la composition du renfort et la récompense du raid. Elles ne confèrent pas cinq effets élémentaires distincts.

Le jeu **déploie les renforts draconiques à la dernière vague** du raid de village, et non à chaque vague :

| Niveau de fiole | Dragons noirs de la dernière vague | Chasseur de dragons illageois monté | Progression récompensée |
|---|---|---|---|
| **I** | **1 adolescent** (60 PV de base) | Non | Héros légendaire I |
| **II** | **1 adolescent** (60 PV de base) | Non | Héros légendaire II |
| **III** | **1 adulte** (120 PV de base) | **Oui, un chasseur sur ce dragon** | Héros légendaire III |
| **IV** | **3 adultes** | **Oui, un seul sur le premier dragon** | Héros légendaire IV |
| **V** | **3 adultes** | **Oui, un seul sur le premier dragon** | Héros légendaire V |

### Un vrai dragon noir monté par un illageois

À partir du niveau **III**, `DraconicRaids.spawn` équipe le **premier dragon noir** d'une **selle draconique**, crée un **`ballista:illager_dragon_hunter`**, l'équipe, puis utilise `DraconicRaids.ride` (appel `startRiding`) pour le faire **monter sur le dragon**. La routine de raid synchronise ensuite la cible du dragon avec celle de son passager ; le dragon conserve son autonomie.

Le chasseur illageois possède **60 PV de base**, une **armure complète en diamant** et un **bâton draconique**. Ce dernier permet une attaque à distance par **boules de feu**, lorsque la cible est à environ **3 à 24 blocs** et dans sa ligne de vue, avec **60 ticks** de recharge entre deux tirs validés. Son code de butin dépose **un cœur noir** et peut produire **une ou deux cartes de tanière illageoise** si des structures correspondantes sont repérées.

À partir de **IV**, les deux dragons noirs supplémentaires ne transportent pas de chasseur dans cette fonction. Le nombre et l'âge des dragons sont des **valeurs programmées**, soumis au chargement des chunks, aux emplacements libres, aux restrictions du monde et à la réussite du montage.

### Victoire et récompenses

Le code attend la **victoire du raid vanilla** et l'élimination de **tous les dragons supplémentaires** avant de marquer le raid achevé. Il enregistre le meilleur rang du joueur et accorde les avancements **Héros légendaire I à V** jusqu'au rang obtenu. Il applique aussi un effet **Héros du village** correspondant avec une **durée infinie**, restauré depuis les données conservées par le mod.

**Fichiers pour les joueurs :** [Guide illustré des cinq fioles](site/raids-draconiques.html) · [Dragon noir et chasseur monté](site/dragon-noir.html) · [Explications exhaustives et sources](DRAGON_NOIR_ET_RAIDS.md).

**Sources internes :** `DraconicOmenItem`, `DraconicRaids.drink/absorb/wave/ride/spawn/beforeTick/afterTick/playerTick`, `DraconicRaidState.dragons/adolescent/mounted/canReward`, `IllagerDragonHunter`, `HunterRules.combat/loot`, `DraconicRaidMixin`, avancements Héros légendaire, traductions FR/EN.

## 10. Combat et déplacement des dragons

Le code distingue les pouvoirs élémentaires : feu, glace et poison pour les couleurs associées, avec des comportements supplémentaires pour le dragon noir/corrompu. La variante bleue est reliée aux **particules de neige**, aux **effets de ralentissement** et aux règles de dégâts de gel. Les comportements de ciblage filtrent les propriétaires et alliés.

Les classes *MountedActions*, *MountedInputMixin*, *MountedScrollMixin*, *DragonMotion*, *DragonHudExtra*, *DiveRules* et *PowerRules* mettent en œuvre les commandes de monture, le **piqué**, les contrôles du souffle, les déplacements et les informations à l'écran. Les actions affichées comprennent souffle, boule de feu, piqué et souffle de glace selon le dragon et le contexte.

**Sources internes :** PowerRules, ElementalCombat, DiveRules, DragonControls, MountedActions, DragonHudExtra, LairPreview, lang/fr_fr.json.

## 11. Recettes, ressources et butin : ce qui change

Deux recettes de forge supplémentaires sont enregistrées :

| Fichier de recette | Type personnalisé | Base |
|---|---|---|
| frozen_dragon_heart.json | ballista:frozen_dragon_heart | #minecraft:enchantable/armor |
| black_dragon_heart.json | ballista:black_dragon_heart | #ballista:black_heart_equipment |

Le JAR comporte **25 tables de butin**, dont celles des trois dragons classiques, du chasseur, des blocs, des grandes cavernes, des antres par couleur et des camps illageois. Les **cavernes de gemmes/reliques** peuvent contenir des ressources rares, y compris, selon leurs pools, des pommes dorées enchantées, totems ou modèles de forge en netherite.

Les modèles d'icônes, variantes de dragons et cartes d'antres sont présents dans les ressources du JAR, y compris les objets **frozen_dragon_heart**, **black_dragon_heart** et **draconic_omen_1** à **draconic_omen_5**. Ces textures réelles devront être intégrées au catalogue visuel du site ; ne pas leur substituer des captures inventées.

**Sources internes :** data/ballista/recipe/, loot_table/, assets/ballista/textures/, lang/fr_fr.json.

## 12. Aide et limites de cette version candidate

- **Mon dragon ne pond pas :** vérifier l'âge adulte, la progression en ticks chargés, l'ordre, la proximité du propriétaire et la disponibilité de la zone de remise. Un timer atteint n'oblige pas à produire un œuf si les autres conditions échouent.
- **Le cœur gelé n'apparaît pas en résultat :** utiliser la **table de forge**, une armure admissible, puis vérifier les conditions du second palier et les niveaux d'expérience (4 ou 12).
- **Le deuxième cœur noir échoue :** l'historique de passage **diamant → netherite** conditionne la progression.
- **La pioche ne fond rien :** vérifier qu'elle porte un cœur noir et que la fonte est **activée** par interaction accroupie.
- **Aucune structure dans les vieux chunks :** explorer de nouveaux chunks et vérifier les tags de biome.
- **Les commandes de tanière échouent :** éviter les blocs de constructions protégées, choisir un terrain naturel adapté, dégager la zone et vérifier la propriété/l'état du dragon.
- **Les images du wiki :** l'ancienne galerie illustre les 29 recettes antérieures ; les nouvelles recettes de cœur sont des **améliorations de forge**.
- **Compatibilité :** ces fichiers sont **Java / Fabric** uniquement ; Minecraft 1.21.x et Bedrock ne sont pas inclus dans cette archive de test.

### Vérifications effectuées / à effectuer

**Contrôles effectués :** inspection des six archives (bundle + cinq JAR), manifestes, contenu des 31 recettes, 25 tables de butin et des ressources, vérification syntaxique des JSON, lecture ciblée du bytecode (notamment les règles de ponte, de forge, de dégâts, de raids et de tanières).

**Tests non effectués :** lancement Minecraft, génération réelle de tous les antres, stabilité serveur, vérification des mixins sur chacune des cinq versions, comportement du multijoueur, fiabilité de tous les crafts en situation, compatibilité intermods. La présence de code ne prouve pas à elle seule son bon fonctionnement pendant une partie.

### À propos de Realms Reforged

Ce wiki est exclusivement celui de **Dragons et Bastions**. Son lien ne doit **pas** servir de lien « wiki » pour Realms Reforged sur CurseForge. Realms Reforged nécessite une documentation différente, fondée sur **son propre JAR**, en particulier pour expliquer ses enchantements.
