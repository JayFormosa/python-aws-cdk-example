from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_dynamodb as dynamodb
)


class PythonAwsCdkExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = dynamodb.Table(self, "Table",
            partition_key=dynamodb.Attribute(name="member_id", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="council", type=dynamodb.AttributeType.STRING)
        )
        
