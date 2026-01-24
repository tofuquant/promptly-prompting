from OpenPermID import OpenPermID
from pandas.core.frame import DataFrame

opid = OpenPermID()
opid.set_access_token("Dh3t6TGs7pz2X830Md8TkfLgxLoNnwLR")
print(opid.get_usage())