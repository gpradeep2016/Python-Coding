''' An old, true, and lurid tale of Python
    featuring raisins, pushy relatives,
    checkerboards, business cards, and
    getting much needed rest.
'''

import csv

vcard_template = '''BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;100 Flat Grape Dr;Fresno;CA;95555;United States of America
EMAIL;PREF;INTERNET:%s
REV:20150824T195243Z
END:VCARD
'''

with open('notes/raisin_team_update.csv') as f:
    for lastname, firstname, title, phone, email in csv.reader(f):
        vcard = vcard_template % (lastname, firstname, firstname, lastname, title, email, phone)

        filename = '%s_%s.vcf' % (firstname, lastname)
        with open(filename, 'w') as vfile:
            vfile.write(vcard)

