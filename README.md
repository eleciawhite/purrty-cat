# Purrty-cat

After 300 episodes, we wanted to throw a party for the listeners of [Embedded](https://embedded.fm/). Through a series of mishaps, the party got named **Cats and Hacks** so I needed to make something to take to the party that was suitable. As I've been playing a lot with origami lately, I decided to make an origami cat that purred when it was pet.

This turned out to be a great project because it used many things from the podcast, from early in the show to recent episodes.

![Origami Cat Beauty Shot](https://github.com/eleciawhite/purrty-cat/raw/master/images/PhotoShootCat.JPG "Origami Cat")

I used an [Adafruit Trinket M0 with CircuitPython](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython) (which I heard about on [show #295](https://embedded.fm/episodes/295)). This had onboard capacitive sense so I used a length of copper tape as the touch sensor, placed on the paper before I started folding. The purring is generated with a coin cell vibration motor, on a board that Casey helped me layout after listening to [episode #20](https://embedded.fm/episodes/2013/9/25/20soldered-together-by-monkeys). Another listener, Philip Freidin (who was on [#146](https://embedded.fm/episodes/146)) taught me how to do SMT and helped me create several boards.

![Origami Cat in the Window](https://github.com/eleciawhite/purrty-cat/raw/master/images/WindowCat.jpeg "Origami Cat in the Window")

## Hardware

![Board schematic](https://github.com/eleciawhite/purrty-cat/raw/master/images/SchematicForMotorBoard.PNG "Schematic") The motor board schematic for the motor board shows a diode and a FET and some connectors that would have been useful on another project.

![Bottom Gerber](https://github.com/eleciawhite/purrty-cat/raw/master/images/BottomGerrber.PNG "Bottom Gerber")
![Top Gerber](https://github.com/eleciawhite/purrty-cat/raw/master/images/TopGerber.PNG "Top Gerber")
Thank you Casey for making [the gerbers](https://github.com/eleciawhite/purrty-cat/tree/master/motorboard) for me!

![Capacitive Sense](https://github.com/eleciawhite/purrty-cat/raw/master/images/CapacitiveSense.jpeg "Capacitve sense") Capacitve sensing is on the Trinket M0 board. I could have put in a long wire but the copper tape is most effective in one direction (the adhesive is not as conductive). This was taped on the inside of the cat's belly so that the copper was close to the spine of the cat.

![Belly Electronics](https://github.com/eleciawhite/purrty-cat/raw/master/images/CatBelly2.JPG "Electronics") Electronics are hidden in the belly of the cat. The two-CR2032 battery holder has easy to access (and its switch is especially easy to access). Everything is held together with hot glue.

![Chest Electronics](https://github.com/eleciawhite/purrty-cat/raw/master/images/CatChest2.JPG "Vibe motor electronics") Vibe motor electronics are hiddle in the ruff/chest of the cat with the wires snaked down to the belly controller.

