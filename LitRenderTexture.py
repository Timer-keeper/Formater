import json, os
import tkinter as tk
from tkinter import PhotoImage
import numpy as np
from Litmatool import grs
from PIL import Image, ImageTk
import math


blocks1 = [
    ((0, 17, 5), "minecraft:piston"),
    ((0, 17, 6), "minecraft:piston"),
    ((0, 17, 10), "minecraft:piston"),
    ((0, 17, 11), "minecraft:piston"),
    ((0, 18, 5), "minecraft:white_stained_glass"),
    ((0, 18, 6), "minecraft:snow_block"),
    ((0, 18, 7), "minecraft:observer"),
    ((0, 18, 8), "minecraft:observer"),
    ((0, 18, 9), "minecraft:observer"),
    ((0, 18, 10), "minecraft:snow_block"),
    ((0, 18, 11), "minecraft:white_stained_glass"),
    ((0, 19, 8), "minecraft:snow_block"),
    ((0, 20, 8), "minecraft:observer"),
    ((0, 21, 7), "minecraft:dropper"),
    ((0, 21, 8), "minecraft:observer"),
    ((1, 15, 5), "minecraft:piston"),
    ((1, 15, 6), "minecraft:piston"),
    ((1, 15, 8), "minecraft:end_stone_brick_wall"),
    ((1, 15, 10), "minecraft:piston"),
    ((1, 15, 11), "minecraft:piston"),
    ((1, 16, 5), "minecraft:soul_soil"),
    ((1, 16, 6), "minecraft:soul_soil"),
    ((1, 16, 7), "minecraft:observer"),
    ((1, 16, 8), "minecraft:iron_trapdoor"),
    ((1, 16, 9), "minecraft:observer"),
    ((1, 16, 10), "minecraft:soul_soil"),
    ((1, 16, 11), "minecraft:soul_soil"),
    ((1, 17, 4), "minecraft:blue_ice"),
    ((1, 17, 5), "minecraft:basalt"),
    ((1, 17, 6), "minecraft:basalt"),
    ((1, 17, 7), "minecraft:blue_ice"),
    ((1, 17, 8), "minecraft:observer"),
    ((1, 17, 9), "minecraft:blue_ice"),
    ((1, 17, 10), "minecraft:basalt"),
    ((1, 17, 11), "minecraft:basalt"),
    ((1, 17, 12), "minecraft:blue_ice"),
    ((1, 18, 4), "minecraft:white_stained_glass"),
    ((1, 18, 5), "minecraft:lava"),
    ((1, 18, 6), "minecraft:lava"),
    ((1, 18, 7), "minecraft:white_stained_glass"),
    ((1, 18, 8), "minecraft:end_stone_brick_wall"),
    ((1, 18, 9), "minecraft:white_stained_glass"),
    ((1, 18, 10), "minecraft:lava"),
    ((1, 18, 11), "minecraft:lava"),
    ((1, 18, 12), "minecraft:white_stained_glass"),
    ((1, 19, 5), "minecraft:piston"),
    ((1, 19, 6), "minecraft:piston"),
    ((1, 19, 7), "minecraft:white_stained_glass"),
    ((1, 19, 8), "minecraft:birch_fence_gate"),
    ((1, 19, 9), "minecraft:white_stained_glass"),
    ((1, 19, 10), "minecraft:piston"),
    ((1, 19, 11), "minecraft:piston"),
    ((1, 20, 5), "minecraft:white_stained_glass"),
    ((1, 20, 6), "minecraft:snow_block"),
    ((1, 20, 7), "minecraft:observer"),
    ((1, 20, 8), "minecraft:observer"),
    ((1, 20, 9), "minecraft:observer"),
    ((1, 20, 10), "minecraft:snow_block"),
    ((1, 20, 11), "minecraft:white_stained_glass"),
    ((1, 21, 6), "minecraft:anvil"),
    ((1, 21, 8), "minecraft:snow_block"),
    ((1, 21, 10), "minecraft:anvil"),
    ((1, 22, 4), "minecraft:snow_block"),
    ((1, 22, 5), "minecraft:sticky_piston"),
    ((1, 22, 6), "minecraft:observer"),
    ((1, 23, 4), "minecraft:redstone_wire"),
    ((2, 9, 4), "minecraft:piston"),
    ((2, 9, 5), "minecraft:piston"),
    ((2, 9, 6), "minecraft:piston"),
    ((2, 9, 7), "minecraft:piston"),
    ((2, 9, 8), "minecraft:piston"),
    ((2, 9, 9), "minecraft:piston"),
    ((2, 9, 10), "minecraft:piston"),
    ((2, 9, 11), "minecraft:piston"),
    ((2, 9, 12), "minecraft:piston"),
    ((2, 10, 2), "minecraft:snow_block"),
    ((2, 10, 3), "minecraft:note_block"),
    ((2, 10, 4), "minecraft:observer"),
    ((2, 10, 5), "minecraft:snow_block"),
    ((2, 10, 6), "minecraft:note_block"),
    ((2, 10, 7), "minecraft:observer"),
    ((2, 10, 8), "minecraft:snow_block"),
    ((2, 10, 9), "minecraft:note_block"),
    ((2, 10, 10), "minecraft:observer"),
    ((2, 10, 11), "minecraft:snow_block"),
    ((2, 10, 12), "minecraft:note_block"),
    ((2, 10, 13), "minecraft:observer"),
    ((2, 10, 14), "minecraft:snow_block"),
    ((2, 11, 3), "minecraft:stone_button"),
    ((2, 11, 6), "minecraft:stone_button"),
    ((2, 11, 9), "minecraft:stone_button"),
    ((2, 11, 12), "minecraft:stone_button"),
    ((2, 14, 5), "minecraft:soul_soil"),
    ((2, 14, 6), "minecraft:soul_soil"),
    ((2, 14, 10), "minecraft:soul_soil"),
    ((2, 14, 11), "minecraft:soul_soil"),
    ((2, 15, 4), "minecraft:blue_ice"),
    ((2, 15, 5), "minecraft:basalt"),
    ((2, 15, 6), "minecraft:basalt"),
    ((2, 15, 7), "minecraft:blue_ice"),
    ((2, 15, 8), "minecraft:observer"),
    ((2, 15, 9), "minecraft:blue_ice"),
    ((2, 15, 10), "minecraft:basalt"),
    ((2, 15, 11), "minecraft:basalt"),
    ((2, 15, 12), "minecraft:blue_ice"),
    ((2, 16, 4), "minecraft:white_stained_glass"),
    ((2, 16, 5), "minecraft:lava"),
    ((2, 16, 6), "minecraft:lava"),
    ((2, 16, 7), "minecraft:white_stained_glass"),
    ((2, 16, 8), "minecraft:white_stained_glass_pane"),
    ((2, 16, 9), "minecraft:white_stained_glass"),
    ((2, 16, 10), "minecraft:lava"),
    ((2, 16, 11), "minecraft:lava"),
    ((2, 16, 12), "minecraft:white_stained_glass"),
    ((2, 17, 4), "minecraft:white_stained_glass"),
    ((2, 17, 5), "minecraft:basalt"),
    ((2, 17, 6), "minecraft:basalt"),
    ((2, 17, 7), "minecraft:piston"),
    ((2, 17, 8), "minecraft:observer"),
    ((2, 17, 9), "minecraft:piston"),
    ((2, 17, 10), "minecraft:basalt"),
    ((2, 17, 11), "minecraft:basalt"),
    ((2, 17, 12), "minecraft:white_stained_glass"),
    ((2, 18, 4), "minecraft:white_stained_glass"),
    ((2, 18, 5), "minecraft:soul_soil"),
    ((2, 18, 6), "minecraft:soul_soil"),
    ((2, 18, 7), "minecraft:white_stained_glass"),
    ((2, 18, 8), "minecraft:snow_block"),
    ((2, 18, 9), "minecraft:white_stained_glass"),
    ((2, 18, 10), "minecraft:soul_soil"),
    ((2, 18, 11), "minecraft:soul_soil"),
    ((2, 18, 12), "minecraft:white_stained_glass"),
    ((2, 19, 4), "minecraft:blue_ice"),
    ((2, 19, 5), "minecraft:basalt"),
    ((2, 19, 6), "minecraft:basalt"),
    ((2, 19, 7), "minecraft:blue_ice"),
    ((2, 19, 8), "minecraft:white_stained_glass"),
    ((2, 19, 9), "minecraft:blue_ice"),
    ((2, 19, 10), "minecraft:basalt"),
    ((2, 19, 11), "minecraft:basalt"),
    ((2, 19, 12), "minecraft:blue_ice"),
    ((2, 20, 4), "minecraft:white_stained_glass"),
    ((2, 20, 5), "minecraft:lava"),
    ((2, 20, 6), "minecraft:lava"),
    ((2, 20, 7), "minecraft:white_stained_glass"),
    ((2, 20, 8), "minecraft:white_stained_glass"),
    ((2, 20, 9), "minecraft:white_stained_glass"),
    ((2, 20, 10), "minecraft:lava"),
    ((2, 20, 11), "minecraft:lava"),
    ((2, 20, 12), "minecraft:white_stained_glass"),
    ((2, 21, 4), "minecraft:white_stained_glass"),
    ((2, 21, 5), "minecraft:piston"),
    ((2, 21, 6), "minecraft:piston"),
    ((2, 21, 7), "minecraft:white_stained_glass"),
    ((2, 21, 8), "minecraft:iron_door"),
    ((2, 21, 9), "minecraft:white_stained_glass"),
    ((2, 21, 10), "minecraft:piston"),
    ((2, 21, 11), "minecraft:piston"),
    ((2, 21, 12), "minecraft:white_stained_glass"),
    ((2, 22, 4), "minecraft:white_stained_glass"),
    ((2, 22, 6), "minecraft:snow_block"),
    ((2, 22, 7), "minecraft:observer"),
    ((2, 22, 8), "minecraft:iron_door"),
    ((2, 22, 9), "minecraft:observer"),
    ((2, 22, 10), "minecraft:snow_block"),
    ((2, 23, 4), "minecraft:redstone_wire"),
    ((2, 29, 5), "minecraft:white_stained_glass"),
    ((2, 29, 6), "minecraft:white_stained_glass"),
    ((2, 30, 5), "minecraft:redstone_wire"),
    ((2, 30, 6), "minecraft:redstone_wire"),
    ((3, 9, 2), "minecraft:white_stained_glass"),
    ((3, 9, 4), "minecraft:white_stained_glass"),
    ((3, 9, 5), "minecraft:white_stained_glass"),
    ((3, 9, 6), "minecraft:white_stained_glass"),
    ((3, 9, 7), "minecraft:white_stained_glass"),
    ((3, 9, 8), "minecraft:white_stained_glass"),
    ((3, 9, 9), "minecraft:white_stained_glass"),
    ((3, 9, 10), "minecraft:white_stained_glass"),
    ((3, 9, 11), "minecraft:white_stained_glass"),
    ((3, 9, 12), "minecraft:white_stained_glass"),
    ((3, 9, 14), "minecraft:white_stained_glass"),
    ((3, 10, 2), "minecraft:repeater"),
    ((3, 10, 4), "minecraft:white_stained_glass"),
    ((3, 10, 5), "minecraft:white_stained_glass"),
    ((3, 10, 6), "minecraft:white_stained_glass"),
    ((3, 10, 7), "minecraft:white_stained_glass"),
    ((3, 10, 8), "minecraft:white_stained_glass"),
    ((3, 10, 9), "minecraft:white_stained_glass"),
    ((3, 10, 10), "minecraft:white_stained_glass"),
    ((3, 10, 11), "minecraft:white_stained_glass"),
    ((3, 10, 12), "minecraft:white_stained_glass"),
    ((3, 10, 14), "minecraft:repeater"),
    ((3, 11, 4), "minecraft:white_stained_glass"),
    ((3, 11, 5), "minecraft:white_stained_glass"),
    ((3, 11, 6), "minecraft:white_stained_glass"),
    ((3, 11, 7), "minecraft:white_stained_glass"),
    ((3, 11, 8), "minecraft:white_stained_glass"),
    ((3, 11, 9), "minecraft:white_stained_glass"),
    ((3, 11, 10), "minecraft:white_stained_glass"),
    ((3, 11, 11), "minecraft:white_stained_glass"),
    ((3, 11, 12), "minecraft:white_stained_glass"),
    ((3, 12, 4), "minecraft:white_stained_glass"),
    ((3, 12, 5), "minecraft:white_stained_glass"),
    ((3, 12, 6), "minecraft:white_stained_glass"),
    ((3, 12, 7), "minecraft:white_stained_glass"),
    ((3, 12, 8), "minecraft:white_stained_glass"),
    ((3, 12, 9), "minecraft:white_stained_glass"),
    ((3, 12, 10), "minecraft:white_stained_glass"),
    ((3, 12, 11), "minecraft:white_stained_glass"),
    ((3, 12, 12), "minecraft:white_stained_glass"),
    ((3, 13, 4), "minecraft:white_stained_glass"),
    ((3, 13, 5), "minecraft:white_stained_glass"),
    ((3, 13, 6), "minecraft:white_stained_glass"),
    ((3, 13, 7), "minecraft:white_stained_glass"),
    ((3, 13, 8), "minecraft:white_stained_glass"),
    ((3, 13, 9), "minecraft:white_stained_glass"),
    ((3, 13, 10), "minecraft:white_stained_glass"),
    ((3, 13, 11), "minecraft:white_stained_glass"),
    ((3, 13, 12), "minecraft:white_stained_glass"),
    ((3, 14, 4), "minecraft:white_stained_glass"),
    ((3, 14, 5), "minecraft:white_stained_glass"),
    ((3, 14, 6), "minecraft:white_stained_glass"),
    ((3, 14, 7), "minecraft:white_stained_glass"),
    ((3, 14, 8), "minecraft:white_stained_glass"),
    ((3, 14, 9), "minecraft:white_stained_glass"),
    ((3, 14, 10), "minecraft:white_stained_glass"),
    ((3, 14, 11), "minecraft:white_stained_glass"),
    ((3, 14, 12), "minecraft:white_stained_glass"),
    ((3, 15, 4), "minecraft:iron_block"),
    ((3, 15, 5), "minecraft:basalt"),
    ((3, 15, 6), "minecraft:basalt"),
    ((3, 15, 7), "minecraft:piston"),
    ((3, 15, 8), "minecraft:snow_block"),
    ((3, 15, 9), "minecraft:piston"),
    ((3, 15, 10), "minecraft:basalt"),
    ((3, 15, 11), "minecraft:basalt"),
    ((3, 15, 12), "minecraft:iron_block"),
    ((3, 16, 4), "minecraft:iron_block"),
    ((3, 16, 5), "minecraft:iron_block"),
    ((3, 16, 6), "minecraft:white_stained_glass"),
    ((3, 16, 7), "minecraft:soul_soil"),
    ((3, 16, 9), "minecraft:soul_soil"),
    ((3, 16, 10), "minecraft:white_stained_glass"),
    ((3, 16, 11), "minecraft:iron_block"),
    ((3, 16, 12), "minecraft:iron_block"),
    ((3, 17, 4), "minecraft:iron_block"),
    ((3, 17, 5), "minecraft:basalt"),
    ((3, 17, 6), "minecraft:basalt"),
    ((3, 17, 7), "minecraft:basalt"),
    ((3, 17, 8), "minecraft:blue_ice"),
    ((3, 17, 9), "minecraft:basalt"),
    ((3, 17, 10), "minecraft:basalt"),
    ((3, 17, 11), "minecraft:basalt"),
    ((3, 17, 12), "minecraft:iron_block"),
    ((3, 18, 4), "minecraft:iron_block"),
    ((3, 18, 5), "minecraft:iron_block"),
    ((3, 18, 6), "minecraft:white_stained_glass"),
    ((3, 18, 7), "minecraft:lava"),
    ((3, 18, 8), "minecraft:white_stained_glass"),
    ((3, 18, 9), "minecraft:lava"),
    ((3, 18, 10), "minecraft:white_stained_glass"),
    ((3, 18, 11), "minecraft:iron_block"),
    ((3, 18, 12), "minecraft:iron_block"),
    ((3, 19, 4), "minecraft:iron_block"),
    ((3, 19, 5), "minecraft:basalt"),
    ((3, 19, 6), "minecraft:basalt"),
    ((3, 19, 7), "minecraft:piston"),
    ((3, 19, 8), "minecraft:snow_block"),
    ((3, 19, 9), "minecraft:piston"),
    ((3, 19, 10), "minecraft:basalt"),
    ((3, 19, 11), "minecraft:basalt"),
    ((3, 19, 12), "minecraft:iron_block"),
    ((3, 20, 4), "minecraft:iron_block"),
    ((3, 20, 5), "minecraft:soul_soil"),
    ((3, 20, 6), "minecraft:soul_soil"),
    ((3, 20, 7), "minecraft:white_stained_glass"),
    ((3, 20, 8), "minecraft:observer"),
    ((3, 20, 9), "minecraft:white_stained_glass"),
    ((3, 20, 10), "minecraft:soul_soil"),
    ((3, 20, 11), "minecraft:soul_soil"),
    ((3, 20, 12), "minecraft:iron_block"),
    ((3, 21, 3), "minecraft:white_stained_glass"),
    ((3, 21, 4), "minecraft:lava"),
    ((3, 21, 5), "minecraft:basalt"),
    ((3, 21, 6), "minecraft:basalt"),
    ((3, 21, 7), "minecraft:lava"),
    ((3, 21, 8), "minecraft:white_stained_glass_pane"),
    ((3, 21, 9), "minecraft:lava"),
    ((3, 21, 10), "minecraft:basalt"),
    ((3, 21, 11), "minecraft:basalt"),
    ((3, 21, 12), "minecraft:lava"),
    ((3, 21, 13), "minecraft:white_stained_glass"),
    ((3, 22, 4), "minecraft:white_stained_glass"),
    ((3, 22, 5), "minecraft:blue_ice"),
    ((3, 22, 6), "minecraft:blue_ice"),
    ((3, 22, 8), "minecraft:observer"),
    ((3, 22, 10), "minecraft:blue_ice"),
    ((3, 22, 11), "minecraft:blue_ice"),
    ((3, 23, 4), "minecraft:redstone_wire"),
    ((3, 29, 6), "minecraft:white_stained_glass"),
    ((3, 30, 5), "minecraft:snow_block"),
    ((3, 30, 6), "minecraft:comparator"),
    ((3, 33, 5), "minecraft:observer"),
    ((4, 9, 3), "minecraft:white_stained_glass"),
    ((4, 9, 4), "minecraft:smooth_quartz_slab"),
    ((4, 9, 5), "minecraft:smooth_quartz_slab"),
    ((4, 9, 6), "minecraft:smooth_quartz_slab"),
    ((4, 9, 7), "minecraft:smooth_quartz_slab"),
    ((4, 9, 8), "minecraft:smooth_quartz_slab"),
    ((4, 9, 9), "minecraft:smooth_quartz_slab"),
    ((4, 9, 10), "minecraft:smooth_quartz_slab"),
    ((4, 9, 11), "minecraft:smooth_quartz_slab"),
    ((4, 9, 12), "minecraft:smooth_quartz_slab"),
    ((4, 9, 13), "minecraft:white_stained_glass"),
    ((4, 10, 2), "minecraft:snow_block"),
    ((4, 10, 3), "minecraft:white_stained_glass"),
    ((4, 10, 13), "minecraft:white_stained_glass"),
    ((4, 10, 14), "minecraft:snow_block"),
    ((4, 11, 3), "minecraft:white_stained_glass"),
    ((4, 11, 13), "minecraft:white_stained_glass"),
    ((4, 12, 3), "minecraft:white_stained_glass"),
    ((4, 12, 13), "minecraft:white_stained_glass"),
    ((4, 13, 3), "minecraft:white_stained_glass"),
    ((4, 13, 13), "minecraft:white_stained_glass"),
    ((4, 14, 3), "minecraft:white_stained_glass"),
    ((4, 14, 7), "minecraft:soul_soil"),
    ((4, 14, 9), "minecraft:soul_soil"),
    ((4, 14, 13), "minecraft:white_stained_glass"),
    ((4, 15, 3), "minecraft:iron_block"),
    ((4, 15, 6), "minecraft:basalt"),
    ((4, 15, 7), "minecraft:basalt"),
    ((4, 15, 8), "minecraft:blue_ice"),
    ((4, 15, 9), "minecraft:basalt"),
    ((4, 15, 10), "minecraft:basalt"),
    ((4, 15, 11), "minecraft:basalt"),
    ((4, 15, 13), "minecraft:iron_block"),
    ((4, 16, 2), "minecraft:blue_ice"),
    ((4, 16, 3), "minecraft:iron_block"),
    ((4, 16, 6), "minecraft:white_stained_glass"),
    ((4, 16, 7), "minecraft:lava"),
    ((4, 16, 8), "minecraft:white_stained_glass"),
    ((4, 16, 9), "minecraft:lava"),
    ((4, 16, 10), "minecraft:white_stained_glass"),
    ((4, 16, 13), "minecraft:iron_block"),
    ((4, 16, 14), "minecraft:blue_ice"),
    ((4, 17, 2), "minecraft:white_stained_glass"),
    ((4, 17, 3), "minecraft:iron_block"),
    ((4, 17, 6), "minecraft:basalt"),
    ((4, 17, 7), "minecraft:basalt"),
    ((4, 17, 8), "minecraft:white_stained_glass"),
    ((4, 17, 9), "minecraft:basalt"),
    ((4, 17, 10), "minecraft:basalt"),
    ((4, 17, 13), "minecraft:iron_block"),
    ((4, 17, 14), "minecraft:white_stained_glass"),
    ((4, 18, 1), "minecraft:blue_ice"),
    ((4, 18, 2), "minecraft:white_stained_glass"),
    ((4, 18, 3), "minecraft:iron_block"),
    ((4, 18, 6), "minecraft:white_stained_glass"),
    ((4, 18, 7), "minecraft:soul_soil"),
    ((4, 18, 8), "minecraft:white_stained_glass"),
    ((4, 18, 9), "minecraft:soul_soil"),
    ((4, 18, 10), "minecraft:white_stained_glass"),
    ((4, 18, 13), "minecraft:iron_block"),
    ((4, 18, 14), "minecraft:white_stained_glass"),
    ((4, 18, 15), "minecraft:blue_ice"),
    ((4, 19, 1), "minecraft:white_stained_glass"),
    ((4, 19, 2), "minecraft:white_stained_glass"),
    ((4, 19, 3), "minecraft:iron_block"),
    ((4, 19, 6), "minecraft:basalt"),
    ((4, 19, 7), "minecraft:basalt"),
    ((4, 19, 8), "minecraft:blue_ice"),
    ((4, 19, 9), "minecraft:basalt"),
    ((4, 19, 10), "minecraft:basalt"),
    ((4, 19, 13), "minecraft:iron_block"),
    ((4, 19, 14), "minecraft:white_stained_glass"),
    ((4, 19, 15), "minecraft:white_stained_glass"),
    ((4, 20, 2), "minecraft:blue_ice"),
    ((4, 20, 3), "minecraft:iron_block"),
    ((4, 20, 5), "minecraft:iron_block"),
    ((4, 20, 6), "minecraft:white_stained_glass"),
    ((4, 20, 7), "minecraft:lava"),
    ((4, 20, 8), "minecraft:white_stained_glass"),
    ((4, 20, 9), "minecraft:lava"),
    ((4, 20, 10), "minecraft:white_stained_glass"),
    ((4, 20, 11), "minecraft:iron_block"),
    ((4, 20, 13), "minecraft:iron_block"),
    ((4, 20, 14), "minecraft:blue_ice"),
    ((4, 21, 2), "minecraft:white_stained_glass"),
    ((4, 21, 3), "minecraft:white_stained_glass"),
    ((4, 21, 4), "minecraft:iron_block"),
    ((4, 21, 5), "minecraft:basalt"),
    ((4, 21, 6), "minecraft:basalt"),
    ((4, 21, 7), "minecraft:piston"),
    ((4, 21, 8), "minecraft:white_stained_glass"),
    ((4, 21, 9), "minecraft:piston"),
    ((4, 21, 10), "minecraft:basalt"),
    ((4, 21, 11), "minecraft:basalt"),
    ((4, 21, 12), "minecraft:iron_block"),
    ((4, 21, 13), "minecraft:white_stained_glass"),
    ((4, 21, 14), "minecraft:white_stained_glass"),
    ((4, 22, 4), "minecraft:white_stained_glass"),
    ((4, 22, 5), "minecraft:white_stained_glass"),
    ((4, 22, 6), "minecraft:white_stained_glass"),
    ((4, 22, 7), "minecraft:white_stained_glass"),
    ((4, 22, 8), "minecraft:snow_block"),
    ((4, 22, 9), "minecraft:white_stained_glass"),
    ((4, 22, 10), "minecraft:white_stained_glass"),
    ((4, 22, 11), "minecraft:white_stained_glass"),
    ((4, 22, 12), "minecraft:white_stained_glass"),
    ((4, 23, 4), "minecraft:redstone_wire"),
    ((4, 29, 5), "minecraft:white_stained_glass"),
    ((4, 29, 6), "minecraft:white_stained_glass"),
    ((4, 30, 5), "minecraft:comparator"),
    ((4, 30, 6), "minecraft:comparator"),
    ((4, 31, 6), "minecraft:white_stained_glass"),
    ((4, 32, 4), "minecraft:dropper"),
    ((4, 32, 5), "minecraft:observer"),
    ((4, 32, 6), "minecraft:repeater"),
    ((4, 32, 7), "minecraft:snow_block"),
    ((4, 33, 5), "minecraft:piston_head"),
    ((4, 33, 6), "minecraft:dropper"),
    ((4, 33, 7), "minecraft:redstone_torch"),
    ((4, 33, 8), "minecraft:sticky_piston"),
    ((4, 34, 7), "minecraft:sticky_piston"),
    ((5, 9, 2), "minecraft:white_stained_glass"),
    ((5, 9, 3), "minecraft:white_stained_glass"),
    ((5, 9, 4), "minecraft:iron_trapdoor"),
    ((5, 9, 5), "minecraft:iron_trapdoor"),
    ((5, 9, 6), "minecraft:iron_trapdoor"),
    ((5, 9, 7), "minecraft:iron_trapdoor"),
    ((5, 9, 8), "minecraft:iron_trapdoor"),
    ((5, 9, 9), "minecraft:iron_trapdoor"),
    ((5, 9, 10), "minecraft:iron_trapdoor"),
    ((5, 9, 11), "minecraft:iron_trapdoor"),
    ((5, 9, 12), "minecraft:iron_trapdoor"),
    ((5, 9, 13), "minecraft:white_stained_glass"),
    ((5, 9, 14), "minecraft:white_stained_glass"),
    ((5, 10, 2), "minecraft:repeater"),
    ((5, 10, 3), "minecraft:white_stained_glass"),
    ((5, 10, 13), "minecraft:white_stained_glass"),
    ((5, 10, 14), "minecraft:repeater"),
    ((5, 11, 3), "minecraft:white_stained_glass"),
    ((5, 11, 13), "minecraft:white_stained_glass"),
    ((5, 12, 3), "minecraft:white_stained_glass"),
    ((5, 12, 13), "minecraft:white_stained_glass"),
    ((5, 13, 3), "minecraft:white_stained_glass"),
    ((5, 13, 13), "minecraft:white_stained_glass"),
    ((5, 14, 3), "minecraft:white_stained_glass"),
    ((5, 14, 13), "minecraft:white_stained_glass"),
    ((5, 15, 2), "minecraft:soul_soil"),
    ((5, 15, 3), "minecraft:iron_block"),
    ((5, 15, 7), "minecraft:basalt"),
    ((5, 15, 9), "minecraft:basalt"),
    ((5, 15, 13), "minecraft:iron_block"),
    ((5, 15, 14), "minecraft:soul_soil"),
    ((5, 16, 1), "minecraft:piston"),
    ((5, 16, 2), "minecraft:basalt"),
    ((5, 16, 3), "minecraft:basalt"),
    ((5, 16, 7), "minecraft:white_stained_glass"),
    ((5, 16, 9), "minecraft:white_stained_glass"),
    ((5, 16, 13), "minecraft:basalt"),
    ((5, 16, 14), "minecraft:basalt"),
    ((5, 16, 15), "minecraft:piston"),
    ((5, 17, 1), "minecraft:soul_soil"),
    ((5, 17, 2), "minecraft:lava"),
    ((5, 17, 3), "minecraft:iron_block"),
    ((5, 17, 7), "minecraft:basalt"),
    ((5, 17, 9), "minecraft:basalt"),
    ((5, 17, 13), "minecraft:iron_block"),
    ((5, 17, 14), "minecraft:lava"),
    ((5, 17, 15), "minecraft:soul_soil"),
    ((5, 18, 0), "minecraft:piston"),
    ((5, 18, 1), "minecraft:basalt"),
    ((5, 18, 2), "minecraft:basalt"),
    ((5, 18, 3), "minecraft:basalt"),
    ((5, 18, 7), "minecraft:white_stained_glass"),
    ((5, 18, 9), "minecraft:white_stained_glass"),
    ((5, 18, 13), "minecraft:basalt"),
    ((5, 18, 14), "minecraft:basalt"),
    ((5, 18, 15), "minecraft:basalt"),
    ((5, 18, 16), "minecraft:piston"),
    ((5, 19, 0), "minecraft:white_stained_glass"),
    ((5, 19, 1), "minecraft:lava"),
    ((5, 19, 2), "minecraft:soul_soil"),
    ((5, 19, 3), "minecraft:iron_block"),
    ((5, 19, 7), "minecraft:basalt"),
    ((5, 19, 9), "minecraft:basalt"),
    ((5, 19, 13), "minecraft:iron_block"),
    ((5, 19, 14), "minecraft:soul_soil"),
    ((5, 19, 15), "minecraft:lava"),
    ((5, 19, 16), "minecraft:white_stained_glass"),
    ((5, 20, 1), "minecraft:piston"),
    ((5, 20, 2), "minecraft:basalt"),
    ((5, 20, 3), "minecraft:basalt"),
    ((5, 20, 7), "minecraft:soul_soil"),
    ((5, 20, 8), "minecraft:white_stained_glass"),
    ((5, 20, 9), "minecraft:soul_soil"),
    ((5, 20, 13), "minecraft:basalt"),
    ((5, 20, 14), "minecraft:basalt"),
    ((5, 20, 15), "minecraft:piston"),
    ((5, 21, 1), "minecraft:white_stained_glass"),
    ((5, 21, 2), "minecraft:lava"),
    ((5, 21, 3), "minecraft:white_stained_glass"),
    ((5, 21, 6), "minecraft:basalt"),
    ((5, 21, 7), "minecraft:basalt"),
    ((5, 21, 8), "minecraft:blue_ice"),
    ((5, 21, 9), "minecraft:basalt"),
    ((5, 21, 11), "minecraft:basalt"),
    ((5, 21, 13), "minecraft:white_stained_glass"),
    ((5, 21, 14), "minecraft:lava"),
    ((5, 21, 15), "minecraft:white_stained_glass"),
    ((5, 22, 4), "minecraft:blue_ice"),
    ((5, 22, 5), "minecraft:iron_block"),
    ((5, 22, 6), "minecraft:iron_block"),
    ((5, 22, 7), "minecraft:lava"),
    ((5, 22, 8), "minecraft:white_stained_glass"),
    ((5, 22, 9), "minecraft:lava"),
    ((5, 22, 10), "minecraft:iron_block"),
    ((5, 22, 11), "minecraft:iron_block"),
    ((5, 22, 12), "minecraft:blue_ice"),
    ((5, 23, 4), "minecraft:snow_block"),
    ((5, 23, 5), "minecraft:white_stained_glass"),
    ((5, 23, 6), "minecraft:white_stained_glass"),
    ((5, 23, 7), "minecraft:white_stained_glass"),
    ((5, 23, 8), "minecraft:white_stained_glass"),
    ((5, 23, 9), "minecraft:white_stained_glass"),
    ((5, 23, 10), "minecraft:white_stained_glass"),
    ((5, 23, 11), "minecraft:white_stained_glass"),
    ((5, 23, 12), "minecraft:white_stained_glass"),
    ((5, 24, 4), "minecraft:redstone_wire"),
    ((5, 24, 5), "minecraft:redstone_wire"),
    ((5, 29, 5), "minecraft:white_stained_glass"),
    ((5, 30, 5), "minecraft:redstone_wire"),
    ((5, 30, 6), "minecraft:snow_block"),
    ((5, 31, 5), "minecraft:redstone_wall_torch"),
    ((5, 32, 5), "minecraft:snow_block"),
    ((5, 33, 5), "minecraft:sticky_piston"),
    ((5, 33, 8), "minecraft:piston_head"),
    ((5, 34, 7), "minecraft:piston_head"),
    ((6, 2, 9), "minecraft:white_glazed_terracotta"),
    ((6, 3, 9), "minecraft:sticky_piston"),
    ((6, 4, 5), "minecraft:note_block"),
    ((6, 4, 6), "minecraft:observer"),
    ((6, 4, 7), "minecraft:note_block"),
    ((6, 4, 8), "minecraft:observer"),
    ((6, 4, 9), "minecraft:note_block"),
    ((6, 8, 3), "minecraft:white_stained_glass"),
    ((6, 8, 4), "minecraft:white_stained_glass"),
    ((6, 8, 5), "minecraft:white_stained_glass"),
    ((6, 8, 6), "minecraft:white_stained_glass"),
    ((6, 8, 7), "minecraft:white_stained_glass"),
    ((6, 8, 8), "minecraft:white_stained_glass"),
    ((6, 8, 9), "minecraft:white_stained_glass"),
    ((6, 8, 10), "minecraft:white_stained_glass"),
    ((6, 8, 11), "minecraft:white_stained_glass"),
    ((6, 8, 12), "minecraft:white_stained_glass"),
    ((6, 8, 13), "minecraft:white_stained_glass"),
    ((6, 9, 3), "minecraft:white_stained_glass"),
    ((6, 9, 4), "minecraft:light_blue_carpet"),
    ((6, 9, 5), "minecraft:light_blue_carpet"),
    ((6, 9, 6), "minecraft:light_blue_carpet"),
    ((6, 9, 7), "minecraft:light_blue_carpet"),
    ((6, 9, 8), "minecraft:light_blue_carpet"),
    ((6, 9, 9), "minecraft:light_blue_carpet"),
    ((6, 9, 10), "minecraft:light_blue_carpet"),
    ((6, 9, 11), "minecraft:light_blue_carpet"),
    ((6, 9, 12), "minecraft:light_blue_carpet"),
    ((6, 9, 13), "minecraft:white_stained_glass"),
    ((6, 10, 2), "minecraft:snow_block"),
    ((6, 10, 3), "minecraft:white_stained_glass"),
    ((6, 10, 13), "minecraft:white_stained_glass"),
    ((6, 10, 14), "minecraft:snow_block"),
    ((6, 11, 3), "minecraft:white_stained_glass"),
    ((6, 11, 13), "minecraft:white_stained_glass"),
    ((6, 12, 3), "minecraft:white_stained_glass"),
    ((6, 12, 13), "minecraft:white_stained_glass"),
    ((6, 13, 3), "minecraft:white_stained_glass"),
    ((6, 13, 13), "minecraft:white_stained_glass"),
    ((6, 14, 3), "minecraft:white_stained_glass"),
    ((6, 14, 13), "minecraft:white_stained_glass"),
    ((6, 15, 2), "minecraft:soul_soil"),
    ((6, 15, 3), "minecraft:white_stained_glass"),
    ((6, 15, 13), "minecraft:white_stained_glass"),
    ((6, 15, 14), "minecraft:soul_soil"),
    ((6, 16, 1), "minecraft:piston"),
    ((6, 16, 2), "minecraft:basalt"),
    ((6, 16, 3), "minecraft:basalt"),
    ((6, 16, 4), "minecraft:basalt"),
    ((6, 16, 12), "minecraft:basalt"),
    ((6, 16, 13), "minecraft:basalt"),
    ((6, 16, 14), "minecraft:basalt"),
    ((6, 16, 15), "minecraft:piston"),
    ((6, 17, 1), "minecraft:soul_soil"),
    ((6, 17, 2), "minecraft:lava"),
    ((6, 17, 3), "minecraft:white_stained_glass"),
    ((6, 17, 4), "minecraft:white_stained_glass"),
    ((6, 17, 12), "minecraft:white_stained_glass"),
    ((6, 17, 13), "minecraft:white_stained_glass"),
    ((6, 17, 14), "minecraft:lava"),
    ((6, 17, 15), "minecraft:soul_soil"),
    ((6, 18, 0), "minecraft:piston"),
    ((6, 18, 1), "minecraft:basalt"),
    ((6, 18, 2), "minecraft:basalt"),
    ((6, 18, 3), "minecraft:basalt"),
    ((6, 18, 4), "minecraft:basalt"),
    ((6, 18, 12), "minecraft:basalt"),
    ((6, 18, 13), "minecraft:basalt"),
    ((6, 18, 14), "minecraft:basalt"),
    ((6, 18, 15), "minecraft:basalt"),
    ((6, 18, 16), "minecraft:piston"),
    ((6, 19, 0), "minecraft:snow_block"),
    ((6, 19, 1), "minecraft:lava"),
    ((6, 19, 2), "minecraft:soul_soil"),
    ((6, 19, 3), "minecraft:white_stained_glass"),
    ((6, 19, 4), "minecraft:white_stained_glass"),
    ((6, 19, 12), "minecraft:white_stained_glass"),
    ((6, 19, 13), "minecraft:white_stained_glass"),
    ((6, 19, 14), "minecraft:soul_soil"),
    ((6, 19, 15), "minecraft:lava"),
    ((6, 19, 16), "minecraft:snow_block"),
    ((6, 20, 1), "minecraft:piston"),
    ((6, 20, 2), "minecraft:basalt"),
    ((6, 20, 3), "minecraft:basalt"),
    ((6, 20, 4), "minecraft:basalt"),
    ((6, 20, 12), "minecraft:basalt"),
    ((6, 20, 13), "minecraft:basalt"),
    ((6, 20, 14), "minecraft:basalt"),
    ((6, 20, 15), "minecraft:piston"),
    ((6, 21, 1), "minecraft:snow_block"),
    ((6, 21, 2), "minecraft:lava"),
    ((6, 21, 3), "minecraft:white_stained_glass"),
    ((6, 21, 4), "minecraft:soul_soil"),
    ((6, 21, 7), "minecraft:basalt"),
    ((6, 21, 9), "minecraft:basalt"),
    ((6, 21, 11), "minecraft:basalt"),
    ((6, 21, 12), "minecraft:soul_soil"),
    ((6, 21, 13), "minecraft:white_stained_glass"),
    ((6, 21, 14), "minecraft:lava"),
    ((6, 21, 15), "minecraft:snow_block"),
    ((6, 22, 3), "minecraft:piston"),
    ((6, 22, 4), "minecraft:basalt"),
    ((6, 22, 5), "minecraft:basalt"),
    ((6, 22, 6), "minecraft:basalt"),
    ((6, 22, 7), "minecraft:white_stained_glass"),
    ((6, 22, 8), "minecraft:crying_obsidian"),
    ((6, 22, 9), "minecraft:white_stained_glass"),
    ((6, 22, 10), "minecraft:basalt"),
    ((6, 22, 11), "minecraft:basalt"),
    ((6, 22, 12), "minecraft:basalt"),
    ((6, 22, 13), "minecraft:piston"),
    ((6, 23, 3), "minecraft:white_stained_glass"),
    ((6, 23, 4), "minecraft:lava"),
    ((6, 23, 5), "minecraft:white_stained_glass"),
    ((6, 23, 6), "minecraft:iron_block"),
    ((6, 23, 7), "minecraft:white_stained_glass"),
    ((6, 23, 8), "minecraft:white_stained_glass"),
    ((6, 23, 9), "minecraft:white_stained_glass"),
    ((6, 23, 10), "minecraft:iron_block"),
    ((6, 23, 11), "minecraft:white_stained_glass"),
    ((6, 23, 12), "minecraft:lava"),
    ((6, 23, 13), "minecraft:white_stained_glass"),
    ((6, 24, 5), "minecraft:redstone_wire"),
    ((6, 24, 6), "minecraft:redstone_wire"),
    ((6, 26, 6), "minecraft:redstone_block"),
    ((6, 27, 6), "minecraft:sticky_piston"),
]
blocks = [
    ((0, 0, 0), "minecraft:dirt"),
    ((0, 0, 1), "minecraft:grass_block"),
    ((0, 1, 0), "minecraft:lava"),
    ((1, 0, 0), "minecraft:glass"),
]
xl = max([x for (x, _, _), _ in blocks])
yl = max([y for (_, y, _), _ in blocks])
zl = max([z for (_, _, z), _ in blocks])
screen_x = np.sqrt(xl * xl + zl * zl)
screen_y = np.sqrt(screen_x * screen_x + yl * yl)
data = json.load(open(grs(os.path.join("lang", "data.json")), "r", encoding="utf-8"))
color_map = data["Color_map"][data["Save"]["ui"]["ColorMap"]]
block_face = []

