## Deprecated Anniversary Event Mods

These are related to the 10-Year Anniversary events which took place shortly
after BL3's release.  With the November 21, 2019 patch (Mayhem 4 / Maliwan
Takedown), nearly all gear was given a dedicated source, which is slightly at
odds with the mods now found here.  Some bits of functionality from these have
been merged into Better Loot, though.

- `2019-10-01_-_10-year-anniversary-event-1_-_bonus_boss_loot.txt` - This
  is the Week 1 event, as sent by GBX itself.
- `better_bonus_boss_loot.txt` - This is a better (ie: OP and cheaty) version
  of the Week 1 event, which guarantees that all affected bosses will drop
  from their pools.
- `2019-10-08_-_10-year-anniversary-event-2_-_rare_spawn_hunt.txt` - This
  is the Week 2 event, as sent by GBX itself.
- `better_rare_spawn_hunt.txt` - This is a better (ie: OP and cheaty) version
  of the Week 2 event, which guarantees that all of the rare spawns will always
  drop their unique loot, and also removes the undocumented health buffs which
  are in the vanilla version.  Also theoretically makes any other rare spawn
  in the game which was *not* touched by this mod spawn with 100% frequency,
  though I'm not sure what else there is which might be affected by this.

## Deprecated/Testing Mods

- `mayhem_1_better_loot.txt` - This was my first mod attempt, actually,
  and improves the quality of drops in Mayhem 1 (not that it really needed
  it).  As I say, not really useful at all, but I've kept it here for my
  own historical interest.
- `mission_unlocks.txt` - This is actually partially successful; I can at
  least set mission reward pools here.  I'd hoped to also unlock Sanctuary
  with the first mission load, too, though, which didn't work.
- `datatable.txt` - Was used to test out how DataTable values interact with
  the rest of the BVC tuple - turns out that they probably override everything
  except for BVSC, which gets multiplied at the end as per usual.
- `free_fabricator.txt` - This actually doesn't do what it *says* it does;
  it actually just spits out 10 Eridium bars, at a cost of 10 Eridium.
  Useful!  (Actually I suppose it *could* be useful to give Eridium to
  other co-op players.)

These mods were used for awhile for testing, and a few for doing some
Bloody Harvest farming, but they're basically now obsolete (or at least
I'll probably not use them again) with my Crader EM-P5 and Back Ham setup:

- `maggie_super_buff.txt` - Cheat mod which gives the Maggie an absurd
  amount of damage.  Mostly just used for testing mods where I don't want
  to deal with enemies.  Also turns the Maggie into an Infinity -- doesn't
  consume ammo.
- `backham_super_buff.txt` - Cheat mod which makes the Back Ham practically
  invulnerable.  It reports a 100% damage reduction, though that's not
  entirely accurate; some damage can and will get through, but it'll be
  quite minor.  Damage reduction is applied regardless of the direction it
  came from, contrary to what the card reports.  I was quite happy with
  this shield, but the 40% reflect chance often made it difficult to
  manage enemy damage when I was trying to test gear functionality, etc,
  so I switched to the Transformer instead.
- Bloody Harvest-related buffs (for getting the cryo challenge specifically
  done as easily as possible)
  - `stalker_super_buff.txt` - Used to take down Captain Haunt pretty
    quickly for the Haunt-specific challenge.  May as well use the Maggie
    buff until the final phase.
  - `westergun_super_buff.txt` - Probably the easiest way to get the cryo
    challenge.  Should tear through practically anything.  A few Mayhem
    3 modifiers stacked together can make it a bit less effective but it'll
    still perform extremely well.
  - `snowdrift_super_buff.txt` - Ended up not using it really, but it
    technically worked for the cryo challenge.
  - `whispering_ice_slight_buff.txt` - Compared to the other OP mods in
    this section, the buff is pretty slight here, but it's still more
    powerful than usual.  Went a bit overboard with the radius on the
    grenade; you'll probably get hit by it yourself occasionally.

## Failed Attempts

These are some mod attempts that I've yet to actually get working at all.  So
don't look at these thinking that they're any good.  :)

- `cdh.txt` - Just a quick attempt to see if `bDropOnDeath` still existed in
  item pools, even though it didn't look that it did.  Either it doesn't, or
  there's other problems with my attempts.  :)
- `faster_cost_spin.txt` - An attempt to get the cost spinner to resolve to
  the cost much more quickly, when mousing around items.  Not sure why this
  doesn't work, but I suspect that perhaps the object doesn't exist at the
  time that the hotfix executes?
- `no_delay_red_chests.txt` - An attempt to remove the 30-minute in-game
  delay between re-opening red chests.
- `bloody_harvest_challenges.txt` - An attempt to cheat the Bloody Harvest
  challenges to have lower target numbers.  Total fail!
- `guaranteed_badasses.txt` - A few little attempts to increase the number
  of Badasses.  Didn't do the trick, alas.
- `eridian_unlocks.txt` - Some attempts to unlock Eridian Resonator from the
  beginning of the game (would have gone on to the translator as well,
  had I figured this out)
- `torgue_full_auto.txt` - Tried to set Torgue ARs to full auto, but this
  didn't seem to do the trick (the version getting checked in actually tried
  to give them a 5-burst count).
- `golden_chest_costs_eridium.txt` - Just testing to see if I could get the
  Golden Chest to take Eridium instead.  Object/attr syntax is wrong somehow
  in here, and I don't really care enough to track it down.  Also the thing
  I'm trying to change might just be a visual thing anyway, so who knows.
- `better_vehicles.txt` - Was going to just be improving the hover mode for
  hover wheels, to be speedier all around.  The stuff I was trying wasn't
  working, though, so I've given up.  :)
- `charitempoolexpansions.txt` - Some attempts to modify `CharacterItemPoolExpansionData`
  objects.  It'd be nice to be able to edit these directly, because Better Loot
  has to resort to some kind of dumb behavior, otherwise.  BL ends up leaving
  the chances for double-drops in place.  Anyway, thus far I haven't figured
  it out yet.
