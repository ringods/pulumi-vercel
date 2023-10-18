# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DeploymentArgs', 'Deployment']

@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 delete_on_destroy: Optional[pulumi.Input[bool]] = None,
                 environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 path_prefix: Optional[pulumi.Input[str]] = None,
                 production: Optional[pulumi.Input[bool]] = None,
                 project_settings: Optional[pulumi.Input['DeploymentProjectSettingsArgs']] = None,
                 ref: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Deployment resource.
        :param pulumi.Input[str] project_id: The project ID to add the deployment to.
        :param pulumi.Input[bool] delete_on_destroy: Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are
               retained indefinitely. Note that deleted deployments are not recoverable.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment: A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the `Project` resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] files: A map of files to be uploaded for the deployment. This should be provided by a `get_project_directory` or `get_file` data source. Required if `git_source` is not set.
        :param pulumi.Input[str] path_prefix: If specified then the `path_prefix` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading `../`s will be stripped.
        :param pulumi.Input[bool] production: true if the deployment is a production deployment, meaning production aliases will be assigned.
        :param pulumi.Input['DeploymentProjectSettingsArgs'] project_settings: Project settings that will be applied to the deployment.
        :param pulumi.Input[str] ref: The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if `ref` is not set.
        :param pulumi.Input[str] team_id: The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider.
        """
        DeploymentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            project_id=project_id,
            delete_on_destroy=delete_on_destroy,
            environment=environment,
            files=files,
            path_prefix=path_prefix,
            production=production,
            project_settings=project_settings,
            ref=ref,
            team_id=team_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             project_id: pulumi.Input[str],
             delete_on_destroy: Optional[pulumi.Input[bool]] = None,
             environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             path_prefix: Optional[pulumi.Input[str]] = None,
             production: Optional[pulumi.Input[bool]] = None,
             project_settings: Optional[pulumi.Input['DeploymentProjectSettingsArgs']] = None,
             ref: Optional[pulumi.Input[str]] = None,
             team_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'projectId' in kwargs:
            project_id = kwargs['projectId']
        if 'deleteOnDestroy' in kwargs:
            delete_on_destroy = kwargs['deleteOnDestroy']
        if 'pathPrefix' in kwargs:
            path_prefix = kwargs['pathPrefix']
        if 'projectSettings' in kwargs:
            project_settings = kwargs['projectSettings']
        if 'teamId' in kwargs:
            team_id = kwargs['teamId']

        _setter("project_id", project_id)
        if delete_on_destroy is not None:
            _setter("delete_on_destroy", delete_on_destroy)
        if environment is not None:
            _setter("environment", environment)
        if files is not None:
            _setter("files", files)
        if path_prefix is not None:
            _setter("path_prefix", path_prefix)
        if production is not None:
            _setter("production", production)
        if project_settings is not None:
            _setter("project_settings", project_settings)
        if ref is not None:
            _setter("ref", ref)
        if team_id is not None:
            _setter("team_id", team_id)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The project ID to add the deployment to.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="deleteOnDestroy")
    def delete_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are
        retained indefinitely. Note that deleted deployments are not recoverable.
        """
        return pulumi.get(self, "delete_on_destroy")

    @delete_on_destroy.setter
    def delete_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_on_destroy", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the `Project` resource.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def files(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of files to be uploaded for the deployment. This should be provided by a `get_project_directory` or `get_file` data source. Required if `git_source` is not set.
        """
        return pulumi.get(self, "files")

    @files.setter
    def files(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "files", value)

    @property
    @pulumi.getter(name="pathPrefix")
    def path_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        If specified then the `path_prefix` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading `../`s will be stripped.
        """
        return pulumi.get(self, "path_prefix")

    @path_prefix.setter
    def path_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path_prefix", value)

    @property
    @pulumi.getter
    def production(self) -> Optional[pulumi.Input[bool]]:
        """
        true if the deployment is a production deployment, meaning production aliases will be assigned.
        """
        return pulumi.get(self, "production")

    @production.setter
    def production(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "production", value)

    @property
    @pulumi.getter(name="projectSettings")
    def project_settings(self) -> Optional[pulumi.Input['DeploymentProjectSettingsArgs']]:
        """
        Project settings that will be applied to the deployment.
        """
        return pulumi.get(self, "project_settings")

    @project_settings.setter
    def project_settings(self, value: Optional[pulumi.Input['DeploymentProjectSettingsArgs']]):
        pulumi.set(self, "project_settings", value)

    @property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[str]]:
        """
        The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if `ref` is not set.
        """
        return pulumi.get(self, "ref")

    @ref.setter
    def ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ref", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)


