class Univeristy:
    def __init__(self,name,ranking):
        self.name =name
        self.ranking = ranking

    def getUniFor(self):
        print('The Name of the university is '+self.name+' and the ranking is '+self.ranking+"")

obj = Univeristy('Makerere University','16')
obj2 = Univeristy('Kyabogo University','27')
obj.getUniFor()
obj2.getUniFor()


class Makerere(Univeristy):
    def __init__(self,name,rankikng,location):
        super().__init__(name,rankikng)
        self.location = location

    def getLocation(self):
        print('The Location is ',self.location)

obj_mak = Makerere('Makerere University','16','Kampala')
obj_mak.getLocation()