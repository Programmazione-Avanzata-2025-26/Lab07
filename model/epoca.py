import roman as r

class Epoca:
    def __init__(self, epoca):
        self.epoca : str = epoca

        elements = self.epoca.split(" ")
        self.secolo = r.fromRoman(elements[0])
        # Le epoche d.C. non hanno la locuzione esplicitata quindi elements[] avrà solo due elementi
        self.locuzione = 1 if len(elements) == 2 else 0  # Mappo a.C.-->0 , d.C.-->1

    def __str__(self):
        return f"{self.epoca}"

    def __repr__(self):
        return f"{self.epoca}"

    def __lt__(self, other):
        if self.locuzione != other.locuzione:
            return self.locuzione < other.locuzione
        elif self.locuzione == 1: # d.C.
            return self.secolo < other.secolo
        else: # a.C.
            return self.secolo > other.secolo
