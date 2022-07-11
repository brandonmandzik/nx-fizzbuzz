from cgitb import handler
from weakref import proxy
from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_logs as logs,
    aws_apigateway as gateway
    # aws_sqs as sqs,
)
from constructs import Construct

class InfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        my_lambda_function = _lambda.Function(
            self, "FizzbuzzHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('../fizzbuzz/src'),
            handler='lambda_function.lambda_handler',
            log_retention=logs.RetentionDays.ONE_WEEK
        )

        my_rest_api = gateway.LambdaRestApi(
            self, "fizzbuzz-api-cdk",
            handler= my_lambda_function,
            proxy=False
        )

        rest_function = my_rest_api.root.add_resource('fizzbuzz')
        rest_function.add_method('POST')
       
