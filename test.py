from estsblib import info
from estsblib.cstc import Python
from estsblib.cstc import Devsecops
from estsblib.cstc import Network
from estsblib.cstc import Sdn

'''
author: Oussama Binike
'''


sdn = Sdn("Network", "PR.saidi", 18, 10)
dev = Devsecops("Network", "PR.saidi", 18, 10)
net = Network("Network", "PR.saidi", 18, 10)
python = Python("Network", "PR.saidi", 18, 10)

print(net.get_prof_name())
print(net.is_passed())
print(net._print())

