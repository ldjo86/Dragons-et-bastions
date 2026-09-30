# Recettes

Le JAR contient **29 recettes**. Les fabrications classiques sont représentées comme dans une table de craft 3×3. Les recettes sans forme sont indiquées séparément.

## Balistes

### Baliste lourde
```
Ficelle | Fer      | Ficelle
Bûche   | Arbalète | Bûche
Fer     | Bûche    | Fer
```

### Baliste moyenne
```
Ficelle | Fer      | Ficelle
Planches| Arbalète | Planches
Bâton   | Planches | Bâton
```

### Baliste légère
```
Ficelle | Vide     | Ficelle
Bâton   | Arc      | Bâton
Bâton   | Planches | Bâton
```

**Amorce de carreau — sans forme :** pépite de fer + bâton + plume → **4 amorces**.

## Équipement draconique

### Selle draconique
```
Cuir | Cuir    | Cuir
Fer  | Écaille | Fer
Vide | Écaille | Vide
```

**Selle de transport — sans forme :** selle draconique + 4 coffres.

### Armures de dragon
Le motif est identique pour le fer, l'or et le diamant :
```
Matériau | Vide    | Matériau
Matériau | Écaille | Matériau
Matériau | Vide    | Matériau
```
**Netherite — sans forme :** armure de dragon en diamant + lingot de netherite + écaille de dragon.

### Bâton draconique
```
Vide    | Or      | Vide
Écaille | Émeraude| Écaille
Vide    | Bâton   | Vide
```

## Renforts en écailles

**Casque**
```
Écaille | Écaille | Écaille
Écaille | Vide    | Écaille
Vide    | Vide    | Vide
```

**Plastron**
```
Écaille | Vide    | Écaille
Écaille | Écaille | Écaille
Écaille | Écaille | Écaille
```

**Jambières**
```
Écaille | Écaille | Écaille
Écaille | Vide    | Écaille
Écaille | Vide    | Écaille
```

**Bottes**
```
Écaille | Vide    | Écaille
Écaille | Vide    | Écaille
Vide    | Vide    | Vide
```

Leur application sur une armure utilise le type personnalisé `ballista:scale_armor` : ce n'est pas une seconde recette 3×3 classique.

## Tables et défenses

**Table de chasse draconique**
```
Planches | Carte        | Planches
Or       | Pierre lisse | Or
Or       | Pierre lisse | Or
```

**Pieux en bois**
```
Bâton | Bâton | Bâton
Vide  | Vide  | Vide
Dalle de pierre | Dalle de pierre | Dalle de pierre
```

- Pieux en fer — sans forme : pieux en bois + 3 lingots de fer.
- Table d'archerie en obsidienne — sans forme : table d'archerie + 4 obsidiennes.
- Table d'archerie infernale — sans forme : table d'archerie + 2 poudres de Blaze + 2 briques du Nether.
- Table d'archerie des profondeurs — sans forme : table d'archerie + 4 éclats d'écho.

## Réparation des épaves

- Lourde : épave lourde + 3 lingots de fer + arbalète.
- Moyenne : épave moyenne + 2 lingots de fer + bûche.
- Légère : épave légère + 2 bâtons + 2 ficelles.

## Cœur de dragon

`dragon_heart.json` utilise une recette personnalisée `ballista:dragon_heart` sur `#ballista:heart_equipment`. Son fonctionnement sera présenté depuis le code plutôt que sous une fausse grille de craft.