@pulumi.input_type
class _DeploymentState:
    def __init__(__self__, *,
                 delete_on_destroy: Optional[pulumi.Input[bool]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 path_prefix: Optional[pulumi.Input[str]] = None,
                 production: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 project_settings: Optional[pulumi.Input['DeploymentProjectSettingsArgs']] = None,
                 ref: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Deployment resources.
        :param pulumi.Input[bool] delete_on_destroy: Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are
               retained indefinitely. Note that deleted deployments are not recoverable.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domains: A list of all the domains (default domains, staging domains and production domains) that were assigned upon deployment creation.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment: A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the `Project` resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] files: A map of files to be uploaded for the deployment. This should be provided by a `get_project_directory` or `get_file` data source. Required if `git_source` is not set.
        :param pulumi.Input[str] path_prefix: If specified then the `path_prefix` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading `../`s will be stripped.
        :param pulumi.Input[bool] production: true if the deployment is a production deployment, meaning production aliases will be assigned.
        :param pulumi.Input[str] project_id: The project ID to add the deployment to.
        :param pulumi.Input['DeploymentProjectSettingsArgs'] project_settings: Project settings that will be applied to the deployment.
        :param pulumi.Input[str] ref: The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if `ref` is not set.
        :param pulumi.Input[str] team_id: The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider.
        :param pulumi.Input[str] url: A unique URL that is automatically generated for a deployment.
        """
        _DeploymentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            delete_on_destroy=delete_on_destroy,
            domains=domains,
            environment=environment,
            files=files,
            path_prefix=path_prefix,
            production=production,
            project_id=project_id,
            project_settings=project_settings,
            ref=ref,
            team_id=team_id,
            url=url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             delete_on_destroy: Optional[pulumi.Input[bool]] = None,
             domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             path_prefix: Optional[pulumi.Input[str]] = None,
             production: Optional[pulumi.Input[bool]] = None,
             project_id: Optional[pulumi.Input[str]] = None,
             project_settings: Optional[pulumi.Input['DeploymentProjectSettingsArgs']] = None,
             ref: Optional[pulumi.Input[str]] = None,
             team_id: Optional[pulumi.Input[str]] = None,
             url: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'deleteOnDestroy' in kwargs:
            delete_on_destroy = kwargs['deleteOnDestroy']
        if 'pathPrefix' in kwargs:
            path_prefix = kwargs['pathPrefix']
        if 'projectId' in kwargs:
            project_id = kwargs['projectId']
        if 'projectSettings' in kwargs:
            project_settings = kwargs['projectSettings']
        if 'teamId' in kwargs:
            team_id = kwargs['teamId']

        if delete_on_destroy is not None:
            _setter("delete_on_destroy", delete_on_destroy)
        if domains is not None:
            _setter("domains", domains)
        if environment is not None:
            _setter("environment", environment)
        if files is not None:
            _setter("files", files)
        if path_prefix is not None:
            _setter("path_prefix", path_prefix)
        if production is not None:
            _setter("production", production)
        if project_id is not None:
            _setter("project_id", project_id)
        if project_settings is not None:
            _setter("project_settings", project_settings)
        if ref is not None:
            _setter("ref", ref)
        if team_id is not None:
            _setter("team_id", team_id)
        if url is not None:
            _setter("url", url)

    @property
    @pulumi.getter(name="deleteOnDestroy")
    def delete_on_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are
        retained indefinitely. Note that deleted deployments are not recoverable.
        """
        return pulumi.get(self, "delete_on_destroy")

    @delete_on_destroy.setter
    def delete_on_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_on_destroy", value)

    @property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of all the domains (default domains, staging domains and production domains) that were assigned upon deployment creation.
        """
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the `Project` resource.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def files(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of files to be uploaded for the deployment. This should be provided by a `get_project_directory` or `get_file` data source. Required if `git_source` is not set.
        """
        return pulumi.get(self, "files")

    @files.setter
    def files(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "files", value)

    @property
    @pulumi.getter(name="pathPrefix")
    def path_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        If specified then the `path_prefix` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading `../`s will be stripped.
        """
        return pulumi.get(self, "path_prefix")

    @path_prefix.setter
    def path_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path_prefix", value)

    @property
    @pulumi.getter
    def production(self) -> Optional[pulumi.Input[bool]]:
        """
        true if the deployment is a production deployment, meaning production aliases will be assigned.
        """
        return pulumi.get(self, "production")

    @production.setter
    def production(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "production", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project ID to add the deployment to.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="projectSettings")
    def project_settings(self) -> Optional[pulumi.Input['DeploymentProjectSettingsArgs']]:
        """
        Project settings that will be applied to the deployment.
        """
        return pulumi.get(self, "project_settings")

    @project_settings.setter
    def project_settings(self, value: Optional[pulumi.Input['DeploymentProjectSettingsArgs']]):
        pulumi.set(self, "project_settings", value)

    @property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[str]]:
        """
        The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if `ref` is not set.
        """
        return pulumi.get(self, "ref")

    @ref.setter
    def ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ref", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL that is automatically generated for a deployment.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Deployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_on_destroy: Optional[pulumi.Input[bool]] = None,
                 environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 path_prefix: Optional[pulumi.Input[str]] = None,
                 production: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 project_settings: Optional[pulumi.Input[pulumi.InputType['DeploymentProjectSettingsArgs']]] = None,
                 ref: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Deployment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_on_destroy: Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are
               retained indefinitely. Note that deleted deployments are not recoverable.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment: A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the `Project` resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] files: A map of files to be uploaded for the deployment. This should be provided by a `get_project_directory` or `get_file` data source. Required if `git_source` is not set.
        :param pulumi.Input[str] path_prefix: If specified then the `path_prefix` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading `../`s will be stripped.
        :param pulumi.Input[bool] production: true if the deployment is a production deployment, meaning production aliases will be assigned.
        :param pulumi.Input[str] project_id: The project ID to add the deployment to.
        :param pulumi.Input[pulumi.InputType['DeploymentProjectSettingsArgs']] project_settings: Project settings that will be applied to the deployment.
        :param pulumi.Input[str] ref: The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if `ref` is not set.
        :param pulumi.Input[str] team_id: The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Deployment resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DeploymentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_on_destroy: Optional[pulumi.Input[bool]] = None,
                 environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 path_prefix: Optional[pulumi.Input[str]] = None,
                 production: Optional[pulumi.Input[bool]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 project_settings: Optional[pulumi.Input[pulumi.InputType['DeploymentProjectSettingsArgs']]] = None,
                 ref: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentArgs.__new__(DeploymentArgs)

            __props__.__dict__["delete_on_destroy"] = delete_on_destroy
            __props__.__dict__["environment"] = environment
            __props__.__dict__["files"] = files
            __props__.__dict__["path_prefix"] = path_prefix
            __props__.__dict__["production"] = production
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            if project_settings is not None and not isinstance(project_settings, DeploymentProjectSettingsArgs):
                project_settings = project_settings or {}
                def _setter(key, value):
                    project_settings[key] = value
                DeploymentProjectSettingsArgs._configure(_setter, **project_settings)
            __props__.__dict__["project_settings"] = project_settings
            __props__.__dict__["ref"] = ref
            __props__.__dict__["team_id"] = team_id
            __props__.__dict__["domains"] = None
            __props__.__dict__["url"] = None
        super(Deployment, __self__).__init__(
            'vercel:index/deployment:Deployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            delete_on_destroy: Optional[pulumi.Input[bool]] = None,
            domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            files: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            path_prefix: Optional[pulumi.Input[str]] = None,
            production: Optional[pulumi.Input[bool]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            project_settings: Optional[pulumi.Input[pulumi.InputType['DeploymentProjectSettingsArgs']]] = None,
            ref: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Deployment':
        """
        Get an existing Deployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_on_destroy: Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are
               retained indefinitely. Note that deleted deployments are not recoverable.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domains: A list of all the domains (default domains, staging domains and production domains) that were assigned upon deployment creation.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] environment: A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the `Project` resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] files: A map of files to be uploaded for the deployment. This should be provided by a `get_project_directory` or `get_file` data source. Required if `git_source` is not set.
        :param pulumi.Input[str] path_prefix: If specified then the `path_prefix` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading `../`s will be stripped.
        :param pulumi.Input[bool] production: true if the deployment is a production deployment, meaning production aliases will be assigned.
        :param pulumi.Input[str] project_id: The project ID to add the deployment to.
        :param pulumi.Input[pulumi.InputType['DeploymentProjectSettingsArgs']] project_settings: Project settings that will be applied to the deployment.
        :param pulumi.Input[str] ref: The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if `ref` is not set.
        :param pulumi.Input[str] team_id: The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider.
        :param pulumi.Input[str] url: A unique URL that is automatically generated for a deployment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeploymentState.__new__(_DeploymentState)

        __props__.__dict__["delete_on_destroy"] = delete_on_destroy
        __props__.__dict__["domains"] = domains
        __props__.__dict__["environment"] = environment
        __props__.__dict__["files"] = files
        __props__.__dict__["path_prefix"] = path_prefix
        __props__.__dict__["production"] = production
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["project_settings"] = project_settings
        __props__.__dict__["ref"] = ref
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["url"] = url
        return Deployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deleteOnDestroy")
    def delete_on_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        Set to true to hard delete the Vercel deployment when destroying the Terraform resource. If unspecified, deployments are
        retained indefinitely. Note that deleted deployments are not recoverable.
        """
        return pulumi.get(self, "delete_on_destroy")

    @property
    @pulumi.getter
    def domains(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of all the domains (default domains, staging domains and production domains) that were assigned upon deployment creation.
        """
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of environment variable names to values. These are specific to a Deployment, and can also be configured on the `Project` resource.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def files(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of files to be uploaded for the deployment. This should be provided by a `get_project_directory` or `get_file` data source. Required if `git_source` is not set.
        """
        return pulumi.get(self, "files")

    @property
    @pulumi.getter(name="pathPrefix")
    def path_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        If specified then the `path_prefix` will be stripped from the start of file paths as they are uploaded to Vercel. If this is omitted, then any leading `../`s will be stripped.
        """
        return pulumi.get(self, "path_prefix")

    @property
    @pulumi.getter
    def production(self) -> pulumi.Output[bool]:
        """
        true if the deployment is a production deployment, meaning production aliases will be assigned.
        """
        return pulumi.get(self, "production")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project ID to add the deployment to.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="projectSettings")
    def project_settings(self) -> pulumi.Output[Optional['outputs.DeploymentProjectSettings']]:
        """
        Project settings that will be applied to the deployment.
        """
        return pulumi.get(self, "project_settings")

    @property
    @pulumi.getter
    def ref(self) -> pulumi.Output[Optional[str]]:
        """
        The branch or commit hash that should be deployed. Note this will only work if the project is configured to use a Git repository. Required if `ref` is not set.
        """
        return pulumi.get(self, "ref")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The team ID to add the deployment to. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        A unique URL that is automatically generated for a deployment.
        """
        return pulumi.get(self, "url")

