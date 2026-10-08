# Dragons et Bastions — Wiki de la version **0.27.12-candidate**

> **Fichier inspecté :** `ballista-fabric-0.27.12-candidate+mc26.1-26.3-test.jar` · **Fabric**, Java **25+**, Fabric Loader **0.19.3+**, Fabric API · Minecraft Java **26.1 / 26.1.1 / 26.1.2 / 26.2 / 26.3**, **pour CE paquet seulement**. Ne pas en déduire que tous les autres JAR de Dragons et Bastions exigent les mêmes versions. **Build candidate de test : mécaniques vérifiées statiquement, pas en jeu.**

[← Accueil](README.md) · [Recettes 32/32](RECETTES_VERSION_0_27_12.md) · [Guide du dragon noir et des raids](DRAGON_NOIR_ET_RAIDS.md) · [Audit](ANALYSE_JAR_0_27_12.md)

## 1. Installer et distinguer les versions

Le JAR externe porte le mod-id `ballista_bundle` et embarque **cinq JAR internes** (`ballista`) correspondant aux cinq versions Minecraft 26.x indiquées. Il ne faut **pas** extraire les cinq fichiers ni les installer tous côte à côte. Le nom public du projet est **Dragons et Bastions** ; le mod-id technique principal intégré est `ballista` (« Baliste »). Cette disposition n'a pas été testée en lancement réel : vérifiez le chargement sous Fabric et l'absence de mod `ballista` dupliqué. **Sauvegardez votre monde** avant un essai.

Le fichier transmis ne permet pas de valider les versions Minecraft 1.21.x : elles nécessitent leurs propres JAR à auditer. `candidate` et `test` doivent rester visibles dans la documentation, même si un utilisateur peut essayer la version.

## 2. Dragons et élevage

