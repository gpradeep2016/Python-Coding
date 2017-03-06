''' Goal:  Learn to parse column-oriented text intended for humans
           Learn why it is a bad idea to have to parse this data, why it is fragile.

    * Missing fields can confuse str.split()
    * Fields that contains spaces can also confuse str.split()
    * ANSI.SYS color codes
    * Pager like "more" and "less"
    * Line wrap
    * Page headings
    * Section headings and totals

'''

with open('notes/ipv4_int_bri.txt') as f:
    for line in f:
        # line = line.rstrip()
        # interface, ipaddr, status, protocol = line.split()
        interface = line[:31].rstrip()
        ipaddr = line[31:47].rstrip()
        status = line[47:69].rstrip()
        protocol = line[69:].rstrip()
        if status.lower() == 'up':
            print '%-15s %s' % (ipaddr, interface)

