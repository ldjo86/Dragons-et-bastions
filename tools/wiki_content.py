"""Texte français vérifié dans le JAR 0.27.1+mc26.2. Pas de modification du mod."""
NAMES = {
'ballista':'Baliste lourde','medium_ballista':'Baliste moyenne','light_ballista':'Baliste légère',
'bolt_primer':'Amorce de carreau','dragon_scale':'Écaille de dragon','dragon_heart':'Cœur de dragon',
'dragon_saddle':'Selle draconique','dragon_pack_saddle':'Selle draconique de transport',
'draconic_staff':'Bâton draconique','draconic_whistle':'Sifflet draconique',
'iron_dragon_armor':'Armure de dragon en fer','gold_dragon_armor':'Armure de dragon en or',
'diamond_dragon_armor':'Armure de dragon en diamant','netherite_dragon_armor':'Armure de dragon en netherite',
'scale_helmet_lining':'Renfort de casque en écailles','scale_chest_lining':'Renfort de plastron en écailles',
'scale_leggings_lining':'Renfort de jambières en écailles','scale_boots_lining':'Renfort de bottes en écailles',
'dragon_hunter_table':'Table de chasse draconique','obsidian_fletching_table':"Table d’archerie en obsidienne",
'infernal_fletching_table':"Table d’archerie infernale",'echo_fletching_table':"Table d’archerie des profondeurs",
'wooden_spikes':'Pieux en bois','iron_spikes':'Pieux renforcés en fer',
'heavy_ballista_wreck':'Baliste lourde endommagée','medium_ballista_wreck':'Baliste moyenne endommagée',
'light_ballista_wreck':'Baliste légère endommagée',
'red_dragon_egg':'Œuf de dragon rouge','green_dragon_egg':'Œuf de dragon vert','blue_dragon_egg':'Œuf de dragon bleu',
'red_dragon_spawn_egg':"Œuf d’apparition de dragon rouge",'green_dragon_spawn_egg':"Œuf d’apparition de dragon vert",
'blue_dragon_spawn_egg':"Œuf d’apparition de dragon bleu",'dragon_hunter_spawn_egg':"Œuf d’apparition de chasseur de dragons"}
USES = {
'light_ballista':'Défense automatique compacte : dégâts de base 8, portée 12 blocs, délai de rechargement 40 ticks. Pose-la sur un support adapté, puis charge-la avec des flèches ou des amorces.',
'medium_ballista':'Défense automatique : dégâts de base 14, portée 14 blocs, rechargement 80 ticks. Elle tire plus fort, mais moins souvent que la légère.',
'ballista':'Défense automatique lourde : dégâts de base 22, portée 16 blocs, rechargement 40 ticks. Son emprise est de 2 × 2 blocs ; prévois un support et un espace dégagés.',
'bolt_primer':'Munition directement acceptée par les balistes, au même titre que les flèches. Interagis avec la baliste en tenant les amorces : chaque objet chargé ajoute un tir, jusqu’à une réserve de 64. La recette produit 4 amorces.',
'dragon_saddle':'Selle spécifique nécessaire pour monter ton dragon adulte. Équipe-la par interaction ; la selle vanilla ne remplace pas cet objet. Monte ensuite avec la main vide, sans être accroupi.',
'dragon_pack_saddle':'Remplace la selle simple par une selle avec deux compartiments de 54 emplacements, soit 108 emplacements. Elle reste une selle pour la monte d’un dragon adulte possédé.',
'draconic_staff':'Objet de commandement : sélectionner son dragon et lui donner des ordres. Il ne sert pas à apprivoiser un dragon sauvage ; le lien de propriété est établi à l’éclosion.',
'draconic_whistle':'Autre objet de commandement qui permet de sélectionner un dragon déjà possédé. Aucune recette dans ce JAR : le chasseur de dragons en propose un contre 8 émeraudes, avant variations éventuelles du prix.',
'iron_dragon_armor':'Équipement du dragon adulte possédé. Donne 8 points d’armure de base. Ce n’est pas une armure à porter par le joueur.',
'gold_dragon_armor':'Équipement du dragon adulte possédé. Donne 10 points d’armure de base ; l’or protège ici davantage que le fer.',
'diamond_dragon_armor':'Équipement du dragon adulte possédé. Donne 14 points d’armure et sert de base à la fabrication de la variante netherite.',
'netherite_dragon_armor':'Équipement du dragon adulte possédé. Donne 18 points d’armure. Dans ce JAR, son amélioration se fait par craft sans forme, sans modèle de forge.',
'dragon_scale':'Ressource des dragons utilisée pour les selles, armures, bâton et renforts. Les tables de butin des dragons en contiennent. Le chasseur propose aussi 2 écailles contre 10 émeraudes comme prix de base.',
'dragon_heart':'Ressource servant à améliorer un équipement compatible à la table de forge, en laissant le modèle vide. Le fichier dragon_heart.json consomme un cœur : il ne fabrique pas de cœur. Le chasseur propose également un cœur contre 32 émeraudes comme prix de base.',
'scale_helmet_lining':'Pièce à fabriquer puis à appliquer à un casque compatible dans la table de forge. Elle ne se porte pas seule. Le casque conserve son identité et reçoit le renfort.',
'scale_chest_lining':'Pièce à appliquer à un plastron compatible dans la table de forge. L’application est distincte de la fabrication du renfort et refuse une pièce déjà renforcée.',
'scale_leggings_lining':'Pièce à appliquer aux jambières compatibles dans la table de forge. Elle participe à l’ensemble complet de quatre pièces renforcées.',
'scale_boots_lining':'Pièce à appliquer à des bottes compatibles dans la table de forge. Les protections liées au feu et à la nage dans la lave exigent l’ensemble complet des quatre pièces renforcées.',
'dragon_hunter_table':'Poste lié au chasseur de dragons : son comportement recherche cette table et s’y rattache. Les échanges se font avec le chasseur, pas dans une interface de fabrication de la table.',
'obsidian_fletching_table':'Ravitaille une baliste et sélectionne les carreaux d’obsidienne associés à l’effet Fissure. Place la table directement sous l’emprise de la baliste ou contre l’un de ses côtés.',
'infernal_fletching_table':'Ravitaille une baliste et sélectionne les carreaux infernaux : effets incendiaires et zone de flammes. Place-la sous l’emprise ou contre un côté ; simplement la laisser loin dans la pièce ne suffit pas.',
'echo_fletching_table':'Ravitaille une baliste avec les tirs des profondeurs, associés au choc acoustique. Le choix du projectile dépend de la table détectée par la baliste, pas d’un craft supplémentaire de carreaux.',
'wooden_spikes':'Piège défensif au contact. Pose-le sur le terrain pour entraver et blesser les créatures concernées. La ligne centrale vide de la recette est obligatoire ; les dalles demandées sont les dalles de pierre.',
'iron_spikes':'Version renforcée du piège en bois. La transformation consomme les pieux en bois et trois lingots de fer ; les quatre ingrédients se placent librement dans la grille.',
'light_ballista_wreck':'Épave récupérable liée à la génération du monde. Elle ne tire pas telle quelle : sa réparation restitue une baliste légère à poser.',
'medium_ballista_wreck':'Épave à récupérer puis à réparer avec deux lingots de fer et une bûche acceptée. Le résultat est une baliste moyenne utilisable.',
'heavy_ballista_wreck':'Épave lourde à réparer avec trois lingots de fer et une arbalète. Le craft restitue l’objet baliste lourde, pas un nouveau bloc décoratif.'}
for color,fr in [('red','rouge'),('green','vert'),('blue','bleu')]:
    USES[f'{color}_dragon_egg']=f'Œuf {fr} à récupérer dans le monde, notamment via les antres, puis à poser et incuber. Magma ou lave à 3 blocs au plus ; environ 40 minutes d’incubation. Aucun craft. Reste près de lui pour devenir propriétaire à la naissance.'
    USES[f'{color}_dragon_spawn_egg']=f'Objet d’apparition directe du dragon {fr}, à distinguer de l’œuf posé qui incube. Aucune recette de survie déclarée. Il ne remplace pas le parcours œuf → apprivoisement → croissance.'