Le code et les traductions comprennent **quatre couleurs** : rouge (`red_dragon`, feu), verte (`green_dragon`, poison), bleue (`blue_dragon`, glace) et **noire** (`black_dragon`, corrompue). Les œufs (y compris l'œuf noir), les œufs d'apparition, les armures, les selles et le développement des dragons sont présents. Le mod gère :

- l'incubation, l'éclosion, l'apprivoisement, la croissance et la gestion de la famille/ponte ;
- les ordres suivre, garde, patrouille, promenade, retour et contrôle du dragon ;
- les inventaires de transport, la selle, les armures et les informations propriétaire/parent/âge/œuf ;
- les capacités liées à la couleur (souffles, projectile, mobilité et plongeon) ;
- les tanières, leurs thèmes de terrain et l'aménagement par un dragon.

Le [guide historique des dragons](DRAGONS.md) expose les bases de l'incubation et du dressage ; les spécificités du [dragon noir et des cœurs](DRAGON_NOIR_ET_RAIDS.md) restent documentées à part. Les mécanismes sont implémentés en Java, pas tous décrits par les JSON.

## 3. Dragon noir **monté par un chasseur illageois**

Le dragon noir est bien une entité de dragon. Le chasseur (`ballista:illager_dragon_hunter`) est une entité illageoise distincte. La classe `DraconicRaids` contient des tentatives explicites de monte (`startRidingExtended` si disponible, sinon `startRiding`) ; il ne s'agit donc **pas** simplement de deux entités générées à côté l'une de l'autre. Le spawn dépend des règles, de la place et du déroulement du raid. Cela doit être confirmé visuellement en jeu.

[Consulter le guide complet du dragon noir, des raids et des cœurs](DRAGON_NOIR_ET_RAIDS.md).

## 4. Fioles de mauvais présage draconique, raids et récompenses

Il existe **cinq objets consommables**, `ballista:draconic_omen_1` à `_5`. Ils déclenchent une logique de raid draconique avec paramètres différents selon le rang ; la gestion complète réside dans `DraconicOmenItem` et `upgrade/DraconicRaids`. Les cinq avancements `legendary_hero/level_1` à `level_5` existent. Leur condition `minecraft:impossible` signifie qu'ils sont **accordés par le code** lors de la victoire, et non par une action générique Minecraft. Les récompenses et remises associées sont détaillées dans le [guide existant](DRAGON_NOIR_ET_RAIDS.md).

## 5. Balistes et défenses

Le mod contient les balistes **légère, moyenne et lourde**, les carreaux/amorçes, plusieurs tables d'archerie, les pieux en bois et en fer, les épaves réparables et le ravitaillement automatique. Les classes `BallistaEntity`, `BallistaSupply`, `BallistaSupplyNetwork` et leurs variantes contrôlent les attaques, réserves et systèmes de réseau. Les trois effets personnalisés **Fissure**, **Choc acoustique** et **Saut interdit** figurent dans les données/traductions ; des dégâts perforants et des flammes sont également implémentés.

Les **29 recettes illustrées historiques** du [README](README.md) concernent la version 0.27.1 ; reportez-vous à la liste **32/32 vérifiée dans ce JAR** pour les fabrications de la version candidate. Aucun équilibrage chiffré repris d'une ancienne version ne doit être attribué à 0.27.12 sans vérification correspondante.

## 6. Nouveau bloc : tas d'ossements

Le **tas d'ossements** (`ballista:bone_pile`) est un élément de tanière construit avec un **modèle de 82 pièces en relief** : il n'est pas un cube compact à six faces. Son modèle utilise une texture d'os carbonisé propre au mod et une texture de squelette Minecraft. Le bloc est **traversable** selon la forme de collision vide, peut produire un son de pas de squelette lorsque l'on bouge à l'intérieur, et **rapporte 7 os** à la casse normale. Pas de recette de craft JSON directe dans ce JAR.

[Voir tous les détails et les ressources visuelles réelles](BLOCS_ET_MECANIQUES_0_27_12.md).

## 7. Nouveau bloc : nasse à poissons

La **nasse** (`ballista:fish_trap`) possède un inventaire de cinq emplacements (1 appât : **graines de blé** ; 4 sorties : **poissons**), une recette 3×3, une orientation et un affichage de prise. Elle doit être remplie d'eau et avoir une case d'eau devant elle ; le délai théorique pour une capture est **120 à 240 secondes**, sous réserve d'une place disponible. Le code sélectionne cabillaud/saumon/poisson tropical/poisson-globe selon le biome et le hasard.

[Guide d'installation, recette et fonctionnement](BLOCS_ET_MECANIQUES_0_27_12.md).

## 8. Enchantement **Savoir I–III**

`ballista:savoir` est **actif par Java/mixins**, même si son JSON indique `effects: {}`. Il attire les orbes d'XP sur une portée calculée `8 + 2 × niveaux cumulés` blocs et ajoute théoriquement **10 % d'XP par rang cumulé**, avec conservation des dixièmes entre gains. Le code adapte également des offres de bibliothécaires. Les objets autorisés sont listés dans [sa fiche précise](ENCHANTEMENT_SAVOIR_0_27_12.md).

## 9. Dangers nocturnes et invasion zombie

`NightThreats` implémente un danger nocturne dans l'Overworld, conditionné par la difficulté (hors Paisible) et les règles de génération des monstres. Une **invasion zombie** peut être déclenchée pour un joueur éligible au cours de la nuit, avec barre de progression et vagues de **20 ou 40 zombies**, jusqu'à **200 au total** si la partie se déroule jusqu'au bout. Le code prévoit aussi des apparitions distinctes de zombies, squelettes, araignées et creepers. La probabilité d'invasion dépend notamment d'un tirage `nextInt(4)`, mais les conditions de distance, de zone et de monde peuvent l'empêcher : il ne faut pas promettre un raid toutes les quatre nuits.

## 10. Tanières, camps illageois et expéditions

Le JAR contient **23 fichiers NBT de structure** et **3 ensembles de placement de structure** ; certains incluent plusieurs variantes selon terrain. Les tanières de montagne rouge, verte et bleue, les grandes cavernes et les camps illageois ont leurs données JSON/NBT. Les classes `IllagerExpeditions`, `CampAlarm`, `CampPrisonRules`, `LairRules`, `DomesticLairs`, `MountainLairs`, `LairScars` et `EggRules` pilotent en plus des comportements conditionnels au chargement des zones.

[Liste exacte des structures et tables de butin](STRUCTURES_BUTIN_0_27_12.md).

## 11. Cœurs draconiques et amélioration d'équipement

La liste de recettes inclut les recettes spéciales de **cœur de dragon**, **cœur de dragon gelé** et **cœur de dragon noir** ; ces recettes utilisent des types `ballista:*` personnalisés et **ne sont pas des recettes en grille normale**. Le code comprend des règles d'amélioration du combat, d'armure et d'outils. Pour la description des paliers et interactions déjà documentés, voir [Dragon noir et raids](DRAGON_NOIR_ET_RAIDS.md) ; les coûts doivent être contrôlés sur la version installée.

## 12. Liste exacte des recettes, contenus et contrôles

- **32 recettes** (`29` historiques + `3` ajoutées au fil des versions, dont la nasse), avec les recettes spéciales distinguées : [liste complète](RECETTES_VERSION_0_27_12.md).
- **33 avancements JSON**, dont cinq « Héros légendaire ».
- **28 tables de butin**, **23 structures NBT**, **16 ressources de worldgen**.
- **90 PNG et 2 fichiers de traduction** (`fr_fr`, `en_us`) de 160 entrées chacun.
- **1 enchantement JSON** propre au mod (`savoir`).
- [Index des objets, blocs, entités, enchantements et effets](INDEX_CONTENU_0_27_12.md) · [Audit détaillé et limites](ANALYSE_JAR_0_27_12.md).

**Limite importante :** ces chiffres proviennent du module 26.3 du paquet audité ; le nombre de classes diffère légèrement selon la version Minecraft. La conformité au format JSON et la présence du bytecode **ne prouvent pas que toutes les fonctionnalités fonctionnent sans erreur dans le jeu**.
