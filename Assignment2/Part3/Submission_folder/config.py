# record = [position, material, n_arrows, mm_state, mm_health, action]

meta_data = {
    "position": ['W', 'N', 'E', 'S', 'C'],
    "material": [0, 1, 2],
    "no_of_arrow": [0, 1, 2, 3],
    "MM_state": ['D', 'R'],
    "MM_health": [0, 25, 50, 75, 100],
    "action": ['UP', 'LEFT', 'DOWN', 'RIGHT', 'STAY', 'SHOOT', 'HIT', 'CRAFT', 'GATHER', 'NONE']
}

state_meta = {
    "N": {
        "DOWN": {
            "p": 0.85,
            "s_next": "C", # on success next state
            "f_next": "E"  # on failure next state
        },
        "STAY": {
            "p": 0.85,
            "s_next": "N",
            "f_next": "E"
        },
        "CRAFT": {
            "p_1": 0.5,
            "s_1": 1,
            "p_2": 0.35,
            "s_2": 2,
            "p_3": 0.15,
            "s_3": 3
        }
    },
    "S": {
        "UP": {
            "p": 0.85,
            "s_next": "C", # on success next state
            "f_next": "E"  # on failure next state
        },
        "STAY": {
            "p": 0.85,
            "s_next": "S",
            "f_next": "E"
        },
        "GATHER": {
            "p": 0.75,
            "s": 1
        }
    },
    "E": {
        "LEFT": {
            "p": 1.0,
            "s_next": "C", # on success next state
            "f_next": "E"  # on failure next state
        },
        "STAY": {
            "p": 1.0,
            "s_next": "E",
            "f_next": "E"
        },
        "SHOOT": {
            "p": 0.9,
            "damage": 25
        },
        "HIT": {
            "p": 0.2,
            "damage": 50
        }
    },
    "W": {
        "RIGHT": {
            "p": 1.0,
            "s_next": "C", # on success next state
            "f_next": "E"  # on failure next state
        },
        "STAY": {
            "p": 1.0,
            "s_next": "W",
            "f_next": "E"
        },
        "SHOOT": {
            "p": 0.25,
            "damage": 25
        }
    },
    "C": {
        "RIGHT": {
            "p": 0.85,
            "s_next": "E", # on success next state
            "f_next": "E"  # on failure next state
        },
        "LEFT": {
            "p": 0.85,
            "s_next": "W", # on success next state
            "f_next": "E"  # on failure next state
        },
        "UP": {
            "p": 0.85,
            "s_next": "N", # on success next state
            "f_next": "E"  # on failure next state
        },
        "DOWN": {
            "p": 0.85,
            "s_next": "S", # on success next state
            "f_next": "E"  # on failure next state
        },
        "STAY": {
            "p": 0.85,
            "s_next": "C",
            "f_next": "E"
        },
        "SHOOT": {
            "p": 0.5,
            "damage": 25
        },
        "HIT": {
            "p": 0.1,
            "damage": 50
        }
    }
}