dirtTest = grs(os.path.join("block", "dirt.png"))
glassTest = grs(os.path.join("block", "glass.png"))

print(xl, yl, zl, screen_x, screen_y)
struct_list = [[[None] * (zl + 1) for _ in range(yl + 1)] for _ in range(xl + 1)]
for pos, id in blocks:
    struct_list[pos[0]][pos[1]][pos[2]] = str(id).split(":")[-1]
for x in range(xl):
    for y in range(yl):
        for z in range(zl):
            if not struct_list[x][y][z]:
                continue
            top_face = True if struct_list[x][min(y + 1, yl)][z] else False
            side_face = True if struct_list[min(x + 1, xl)][y][z] else False
            front_face = True if struct_list[x][y][min(z + 1, zl)] else False
            if not (top_face or side_face or front_face):
                continue
            block_face.append(
                [struct_list[x][y][z], (x, y, z), (top_face, side_face, front_face)]
            )
            print(struct_list[x][y][z], (x, y, z), (top_face, side_face, front_face))

# 画布尺寸
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

TILE_WIDTH_HALF = 16  # 方块等轴投影宽度的一半
TILE_HEIGHT_HALF = 16  # 方块等轴投影垂直高度的一半
TILE_HEIGHT_QUARTER = TILE_HEIGHT_HALF // 2

