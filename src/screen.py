import numpy as np
import pandas as pd

np.random.seed(seed=15) # I fiddled with the seed until it produced
                        # a relatively even distribution of attendance
                        # across all sessions.

workshops = {"PDS Geosciences Node Services Update (10:00)":1,
    "Introduction to Planetary Updates and Tips for using GDAL (10:00)":2,
    "NAIF's Webgeocalc (WGC) Demo (11:00)":3,
    "Introduction to Planetary Image Analysis with ArcGIS (13:00)":4,
    "Creating a PDS4 Archive (13:00)":5,
    "How to live peacefully with Ana/Mini/Conda (13:00)":6,
    "Practical Software Project Management for Research (15:30)":7,
    "The Outer Planets Unified Search (OPUS) - Part 1 (15:30)":8,
    "The Outer Planets Unified Search (OPUS) - Part 2 (16:30)":9}

# This maps each workshop to a list of workshops that it overlaps with
#conflicts = [[1,2],[2,3],[4,5],[4,6],[4,7],[4,8],[4,9],[5,6],[7,8],[7,9],]
conflicts = {1:[2],
             2:[1,3],
             3:[2],
             4:[5,6,7,8,9],
             5:[4,6],
             6:[4,5],
             7:[4,8,9],
             8:[4,7],
             9:[4,7]}

nreg = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
reglist = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
overflow = 0

file = "OpenPlanetary Virtual Conference (ALL) copy.csv"
data = pd.read_csv(file)
print('')
print('####')
for i in np.arange(len(data)):
    foo = False
    print(f"{data.iloc[i]['Email Address']}")
    print(f"""{data.iloc[i]['First Name']} {data.iloc[i]['Last Name']},
           
This email confirms your registration for OPvCon (June 22-24).
Your workshop registration confirmations appear below. Workshops
are scheduled for June 23 and all times are in ET (UTC-4). We
will send addtional information for signing on to the conference
talks and workshops at a later date. Your contact information
has been shared with the hosts of workshops for which you are
registered, and they may contact you directly with additional
information or instructions.""")
    print('')
    print('Workshop schedule:')
    try:
        registered = []
        x = data.iloc[i]['OPvCon Workshops'].split(',')
        np.random.shuffle(x) # this mitigates the bias of preferentially
                             # filling up workshops with earlier start times in
                             # the case of a conflict
        for workshop in x:
            w_i = workshops[workshop.strip()]
            if not len(set(registered).intersection(conflicts[w_i])): # No prior time conflicts
                if (w_i==4) & (nreg[w_i] == 25): # Enforce a participant cap
                    print ('    * Skipping ArcGIS registration due to participant cap.')
                    overflow += 1
                    continue
                registered += [w_i]
                nreg[w_i] += 1
                reglist[w_i] += [f"\"{data.iloc[i]['First Name']} {data.iloc[i]['Last Name']}\" <{data.iloc[i]['Email Address']}>"]
                print(f"    Confirming registration for {workshop.strip()}")
            else:
                print(f'    *** Not registered for {workshop.strip()} due to schedule conflict.')
                if w_i==4:
                    foo = True
    except AttributeError:
        print('   You did not request registration for any workshops.')
        pass
    if foo: # only print this is the ArcGIS workshop was unscheduled
        print('')
        print("""Note: You were not registered for the ArcGIS workshop due to a
time conflict and / or participant cap. An overflow session will
be scheduled for 8am ET on June 24. Please respond immediately
if you would like to be registered for the overflow session.""")

    print('')
    print('Thank you,')
    print('The OpenPlanetary Board')
    print('#####')
    print('')

print('')
# workshop attendee contact lists for the hosts
for k in reglist.keys():
    print(f"{k} - {len(reglist[k])} registered")
    print(", ".join(reglist[k]) )
    print('')

print('')
# summary stats
print(nreg)
print(overflow) # for the ArcGIS workshop