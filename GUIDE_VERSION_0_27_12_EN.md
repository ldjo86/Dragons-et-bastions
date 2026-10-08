# Dragons et Bastions — 0.27.12 candidate (English overview)

**Audited artifact:** `ballista-fabric-0.27.12-candidate+mc26.1-26.3-test.jar` (SHA-256 `5cb0158c309bd38fad9bfe090bee32eac43ee70996607625dd640f88ec72c284`). This is a **test candidate**, not a fully playtested release. Its outer `ballista_bundle` includes five separate Fabric `ballista` jars for **Minecraft Java 26.1, 26.1.1, 26.1.2, 26.2 and 26.3**. Requires Java 25+, Fabric Loader 0.19.3+ and Fabric API according to the embedded metadata. No statement about Minecraft 1.21.x is inferred from this file.

## What the mod includes

- **Four dragons** (red/fire, green/poison, blue/ice, black/corrupted), eggs, incubation, raising, commands, lairs, saddles, armors, flying and family mechanics. See [dragons (French)](DRAGONS.md).
- **Black dragon with an illager dragon hunter rider** during draconic raid logic. Actual riding calls are present in `DraconicRaids`, rather than spawning two unrelated creatures. See [black dragon and raids (French)](DRAGON_NOIR_ET_RAIDS.md).
- **Five Draconic Omen consumables** (I–V) and five Legendary Hero advancements granted by code upon completing the appropriate challenge.
- **Ballistas** (light, medium, heavy), piercing bolts, special fletching tables, spikes, wreck repairs and automatic supply-network mechanisms.
- **Bone Pile (`ballista:bone_pile`)**: an actual *3D* block model containing 82 cuboids, used by lair layouts, with no physical collision, skeleton footstep sound, and a loot table of 7 bones.
- **Fish Trap (`ballista:fish_trap`)**: crafted 3×3, requires water at the trap and in front of it; one seed-bait slot and four fish-output slots, captures roughly every 120–240 seconds when eligible; different fish by biome.
- **Knowledge (`ballista:savoir`) I–III**: Java-handled XP orb magnet range of `8 + 2 × cumulative ranks` blocks, and a +10% XP calculation per equipped cumulative rank with fractional remainders; additional librarian-trade handling.
- **Night hazards**: conditional Overworld zombie invasions with up to 200 zombie spawns and separate monster encounters, gated by game rules and player conditions.
- **32 recipe JSONs**, 33 advancement JSONs, 28 loot tables, 23 compressed NBT templates, 16 worldgen data files and 90 PNG textures in the 26.3 module.

## Guides and raw evidence

- [Full French 0.27.12 guide](GUIDE_VERSION_0_27_12.md)
- [All 32 recipes (source-based)](RECETTES_VERSION_0_27_12.md)
- [Bone pile and fish trap](BLOCS_ET_MECANIQUES_0_27_12.md)
- [Knowledge enchantment](ENCHANTEMENT_SAVOIR_0_27_12.md)
- [World generation and loot](STRUCTURES_BUTIN_0_27_12.md)
- [Technical audit and known limitations](ANALYSE_JAR_0_27_12.md)

**Not verified:** actual Minecraft launch, gameplay balance, exact spawn probabilities after world/player gating, multi-player behavior and cross-mod compatibility. Two French translation strings have broken accented characters in the JAR itself.
