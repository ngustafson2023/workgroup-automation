import pickle
import random
import brothers
import workgroups


def getCompatibleBrothers(year, brothers, workgroup):
    indexes = []
    for i in range(len(brothers[year])):
        brother = brothers[year][i]
        if workgroup.getFloor() in [3, 4, 5] and year != 'freshmen':  # freshmen can be assigned to any workgroup
            if brother.getFloor() == workgroup.getFloor():
                indexes.append(i)
        else:
            indexes.append(i)
    return indexes


def assign(classes, brothers, workgroups):
    
    file = open('workgroup_data.pkl', 'rb')
    workgroup_data = pickle.load(file)  # upload data from db
    file.close()

    for year, unweighted_brothers in brothers.items():
        for brother in unweighted_brothers:
            brother.setWeight(workgroup_data[brother.getName()])
        brothers[year] = sorted(brothers[year], key=lambda x: x.getWeight())  # sort by # of workgroups already completed

    assignments = {}

    for workgroup in workgroups:
        name = workgroup.getName()
        capacity = workgroup.getCapacity()
        
        year = random.choice(classes)
        compatible_brothers = getCompatibleBrothers(year, brothers, workgroup)
        while len(compatible_brothers) < capacity:
            year = random.choice(classes)
            compatible_brothers = getCompatibleBrothers(year, brothers, workgroup)

        assigned_brothers = []
        for i in range(capacity):
            assigned_brothers.append(brothers[year].pop(compatible_brothers[i]))  # assign brothers in year with lowest # of workgroups completed

        assignments[name] = ''
        for i in range(len(assigned_brothers)):
            workgroup_data[assigned_brothers[i].getName()] += 1  # update db
            assignments[name] += assigned_brothers[i].getName()
            if i != len(assigned_brothers) - 1:
                assignments[name] += ', '

    return assignments, workgroup_data