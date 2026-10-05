""" optinal used for a specific output of nothing"""
import typeguard
from typeguard import typechecked
from typing import Optional

# can be retrun as
# def testing(a:int) -> str | None:
#     if a==0:
#         return 'pass'
@typechecked()
def testing(a: int) -> Optional[int]:
    return a

print(testing(5))