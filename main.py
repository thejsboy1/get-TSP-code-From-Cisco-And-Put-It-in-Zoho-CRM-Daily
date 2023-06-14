# this code is developed By Kapil Kumar
@csrf_exempt
def tspcode(request):
    singlezohocrmtoken = zohodesktoken()
    Smartbondingtoken = smartbondingtoken()
    url = "https://stage.sbnprd.xylem.cisco.com/sb-partner-oauth-proxy-api/tsp/api/v1/xylem/tspcodes"
    payload = {}
    headers = {
        "Authorization" : f"Bearer {Smartbondingtoken}"
        }
    response = requests.request("GET", url, headers=headers, data = payload)
    tspdata = json.loads(response.text)
    # return JsonResponse(data,safe=False)
    payloadhalf=[]
    for x in tspdata['tspCodes']:
        # print(x) 
        item = {
            "Change_Flag":x["changeFlag"] ,
            "Edit_Time_UTC":x["editTimeUtc"] ,
            "Problem_Code_Description":x["problemCodeDescription"] ,
            "Problem_Code_Name":x["problemCodeName"] ,
            "Sub_Technology_ID":f"{x['subTechId']}" ,
            "Sub_Technology_Name":x["subTechName"] ,
            "Technology_ID":f"{x['techId']}" ,
            "Technology_Name":x["techName"] ,
            "Name":f"{x['id']}"
        }
        payloadhalf.append(item)
        # print(item)
        # break

    # payload
    count = 1
    data = []
    for x in payloadhalf:
        data.append(x)
        if count/99 == int(count/99):
            payload = json.dumps({
                'data' :     data 
            }) 
            # return JsonResponse(payloadhalf,safe=False)
            headerscrm = {'Authorization': f'Zoho-oauthtoken {singlezohocrmtoken}'}
            url1 = f"https://www.zohoapis.com/crm/v4/Smart_Bonding_TSP_Code/upsert"
            response = requests.request("POST", url1, headers=headerscrm, data=payload)
            print("r1",response.status_code)
            print("r12",response.text)
            data = json.loads(response.text)
            data = []
        count = count + 1
        print(count)
        # print(x)
    print("last",data)
    payload = json.dumps({
       
      'data' :     data  
    }) 
    # return JsonResponse(payloadhalf,safe=False)
    headerscrm = {'Authorization': f'Zoho-oauthtoken {singlezohocrmtoken}'}
    url1 = f"https://www.zohoapis.com/crm/v4/Smart_Bonding_TSP_Code/upsert"
    response = requests.request("POST", url1, headers=headerscrm, data=payload)
    print("r1",response.status_code)
    print("r12",response.text)
    data = json.loads(response.text)
    return JsonResponse(data,safe=False)
