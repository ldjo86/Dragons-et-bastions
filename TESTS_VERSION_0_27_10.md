# Plan de vérification en jeu — Dragons et Bastions 0.27.10-candidate

Ce document accompagne le [guide 0.27.10](GUIDE_VERSION_0_27_10.md). Il explique **ce qui a été observé dans le JAR** et les **tests reproductibles qui restent à faire**, sans présenter des résultats non obtenus comme réussis.

## Environnements

Tester séparément Minecraft Java **26.1 / 26.1.1 / 26.1.2 / 26.2 / 26.3**, avec **Java 25+, Fabric Loader 0.19.3+ et Fabric API** compatible. Utiliser une sauvegarde *neuve*, puis une copie de monde existant. Tester client local et serveur dédié. Conserver les fichiers `latest.log` et, en cas de plantage, `crash-reports/`.

| ID | Scénario | Manipulation / résultat attendu à contrôler | État |
|---|---|---|---|
| C01 | Chargement des cinq versions | Sur chaque version exacte : lancer, entrer en monde, confirmer que le mod est détecté et qu'aucune exception de mixin/registre n'apparaît | ☐ Non testé |
| C02 | Recettes héritées | Vérifier les 29 recettes déjà illustrées, ingrédients, quantités et table de craft/forge | ☐ Non testé |
| C03 | Cœur gelé I | Sur une armure admissible, vérifier la recette spéciale, les **4 niveaux** et la persistance de l'amélioration | ☐ Non testé |
| C04 | Cœur gelé II | Faire évoluer la même armure du diamant à la netherite ; vérifier les **12 niveaux** et le refus des combinaisons invalides | ☐ Non testé |
| C05 | Cœur noir I–II | Vérifier sur les 18 types d'objets diamant/netherite admis, et refuser bois/pierre/fer/or | ☐ Non testé |
| C06 | Vol de vie | Sur une arme avec cœur noir, comparer points de vie avant/après plusieurs attaques aux stades I et II | ☐ Non testé |
| C07 | Protection de l'armure noire | Comparer dégâts effectivement subis à équipement équivalent, sans et avec les stades I et II | ☐ Non testé |
| C08 | Fonte automatique | Avec pioche noire en main : utiliser en s'accroupissant, constater le message d'état ; miner minerai admissible et minerai non admissible | ☐ Non testé |
| C09 | Anti-duplication / récolte | Essayer blocs posés par joueur, déplacés par piston, Fortune/Toucher de soie, inventaire plein | ☐ Non testé |
| C10 | Dragon noir | Générer ou trouver un dragon noir, vérifier IA, hostilité, animation, vie, drops, œuf de sa couleur | ☐ Non testé |
| C11 | Incubation des œufs | Poser œufs rouge/vert/bleu/noir, tester chaleur, espace libre, sauvegarde/rechargement, naissance | ☐ Non testé |
| C12 | Croissance et contrôle | Nourrir bébé et adolescent, vérifier équipement adulte, ordre de suivre/rester, monture et HUD | ☐ Non testé |
| C13 | Ponte sauvage | Sur dragon adulte, vérifier l'échéance **36 000 ticks**, emplacement valide, absence d'œuf en cas de zone bloquée | ☐ Non testé |
| C14 | Ponte apprivoisée | Vérifier **144 000 ticks**, propriétaire proche et loin, espaces refusés, comportement du monde déchargé | ☐ Non testé |
| C15 | Famille | Confirmer propriétaire/parent du dragon, ordres familiaux et reprise après reconnexion | ☐ Non testé |
| C16 | Tanière domestique | Tester rotation, hauteur, confirmation/annulation, matériaux, progression et sauvegarde | ☐ Non testé |
| C17 | Protection du terrain | Refuser une tanière sur maison joueur, près d'autres structures, en relief impossible et sur terrain protégé | ☐ Non testé |
| C18 | Structures naturelles | En monde neuf, trouver antres des trois couleurs, cavernes et tanières illageoises dans biomes prévus | ☐ Non testé |
| C19 | Butins | Ouvrir plusieurs coffres par structure, vérifier tables de butin, raretés et objets annoncés | ☐ Non testé |
| C20 | Chasseurs illageois | Tester équipement, cibles, relations avec les dragons et campements, dégâts et alarmes | ☐ Non testé |
| C21 | Raids I–V | Déclencher séparément les cinq présages, compter vagues/dragons et tester annulation/interruption | ☐ Non testé |
| C22 | Succès et réduction | Gagner chaque niveau, vérifier attribution Héros légendaire et remises commerciales après reconnexion | ☐ Non testé |
| C23 | Multijoueur | Test 2 joueurs : propriété, œufs, tanières, projectiles, équipe, raid simultané et synchronisation client/serveur | ☐ Non testé |
| C24 | Performance | Explorer des chunks neufs, surveiller TPS, entités et générations lors de plusieurs tanières et raids | ☐ Non testé |
| C25 | Traductions | Vérifier en français et anglais les noms de cœur/œuf, accents, infobulles, messages et interfaces | ☐ Non testé |

## Problèmes de documentation à éviter

- **0.27.1 et 0.27.10 ne sont pas interchangeables :** les visuels des 29 recettes historiques restent utiles, mais 0.27.10 apporte deux recettes personnalisées de forge.
- **Une texture présente ne garantit pas un objet obtenable en survie** : vérifier la recette, le drop ou la commande correspondante.
- **Une méthode de raid ou de tanière présente dans le code ne garantit pas un événement réussi** : vérifier les conditions du monde et les chargements de chunks.
- **Les paramètres de placement des structures ne sont pas des distances garanties**.
- **Les taux théoriques de réduction/vol de vie ne sont pas forcément les résultats bruts de combat** : l'armure, les protections et les autres événements peuvent intervenir.
- **Mod Java/Fabric, pas Bedrock ni Forge**.

## Comment documenter les résultats

Pour chaque test, enregistrer : version précise de Minecraft, version Fabric API/Loader, solo/serveur, commandes de préparation, nombre d'essais, résultat, et captures ou extraits de `latest.log`. Cocher uniquement les tests réellement exécutés. La présence d'une classe, d'une recette ou d'un JSON n'est **pas** un test en jeu.

## Références

- [Wiki principal](README.md)
- [Fonctionnalités détaillées du JAR 0.27.10](GUIDE_VERSION_0_27_10.md)
- [Page web des nouveautés](site/maj-0-27-10.html)
