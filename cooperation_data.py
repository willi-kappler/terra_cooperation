from enum import Enum

class Institution(Enum):
    tuebingen = 1
    hohenheim = 2
    senckenberg = 3

class Department(Enum):
    geo = 1
    bio = 2
    comp = 3

class Workgroup:
    def __init__(self, name):
        self.name = name
        self.symbolPos = (0.0, 0.0)
        self.textPos = (0.0, 0.0)
        self.textAlignment = "left"
        self.department = [Department.geo]
        self.institution = Institution.tuebingen
        self.appointmentSince = ""
        self.cooperations = []

#Norton: Tübingen, 100% Geo, appointment at Tübingen 2024
#Tsukamoto: Tübingen, 100% Geo, appointment at Tübingen 2023



def generateWorkgroups():
    print("Create workgroups")

    result = []

    workgroup = Workgroup("Schönberg")
    workgroup.cooperations = [("Böhme", 1), ("Cirpka", 1), ("Kappler", 8), ("Mulch", 1)]
    result.append(workgroup)

    workgroup = Workgroup("Cirpka")
    workgroup.department = [(Department.geo, 3), (Department.comp, 1)]
    workgroup.cooperations = [("Kappler", 7), ("Streck", 8), ("Tielbörger", 1), ("Zarfl", 8)]
    result.append(workgroup)

    workgroup = Workgroup("Macke")
    workgroup.department = [Department.comp]
    workgroup.appointmentSince = "2020"
    workgroup.cooperations = [("Drews", 1), ("Henning", 2)]
    result.append(workgroup)

    workgroup = Workgroup("Henning")
    workgroup.department = [Department.comp]
    workgroup.cooperations = [("Drews", 1), ("Scholten", 1)]
    result.append(workgroup)

    workgroup = Workgroup("Scholten")
    workgroup.cooperations = [("Dippold", 4), ("Kappler", 4), ("Oelmann", 5), ("Tielbörger", 5), ("Zarfl", 1)]
    result.append(workgroup)

    workgroup = Workgroup("Rehfeld")
    workgroup.department = [(Department.geo, 3), (Department.comp, 1)]
    workgroup.appointmentSince = "2020"
    workgroup.cooperations = [("Dippold", 1), ("Schweiger", 1)]
    result.append(workgroup)

    workgroup = Workgroup("Dippold")
    workgroup.department = [(Department.geo, 1),  (Department.bio, 1)]
    workgroup.appointmentSince = "2020"
    workgroup.cooperations = [("Drews", 1), ("Mulch", 1), ("Oelmann", 4), ("Schweiger", 1), ("Tielbörger", 4)]
    result.append(workgroup)

    workgroup = Workgroup("Drews")
    workgroup.department = [(Department.geo, 3), (Department.comp, 1)]
    workgroup.appointmentSince = "2020"
    workgroup.cooperations = [("Oelmann", 1), ("Tielbörger", 1)]
    result.append(workgroup)

    workgroup = Workgroup("Norton")
    workgroup.department = [Department.geo]
    workgroup.appointmentSince = "2024"
    result.append(workgroup)

    workgroup = Workgroup("Tsukamoto")
    workgroup.department = [Department.geo]
    workgroup.appointmentSince = "2023"
    workgroup.cooperations = [("Mulch", 1), ("Rehfeld", 1)]
    result.append(workgroup)

    workgroup = Workgroup("Tielbörger")
    workgroup.department = [Department.bio]
    workgroup.cooperations = [("Bocherens", 1), ("Hickler", 1), ("Oelmann", 4), ("Schweiger", 1), ("Schurr", 3), ("Streck", 1), ("Zarfl", 1)]
    result.append(workgroup)

    workgroup = Workgroup("Schurr")
    workgroup.department = [Department.bio]
    workgroup.institution = Institution.hohenheim
    workgroup.cooperations = [("Bossdorf", 3), ("Hickler", 5), ("Schweiger", 1), ("Streck", 2)]
    result.append(workgroup)

    workgroup = Workgroup("Streck")
    workgroup.department = [(Department.geo, 3), (Department.comp, 1)]
    workgroup.institution = Institution.hohenheim
    workgroup.cooperations = [("Kappler", 2), ("Zarfl", 2)]
    result.append(workgroup)

    workgroup = Workgroup("Schweiger")
    workgroup.department = [Department.bio]
    workgroup.appointmentSince = "2020"
    workgroup.institution = Institution.hohenheim
    workgroup.cooperations = []
    result.append(workgroup)

    workgroup = Workgroup("Hickler")
    workgroup.department = [(Department.bio, 2), (Department.geo, 1)]
    workgroup.institution = Institution.senckenberg
    workgroup.cooperations = [("Fritz", 1), ("Mulch", 5)]
    result.append(workgroup)

    workgroup = Workgroup("Fritz")
    workgroup.department = [(Department.bio, 2), (Department.geo, 1)]
    workgroup.institution = Institution.senckenberg
    workgroup.cooperations = [("Mulch", 5)]
    result.append(workgroup)

    workgroup = Workgroup("Mulch")
    workgroup.department = [Department.geo]
    workgroup.institution = Institution.senckenberg
    workgroup.cooperations = [("Bocherens", 1), ("Böhme", 1)]
    result.append(workgroup)

    #workgroup = Workgroup("Böhning-Gaese")
    #workgroup.department = [Department.bio]
    #workgroup.institution = Institution.senckenberg
    #workgroup.cooperations = [("Oelmann", 1)]
    #result.append(workgroup)

    #workgroup = Workgroup("Fitzsimmons")
    #workgroup.appointmentSince2020 = True
    #workgroup.cooperations = []
    #result.append(workgroup)

    workgroup = Workgroup("Böhme")
    workgroup.department = [(Department.geo, 2), (Department.bio, 1)]
    workgroup.cooperations = [("Bocherens", 2)]
    result.append(workgroup)

    workgroup = Workgroup("Bocherens")
    workgroup.department = [(Department.geo, 2), (Department.bio, 1)]
    workgroup.cooperations = [("Oelmann", 1)]
    result.append(workgroup)

    workgroup = Workgroup("Bossdorf")
    workgroup.department = [Department.bio]
    workgroup.cooperations = []
    result.append(workgroup)

    workgroup = Workgroup("Zarfl")
    workgroup.department = [Department.geo]
    workgroup.cooperations = [("Kappler", 3)]
    result.append(workgroup)

    workgroup = Workgroup("Monte")
    workgroup.department = [Department.bio]
    workgroup.appointmentSince = "2020"
    workgroup.cooperations = []
    result.append(workgroup)

    workgroup = Workgroup("Oelmann")
    workgroup.department = [(Department.geo, 1), (Department.bio, 1)]
    workgroup.cooperations = [("Kappler", 2)]
    result.append(workgroup)

    workgroup = Workgroup("Kappler")
    workgroup.department = [(Department.geo, 1), (Department.bio, 1)]
    workgroup.cooperations = []
    result.append(workgroup)

    return result

