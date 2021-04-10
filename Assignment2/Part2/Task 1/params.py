SHOOT_DAMAGE = 25
HIT_DAMAGE = 50
FINAL_REWARD = 50
MM_ATTACK_COST = -40
POS = ["W", "N", "E", "S", "C"]
MAT = [0, 1, 2]
ARROW = [0, 1, 2, 3]
STATE = ["D", "R"]
HEALTH = [0, 25, 50, 75, 100]
ACTION = ["UP", "LEFT", "DOWN", "RIGHT", 
            "STAY", "SHOOT", "HIT", 
            "CRAFT", "GATHER", "NONE"]

STEP_COST = -10 # Team number 97 => 97%3 = 1 => arr[1] = 1 
GAMMA = 0.999
DELTA = 0.001

MM = {
    "R": {
        "R": 0.5,
        "D": 0.5
    },
    "D": {
        "R": 0.2,
        "D": 0.8
    }
}

IJ = {
    "S": {
        "UP": [
            {
                "Prob": 0.85,
                "Pos": "C",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "STAY": [
            {
                "Prob": 0.85,
                "Pos": "S",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "GATHER": [
            {
                "Prob": 0.75,
                "Pos": "S",
                "Arrow": 0,
                "Mat": 1,
                "Damage": 0,
            },
            {
                "Prob": 0.25,
                "Pos": "S",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
    },
    "N": {
        "DOWN": [
            {
                "Prob": 0.85,
                "Pos": "C",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "STAY": [
            {
                "Prob": 0.85,
                "Pos": "N",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "CRAFT": [
            {
                "Prob": 0.5,
                "Pos": "N",
                "Arrow": 1,
                "Mat": -1,
                "Damage": 0,
            },
            {
                "Prob": 0.35,
                "Pos": "N",
                "Arrow": 2,
                "Mat": -1,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "N",
                "Arrow": 3,
                "Mat": -1,
                "Damage": 0,
            },
        ],
    },
    "C": {
        "DOWN": [
            {
                "Prob": 0.85,
                "Pos": "S",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "UP": [
            {
                "Prob": 0.85,
                "Pos": "N",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "LEFT": [
            {
                "Prob": 0.85,
                "Pos": "W",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "RIGHT": [
            {
                "Prob": 1.0,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            }
        ],
        "STAY": [
            {
                "Prob": 0.85,
                "Pos": "C",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
            {
                "Prob": 0.15,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "SHOOT": [
            {
                "Prob": 0.5,
                "Pos": "C",
                "Arrow": -1,
                "Mat": 0,
                "Damage": 25,
            },
            {
                "Prob": 0.5,
                "Pos": "C",
                "Arrow": -1,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "HIT": [
            {
                "Prob": 0.1,
                "Pos": "C",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 50,
            },
            {
                "Prob": 0.9,
                "Pos": "C",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
    },
    "E": {
        "LEFT": [
            {
                "Prob": 1.0,
                "Pos": "C",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            }
        ],
        "STAY": [
            {
                "Prob": 1.0,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            }
        ],
        "SHOOT": [
            {
                "Prob": 0.9,
                "Pos": "E",
                "Arrow": -1,
                "Mat": 0,
                "Damage": 25,
            },
            {
                "Prob": 0.1,
                "Pos": "E",
                "Arrow": -1,
                "Mat": 0,
                "Damage": 0,
            },
        ],
        "HIT": [
            {
                "Prob": 0.2,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 50,
            },
            {
                "Prob": 0.8,
                "Pos": "E",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            },
        ],
    },
    "W": {
        "RIGHT": [
            {
                "Prob": 1.0,
                "Pos": "C",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            }
        ],
        "STAY": [
            {
                "Prob": 1.0,
                "Pos": "W",
                "Arrow": 0,
                "Mat": 0,
                "Damage": 0,
            }
        ],
        "SHOOT": [
            {
                "Prob": 0.25,
                "Pos": "W",
                "Arrow": -1,
                "Mat": 0,
                "Damage": 25,
            },
            {
                "Prob": 0.75,
                "Pos": "W",
                "Arrow": -1,
                "Mat": 0,
                "Damage": 0,
            },
        ],
    },
}