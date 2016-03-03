n = int(raw_input())
for _ in xrange(n):
    name, started, dob, courses = raw_input().split()
    if int(started[:4]) >= 2010:
        print "%s eligible" % name
    elif int(dob[:4]) >= 1991:
        print "%s eligible" % name
    elif int(courses) > 40:
        print "%s ineligible" % name
    else:
        print "%s coach petitions" % name
