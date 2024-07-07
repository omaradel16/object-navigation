ROOMS = ["kitchen", "living_room", "bedroom", "bathroom"]

FURNITURE = ["counter", "table", "shelf", "fridge", "top_cabinet", "coffee_table", "cooktop", "counter_top",
             "dining_table", "chair", "t_v_stand", "can", "sofa", "bed", "dresser", "toilet", "sink", "shelving_unit",
             "desk", "side_table", "ottoman"]

OBJECTS = ["apple", "box", "cereal", "dishtowel", "flour", "jar", "kettle", "lettuce", "mug", "oil", "pasta", "rice",
           "soda", "egg", "spray_bottle", "salt_shaker", "wine_bottle", "potato", "pencil", "soap_bottle", "plate",
           "ladle", "fork", "book", "pan", "towel_roll", "butter_knife", "spoon", "watch", "phone", "pen",
           "credit_card", "candle", "tissue_box", "newspaper", "remote_control", "house_plant", "laptop", "desk_lamp",
           "alarm_clock", "soap_bar", "toilet_paper", "baseball_bat", "dish_sponge", "tennis_racket", "basket_ball",
           "coffee_machine", "knife", "bread", "cup", "pot", "bottle", "toaster", "cloth", "microwave", "chairs",
           "couch", "footrest", "stool", "apples", "oranges", "bananas", "orange", "banana", "lemon", "garlic", "peach",
           "grapes", "avocado", "towels", "container_of", "beet", "radish", "eggplant", "basil", "tomato", "kale",
           "squash", "pop", "butter", "pepper_shaker", "paprika_shaker", "bottle_of_soap", "plates", "binder",
           "document", "books", "binders", "documents", "spoons", "smartphone", "wallet", "debit_card", "candles",
           "box_of_tissues", "pc", "bar_of_soap", "soap", "dish_soap", "sponge", "baguette", "bottles"]

# Map of object type to integers
OBJECT_TO_IDX = {
    "counter": 0,
    "table": 1,
    "shelf": 2,
    "fridge": 3,
    "top_cabinet": 4,
    "coffee_table": 5,
    "cooktop": 6,
    "counter_top": 7,
    "dining_table": 8,
    "chair": 9,
    "t_v_stand": 10,
    "can": 11,
    "sofa": 12,
    "bed": 13,
    "dresser": 14,
    "toilet": 15,
    "sink": 16,
    "shelving_unit": 17,
    "desk": 18,
    "side_table": 19,
    "ottoman": 20,
    "apple": 21,
    "box": 22,
    "cereal": 23,
    "dishtowel": 24,
    "flour": 25,
    "jar": 26,
    "kettle": 27,
    "lettuce": 28,
    "mug": 29,
    "oil": 30,
    "pasta": 31,
    "rice": 32,
    "soda": 33,
    "egg": 34,
    "spray_bottle": 35,
    "salt_shaker": 36,
    "wine_bottle": 37,
    "potato": 38,
    "pencil": 39,
    "soap_bottle": 40,
    "plate": 41,
    "ladle": 42,
    "fork": 43,
    "book": 44,
    "pan": 45,
    "towel_roll": 46,
    "butter_knife": 47,
    "spoon": 48,
    "watch": 49,
    "phone": 50,
    "pen": 51,
    "credit_card": 52,
    "candle": 53,
    "tissue_box": 54,
    "newspaper": 55,
    "remote_control": 56,
    "house_plant": 57,
    "laptop": 58,
    "desk_lamp": 59,
    "alarm_clock": 60,
    "soap_bar": 61,
    "toilet_paper": 62,
    "baseball_bat": 63,
    "dish_sponge": 64,
    "tennis_racket": 65,
    "basket_ball": 66,
    "coffee_machine": 67,
    "knife": 68,
    "bread": 69,
    "cup": 70,
    "pot": 71,
    "bottle": 72,
    "toaster": 73,
    "cloth": 74,
    "microwave": 75,
    "chairs": 76,
    "couch": 77,
    "footrest": 78,
    "stool": 79,
    "apples": 80,
    "oranges": 81,
    "bananas": 82,
    "orange": 83,
    "banana": 84,
    "lemon": 85,
    "garlic": 86,
    "peach": 87,
    "grapes": 88,
    "avocado": 89,
    "towels": 90,
    "container_of": 91,
    "beet": 92,
    "radish": 93,
    "eggplant": 94,
    "basil": 95,
    "tomato": 96,
    "kale": 97,
    "squash": 98,
    "pop": 99,
    "butter": 100,
    "pepper_shaker": 101,
    "paprika_shaker": 102,
    "bottle_of_soap": 103,
    "plates": 104,
    "binder": 105,
    "document": 106,
    "books": 107,
    "binders": 108,
    "documents": 109,
    "spoons": 110,
    "smartphone": 111,
    "wallet": 112,
    "debit_card": 113,
    "candles": 114,
    "box_of_tissues": 115,
    "pc": 116,
    "bar_of_soap": 117,
    "soap": 118,
    "dish_soap": 119,
    "sponge": 120,
    "baguette": 121,
    "bottles": 122,
    "wall": 123,
    "door": 124,
    "empty": 125
}

