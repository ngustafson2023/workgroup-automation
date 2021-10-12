"""

Script for automating workgroup assignments for the Epsilon
position for the Chi Phi Beta Chapter.

Author: Nicholas Gustafson, Class of 2023, Epsilon
Last Updated: Fall 2021

"""

import pickle
from subprocess import call
from time import sleep
import openpyxl
import xlrd
from datetime import datetime
import brothers
import workgroups
from assign import assign


Brothers = {}
Brothers['seniors'] = brothers.seniors
Brothers['juniors'] = brothers.juniors
Brothers['sophomores'] = brothers.sophomores
Brothers['freshmen'] = brothers.freshmen

# weight by class
classes = ['seniors']
for _ in range(2):
    classes.append('juniors')
for _ in range(4):
    classes.append('sophomores')
for _ in range(8):
    classes.append('freshmen')

Workgroups = workgroups.workgroups

assignments, workgroup_data = assign(classes, Brothers, Workgroups)


_ = call('clear')
print('Assignments:')
for key, val in assignments.items():
    print(key + ': ' + val)
print('\nEnter [c] to confirm, [r] to regenerate, [e \'workgroup\' \'new assignment name(s)\'] to reassign a workgroup, or [s \'workgroup 1\' \'workgroup 2\'] to swap assignments')
command = input('>>> ')
while command != 'c':
    if command == 'r':
        _ = call('clear')
        sleep(.5)
        for workgroup in Workgroups:
            workgroup.setOccupancy(0)
        assignments, workgroup_data = assign(classes, Brothers, Workgroups)
        print('Assignments:')
        for key, val in assignments.items():
            print(key + ': ' + val)
        print('\nEnter [c] to confirm, [r] to regenerate, [e \'workgroup\' \'new assignment name(s)\'] to reassign a workgroup, or [s \'workgroup 1\' \'workgroup 2\'] to swap assignments')
        command = input('>>> ')
    elif command[0] == 'e':
        inputs = command[2:].split('\' \'')
        if len(inputs) != 0 and inputs[0][1:] in assignments.keys():
            assignments[inputs[0][1:]] = inputs[1][:-1]
        else:
            print('Invalid command, please try again...')
            print('Enter [c] to confirm, [r] to regenerate, [e \'workgroup\' \'new assignment name(s)\'] to reassign a workgroup, or [s \'workgroup 1\' \'workgroup 2\'] to swap assignments')
            command = input('>>> ')
            continue
        _ = call('clear')
        sleep(.5)
        print('Assignments:')
        for key, val in assignments.items():
            print(key + ': ' + val)
        print('\nAssigned ' + inputs[1][:-1] + ' to ' + inputs[0][1:] + '...')
        print('Enter [c] to confirm, [r] to regenerate, [e \'workgroup\' \'new assignment name(s)\'] to reassign a workgroup, or [s \'workgroup 1\' \'workgroup 2\'] to swap assignments')
        command = input('>>> ')
    elif command[0] == 's':
        inputs = command[2:].split('\' \'')
        if len(inputs) != 0 and inputs[0][1:] in assignments.keys() and inputs[1][:-1] in assignments.keys():  # could check to make sure workgroups have same capacity
            assignments[inputs[0][1:]],  assignments[inputs[1][:-1]] = assignments[inputs[1][:-1]], assignments[inputs[0][1:]]
        else:
            print('Invalid command, please try again...')
            print('Enter [c] to confirm, [r] to regenerate, [e \'workgroup\' \'new assignment name(s)\'] to reassign a workgroup, or [s \'workgroup 1\' \'workgroup 2\'] to swap assignments')
            command = input('>>> ')
            continue
        _ = call('clear')
        sleep(.5)
        print('Assignments:')
        for key, val in assignments.items():
            print(key + ': ' + val)
        print('\nSwapped ' + inputs[0][1:] + ' and ' + inputs[1][:-1] + '...')
        print('Enter [c] to confirm, [r] to regenerate, [e \'workgroup\' \'new assignment name(s)\'] to reassign a workgroup, or [s \'workgroup 1\' \'workgroup 2\'] to swap assignments')
        command = input('>>> ')
    else:
        print('Invalid command, please try again...')
        print('Enter [c] to confirm, [r] to regenerate, [e \'workgroup\' \'new assignment name(s)\'] to reassign a workgroup, or [s \'workgroup 1\' \'workgroup 2\'] to swap assignments')
        command = input('>>> ')

file = open(r'workgroup_data.pkl', 'wb')
pickle.dump(workgroup_data, file)
file.close()

loc = './template.xlsx'
    
wb = xlrd.open_workbook(loc)
xfile = openpyxl.load_workbook(loc)
sheetRead = wb.sheet_by_index(0)
sheetWrite = xfile['Sheet1']
sheetRead.cell_value(1, 0)
    
saveAs = datetime.date(datetime.now())
    
for i in range(sheetRead.nrows - 1):
    whichWorkgroup = sheetRead.cell_value(i + 1, 0)
        
    if whichWorkgroup not in [str(x) for x in Workgroups]:
        continue
        
    workgroupReference = [x for x in assignments if str(x) == whichWorkgroup][0]
        
    sheetWrite['B' + str(i + 2)] = assignments[workgroupReference]
        
xfile.save('./Sheets/' + str(saveAs) + '.xlsx')
        
    

        
        
    
