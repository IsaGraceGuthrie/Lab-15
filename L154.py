#ISA GRACE GUTHRIE
class Fabric:
    def __init__(self,countryOfOrigin,color):
        self.countryOfOrigin=countryOfOrigin
        self.color=color
    def __str__(self):
        return self.countryOfOrigin+"("+str(self.color)+")"

region1=Fabric("United States","Green")

print(region1)
