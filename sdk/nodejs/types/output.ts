// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface DeploymentProjectSettings {
    /**
     * The build command for this deployment. If omitted, this value will be taken from the project or automatically detected.
     */
    buildCommand?: string;
    /**
     * The framework that is being used for this deployment. If omitted, no framework is selected.
     */
    framework?: string;
    /**
     * The install command for this deployment. If omitted, this value will be taken from the project or automatically detected.
     */
    installCommand?: string;
    /**
     * The output directory of the deployment. If omitted, this value will be taken from the project or automatically detected.
     */
    outputDirectory?: string;
    /**
     * The name of a directory or relative path to the source code of your project. When null is used it will default to the project root.
     */
    rootDirectory?: string;
}

export interface DnsRecordSrv {
    /**
     * The TCP or UDP port on which the service is to be found.
     */
    port: number;
    /**
     * The priority of the target host, lower value means more preferred.
     */
    priority: number;
    /**
     * The canonical hostname of the machine providing the service, ending in a dot.
     */
    target: string;
    /**
     * A relative weight for records with the same priority, higher value means higher chance of getting picked.
     */
    weight: number;
}

export interface GetProjectEnvironment {
    /**
     * The git branch of the environment variable.
     */
    gitBranch: string;
    /**
     * The ID of the environment variable
     */
    id: string;
    /**
     * The name of the environment variable.
     */
    key: string;
    /**
     * Whether the Environment Variable is sensitive or not. Note that the value will be `null` for sensitive environment variables.
     */
    sensitive: boolean;
    /**
     * The environments that the environment variable should be present on. Valid targets are either `production`, `preview`, or `development`.
     */
    targets: string[];
    /**
     * The value of the environment variable.
     */
    value: string;
}

export interface GetProjectGitComments {
    /**
     * Whether Commit comments are enabled
     */
    onCommit: boolean;
    /**
     * Whether Pull Request comments are enabled
     */
    onPullRequest: boolean;
}

export interface GetProjectGitRepository {
    /**
     * Deploy hooks are unique URLs that allow you to trigger a deployment of a given branch. See https://vercel.com/docs/deployments/deploy-hooks for full information.
     */
    deployHooks: outputs.GetProjectGitRepositoryDeployHook[];
    /**
     * By default, every commit pushed to the main branch will trigger a Production Deployment instead of the usual Preview Deployment. You can switch to a different branch here.
     */
    productionBranch: string;
    /**
     * The name of the git repository. For example: `vercel/next.js`.
     */
    repo: string;
    /**
     * The git provider of the repository. Must be either `github`, `gitlab`, or `bitbucket`.
     */
    type: string;
}

export interface GetProjectGitRepositoryDeployHook {
    /**
     * The ID of the deploy hook.
     */
    id: string;
    /**
     * The name of the deploy hook.
     */
    name: string;
    /**
     * The branch or commit hash that should be deployed.
     */
    ref: string;
    /**
     * A URL that, when a POST request is made to, will trigger a new deployment.
     */
    url: string;
}

export interface GetProjectPasswordProtection {
    /**
     * The deployment environment that will be protected.
     */
    deploymentType: string;
}

export interface GetProjectTrustedIps {
    /**
     * The allowed IP addressses and CIDR ranges with optional descriptions.
     */
    addresses: outputs.GetProjectTrustedIpsAddress[];
    /**
     * The deployment environment that will be protected.
     */
    deploymentType: string;
    /**
     * Whether or not Trusted IPs is required or optional to access a deployment.
     */
    protectionMode: string;
}

export interface GetProjectTrustedIpsAddress {
    note: string;
    value: string;
}

export interface GetProjectVercelAuthentication {
    /**
     * The deployment environment that will be protected.
     */
    deploymentType: string;
}

export interface ProjectEnvironment {
    /**
     * The git branch of the Environment Variable.
     */
    gitBranch?: string;
    /**
     * The ID of the Environment Variable.
     */
    id: string;
    /**
     * The name of the Environment Variable.
     */
    key: string;
    /**
     * Whether the Environment Variable is sensitive or not. (May be affected by a [team-wide environment variable policy](https://vercel.com/docs/projects/environment-variables/sensitive-environment-variables#environment-variables-policy))
     */
    sensitive: boolean;
    /**
     * The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
     */
    targets: string[];
    /**
     * The value of the Environment Variable.
     */
    value: string;
}

export interface ProjectGitComments {
    /**
     * Whether Commit comments are enabled
     */
    onCommit: boolean;
    /**
     * Whether Pull Request comments are enabled
     */
    onPullRequest: boolean;
}

export interface ProjectGitRepository {
    /**
     * Deploy hooks are unique URLs that allow you to trigger a deployment of a given branch. See https://vercel.com/docs/deployments/deploy-hooks for full information.
     */
    deployHooks?: outputs.ProjectGitRepositoryDeployHook[];
    /**
     * By default, every commit pushed to the main branch will trigger a Production Deployment instead of the usual Preview Deployment. You can switch to a different branch here.
     */
    productionBranch: string;
    /**
     * The name of the git repository. For example: `vercel/next.js`.
     */
    repo: string;
    /**
     * The git provider of the repository. Must be either `github`, `gitlab`, or `bitbucket`.
     */
    type: string;
}

export interface ProjectGitRepositoryDeployHook {
    /**
     * The ID of the deploy hook.
     */
    id: string;
    /**
     * The name of the deploy hook.
     */
    name: string;
    /**
     * The branch or commit hash that should be deployed.
     */
    ref: string;
    /**
     * A URL that, when a POST request is made to, will trigger a new deployment.
     */
    url: string;
}

export interface ProjectPasswordProtection {
    /**
     * The deployment environment to protect. Must be one of `standardProtection`, `allDeployments`, or `onlyPreviewDeployments`.
     */
    deploymentType: string;
    /**
     * The password that visitors must enter to gain access to your Preview Deployments. Drift detection is not possible for this field.
     */
    password: string;
}

export interface ProjectTrustedIps {
    /**
     * The allowed IP addressses and CIDR ranges with optional descriptions.
     */
    addresses: outputs.ProjectTrustedIpsAddress[];
    /**
     * The deployment environment to protect. Must be one of `standardProtection`, `allDeployments`, `onlyProductionDeployments`, or `onlyPreviewDeployments`.
     */
    deploymentType: string;
    /**
     * Whether or not Trusted IPs is optional to access a deployment. Must be either `trustedIpRequired` or `trustedIpOptional`. `trustedIpOptional` is only available with Standalone Trusted IPs.
     */
    protectionMode: string;
}

export interface ProjectTrustedIpsAddress {
    /**
     * A description for the value
     */
    note?: string;
    /**
     * The address or CIDR range that can access deployments.
     */
    value: string;
}

export interface ProjectVercelAuthentication {
    /**
     * The deployment environment to protect. Must be one of `standardProtection`, `allDeployments`, `onlyPreviewDeployments`, or `none`.
     */
    deploymentType: string;
}

