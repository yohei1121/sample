class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """temp(湿度)は摂氏"""
        self.mold = days * temp


ora1 = Orange(200, "dark orange")
print(ora1.mold)
ora1.rot(10, 37)
print(ora1.mold)

#ora1.weight = 100
#ora1.color = "light orange"
#print(ora1.weight)
#print(ora1.color)

#ora2 = Orange(8, "dark orange")
#ora3 = Orange(14, "yellow")