ORIGIN_X = CANVAS_WIDTH // 2
ORIGIN_Y = CANVAS_HEIGHT // 2 + 150

block_images_tk = {}
block_images_pil = {}


def create_placeholder_image(path, color, text):
    try:
        img = Image.new(
            "RGBA", (TILE_WIDTH_HALF * 2, TILE_HEIGHT_HALF * 2), (0, 0, 0, 0)
        )  # 透明背景
        from PIL import ImageDraw

        draw = ImageDraw.Draw(img)
        points = [
            (TILE_WIDTH_HALF, 0),  # Top point
            (TILE_WIDTH_HALF * 2, TILE_HEIGHT_QUARTER),  # Top right
            (
                TILE_WIDTH_HALF * 2,
                TILE_HEIGHT_QUARTER + TILE_HEIGHT_HALF,
            ),  # Bottom right
            (
                TILE_WIDTH_HALF,
                TILE_HEIGHT_HALF * 2 - TILE_HEIGHT_QUARTER,
            ),  # Bottom point *** 修正了这里的计算，应该是总高度减去顶部偏移 ***
            (0, TILE_HEIGHT_QUARTER + TILE_HEIGHT_HALF),  # Bottom left
            (0, TILE_HEIGHT_QUARTER),  # Top left
            (TILE_WIDTH_HALF, 0),  # Close loop
        ]
        draw.polygon(points, fill=color, outline="black")
        draw.text((TILE_WIDTH_HALF - 5, TILE_HEIGHT_HALF - 10), str(text), fill="black")
        img.save(path)
        print(f"Created placeholder: {path}")  # Debug 输出
        return True
    except Exception as e:
        print(f"Error creating placeholder {path}: {e}")
        return False


