import json
import boto3
import uuid
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BMIHistory')

def lambda_handler(event, context):
    try:
        # API Gateway sends the body as a JSON string
        body = json.loads(event.get('body', '{}')) if 'body' in event else event
        weight = float(body['weight'])
        height_cm = float(body['height'])

        # Calculate BMI
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi_rounded = round(bmi, 2)

        # Determine Category
        if bmi_rounded < 18.5:
            category = "Underweight"
        elif bmi_rounded <= 24.9:
            category = "Normal Weight"
        elif bmi_rounded <= 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Save to DynamoDB
        table.put_item(
            Item={
                'ID': str(uuid.uuid4()),
                'Weight': Decimal(str(weight)),
                'Height': Decimal(str(height_cm)),
                'BMI': Decimal(str(bmi_rounded)),
                'Category': category,
                'Date': datetime.now().isoformat()
            }
        )

        # Return success with CORS headers
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'bmi': bmi_rounded,
                'category': category
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }