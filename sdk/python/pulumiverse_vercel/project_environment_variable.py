# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProjectEnvironmentVariableArgs', 'ProjectEnvironmentVariable']

@pulumi.input_type
class ProjectEnvironmentVariableArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 project_id: pulumi.Input[str],
                 targets: pulumi.Input[Sequence[pulumi.Input[str]]],
                 value: pulumi.Input[str],
                 git_branch: Optional[pulumi.Input[str]] = None,
                 sensitive: Optional[pulumi.Input[bool]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ProjectEnvironmentVariable resource.
        :param pulumi.Input[str] key: The name of the Environment Variable.
        :param pulumi.Input[str] project_id: The ID of the Vercel project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] targets: The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        :param pulumi.Input[str] value: The value of the Environment Variable.
        :param pulumi.Input[str] git_branch: The git branch of the Environment Variable.
        :param pulumi.Input[bool] sensitive: Whether the Environment Variable is sensitive or not.
        :param pulumi.Input[str] team_id: The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "targets", targets)
        pulumi.set(__self__, "value", value)
        if git_branch is not None:
            pulumi.set(__self__, "git_branch", git_branch)
        if sensitive is not None:
            pulumi.set(__self__, "sensitive", sensitive)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The name of the Environment Variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The ID of the Vercel project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        """
        return pulumi.get(self, "targets")

    @targets.setter
    def targets(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "targets", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the Environment Variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="gitBranch")
    def git_branch(self) -> Optional[pulumi.Input[str]]:
        """
        The git branch of the Environment Variable.
        """
        return pulumi.get(self, "git_branch")

    @git_branch.setter
    def git_branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "git_branch", value)

    @property
    @pulumi.getter
    def sensitive(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the Environment Variable is sensitive or not.
        """
        return pulumi.get(self, "sensitive")

    @sensitive.setter
    def sensitive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sensitive", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)


