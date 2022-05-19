# MTG Creature Type Co-occurrence Analysis

This project was an afternoon project in analyzing creature type co-occurrence in Magic: The Gathering.
The "final" results are sorted and cleaned in CreatureTypeCoOccurrences.json.
The initial data used was the legacy atomic dataset from MTGJSON available at https://mtgjson.com/downloads/all-files/#legacyatomic

Cubes are a method of playing Magic: The Gathering (hereafter referred to as "magic"), where a curated set of magic cards is drafted from. 
A 'Tribal Cube' is a cube where the primary strategy is to draft cards with similar creature types for increased deck synergy. 
Tribal cubes suffer from a tunnel vision-like effect, where players do not compete for each other's cards; a player drafting Humans does not want Vampires.

This project was prompted by my wish to alleviate the tunnel vision effect tribal cubes suffer from by assigning each color pairing alternating tribes, e.g.

WU - Human

UB - Rogue

BR - Vampire

Where cards in U would support Human Rogues, cards in B would support Vampire Rogues, etc.
I found difficulty in selecting tribes for each color pair to support each tribe combination equally and I had no resources to refer to creature type co-occurrences, so I coded it myself.

This dataset has some sources of error as my code does not handle two-sided cards properly. 
For example, my dataset states that there are 481 co-occurrences of Human and Wizard whereas a scryfall search (https://scryfall.com/search?q=t%3Ahuman+t%3Awizard (as of 19.5.2022)) states that there are 490. 
As an another example, my dataset states that there is 1 co-occurrence of Fungus and Horror whereas a scryfall search (https://scryfall.com/search?q=t%3Afungus+t%3Ahorror) states that there are 2. 
Each value can therefore have an error of anywhere from 1-50%, though if the error percentage is high the total count of co-occurrences will be conversely low enough to eliminate that combination of creature types for consideration for a potential cube regardless.

Another source of error when analyzing the results from the lens of building a cube, though not something in the scope of this project, is that the code does not take into account tribal synergies within the cards' text boxes proper, ignoring creature types. 
For example, Geralf, Visionary Stitcher (https://scryfall.com/card/vow/61/geralf-visionary-stitcher) is a Human Wizard so it might be played in a Human deck or a Wizard deck. 
However, Geralf has card-specific synergies with Zombies that are not taken into account within co-occurrence analysis.

This code does not take into account color identity, though that was the original intent of the project. 
Color identities have been included in CreatureSubtypes.json.
I realized I do not have the time to do additional analysis on creature type co-occurrence in regards to color identity, i.e. Which creature type co-occurrences are
most common in each color combination? 
I invite anyone interested to continue the work and share it with the mtg cube community.
I recommend Donald Miller's website for preliminary insight into creature type occurrence in regards to color identity. 
http://www.smileylich.com/mtg/magocracy/Magocracy_C1.html
