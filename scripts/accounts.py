from brownie import accounts

def load_accounts():
    acc = ["instanceOperator", "instanceWallet", "riskpoolKeeper", "riskpoolWallet", "investor", "oracleProvider",
           "productOwner", "insurer", "customer", "customer2", "arbitratorOwner"]
    
    for a in acc:
        accounts.load(a)

load_accounts()