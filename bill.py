
import pandas as pd
from bill_handling import Hist
his=Hist()
class Bill:

    def __init__(self):
        pass

    def b(self,p):
        df=pd.DataFrame(p)
        total=0
        for pro in p:
            quna=pro["quantity"]
            pricr=pro["price"]

            total+=quna*pricr

        # print(df)

        # print(f"*****Total price =  {total} " )
        his.generate_bill(p)
