from simple_salesforce import Salesforce

# ログイン
sf = Salesforce(username='<YOUR_USERNAME>', password='<YOUR_PASSWORD>', security_token='<YOUR_SECURITY_TOKEN>')

cList = sf.query("SELECT Id, LastName, FirstName, Email FROM Contact")
print(cList)
sf.Contact.metadata()