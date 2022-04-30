#!/usr/bin/env python3

import aws_cdk as cdk

from python_aws_cdk_example.python_aws_cdk_example_stack import PythonAwsCdkExampleStack


app = cdk.App()
PythonAwsCdkExampleStack(app, "python-aws-cdk-example")

app.synth()