GROUPS = [
('balistes-crafts','01 · Construire ses balistes',['light_ballista','medium_ballista','ballista','bolt_primer']),
('defenses-crafts','02 · Installer les défenses et le ravitaillement',['wooden_spikes','iron_spikes','obsidian_fletching_table','infernal_fletching_table','echo_fletching_table','dragon_hunter_table']),
('reparations-crafts','03 · Réparer les balistes trouvées',['repair_light_ballista','repair_medium_ballista','repair_heavy_ballista']),
('equipements-crafts','04 · Préparer l’équipement du dragon',['dragon_saddle','dragon_pack_saddle','draconic_staff','iron_dragon_armor','gold_dragon_armor','diamond_dragon_armor','netherite_dragon_armor']),
('renforts-crafts','05 · Fabriquer les renforts du joueur',['scale_helmet_lining','scale_chest_lining','scale_leggings_lining','scale_boots_lining']),
('forge-crafts','06 · Appliquer les améliorations à la forge',['apply_scale_helmet_lining','apply_scale_chest_lining','apply_scale_leggings_lining','apply_scale_boots_lining','dragon_heart'])]

SMITHING_BASE = {'#minecraft:head_armor':'minecraft:diamond_helmet','#minecraft:chest_armor':'minecraft:diamond_chestplate','#minecraft:leg_armor':'minecraft:diamond_leggings','#minecraft:foot_armor':'minecraft:diamond_boots','#ballista:heart_equipment':'minecraft:diamond_sword'}

HEART_NOTE = 'Exemple avec une épée en diamant : modèle vide + équipement compatible + cœur → même équipement amélioré. Le cœur accepte notamment les outils de minage, épées, lances, masse, arc, arbalète et bouclier, ainsi que les livres enchantés selon les conditions du code. Une nouvelle application sur un équipement déjà infusé, ou sur un livre, exige au moins un enchantement encore améliorable. Une armure ordinaire ne fait pas partie du tag heart_equipment fourni.'
SCALE_NOTE = 'Exemple illustré avec une pièce en diamant ; les autres bases acceptées par le tag correspondant fonctionnent aussi. Laisser l’emplacement du modèle de forge vide. Appliquer le renfort correspondant à la bonne pièce ; une pièce déjà renforcée est refusée. Le résultat conserve la même apparence de base. Les effets de l’ensemble exigent les quatre pièces renforcées.'
