from tests.integration.unit_test.unit_test_base import UnitTestBase


class UnitTest_nodejs12_x_cookiecutter_aws_sam_hello_nodejs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/hello"
    code_directories = ["hello-world"]


class UnitTest_nodejs12_x_cookiecutter_aws_sam_step_functions_sample_app(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/step-func"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]


class UnitTest_nodejs12_x_cookiecutter_quick_start_from_scratch(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/scratch"


class UnitTest_nodejs12_x_cookiecutter_quick_start_cloudwatch_events(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/cw-event"


class UnitTest_nodejs12_x_cookiecutter_quick_start_s3(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/s3"


class UnitTest_nodejs12_x_cookiecutter_quick_start_sns(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/sns"


class UnitTest_nodejs12_x_cookiecutter_quick_start_sqs(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/sqs"


class UnitTest_nodejs12_x_cookiecutter_quick_start_web(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/web"

class UnitTest_nodejs12_x_cookiecutter_typescript_app_template(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/ts"
    code_directories = [ "app" ]


class UnitTest_nodejs12_x_cookiecutter_aws_sam_quick_start_web_with_connectors(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/web-conn"

class UnitTest_nodejs12_x_cookiecutter_aws_sam_step_functions_with_connectors(UnitTestBase.NodejsUnitTestBase):
    directory = "nodejs12.x/step-func-conn"
    code_directories = [
        "functions/stock-buyer",
        "functions/stock-checker",
        "functions/stock-seller",
    ]