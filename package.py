class Package(object):
    def __init__(self, plist):
        self.package_id = int(plist[0])
        self.address = plist[1]
        self.city = plist[2]
        self.state = plist[3]
        self.zip = plist[4]
        self.deadline = plist[5]
        self.weight = plist[6]
        self.notes = plist[7]
        self.delivery_time = "00:00"
        self.delivery_status = "At hub"

    def print_long(self):
        print("Package ID: %i" % self.package_id)
        print("Address:  %s" % self.address)
        print("City: %s" % self.city)
        print("State: %s" % self.state)
        print("Zip: %s" % self.zip)
        print("Deadline: %s" % self.deadline)
        print("Weight: %s" % self.weight)
        print("Notes: %s" % self.notes)
        print("Delivery Time: %s" % self.delivery_time)
        print("Status: %s" % self.delivery_status)

    def print_inline(self):
        print("Package ID: %i, Address:  %s, City: %s, State: %s, Zip: %s, Deadline: %s, "
              "Weight: %s, Notes: %s, Delivery Time: %s, Status: %s" %
              (self.package_id, self.address, self.city, self.state, self.zip, self.deadline,
               self.weight, self.notes, self.delivery_time, self.delivery_status))
