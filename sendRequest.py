import xml.etree.ElementTree as ET
import requests

xmlstring = """
        <REQUEST_GROUP MISMOVersionID="2.3.1">
          <RECEIVING_PARTY _Identifier="AR"></RECEIVING_PARTY>
          <SUBMITTING_PARTY _Name="submitterName" _Identifier="MIDAMERICA02092017">
            <PREFERRED_RESPONSE _Format="Other" _FormatOtherDescription="HTML"></PREFERRED_RESPONSE>
            </SUBMITTING_PARTY>
          <REQUEST RequestDatetime="2007-07-25T11:46:24" InternalAccountIdentifier="" LoginAccountIdentifier="jpachiano" LoginAccountPassword="mtg2016test11">
            <REQUEST_DATA>
              <CREDIT_REQUEST MISMOVersionID="2.3.1" LenderCaseIdentifier="lenderID" RequestingPartyRequestedByName="name">
                <CREDIT_REQUEST_DATA CreditRequestID="CreditRequest1" BorrowerID="Borrower" CreditReportIdentifier="" CreditReportRequestActionType="Submit" CreditReportType="Merge" CreditRequestDateTime="2007-07-25T11:46:24" CreditRequestType="Individual">
                  <CREDIT_REPOSITORY_INCLUDED _EquifaxIndicator="Y" _ExperianIndicator="Y" _TransUnionIndicator="Y"></CREDIT_REPOSITORY_INCLUDED>
                </CREDIT_REQUEST_DATA>
                <LOAN_APPLICATION>
                  <BORROWER BorrowerID="Borrower" _FirstName= "{firstname}" _MiddleName="" _LastName="{lastname}" _NameSuffix="" _AgeAtApplicationYears="" _PrintPositionType="Borrower" _SSN="{ssn}" MaritalStatusType="NotProvided">
                    <_RESIDENCE _StreetAddress="{address}" _City="{city}" _State="{state}" _PostalCode="{zip_code}" BorrowerResidencyType="Current"></_RESIDENCE>
                    </BORROWER>
                </LOAN_APPLICATION>
              </CREDIT_REQUEST>
            </REQUEST_DATA>
          </REQUEST>
        </REQUEST_GROUP>
        """.format(firstname='xyz',lastname='Zhang',ssn='12345678',address='address123',city='San Jose',state='CA',zip_code='95134')
# tree = ET.fromstring(xmlstring)
# print xmlstring

headers = {'Content-Type':'application/xml'}
r = requests.post("https://credit.meridianlink.com/inetapi/AU/get_credit_report.aspx",data = xmlstring, headers = headers)
print r.text


