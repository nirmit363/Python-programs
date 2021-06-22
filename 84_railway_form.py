class RailwayForm:
    formtype = 'RailwayForm'
    def printInformation(self):
        print (f'Name is {self.name}')
        print (f'Train name is {self.trainName}')

amreshApplication = RailwayForm()
amreshApplication.name = 'Nirmit Rath'
amreshApplication.trainName = 'Rourlkela to Puri'
amreshApplication.printInformation()