@pulumi.input_type
class _ProjectEnvironmentVariableState:
    def __init__(__self__, *,
                 git_branch: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 sensitive: Optional[pulumi.Input[bool]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ProjectEnvironmentVariable resources.
        :param pulumi.Input[str] git_branch: The git branch of the Environment Variable.
        :param pulumi.Input[str] key: The name of the Environment Variable.
        :param pulumi.Input[str] project_id: The ID of the Vercel project.
        :param pulumi.Input[bool] sensitive: Whether the Environment Variable is sensitive or not.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] targets: The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        :param pulumi.Input[str] team_id: The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
        :param pulumi.Input[str] value: The value of the Environment Variable.
        """
        if git_branch is not None:
            pulumi.set(__self__, "git_branch", git_branch)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if sensitive is not None:
            pulumi.set(__self__, "sensitive", sensitive)
        if targets is not None:
            pulumi.set(__self__, "targets", targets)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="gitBranch")
    def git_branch(self) -> Optional[pulumi.Input[str]]:
        """
        The git branch of the Environment Variable.
        """
        return pulumi.get(self, "git_branch")

    @git_branch.setter
    def git_branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "git_branch", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Environment Variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Vercel project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def sensitive(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the Environment Variable is sensitive or not.
        """
        return pulumi.get(self, "sensitive")

    @sensitive.setter
    def sensitive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sensitive", value)

    @property
    @pulumi.getter
    def targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        """
        return pulumi.get(self, "targets")

    @targets.setter
    def targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "targets", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the Environment Variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class ProjectEnvironmentVariable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 git_branch: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 sensitive: Optional[pulumi.Input[bool]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_vercel as vercel

        example_project = vercel.Project("exampleProject", git_repository=vercel.ProjectGitRepositoryArgs(
            type="github",
            repo="vercel/some-repo",
        ))
        # An environment variable that will be created
        # for this project for the "production" environment.
        example_project_environment_variable = vercel.ProjectEnvironmentVariable("exampleProjectEnvironmentVariable",
            project_id=example_project.id,
            key="foo",
            value="bar",
            targets=["production"])
        # An environment variable that will be created
        # for this project for the "preview" environment when the branch is "staging".
        example_git_branch = vercel.ProjectEnvironmentVariable("exampleGitBranch",
            project_id=example_project.id,
            key="foo",
            value="bar-staging",
            targets=["preview"],
            git_branch="staging")
        # A sensitive environment variable that will be created
        # for this project for the "production" environment.
        example_sensitive = vercel.ProjectEnvironmentVariable("exampleSensitive",
            project_id=example_project.id,
            key="foo",
            value="bar-production",
            targets=["production"],
            sensitive=True)
        ```

        ## Import

        If importing into a personal account, or with a team configured on

         the provider, simply use the project_id and environment variable id.

         - project_id can be found in the project `settings` tab in the Vercel UI.

         - environment variable id is hard to find, but can be taken from the network tab, inside developer tools, on the project page.

        # 

         Note also, that the value field for sensitive environment variables will be imported as `null`.

        ```sh
        $ pulumi import vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable example prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/FdT2e1E5Of6Cihmt
        ```

         Alternatively, you can import via the team_id, project_id and

         environment variable id.

         - team_id can be found in the team `settings` tab in the Vercel UI.

         - project_id can be found in the project `settings` tab in the Vercel UI.

         - environment variable id is hard to find, but can be taken from the network tab, inside developer tools, on the project page.

        # 

         Note also, that the value field for sensitive environment variables will be imported as `null`.

        ```sh
        $ pulumi import vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable example team_xxxxxxxxxxxxxxxxxxxxxxxx/prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/FdT2e1E5Of6Cihmt
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] git_branch: The git branch of the Environment Variable.
        :param pulumi.Input[str] key: The name of the Environment Variable.
        :param pulumi.Input[str] project_id: The ID of the Vercel project.
        :param pulumi.Input[bool] sensitive: Whether the Environment Variable is sensitive or not.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] targets: The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        :param pulumi.Input[str] team_id: The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
        :param pulumi.Input[str] value: The value of the Environment Variable.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectEnvironmentVariableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_vercel as vercel

        example_project = vercel.Project("exampleProject", git_repository=vercel.ProjectGitRepositoryArgs(
            type="github",
            repo="vercel/some-repo",
        ))
        # An environment variable that will be created
        # for this project for the "production" environment.
        example_project_environment_variable = vercel.ProjectEnvironmentVariable("exampleProjectEnvironmentVariable",
            project_id=example_project.id,
            key="foo",
            value="bar",
            targets=["production"])
        # An environment variable that will be created
        # for this project for the "preview" environment when the branch is "staging".
        example_git_branch = vercel.ProjectEnvironmentVariable("exampleGitBranch",
            project_id=example_project.id,
            key="foo",
            value="bar-staging",
            targets=["preview"],
            git_branch="staging")
        # A sensitive environment variable that will be created
        # for this project for the "production" environment.
        example_sensitive = vercel.ProjectEnvironmentVariable("exampleSensitive",
            project_id=example_project.id,
            key="foo",
            value="bar-production",
            targets=["production"],
            sensitive=True)
        ```

        ## Import

        If importing into a personal account, or with a team configured on

         the provider, simply use the project_id and environment variable id.

         - project_id can be found in the project `settings` tab in the Vercel UI.

         - environment variable id is hard to find, but can be taken from the network tab, inside developer tools, on the project page.

        # 

         Note also, that the value field for sensitive environment variables will be imported as `null`.

        ```sh
        $ pulumi import vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable example prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/FdT2e1E5Of6Cihmt
        ```

         Alternatively, you can import via the team_id, project_id and

         environment variable id.

         - team_id can be found in the team `settings` tab in the Vercel UI.

         - project_id can be found in the project `settings` tab in the Vercel UI.

         - environment variable id is hard to find, but can be taken from the network tab, inside developer tools, on the project page.

        # 

         Note also, that the value field for sensitive environment variables will be imported as `null`.

        ```sh
        $ pulumi import vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable example team_xxxxxxxxxxxxxxxxxxxxxxxx/prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/FdT2e1E5Of6Cihmt
        ```

        :param str resource_name: The name of the resource.
        :param ProjectEnvironmentVariableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectEnvironmentVariableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 git_branch: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 sensitive: Optional[pulumi.Input[bool]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectEnvironmentVariableArgs.__new__(ProjectEnvironmentVariableArgs)

            __props__.__dict__["git_branch"] = git_branch
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["sensitive"] = sensitive
            if targets is None and not opts.urn:
                raise TypeError("Missing required property 'targets'")
            __props__.__dict__["targets"] = targets
            __props__.__dict__["team_id"] = team_id
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = None if value is None else pulumi.Output.secret(value)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["value"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ProjectEnvironmentVariable, __self__).__init__(
            'vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            git_branch: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            sensitive: Optional[pulumi.Input[bool]] = None,
            targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'ProjectEnvironmentVariable':
        """
        Get an existing ProjectEnvironmentVariable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] git_branch: The git branch of the Environment Variable.
        :param pulumi.Input[str] key: The name of the Environment Variable.
        :param pulumi.Input[str] project_id: The ID of the Vercel project.
        :param pulumi.Input[bool] sensitive: Whether the Environment Variable is sensitive or not.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] targets: The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        :param pulumi.Input[str] team_id: The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
        :param pulumi.Input[str] value: The value of the Environment Variable.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectEnvironmentVariableState.__new__(_ProjectEnvironmentVariableState)

        __props__.__dict__["git_branch"] = git_branch
        __props__.__dict__["key"] = key
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["sensitive"] = sensitive
        __props__.__dict__["targets"] = targets
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["value"] = value
        return ProjectEnvironmentVariable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="gitBranch")
    def git_branch(self) -> pulumi.Output[Optional[str]]:
        """
        The git branch of the Environment Variable.
        """
        return pulumi.get(self, "git_branch")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The name of the Environment Variable.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the Vercel project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def sensitive(self) -> pulumi.Output[bool]:
        """
        Whether the Environment Variable is sensitive or not.
        """
        return pulumi.get(self, "sensitive")

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Output[Sequence[str]]:
        """
        The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        """
        return pulumi.get(self, "targets")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the Environment Variable.
        """
        return pulumi.get(self, "value")

