# DnD Combat Simulator

## Introduction

DnD Combat Simulator is a Python project that simulates a battle between two creatures in a Dungeons & Dragons game. It provides a `Creature` class that contains all the information of a creature and a `run_two_creature_battle` function that simulates a battle between two creatures until one of them dies.

## Features

- Create creature objects with their respective attributes such as name, armor class, max hit points, attacks, etc.
- Set targets for each creature in a battle.
- Simulate rounds of attacks until one of the creatures dies.
- Roll dice for initiative and attack hits using a `roll_dice` function.

## Installation

1. Clone the repository or download the source code.
   ```
   git clone https://github.com/ProfessorRich/dnd-combat-simulator.git
   ```
2. Navigate to the project folder.
   ```
   cd dnd-combat-simulator
   ```
3. Run the program.
   ```
   python battle.py
   ```

## Usage

1. Create creature objects.
   ```
   creature1 = Creature(name="Dragon", armor_class=18, max_hit_points=200, attacks=[...])
   creature2 = Creature(name="Goblin", armor_class=15, max_hit_points=100, attacks=[...])
   ```

2. Run a battle between the two creatures.
   ```
   run_two_creature_battle(creature1, creature2)
   ```
