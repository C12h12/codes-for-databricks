#MuseumArtifactRegsitry

class MuseumLoanRegistry:
    def __init__(self):
        self.loans={}

    def register_loan(self,loan_id:str,
                      artifact_name:str,
                      destination:str)->dict:
        if loan_id in self.loans:
            raise ValueError('Loan already registered')
        self.loans[loan_id]={
            'artifact_name':artifact_name,
            'destination':destination,
            'status':'On Loan'
        }
        return self.loans

    def change_destination(self,loan_id:str,new_destination:str)->dict:
        if loan_id not in self.loans:
            raise KeyError('Loan not found')

        self.loans[loan_id]['destination']=new_destination
        print('changed destination',self.loans[loan_id])

        return self.loans

    def get_loan_details(self,loan_id:str)->dict:
        if loan_id not in self.loans:
            raise KeyError('Loan not found')
        return self.loans[loan_id]

    def loans_by_destination(self,destination:str)->list:

        result=[]

        for k,v in self.loans.items():
            if v['destination']==destination:
                result.append(k)
        return result



registry = MuseumLoanRegistry()

# Register loans
registry.register_loan("L001", "Mona Lisa Replica", "Louvre Museum")
registry.register_loan("L002", "Ancient Vase", "British Museum")
registry.register_loan("L003", "Roman Coin", "Louvre Museum")

# Get loan details
print(registry.get_loan_details("L001"))

# Change destination
registry.change_destination("L002", "Louvre Museum")

# Find loans by destination
print(registry.loans_by_destination("Louvre Museum"))