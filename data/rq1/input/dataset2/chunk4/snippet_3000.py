#Source: https://stackoverflow.com/questions/75797013/python-invoke-throwing-attributeerror-argument-object-has-no-attribute-pre
@invoke.task
def prepare_ssm(ctx):
    invoke.run("echo 'Preparing the SSM secret string parameter for the Slack OAuth token'")
    invoke.run("""
        cd prepare && \
        npm install && \
        npm run cdk deploy ParameterStack
    """)

@invoke.task(
    invoke.Argument("stage",
                    default="dev",
                    help="Stage of the serverless application",
                    ),
    invoke.Argument("app_name",
                    default="aws-slackbot-py",
                    help="Name of the serverless application",
                    ),
    invoke.Argument("bitbucket_pipeline_client_id",
                    default="",
                    help="Bitbucket OAuth2 client ID",
                    ),
    invoke.Argument("bitbucket_pipeline_auth_url",
                    default="https://bitbucket.org/site/oauth2/access_token",
                    help="Bitbucket OAuth2 access token URL",
                    ),
)
def prepare_bitbucket(ctx, stage, app_name=None, bitbucket_pipeline_client_id=None, bitbucket_pipeline_auth_url=None):
    invoke.run("echo 'Preparing the environment for Bitbucket Pipeline role based access'")
    invoke.run("""
        SERVERLESS_APP_NAME="{app_name}-{stage}" \
        BITBUCKET_PIPELINE_CLIENT_ID="{bitbucket_pipeline_client_id}" \
        BITBUCKET_PIPELINE_AUTH_URL="{bitbucket_pipeline_auth_url}" \
        cd prepare && \
        npm install && \
        npm run cdk deploy BitbucketIAMStack
    """.format(
        stage=stage,
        app_name=app_name,
        bitbucket_pipeline_client_id=bitbucket_pipeline_client_id,
        bitbucket_pipeline_auth_url=bitbucket_pipeline_auth_url
    ))