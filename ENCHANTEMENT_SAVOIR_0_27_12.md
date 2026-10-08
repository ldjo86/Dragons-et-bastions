# Enchantement **Savoir** (`ballista:savoir`) — 0.27.12

La version 0.27.12 contient une définition native `data/ballista/enchantment/savoir.json` et des implémentations dans `SavoirRules.class` ainsi que les mixins `SavoirOrbMixin`, `SavoirDeathMixin` et `SavoirTradeMixin`.

## Niveaux et application

- **Niveaux I, II, III**, rareté/poids JSON = `2`, coût d'enclume `4`, emplacements déclarés = `any`.
- Les objets compatibles sont définis par `data/ballista/tags/item/enchantable/savoir.json` : **tout `#minecraft:enchantable/durability`**, et les balistes légère/moyenne/lourde, le sifflet draconique, ainsi que le bâton draconique.
- Certains achats de livres auprès de **bibliothécaires** utilisent une logique spécifique dans `SavoirRules.trades`; les offres exactes disponibles dépendent du marchand et de ses conditions, et ne sont pas garanties à chaque visite.

## Effets constatés dans le bytecode

1. **Attraction des orbes d'expérience :** la méthode `attractionRange(n)` renvoie `8 + 2 × n` blocs, où `n` est le total de rangs de Savoir pris en compte dans l'équipement. Ex. : 1 rang = 10 blocs ; 3 rangs cumulés = 14 blocs.
2. **Bonus d'expérience :** la méthode `gain(xp, n, reste)` calcule `xp + floor((xp × n + reste)/10)` et mémorise le reste. Le gain théorique est donc de **+10 % par rang cumulé** sur les XP auxquels la logique est appliquée ; les fractions sont reportées, elles ne sont pas perdues.
3. **Sources prises en compte par le code :** les mixins de gestion des orbes, de la mort et des transactions interviennent sur le traitement des XP. La portée réelle dépend de l'événement intercepté, du porteur et du contexte de jeu ; il faut tester les cas particuliers en partie.

**Attention :** le champ `effects` de l'enchantement JSON est `{}`, mais **son effet n'est pas vide** : il est codé dans les classes Java et mixins. Ne pas le présenter comme un enchantement purement décoratif.

### À contrôler en jeu

Empilement de Savoir sur plusieurs objets et emplacements, interactions avec d'autres mods d'XP, fonctionnement au décès, en multijoueur et chez les bibliothécaires. Les valeurs ci-dessus proviennent de l'analyse statique du JAR, et non d'un test automatisé dans Minecraft.

[← Guide 0.27.12](GUIDE_VERSION_0_27_12.md).
