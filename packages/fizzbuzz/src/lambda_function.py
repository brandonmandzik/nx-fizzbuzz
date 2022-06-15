import json

def lambda_handler(event, context):
    returnCode = 500
    returnValue = "ArgumentError - no property (number) provided"
    
    print("Processing incoming request")
    
    #input = event["number"]
    #returnValue, returnCode = validateInput(input)
     
    if "number" in event:
        input = event["number"]
        returnValue, returnCode = validateInput(input)
        
    return {
        'isBase64Encoded': 'true',
        'headers': {
            "Content-Type": "application/json"
        },
        'statusCode': returnCode,
        'body': json.dumps({
            "response" : returnValue,
            
        })
    }

def validateInput(inputNumber):
    code = 400
    value = "ValidationError - Your provided number doesn't fit into the FizzBuzz gaming rules"
    if (inputNumber % 3 == 0):
        value="Fizz"
        code = 200
    if (inputNumber % 5 == 0):
        value="Buzz"
        code = 200
    if ( (inputNumber % 3 == 0 ) and (inputNumber % 5 == 0) ):
        value="Fizzbuzz"
        code = 200
    return value, code

