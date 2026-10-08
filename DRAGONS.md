# Dragons : de l'œuf à la monture

> **🆕 Wiki 0.27.12-candidate (JAR analysé le 08/10/2026) :** [guide complet](GUIDE_VERSION_0_27_12.md) · [32 recettes](RECETTES_VERSION_0_27_12.md) · [tas d'ossements et nasse](BLOCS_ET_MECANIQUES_0_27_12.md) · [Savoir I–III](ENCHANTEMENT_SAVOIR_0_27_12.md) · [audit technique](ANALYSE_JAR_0_27_12.md). Les explications historiques ci-dessous concernent des JAR plus anciens et ne remplacent pas le guide 0.27.12.

**Guide historique basé sur `ballista-fabric-0.27.1+mc26.2.jar`.** La version 0.27.10 ajoute le dragon noir, la ponte périodique, les tanières domestiques et les raids draconiques. Lire le **[complément 0.27.10](GUIDE_VERSION_0_27_10.md)** avant de se fier aux anciennes descriptions. Ce guide décrit les règles lues dans les ressources et le code compilé de ce fichier, sans modification du mod. Les essais en jeu restent à effectuer. Un datapack ou un autre mod peut modifier les règles et les ingrédients.

## Le parcours à suivre

Récupérer un œuf de dragon coloré → préparer un endroit chaud et dégagé → rester près de l'éclosion pour devenir son propriétaire → nourrir le bébé → nourrir l'adolescent → équiper le dragon adulte.

**Attention à la durée :** le compteur de croissance de 48 000 ticks est utilisé deux fois. Il faut environ **40 minutes pour l'incubation**, puis **40 minutes de bébé à adolescent**, puis **40 minutes d'adolescent à adulte**. Soit environ **2 heures de simulation active depuis la pose de l'œuf**, à 20 ticks par seconde, sans pause de chaleur, de nourriture ou de place disponible.

## 1. Obtenir le bon œuf

Le mod possède trois œufs à poser :

| Œuf | Identifiant | Dragon obtenu |
|---|---|---|
| Œuf rouge | `ballista:red_dragon_egg` | Dragon rouge |
| Œuf vert | `ballista:green_dragon_egg` | Dragon vert |
| Œuf bleu | `ballista:blue_dragon_egg` | Dragon bleu |

La génération d'antres peut placer ces œufs dans le monde. Récupère un œuf posé, puis transporte-le vers ton installation d'élevage. La table de butin de chacun de ces blocs rend l'œuf correspondant, sans condition Toucher de soie. Ne confonds pas ces blocs avec les **œufs d'apparition** `*_dragon_spawn_egg`, qui ne suivent pas ce parcours d'incubation, ni avec l'œuf vanilla de l'Ender Dragon.

Aucune des 29 recettes du JAR ne fabrique un œuf à incuber. Ne compte donc pas sur une recette de table de craft pour en obtenir un.

**Déplacement :** le temps d'incubation est enregistré dans le bloc posé. Sa table de butin ne copie pas ce compteur dans l'objet récupéré : casser puis reposer l'œuf ne conserve pas sa progression.

## 2. Construire un endroit pour l'incubation

Les **trois couleurs** utilisent la même règle de chaleur dans cette version, y compris le dragon bleu.

Il faut au moins un **bloc de magma** ou un **bloc de lave** à une distance maximale de **3 blocs** de l'œuf. Le code vérifie une distance dans les trois dimensions, pas seulement l'appartenance à un cube de 7 × 7 × 7 blocs. Une source située en diagonale peut donc être trop éloignée.

Une disposition simple consiste à placer du magma sous un bloc de sol plein, puis l'œuf au-dessus : la distance entre l'œuf et le magma est alors de deux blocs. Cette disposition est proposée pour garder la source de chaleur hors du passage ; ce n'est pas une structure spéciale reconnue par le mod.

Garde de l'espace libre au-dessus et autour de l'œuf. Le bébé apparaît au centre du bloc, **1,1 bloc au-dessus de sa base**, et le mod refuse l'éclosion si sa boîte de collision est bloquée.

### Ce qui ne remplace pas le magma ou la lave

Les torches, lanternes, feux de camp, fours, flammes ordinaires, la lumière du soleil et un biome chaud ne figurent pas dans le test de chaleur du JAR. L'eau et la glace ne constituent pas une condition spéciale pour l'œuf bleu.

### Conditions à maintenir

La zone doit continuer à être simulée par le serveur, la source de chaleur doit être présente et la règle de jeu d'apparition des créatures doit être activée. Le compteur est avancé par les ticks de l'entité de bloc : dormir pour changer l'heure ne remplace pas le temps de simulation requis.

La perte de chaleur **suspend** l'incubation sans effacer le compteur. Une sauvegarde puis un rechargement conservent le temps acquis si l'œuf n'a pas été cassé.

| Progression | Temps accumulé à 20 ticks/s | État visible |
|---|---:|---|
| 0 à 15 999 ticks | Début à moins de 13 min 20 s | `hatch=0` |
| 16 000 à 31 999 ticks | 13 min 20 s à moins de 26 min 40 s | `hatch=1` |
| 32 000 à 47 999 ticks | 26 min 40 s à moins de 40 min | `hatch=2` |
| 48 000 ticks | Environ 40 min | Éclosion, si toutes les conditions restent réunies |

Un œuf au stade de fissure 2 n'a donc pas nécessairement terminé son incubation. À compteur plein, une obstruction peut encore retarder la naissance.

## 3. Réussir l'apprivoisement à l'éclosion

**L'apprivoisement prévu dans ce JAR se fait à la naissance, pas en donnant de la viande à un adulte sauvage.**

Au moment de l'éclosion, le mod cherche d'abord un **dragon adulte sauvage et vivant dans un rayon de 16 blocs** autour du centre de l'œuf. S'il en trouve, le bébé se rattache au plus proche comme parent. Ce choix passe avant la recherche d'un propriétaire humain.

S'il ne trouve pas cet adulte sauvage, le mod cherche le **joueur vivant, non spectateur, le plus proche à moins de 8 blocs du point d'apparition du bébé**. Ce joueur devient le propriétaire. Le code ne mémorise pas le joueur qui avait posé l'œuf pour lui donner la priorité.

### Pour réussir

Prépare l'éclosion à l'écart des adultes sauvages. Reste à quelques blocs de l'œuf avant sa naissance, sans te tenir dans l'espace où le bébé doit apparaître. En multijoueur, assure-toi d'être le joueur éligible le plus proche. Le fait qu'un autre joueur ait posé l'œuf ne réserve pas le dragon à ce joueur.

Il n'y a pas de tirage aléatoire d'apprivoisement dans cette attribution : ce sont la présence et la proximité qui déterminent le résultat. La viande sert ensuite à nourrir le dragon lié à son propriétaire.

**Éclosion manquée :** si aucun joueur éligible n'est présent, cette attribution ne se fait pas. La méthode de nourrissage exige déjà un dragon domestiqué ; donner de la viande à un jeune sauvage ou à un adulte sauvage ne constitue pas une procédure de rattrapage dans le code examiné. Les appels du JAR à `bondTo` ont été vérifiés : l'appel d'apprivoisement se trouve dans l'éclosion.

## 4. Que lui donner à manger ?

Tiens un aliment accepté en main et utilise l'interaction sur **ton dragon**. Les aliments du tag `#ballista:dragon_meat` fourni sont :

| Famille | Aliment cru | Aliment cuit |
|---|---|---|
| Bœuf | Bœuf cru — `minecraft:beef` | Steak — `minecraft:cooked_beef` |
| Porc | Côtelette de porc crue — `minecraft:porkchop` | Côtelette de porc cuite — `minecraft:cooked_porkchop` |
| Poulet | Poulet cru — `minecraft:chicken` | Poulet cuit — `minecraft:cooked_chicken` |
| Mouton | Mouton cru — `minecraft:mutton` | Mouton cuit — `minecraft:cooked_mutton` |
| Lapin | Lapin cru — `minecraft:rabbit` | Lapin cuit — `minecraft:cooked_rabbit` |

Ces dix aliments ont **le même effet de nourrissage** dans la méthode du mod. La viande cuite n'ajoute pas plus de temps de croissance que la viande crue.

Le poisson, la chair putréfiée, les os, le blé, le pain et les pommes ne figurent pas dans ce tag fourni. Les objets du tag `dragon_valuables` sont des objets de valeur destinés à une autre mécanique, pas la liste des aliments de croissance.

### Effet d'un morceau accepté

Pour un bébé ou un adolescent domestiqué, un morceau ajoute **6 000 ticks de réserve alimentaire**, soit **5 minutes** à vitesse normale. La réserve totale est plafonnée à **48 000 ticks**, soit 40 minutes. Le morceau soigne aussi jusqu'à **6 points de vie**, soit 3 cœurs, sans dépasser la santé maximale.

Le nourrissage consomme un objet en survie et produit un son de repas et des particules de cœur. Ces particules ne constituent pas un mode de reproduction : elles sont aussi le retour visuel du repas.

**Donner la viande en main est important :** déposer des aliments dans un coffre ou les jeter par terre n'est pas la méthode qui crédite ce compteur alimentaire dans le JAR.

## 5. Le faire grandir jusqu'à l'âge adulte

| Étape | Temps de croissance nourrie | Nourriture théorique depuis une réserve vide | Santé maximale de base |
|---|---:|---:|---:|
| Bébé → adolescent | 48 000 ticks, environ 40 min | 8 morceaux acceptés | Bébé : 24 PV, soit 12 cœurs |
| Adolescent → adulte | 48 000 ticks supplémentaires, environ 40 min | 8 morceaux supplémentaires | Adolescent : 60 PV, soit 30 cœurs |
| Adulte | Croissance terminée | La viande sert aux soins | 120 PV, soit 60 cœurs |

Prévois donc **16 morceaux au minimum pour toute la croissance d'un bébé domestiqué**, hors nourriture gaspillée en atteignant le plafond et repas supplémentaires destinés aux soins. Une seule réserve pleine ne couvre qu'une étape. Réapprovisionne le dragon après son passage à l'adolescence.

La nourriture ne fait pas sauter le temps : le dragon progresse d'un tick de croissance par tick de simulation et consomme simultanément un tick de réserve. À réserve vide, sa croissance **s'arrête**, puis reprend lorsqu'il est nourri. Cette règle de croissance ne lui retire pas de santé pour la seule absence de nourriture. Les jeunes sauvages suivent une branche différente : leur croissance n'est pas soumise à la réserve du propriétaire.

### La place est aussi nécessaire

Le changement de stade vérifie qu'un volume libre existe autour du dragon : environ **1,8 × 1,8 × 1,8 bloc** pour passer du bébé à l'adolescent, puis **3 × 3 × 3 blocs** pour devenir adulte. Le test est centré horizontalement sur le dragon et part de ses pieds.

Prévois un enclos nettement plus grand qu'un simple bloc ou qu'un plafond bas. Ce volume est un contrôle de collision, pas une promesse que les ailes et la silhouette entière tiennent joliment dans une pièce de cette taille. À compteur plein, le changement attend qu'il y ait assez de place.

### Pourquoi refuse-t-il un repas ?

Un jeune en pleine santé refuse le nourrissage si sa réserve dépasse **42 000 ticks**, car un repas normal dépasserait le plafond. Il n'est pas nécessaire de continuer à cliquer. S'il est blessé, la branche de soins peut encore accepter un repas et plafonner la réserve. Un adulte en pleine santé n'a plus besoin de repas de croissance.

## 6. Équiper et monter son dragon

Attends l'âge **adulte**. Dans cette version, les interactions d'équipement et de monte vérifient qu'il ne s'agit plus d'un jeune dragon et qu'il appartient au joueur.

Utilise une **selle draconique** ou une **selle draconique de transport**, pas simplement une selle vanilla. Avec l'objet en main, l'interaction équipe un emplacement encore vide. Un adulte équipé d'une selle peut ensuite être monté avec la main vide. S'accroupir pendant l'interaction ouvre l'équipement lorsque les conditions sont réunies ; évite donc de rester accroupi si ton objectif est de monter ou de nourrir directement un adulte.

Les quatre armures de dragon donnent les valeurs de protection de base suivantes : fer **8**, or **10**, diamant **14**, netherite **18**. La selle de transport donne accès à deux compartiments de **54 emplacements**, soit 108 au total. Les recettes des selles, armures et du bâton sont présentées dans la rubrique Crafts.

Les ordres disponibles comprennent **Suivre**, **Assis / Garde**, **Patrouille** et **Promenade**. Le bâton draconique sert au commandement du dragon possédé. Consulter aussi les réglages de touches du jeu : ne pas supposer une touche identique chez tous les joueurs.

## 7. Dépannage rapide

| Problème | Vérifications utiles |
|---|---|
| L'œuf ne se fissure pas | Magma ou lave à 3 blocs au plus, zone réellement simulée, apparition des créatures autorisée. Une torche ne suffit pas. |
| L'œuf est fissuré mais n'éclot pas | Stade 2 atteint dès 26 min 40 s ; attendre 40 min complètes. Vérifier aussi l'espace d'apparition. |
| Le dragon appartient à quelqu'un d'autre | C'est le joueur éligible le plus proche à la naissance qui est choisi, pas nécessairement celui qui a posé l'œuf. |
| Le bébé suit un dragon sauvage | Un adulte sauvage dans le rayon de 16 blocs a été choisi comme parent avant la recherche d'un joueur. |
| Le bébé ne grandit plus | Réserve alimentaire vide, simulation interrompue ou collision empêchant le changement de stade. |
| L'adolescent ne devient pas adulte | Il faut une deuxième période de 40 minutes nourries et assez d'espace. |
| La viande ne fonctionne pas | Bon aliment, dragon déjà domestiqué, propriétaire correct, réserve non pleine ou dragon blessé. |
| Impossible de monter | Dragon adulte, propriétaire correct, selle draconique équipée, aucun autre passager, main vide et interaction normale. |

## Sources et limites de vérification

Analyse du JAR fourni, SHA-256 : `e85ac8a4a68c773b2ab5b81c1dc7eedad2b6eee91028ebd29d8c68ab1c245b55`.

- `DragonLifeRules` : constantes et condition de croissance.
- `DragonEggBlockEntity.tick`, `saveAdditional`, `loadAdditional` : progression et persistance de l'incubation.
- `HatchingDragonEgg.isWarm`, `hatch` et ses prédicats : chaleur, collision, priorité du parent sauvage et attribution au joueur.
- `SiegeDragon.makeHatchling`, `makeAdolescent`, `tick`, `mobInteract`, `bondTo`, `applyHatchlingAttributes` : stades, nourriture, soins, propriété et équipement.
- `DragonEquipment`, `DragonEquipmentMenu` : selles, armures et inventaire.
- `DragonLairs`, `data/ballista/loot_table/blocks/*_dragon_egg.json` : œufs posés et récupération.
- `data/ballista/tags/item/dragon_meat.json` : aliments acceptés par défaut.
- `data/ballista/recipe/` : contrôle des 29 recettes présentes.

Les 118 classes ont été désassemblées pour rechercher les appels liés à l'apprivoisement et à la réserve alimentaire. **Aucun lancement de Minecraft n'a été effectué.** Les durées sont calculées à 20 ticks par seconde et peuvent être allongées par les pauses ou ralentissements du serveur.
