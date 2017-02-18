import xml.etree.ElementTree as ET
import requests

from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring

from json import dumps

tree = ET.parse('res.xml')
root = tree.getroot()

for score in root.iter('CREDIT_SCORE'):
	if('FICO' in score.get('_ModelNameType')):
		fico = score.get('_Value')
		# print fico

for res in root.iter('CREDIT_RESPONSE'):
	CreditResponseID = res.get('CreditResponseID')
	CreditReportIdentifier = res.get('CreditReportIdentifier')
	# print CreditResponseID, CreditReportIdentifier

balance_sum = 0
for res in root.iter('CREDIT_LIABILITY'):
	UnpaidBalanceAmount = res.get('_UnpaidBalanceAmount')
	# print UnpaidBalanceAmount
	balance_sum += float(UnpaidBalanceAmount)

# print balance_sum

url = "https://thirdparty.mortech-inc.com/mpg/servlet/mpgThirdPartyServlet?propertyState=CA&loan_amount=200000&loanProduct1=30%20year%20fixed&request_id=1&customerId=15mweq01&thirdPartyName=MidwestEquity&licenseKey=buDrU4ra&emailAddress=daric@eclicklending.com"
r = requests.get(url)

data = bf.data(fromstring(r.content))
data['Fico'] = fico
data['CreditResponseID'] = CreditResponseID
data['CreditReportIdentifier'] = CreditReportIdentifier
data['SumOfUnpaidBalance'] = str(balance_sum)
dumps_data = dumps(data,indent=4, sort_keys=True)

print dumps_data