IDX_TO_OBJECT = dict(zip(OBJECT_TO_IDX.values(),  OBJECT_TO_IDX.keys()))


OBJECT_TO_STR = {
    "counter": "C",
    "table": "T",
    "shelf": "S",
    "fridge": "F",
    "top_cabinet": "T",
    "coffee_table": "C",
    "cooktop": "C",
    "counter_top": "C",
    "dining_table": "D",
    "chair": "C",
    "t_v_stand": "T",
    "can": "C",
    "sofa": "S",
    "bed": "B",
    "dresser": "D",
    "toilet": "T",
    "sink": "S",
    "shelving_unit": "S",
    "desk": "D",
    "side_table": "S",
    "ottoman": "O",
    "apple": "A",
    "box": "B",
    "cereal": "C",
    "dishtowel": "D",
    "flour": "F",
    "jar": "J",
    "kettle": "K",
    "lettuce": "L",
    "mug": "M",
    "oil": "O",
    "pasta": "P",
    "rice": "R",
    "soda": "S",
    "egg": "E",
    "spray_bottle": "S",
    "salt_shaker": "S",
    "wine_bottle": "W",
    "potato": "P",
    "pencil": "P",
    "soap_bottle": "S",
    "plate": "P",
    "ladle": "L",
    "fork": "F",
    "book": "B",
    "pan": "P",
    "towel_roll": "T",
    "butter_knife": "B",
    "spoon": "S",
    "watch": "W",
    "phone": "P",
    "pen": "P",
    "credit_card": "C",
    "candle": "C",
    "tissue_box": "T",
    "newspaper": "N",
    "remote_control": "R",
    "house_plant": "H",
    "laptop": "L",
    "desk_lamp": "D",
    "alarm_clock": "A",
    "soap_bar": "S",
    "toilet_paper": "T",
    "baseball_bat": "B",
    "dish_sponge": "D",
    "tennis_racket": "T",
    "basket_ball": "B",
    "coffee_machine": "C",
    "knife": "K",
    "bread": "B",
    "cup": "C",
    "pot": "P",
    "bottle": "B",
    "toaster": "T",
    "cloth": "C",
    "microwave": "M",
    "chairs": "C",
    "couch": "C",
    "footrest": "F",
    "stool": "S",
    "apples": "A",
    "oranges": "O",
    "bananas": "B",
    "orange": "O",
    "banana": "B",
    "lemon": "L",
    "garlic": "G",
    "peach": "P",
    "grapes": "G",
    "avocado": "A",
    "towels": "T",
    "container_of": "C",
    "beet": "B",
    "radish": "R",
    "eggplant": "E",
    "basil": "B",
    "tomato": "T",
    "kale": "K",
    "squash": "S",
    "pop": "P",
    "butter": "B",
    "pepper_shaker": "P",
    "paprika_shaker": "P",
    "bottle_of_soap": "B",
    "plates": "P",
    "binder": "B",
    "document": "D",
    "books": "B",
    "binders": "B",
    "documents": "D",
    "spoons": "S",
    "smartphone": "S",
    "wallet": "W",
    "debit_card": "D",
    "candles": "C",
    "box_of_tissues": "B",
    "pc": "P",
    "bar_of_soap": "B",
    "soap": "S",
    "dish_soap": "D",
    "sponge": "S",
    "baguette": "B",
    "bottles": "B",
    "wall": 'W',
    "door": 'D',
    "empty": 'E'
}
