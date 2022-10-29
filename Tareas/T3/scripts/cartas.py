"""Module cartas returning DCCard-Jitsu cards."""
from random import randint as ri


def get_penguins() -> dict:
    """Returns a dictionary with 15 elements.
    Each element has the structure:
    {"index": {
        "elemento": Elemento,
        "color": Color,
        "puntos": Valor poder ataque}
    """
    status_color = {"rojo": 0,
                    "azul": 0,
                    "verde": 0
                    }
    status_element = {"agua": 0,
                      "fuego": 0,
                      "nieve": 0
                      }
    out = {}
    while len(out) != 15:
        color = ""
        while True:
            color = list(status_color.keys())[ri(0, 2)]
            if len(out) == 0:
                status_color[color] += 1
                break
            else:
                if (status_color[color] / len(out)) <= 0.6:
                    status_color[color] += 1
                    break
        element = ""
        while True:
            element = list(status_element.keys())[ri(0, 2)]
            if len(out) == 0:
                status_element[element] += 1
                break
            else:
                if (status_element[element] / len(out)) <= 0.6:
                    status_element[element] += 1
                    break
        out[f"{len(out)}"] = {"elemento": f"{element}",
                              "color": f"{color}",
                              "puntos": f"{ri(1, 5)}"
                              }
    return out
