<?php
 // CreditResponseID CreditResponseIdentifier 
 // sum of _UnpaidBalanceAmount on all CREDIT LIABILITY
  $content = simplexml_load_file('res.xml');

  $new_content = $content;

  foreach ($new_content->RESPONSE->RESPONSE_DATA->CREDIT_RESPONSE->CREDIT_SCORE as $credit_score){
    if (strpos($credit_score['_ModelNameType'], 'FICO') !== false){
      $fico = strval($credit_score['_Value']);
    }
  }
  // print $fico;
  // print ' ';
  foreach ($new_content->RESPONSE->RESPONSE_DATA->CREDIT_RESPONSE as $CreditResponse){
    if ($CreditResponse['CreditResponseID'] !== null){
      $CreditResponseID = strval($CreditResponse['CreditResponseID']);
    }
    if ($CreditResponse['CreditReportIdentifier'] !== null){
      $CreditReportIdentifier = strval($CreditResponse['CreditReportIdentifier']);
    }
    
  }
  // print $CreditResponseID;
  // print ' ';
  // print $CreditReportIdentifier;
  // print ' ';

  $sum = 0;
  foreach ($new_content->RESPONSE->RESPONSE_DATA->CREDIT_RESPONSE->CREDIT_LIABILITY as $Creditliability){
    if ($Creditliability['_UnpaidBalanceAmount'] !== null){
      $UnpaidBalanceAmount = $Creditliability['_UnpaidBalanceAmount'];
      $sum += floatval($UnpaidBalanceAmount);
    }
    
  }
  // print round($sum,2);
            

  $url = 'https://thirdparty.mortech-inc.com/mpg/servlet/mpgThirdPartyServlet?propertyState=CA&loan_amount=200000&loanProduct1=30%20year%20fixed&request_id=1&customerId=15mweq01&thirdPartyName=MidwestEquity&licenseKey=buDrU4ra&emailAddress=daric@eclicklending.com';
  $response = json_encode(simplexml_load_string( file_get_contents($url) ));
  $data = json_decode($response,true);
  $data['Fico'] = $fico;
  $data['CreditResponseID'] = $CreditResponseID;
  $data['CreditReportIdentifier'] = $CreditReportIdentifier;
  $data['SumOfUnpaidBalance'] = strval(number_format($sum, 2, '.', ''));

  $res = json_encode($data);
  print $res;




?>