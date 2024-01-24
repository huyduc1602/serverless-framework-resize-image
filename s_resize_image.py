import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='duchh',
    application_name='duchh-pj-internal-serverless',
    app_uid='000000000000000000',
    org_uid='000000000000000000',
    deployment_uid='undefined',
    service_name='duchh-pj-internal-serverless',
    should_log_meta=False,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='7.2.0',
    disable_frameworks_instrumentation=False,
    serverless_platform_stage='prod'
)
handler_wrapper_kwargs = {'function_name': 'duchh-pj-internal-serverless-dev-resize_image', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('handler.resize_image')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
