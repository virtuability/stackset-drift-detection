#!/usr/bin/env python3
import os

from aws_cdk import App, Environment

from lib.stack import StacksetDriftDetectionStack, StacksetDriftDetectionStackProps

app = App()

_ = StacksetDriftDetectionStack(
    app,
    "StacksetDriftDetectionStack",
    env=Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
    props=StacksetDriftDetectionStackProps(
        stackset_names=["ExampleStackSetName"],  # Provide a list of StackSet names to monitor
        schedule_expression="cron(0 5 ? * 2 *)",  # Provide a schedule interval (cron or rate)
        notification_email_endpoints=["example@example.com"],  # Provide a list of email addresses
        notification_https_endpoints=["https://example.com/endpoint"],  # Provide a list of HTTPS endpoints
    ),
)

app.synth()
