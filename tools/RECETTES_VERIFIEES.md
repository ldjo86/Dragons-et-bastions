# Référence des recettes illustrées

Source : `ballista-fabric-0.27.1+mc26.2.jar`, SHA-256 `e85ac8a4a68c773b2ab5b81c1dc7eedad2b6eee91028ebd29d8c68ab1c245b55`.

La page unique doit présenter les 29 recettes : 24 fabrications à la table de craft et 5 améliorations à la table de forge. Les images doivent montrer les icônes des ingrédients, les cases vides, une flèche et le résultat avec sa quantité. Les recettes sans forme restent explicitement indiquées comme telles.

## Correction vérifiée dans le code compilé

`DragonScaleRecipe` et `DragonHeartRecipe` héritent de `SimpleSmithingRecipe`. Leur méthode `matches` exige que le champ du modèle de forge soit vide ; leur affichage utilise `SmithingRecipeDisplay` avec `Items.SMITHING_TABLE`.

- Renforts : modèle vide + pièce d'armure compatible + renfort correspondant → cette pièce d'armure renforcée. Une pièce déjà renforcée est refusée par `DragonScaleArmor.canApply`.
- Cœur : modèle vide + équipement compatible avec `#ballista:heart_equipment` et accepté par `DragonHeartUpgrades.canApply` + cœur de dragon → équipement amélioré.

`dragon_heart.json` n'est PAS une recette pour fabriquer un cœur de dragon. C'est la recette qui consomme un cœur pour améliorer un équipement.

L'application d'un renfort ou d'un cœur conserve l'objet de base ; une épée ou une armure en diamant dans l'image est un exemple de base compatible, pas le seul matériau accepté. Les conditions supplémentaires du cœur doivent être précisées, sans inventer une armure ou un nouvel objet résultat.

## Disposition fidèle

- Baliste lourde : `SIS / LCL / ILI`, S ficelle, I lingot de fer, L bûche du tag `#minecraft:logs`, C arbalète.
- Baliste moyenne : `SIS / PCP / TPT`, S ficelle, I lingot de fer, P planches du tag `#minecraft:planks`, C arbalète, T bâton.
- Baliste légère : `S S / TCT / TPT`, S ficelle, T bâton, C arc, P planches.
- Les bûches et planches de chêne sont des exemples visuels pour les tags, pas une restriction au chêne.
- La ligne vide des pieux en bois doit être conservée au milieu de la grille.
- L'armure de dragon en netherite est fabriquée sans forme à la table de craft, et non à la forge, dans ce JAR.

Vérifications statiques uniquement : ces observations ne constituent pas un lancement ni un test de Minecraft.
