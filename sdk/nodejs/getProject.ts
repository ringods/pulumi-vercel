// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides information about an existing project within Vercel.
 *
 * A Project groups deployments and custom domains. To deploy on Vercel, you need a Project.
 *
 * For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/overview).
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vercel from "@pulumi/vercel";
 *
 * const foo = vercel.getProject({
 *     name: "my-existing-project",
 * });
 * export const projectId = foo.then(foo => foo.id);
 * ```
 */
export function getProject(args: GetProjectArgs, opts?: pulumi.InvokeOptions): Promise<GetProjectResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("vercel:index/getProject:getProject", {
        "name": args.name,
        "teamId": args.teamId,
    }, opts);
}

/**
 * A collection of arguments for invoking getProject.
 */
export interface GetProjectArgs {
    /**
     * The name of the project.
     */
    name: string;
    /**
     * The team ID the project exists beneath. Required when configuring a team resource if a default team has not been set in the provider.
     */
    teamId?: string;
}

/**
 * A collection of values returned by getProject.
 */
export interface GetProjectResult {
    /**
     * Automatically assign custom production domains after each Production deployment via merge to the production branch or Vercel CLI deploy with --prod. Defaults to `true`
     */
    readonly autoAssignCustomDomains: boolean;
    /**
     * Vercel provides a set of Environment Variables that are automatically populated by the System, such as the URL of the Deployment or the name of the Git branch deployed. To expose them to your Deployments, enable this field
     */
    readonly automaticallyExposeSystemEnvironmentVariables: boolean;
    /**
     * The build command for this project. If omitted, this value will be automatically detected.
     */
    readonly buildCommand: string;
    /**
     * Allows Vercel Customer Support to inspect all Deployments' source code in this project to assist with debugging.
     */
    readonly customerSuccessCodeVisibility: boolean;
    /**
     * The dev command for this project. If omitted, this value will be automatically detected.
     */
    readonly devCommand: string;
    /**
     * If no index file is present within a directory, the directory contents will be displayed.
     */
    readonly directoryListing: boolean;
    /**
     * A list of environment variables that should be configured for the project.
     */
    readonly environments: outputs.GetProjectEnvironment[];
    /**
     * The framework that is being used for this project. If omitted, no framework is selected.
     */
    readonly framework: string;
    /**
     * Automatically failover Serverless Functions to the nearest region. You can customize regions through vercel.json. A new Deployment is required for your changes to take effect.
     */
    readonly functionFailover: boolean;
    /**
     * Configuration for Git Comments.
     */
    readonly gitComments: outputs.GetProjectGitComments;
    /**
     * Ensures that pull requests targeting your Git repository must be authorized by a member of your Team before deploying if your Project has Environment Variables or if the pull request includes a change to vercel.json.
     */
    readonly gitForkProtection: boolean;
    /**
     * Enables Git LFS support. Git LFS replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.
     */
    readonly gitLfs: boolean;
    /**
     * The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected Git Repository will be automatically deployed. This requires the corresponding Vercel for [Github](https://vercel.com/docs/concepts/git/vercel-for-github), [Gitlab](https://vercel.com/docs/concepts/git/vercel-for-gitlab) or [Bitbucket](https://vercel.com/docs/concepts/git/vercel-for-bitbucket) plugins to be installed.
     */
    readonly gitRepository: outputs.GetProjectGitRepository;
    /**
     * The ID of this resource.
     */
    readonly id: string;
    /**
     * When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a command that exits with code 1 (new Build needed) or code 0.
     */
    readonly ignoreCommand: string;
    /**
     * The install command for this project. If omitted, this value will be automatically detected.
     */
    readonly installCommand: string;
    /**
     * The name of the project.
     */
    readonly name: string;
    /**
     * Configuration for OpenID Connect (OIDC) tokens.
     */
    readonly oidcTokenConfig: outputs.GetProjectOidcTokenConfig;
    /**
     * Disable Deployment Protection for CORS preflight `OPTIONS` requests for a list of paths.
     */
    readonly optionsAllowlist: outputs.GetProjectOptionsAllowlist;
    /**
     * The output directory of the project. When null is used this value will be automatically detected.
     */
    readonly outputDirectory: string;
    /**
     * Ensures visitors of your Preview Deployments must enter a password in order to gain access.
     */
    readonly passwordProtection: outputs.GetProjectPasswordProtection;
    /**
     * Whether comments are enabled on your Preview Deployments.
     */
    readonly previewComments: boolean;
    /**
     * If enabled, builds for the Production environment will be prioritized over Preview environments.
     */
    readonly prioritiseProductionBuilds: boolean;
    /**
     * Allows automation services to bypass Vercel Authentication and Password Protection for both Preview and Production Deployments on this project when using an HTTP header named `x-vercel-protection-bypass`.
     */
    readonly protectionBypassForAutomation: boolean;
    /**
     * Specifies whether the source code and logs of the deployments for this project should be public or not.
     */
    readonly publicSource: boolean;
    /**
     * Resource Configuration for the project.
     */
    readonly resourceConfig: outputs.GetProjectResourceConfig;
    /**
     * The name of a directory or relative path to the source code of your project. When null is used it will default to the project root.
     */
    readonly rootDirectory: string;
    /**
     * The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see [Vercel's documentation](https://vercel.com/docs/concepts/edge-network/regions) for a full list of regions.
     */
    readonly serverlessFunctionRegion: string;
    /**
     * Ensures that outdated clients always fetch the correct version for a given deployment. This value defines how long Vercel keeps Skew Protection active.
     */
    readonly skewProtection: string;
    /**
     * The team ID the project exists beneath. Required when configuring a team resource if a default team has not been set in the provider.
     */
    readonly teamId: string;
    /**
     * Ensures only visitors from an allowed IP address can access your deployment.
     */
    readonly trustedIps: outputs.GetProjectTrustedIps;
    /**
     * Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.
     */
    readonly vercelAuthentication: outputs.GetProjectVercelAuthentication;
}
/**
 * Provides information about an existing project within Vercel.
 *
 * A Project groups deployments and custom domains. To deploy on Vercel, you need a Project.
 *
 * For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/overview).
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vercel from "@pulumi/vercel";
 *
 * const foo = vercel.getProject({
 *     name: "my-existing-project",
 * });
 * export const projectId = foo.then(foo => foo.id);
 * ```
 */
export function getProjectOutput(args: GetProjectOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetProjectResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("vercel:index/getProject:getProject", {
        "name": args.name,
        "teamId": args.teamId,
    }, opts);
}

/**
 * A collection of arguments for invoking getProject.
 */
export interface GetProjectOutputArgs {
    /**
     * The name of the project.
     */
    name: pulumi.Input<string>;
    /**
     * The team ID the project exists beneath. Required when configuring a team resource if a default team has not been set in the provider.
     */
    teamId?: pulumi.Input<string>;
}
