# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['TeamMemberArgs', 'TeamMember']

@pulumi.input_type
class TeamMemberArgs:
    def __init__(__self__, *,
                 role: pulumi.Input[str],
                 team_id: pulumi.Input[str],
                 user_id: pulumi.Input[str],
                 access_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 projects: Optional[pulumi.Input[Sequence[pulumi.Input['TeamMemberProjectArgs']]]] = None):
        """
        The set of arguments for constructing a TeamMember resource.
        :param pulumi.Input[str] role: The role that the user should have in the project. One of 'MEMBER', 'OWNER', 'VIEWER', 'DEVELOPER', 'BILLING' or
               'CONTRIBUTOR'. Depending on your Team's plan, some of these roles may be unavailable.
        :param pulumi.Input[str] team_id: The ID of the existing Vercel Team.
        :param pulumi.Input[str] user_id: The ID of the user to add to the team.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] access_groups: If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
               specified. A set of access groups IDs that the user should be granted access to.
        :param pulumi.Input[Sequence[pulumi.Input['TeamMemberProjectArgs']]] projects: If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
               specified. A set of projects that the user should be granted access to, along with their role in each project.
        """
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "team_id", team_id)
        pulumi.set(__self__, "user_id", user_id)
        if access_groups is not None:
            pulumi.set(__self__, "access_groups", access_groups)
        if projects is not None:
            pulumi.set(__self__, "projects", projects)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The role that the user should have in the project. One of 'MEMBER', 'OWNER', 'VIEWER', 'DEVELOPER', 'BILLING' or
        'CONTRIBUTOR'. Depending on your Team's plan, some of these roles may be unavailable.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[str]:
        """
        The ID of the existing Vercel Team.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        The ID of the user to add to the team.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="accessGroups")
    def access_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
        specified. A set of access groups IDs that the user should be granted access to.
        """
        return pulumi.get(self, "access_groups")

    @access_groups.setter
    def access_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "access_groups", value)

    @property
    @pulumi.getter
    def projects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TeamMemberProjectArgs']]]]:
        """
        If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
        specified. A set of projects that the user should be granted access to, along with their role in each project.
        """
        return pulumi.get(self, "projects")

    @projects.setter
    def projects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TeamMemberProjectArgs']]]]):
        pulumi.set(self, "projects", value)


@pulumi.input_type
class _TeamMemberState:
    def __init__(__self__, *,
                 access_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 projects: Optional[pulumi.Input[Sequence[pulumi.Input['TeamMemberProjectArgs']]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TeamMember resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] access_groups: If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
               specified. A set of access groups IDs that the user should be granted access to.
        :param pulumi.Input[Sequence[pulumi.Input['TeamMemberProjectArgs']]] projects: If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
               specified. A set of projects that the user should be granted access to, along with their role in each project.
        :param pulumi.Input[str] role: The role that the user should have in the project. One of 'MEMBER', 'OWNER', 'VIEWER', 'DEVELOPER', 'BILLING' or
               'CONTRIBUTOR'. Depending on your Team's plan, some of these roles may be unavailable.
        :param pulumi.Input[str] team_id: The ID of the existing Vercel Team.
        :param pulumi.Input[str] user_id: The ID of the user to add to the team.
        """
        if access_groups is not None:
            pulumi.set(__self__, "access_groups", access_groups)
        if projects is not None:
            pulumi.set(__self__, "projects", projects)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="accessGroups")
    def access_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
        specified. A set of access groups IDs that the user should be granted access to.
        """
        return pulumi.get(self, "access_groups")

    @access_groups.setter
    def access_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "access_groups", value)

    @property
    @pulumi.getter
    def projects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TeamMemberProjectArgs']]]]:
        """
        If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
        specified. A set of projects that the user should be granted access to, along with their role in each project.
        """
        return pulumi.get(self, "projects")

    @projects.setter
    def projects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TeamMemberProjectArgs']]]]):
        pulumi.set(self, "projects", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that the user should have in the project. One of 'MEMBER', 'OWNER', 'VIEWER', 'DEVELOPER', 'BILLING' or
        'CONTRIBUTOR'. Depending on your Team's plan, some of these roles may be unavailable.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the existing Vercel Team.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the user to add to the team.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class TeamMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 projects: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TeamMemberProjectArgs', 'TeamMemberProjectArgsDict']]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a TeamMember resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] access_groups: If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
               specified. A set of access groups IDs that the user should be granted access to.
        :param pulumi.Input[Sequence[pulumi.Input[Union['TeamMemberProjectArgs', 'TeamMemberProjectArgsDict']]]] projects: If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
               specified. A set of projects that the user should be granted access to, along with their role in each project.
        :param pulumi.Input[str] role: The role that the user should have in the project. One of 'MEMBER', 'OWNER', 'VIEWER', 'DEVELOPER', 'BILLING' or
               'CONTRIBUTOR'. Depending on your Team's plan, some of these roles may be unavailable.
        :param pulumi.Input[str] team_id: The ID of the existing Vercel Team.
        :param pulumi.Input[str] user_id: The ID of the user to add to the team.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TeamMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a TeamMember resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param TeamMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TeamMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 projects: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TeamMemberProjectArgs', 'TeamMemberProjectArgsDict']]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TeamMemberArgs.__new__(TeamMemberArgs)

            __props__.__dict__["access_groups"] = access_groups
            __props__.__dict__["projects"] = projects
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
        super(TeamMember, __self__).__init__(
            'vercel:index/teamMember:TeamMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            projects: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TeamMemberProjectArgs', 'TeamMemberProjectArgsDict']]]]] = None,
            role: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'TeamMember':
        """
        Get an existing TeamMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] access_groups: If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
               specified. A set of access groups IDs that the user should be granted access to.
        :param pulumi.Input[Sequence[pulumi.Input[Union['TeamMemberProjectArgs', 'TeamMemberProjectArgsDict']]]] projects: If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
               specified. A set of projects that the user should be granted access to, along with their role in each project.
        :param pulumi.Input[str] role: The role that the user should have in the project. One of 'MEMBER', 'OWNER', 'VIEWER', 'DEVELOPER', 'BILLING' or
               'CONTRIBUTOR'. Depending on your Team's plan, some of these roles may be unavailable.
        :param pulumi.Input[str] team_id: The ID of the existing Vercel Team.
        :param pulumi.Input[str] user_id: The ID of the user to add to the team.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TeamMemberState.__new__(_TeamMemberState)

        __props__.__dict__["access_groups"] = access_groups
        __props__.__dict__["projects"] = projects
        __props__.__dict__["role"] = role
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["user_id"] = user_id
        return TeamMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessGroups")
    def access_groups(self) -> pulumi.Output[Sequence[str]]:
        """
        If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
        specified. A set of access groups IDs that the user should be granted access to.
        """
        return pulumi.get(self, "access_groups")

    @property
    @pulumi.getter
    def projects(self) -> pulumi.Output[Sequence['outputs.TeamMemberProject']]:
        """
        If access groups are enabled on the team, and the user is a CONTRIBUTOR, `projects`, `access_groups` or both must be
        specified. A set of projects that the user should be granted access to, along with their role in each project.
        """
        return pulumi.get(self, "projects")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role that the user should have in the project. One of 'MEMBER', 'OWNER', 'VIEWER', 'DEVELOPER', 'BILLING' or
        'CONTRIBUTOR'. Depending on your Team's plan, some of these roles may be unavailable.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The ID of the existing Vercel Team.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The ID of the user to add to the team.
        """
        return pulumi.get(self, "user_id")

