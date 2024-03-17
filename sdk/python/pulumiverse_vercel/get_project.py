# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    """
    A collection of values returned by getProject.
    """
    def __init__(__self__, automatically_expose_system_environment_variables=None, build_command=None, dev_command=None, environments=None, framework=None, git_repository=None, id=None, ignore_command=None, install_command=None, name=None, output_directory=None, password_protection=None, public_source=None, root_directory=None, serverless_function_region=None, team_id=None, trusted_ips=None, vercel_authentication=None):
        if automatically_expose_system_environment_variables and not isinstance(automatically_expose_system_environment_variables, bool):
            raise TypeError("Expected argument 'automatically_expose_system_environment_variables' to be a bool")
        pulumi.set(__self__, "automatically_expose_system_environment_variables", automatically_expose_system_environment_variables)
        if build_command and not isinstance(build_command, str):
            raise TypeError("Expected argument 'build_command' to be a str")
        pulumi.set(__self__, "build_command", build_command)
        if dev_command and not isinstance(dev_command, str):
            raise TypeError("Expected argument 'dev_command' to be a str")
        pulumi.set(__self__, "dev_command", dev_command)
        if environments and not isinstance(environments, list):
            raise TypeError("Expected argument 'environments' to be a list")
        pulumi.set(__self__, "environments", environments)
        if framework and not isinstance(framework, str):
            raise TypeError("Expected argument 'framework' to be a str")
        pulumi.set(__self__, "framework", framework)
        if git_repository and not isinstance(git_repository, dict):
            raise TypeError("Expected argument 'git_repository' to be a dict")
        pulumi.set(__self__, "git_repository", git_repository)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ignore_command and not isinstance(ignore_command, str):
            raise TypeError("Expected argument 'ignore_command' to be a str")
        pulumi.set(__self__, "ignore_command", ignore_command)
        if install_command and not isinstance(install_command, str):
            raise TypeError("Expected argument 'install_command' to be a str")
        pulumi.set(__self__, "install_command", install_command)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if output_directory and not isinstance(output_directory, str):
            raise TypeError("Expected argument 'output_directory' to be a str")
        pulumi.set(__self__, "output_directory", output_directory)
        if password_protection and not isinstance(password_protection, dict):
            raise TypeError("Expected argument 'password_protection' to be a dict")
        pulumi.set(__self__, "password_protection", password_protection)
        if public_source and not isinstance(public_source, bool):
            raise TypeError("Expected argument 'public_source' to be a bool")
        pulumi.set(__self__, "public_source", public_source)
        if root_directory and not isinstance(root_directory, str):
            raise TypeError("Expected argument 'root_directory' to be a str")
        pulumi.set(__self__, "root_directory", root_directory)
        if serverless_function_region and not isinstance(serverless_function_region, str):
            raise TypeError("Expected argument 'serverless_function_region' to be a str")
        pulumi.set(__self__, "serverless_function_region", serverless_function_region)
        if team_id and not isinstance(team_id, str):
            raise TypeError("Expected argument 'team_id' to be a str")
        pulumi.set(__self__, "team_id", team_id)
        if trusted_ips and not isinstance(trusted_ips, dict):
            raise TypeError("Expected argument 'trusted_ips' to be a dict")
        pulumi.set(__self__, "trusted_ips", trusted_ips)
        if vercel_authentication and not isinstance(vercel_authentication, dict):
            raise TypeError("Expected argument 'vercel_authentication' to be a dict")
        pulumi.set(__self__, "vercel_authentication", vercel_authentication)

    @property
    @pulumi.getter(name="automaticallyExposeSystemEnvironmentVariables")
    def automatically_expose_system_environment_variables(self) -> bool:
        """
        Vercel provides a set of Environment Variables that are automatically populated by the System, such as the URL of the Deployment or the name of the Git branch deployed. To expose them to your Deployments, enable this field
        """
        return pulumi.get(self, "automatically_expose_system_environment_variables")

    @property
    @pulumi.getter(name="buildCommand")
    def build_command(self) -> str:
        """
        The build command for this project. If omitted, this value will be automatically detected.
        """
        return pulumi.get(self, "build_command")

    @property
    @pulumi.getter(name="devCommand")
    def dev_command(self) -> str:
        """
        The dev command for this project. If omitted, this value will be automatically detected.
        """
        return pulumi.get(self, "dev_command")

    @property
    @pulumi.getter
    def environments(self) -> Sequence['outputs.GetProjectEnvironmentResult']:
        """
        A list of environment variables that should be configured for the project.
        """
        return pulumi.get(self, "environments")

    @property
    @pulumi.getter
    def framework(self) -> str:
        """
        The framework that is being used for this project. If omitted, no framework is selected.
        """
        return pulumi.get(self, "framework")

    @property
    @pulumi.getter(name="gitRepository")
    def git_repository(self) -> 'outputs.GetProjectGitRepositoryResult':
        """
        The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected Git Repository will be automatically deployed. This requires the corresponding Vercel for [Github](https://vercel.com/docs/concepts/git/vercel-for-github), [Gitlab](https://vercel.com/docs/concepts/git/vercel-for-gitlab) or [Bitbucket](https://vercel.com/docs/concepts/git/vercel-for-bitbucket) plugins to be installed.
        """
        return pulumi.get(self, "git_repository")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ignoreCommand")
    def ignore_command(self) -> str:
        """
        When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a command that exits with code 1 (new Build needed) or code 0.
        """
        return pulumi.get(self, "ignore_command")

    @property
    @pulumi.getter(name="installCommand")
    def install_command(self) -> str:
        """
        The install command for this project. If omitted, this value will be automatically detected.
        """
        return pulumi.get(self, "install_command")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the project.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputDirectory")
    def output_directory(self) -> str:
        """
        The output directory of the project. When null is used this value will be automatically detected.
        """
        return pulumi.get(self, "output_directory")

    @property
    @pulumi.getter(name="passwordProtection")
    def password_protection(self) -> 'outputs.GetProjectPasswordProtectionResult':
        """
        Ensures visitors of your Preview Deployments must enter a password in order to gain access.
        """
        return pulumi.get(self, "password_protection")

    @property
    @pulumi.getter(name="publicSource")
    def public_source(self) -> bool:
        """
        Specifies whether the source code and logs of the deployments for this project should be public or not.
        """
        return pulumi.get(self, "public_source")

    @property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> str:
        """
        The name of a directory or relative path to the source code of your project. When null is used it will default to the project root.
        """
        return pulumi.get(self, "root_directory")

    @property
    @pulumi.getter(name="serverlessFunctionRegion")
    def serverless_function_region(self) -> str:
        """
        The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see [Vercel's documentation](https://vercel.com/docs/concepts/edge-network/regions) for a full list of regions.
        """
        return pulumi.get(self, "serverless_function_region")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> str:
        """
        The team ID the project exists beneath. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="trustedIps")
    def trusted_ips(self) -> 'outputs.GetProjectTrustedIpsResult':
        """
        Ensures only visitors from an allowed IP address can access your deployment.
        """
        return pulumi.get(self, "trusted_ips")

    @property
    @pulumi.getter(name="vercelAuthentication")
    def vercel_authentication(self) -> 'outputs.GetProjectVercelAuthenticationResult':
        """
        Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.
        """
        return pulumi.get(self, "vercel_authentication")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            automatically_expose_system_environment_variables=self.automatically_expose_system_environment_variables,
            build_command=self.build_command,
            dev_command=self.dev_command,
            environments=self.environments,
            framework=self.framework,
            git_repository=self.git_repository,
            id=self.id,
            ignore_command=self.ignore_command,
            install_command=self.install_command,
            name=self.name,
            output_directory=self.output_directory,
            password_protection=self.password_protection,
            public_source=self.public_source,
            root_directory=self.root_directory,
            serverless_function_region=self.serverless_function_region,
            team_id=self.team_id,
            trusted_ips=self.trusted_ips,
            vercel_authentication=self.vercel_authentication)