def to_iso(x, y, z):
    screen_x = ORIGIN_X + (x - z) * TILE_WIDTH_HALF
    screen_y = ORIGIN_Y + (x + z) * TILE_HEIGHT_QUARTER - y * TILE_HEIGHT_HALF
    return int(screen_x), int(screen_y)


def render_structure(canvas, block_data):
    canvas.delete("all")
    # key = lambda item: (-item[1][1], -(item[1][0] + item[1][2]), -item[1][0])  # Y 降序, X+Z 降序, X 降序
    # block_data = sorted(block_data, key=key)

    """for block_info in block_data:
        block_id, (x, y, z), _ = block_info
        screen_x, screen_y = to_iso(x, y, z)

        image_path = grs(os.path.join('block', f"{block_id}.png"))
        if image_path is None:
            print(f"警告: 无法获取方块 ID {block_id} 的图像路径。")
            continue
        print(f"find path {block_id}")
        if image_path not in block_images_tk:
            try:
                if not os.path.exists(image_path):
                    print(f"警告: 图像文件不存在: {image_path}")
                    if grs(os.path.join('block', f"{block_id}.png")) != image_path:
                        continue
                    if not os.path.exists(image_path):
                        continue

                pil_image = Image.open(image_path).convert("RGBA")
                block_images_pil[image_path] = pil_image
                tk_image = ImageTk.PhotoImage(pil_image)
                block_images_tk[image_path] = tk_image
            except Exception as e:
                print(f"错误: 加载或处理图像 {image_path} 时出错: {e}")
                continue
        else:
            tk_image = block_images_tk[image_path]
        canvas.create_image(screen_x, screen_y, image=tk_image, anchor='s')"""
    block_id, (x, y, z), _ = ("dirt", (0, 0, 0), ())
    screen_x, screen_y = to_iso(x, y, z)

    image_path = dirtTest
    print(f"find path {block_id}")
    if image_path not in block_images_tk:
        try:
            pil_image = Image.open(image_path).convert("RGBA")
            block_images_pil[image_path] = pil_image
            tk_image = ImageTk.PhotoImage(pil_image)
            block_images_tk[image_path] = tk_image
        except Exception as e:
            print(f"错误: 加载或处理图像 {image_path} 时出错: {e}")
    else:
        tk_image = block_images_tk[image_path]
    canvas.create_image(screen_x, screen_y, image=tk_image, anchor="s")
    block_id, (x, y, z), _ = ("dirt", (0, 1, 0), ())
    screen_x, screen_y = to_iso(x, y, z)

    image_path = glassTest
    print(f"find path {block_id}")
    if image_path not in block_images_tk:
        try:
            pil_image = Image.open(image_path).convert("RGBA")
            block_images_pil[image_path] = pil_image
            tk_image = ImageTk.PhotoImage(pil_image)
            block_images_tk[image_path] = tk_image
        except Exception as e:
            print(f"错误: 加载或处理图像 {image_path} 时出错: {e}")
    else:
        tk_image = block_images_tk[image_path]
    canvas.create_image(screen_x, screen_y, image=tk_image, anchor="s")


def on_resize(event):
    global ORIGIN_X, ORIGIN_Y, TILE_WIDTH_HALF, TILE_HEIGHT_HALF, TILE_HEIGHT_QUARTER
    CANVAS_WIDTH = event.width
    CANVAS_HEIGHT = event.height
    ORIGIN_X = CANVAS_WIDTH // 2
    ORIGIN_Y = CANVAS_HEIGHT // 2 + 150
    TILE_WIDTH_HALF = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 50
    TILE_HEIGHT_HALF = TILE_WIDTH_HALF
    TILE_HEIGHT_QUARTER = TILE_HEIGHT_HALF // 2
    render_structure(canvas, block_face)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minecraft Isometric Renderer")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="lightblue")
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.bind("<Configure>", on_resize)
    render_structure(canvas, block_face)
    root.mainloop()
