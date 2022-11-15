import datetime
from functools import lru_cache
import time


@lru_cache(maxsize=50)
class ShareHolder:
    _no__of_employees = 10
    _no_of_shares = 1000

    def __init__(self, _share__holders, _no__of_employees):
        self.share_holders = _share__holders
        self.employees = _no__of_employees
        self.shares = f'Share : {_share__holders} employees : {_no__of_employees}'

    @property
    def returns_statement(self):
        return f"No of share holders are : {self.share_holders} \n" \
               f"No of Employee workers are : {self.employees}"

    def __str__(self):
        return self.returns_statement


anshu = ShareHolder(10, 1903)

try:
    anshu = ShareHolder(10, 1903)
except AttributeError as AttributionError:
    print(AttributionError)
except FileExistsError as FileAlreadyExist:
    print(FileAlreadyExist)
else:
    pass
finally:
    print("Program didn't run successfully")