def get_project(name: Optional[str] = None,
                team_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    Provides information about an existing project within Vercel.

    A Project groups deployments and custom domains. To deploy on Vercel, you need a Project.

    For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/overview).

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_vercel as vercel

    foo = vercel.get_project(name="my-existing-project")
    pulumi.export("projectId", foo.id)
    ```
    <!--End PulumiCodeChooser -->


    :param str name: The name of the project.
    :param str team_id: The team ID the project exists beneath. Required when configuring a team resource if a default team has not been set in the provider.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['teamId'] = team_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('vercel:index/getProject:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        automatically_expose_system_environment_variables=pulumi.get(__ret__, 'automatically_expose_system_environment_variables'),
        build_command=pulumi.get(__ret__, 'build_command'),
        dev_command=pulumi.get(__ret__, 'dev_command'),
        environments=pulumi.get(__ret__, 'environments'),
        framework=pulumi.get(__ret__, 'framework'),
        git_repository=pulumi.get(__ret__, 'git_repository'),
        id=pulumi.get(__ret__, 'id'),
        ignore_command=pulumi.get(__ret__, 'ignore_command'),
        install_command=pulumi.get(__ret__, 'install_command'),
        name=pulumi.get(__ret__, 'name'),
        output_directory=pulumi.get(__ret__, 'output_directory'),
        password_protection=pulumi.get(__ret__, 'password_protection'),
        public_source=pulumi.get(__ret__, 'public_source'),
        root_directory=pulumi.get(__ret__, 'root_directory'),
        serverless_function_region=pulumi.get(__ret__, 'serverless_function_region'),
        team_id=pulumi.get(__ret__, 'team_id'),
        trusted_ips=pulumi.get(__ret__, 'trusted_ips'),
        vercel_authentication=pulumi.get(__ret__, 'vercel_authentication'))


@_utilities.lift_output_func(get_project)
def get_project_output(name: Optional[pulumi.Input[str]] = None,
                       team_id: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    Provides information about an existing project within Vercel.

    A Project groups deployments and custom domains. To deploy on Vercel, you need a Project.

    For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/overview).

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_vercel as vercel

    foo = vercel.get_project(name="my-existing-project")
    pulumi.export("projectId", foo.id)
    ```
    <!--End PulumiCodeChooser -->


    :param str name: The name of the project.
    :param str team_id: The team ID the project exists beneath. Required when configuring a team resource if a default team has not been set in the provider.
    """
    ...
