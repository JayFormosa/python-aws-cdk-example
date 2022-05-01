

Starting point for this was the following AWS Workshop:

https://cdkworkshop.com/30-python.html

Dropped the SQS queue and SNS topic and added a DynamoDB table.

```
cdk init sample-app --language python
```

```
cdk synth

cdk bootstrap

cdk deploy
```
