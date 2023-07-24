// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Project extends pulumi.CustomResource {
    /**
     * Get an existing Project resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectState, opts?: pulumi.CustomResourceOptions): Project {
        return new Project(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vercel:index/project:Project';

    /**
     * Returns true if the given object is an instance of Project.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Project {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Project.__pulumiType;
    }

    /**
     * The build command for this project. If omitted, this value will be automatically detected.
     */
    public readonly buildCommand!: pulumi.Output<string | undefined>;
    /**
     * The dev command for this project. If omitted, this value will be automatically detected.
     */
    public readonly devCommand!: pulumi.Output<string | undefined>;
    /**
     * A set of Environment Variables that should be configured for the project.
     */
    public readonly environments!: pulumi.Output<outputs.ProjectEnvironment[] | undefined>;
    /**
     * The framework that is being used for this project. If omitted, no framework is selected.
     */
    public readonly framework!: pulumi.Output<string | undefined>;
    /**
     * The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected
     * Git Repository will be automatically deployed. This requires the corresponding Vercel for
     * [Github](https://vercel.com/docs/concepts/git/vercel-for-github),
     * [Gitlab](https://vercel.com/docs/concepts/git/vercel-for-gitlab) or
     * [Bitbucket](https://vercel.com/docs/concepts/git/vercel-for-bitbucket) plugins to be installed.
     */
    public readonly gitRepository!: pulumi.Output<outputs.ProjectGitRepository | undefined>;
    /**
     * When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build
     * has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a
     * command that exits with code 1 (new Build needed) or code 0.
     */
    public readonly ignoreCommand!: pulumi.Output<string | undefined>;
    /**
     * The install command for this project. If omitted, this value will be automatically detected.
     */
    public readonly installCommand!: pulumi.Output<string | undefined>;
    /**
     * The desired name for the project.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The output directory of the project. If omitted, this value will be automatically detected.
     */
    public readonly outputDirectory!: pulumi.Output<string | undefined>;
    /**
     * Ensures visitors of your Preview Deployments must enter a password in order to gain access.
     */
    public readonly passwordProtection!: pulumi.Output<outputs.ProjectPasswordProtection | undefined>;
    /**
     * By default, visitors to the `/_logs` and `/_src` paths of your Production and Preview Deployments must log in with
     * Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project. Setting
     * `public_source` to `true` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly
     * viewed.
     */
    public readonly publicSource!: pulumi.Output<boolean | undefined>;
    /**
     * The name of a directory or relative path to the source code of your project. If omitted, it will default to the project
     * root.
     */
    public readonly rootDirectory!: pulumi.Output<string | undefined>;
    /**
     * The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source
     * your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see
     * [Vercel's documentation](https://vercel.com/docs/concepts/edge-network/regions) for a full list of regions.
     */
    public readonly serverlessFunctionRegion!: pulumi.Output<string>;
    /**
     * The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the
     * provider.
     */
    public readonly teamId!: pulumi.Output<string>;
    /**
     * Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.
     */
    public readonly vercelAuthentication!: pulumi.Output<outputs.ProjectVercelAuthentication | undefined>;

    /**
     * Create a Project resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProjectArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProjectArgs | ProjectState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProjectState | undefined;
            resourceInputs["buildCommand"] = state ? state.buildCommand : undefined;
            resourceInputs["devCommand"] = state ? state.devCommand : undefined;
            resourceInputs["environments"] = state ? state.environments : undefined;
            resourceInputs["framework"] = state ? state.framework : undefined;
            resourceInputs["gitRepository"] = state ? state.gitRepository : undefined;
            resourceInputs["ignoreCommand"] = state ? state.ignoreCommand : undefined;
            resourceInputs["installCommand"] = state ? state.installCommand : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["outputDirectory"] = state ? state.outputDirectory : undefined;
            resourceInputs["passwordProtection"] = state ? state.passwordProtection : undefined;
            resourceInputs["publicSource"] = state ? state.publicSource : undefined;
            resourceInputs["rootDirectory"] = state ? state.rootDirectory : undefined;
            resourceInputs["serverlessFunctionRegion"] = state ? state.serverlessFunctionRegion : undefined;
            resourceInputs["teamId"] = state ? state.teamId : undefined;
            resourceInputs["vercelAuthentication"] = state ? state.vercelAuthentication : undefined;
        } else {
            const args = argsOrState as ProjectArgs | undefined;
            resourceInputs["buildCommand"] = args ? args.buildCommand : undefined;
            resourceInputs["devCommand"] = args ? args.devCommand : undefined;
            resourceInputs["environments"] = args ? args.environments : undefined;
            resourceInputs["framework"] = args ? args.framework : undefined;
            resourceInputs["gitRepository"] = args ? args.gitRepository : undefined;
            resourceInputs["ignoreCommand"] = args ? args.ignoreCommand : undefined;
            resourceInputs["installCommand"] = args ? args.installCommand : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["outputDirectory"] = args ? args.outputDirectory : undefined;
            resourceInputs["passwordProtection"] = args ? args.passwordProtection : undefined;
            resourceInputs["publicSource"] = args ? args.publicSource : undefined;
            resourceInputs["rootDirectory"] = args ? args.rootDirectory : undefined;
            resourceInputs["serverlessFunctionRegion"] = args ? args.serverlessFunctionRegion : undefined;
            resourceInputs["teamId"] = args ? args.teamId : undefined;
            resourceInputs["vercelAuthentication"] = args ? args.vercelAuthentication : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Project.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Project resources.
 */
export interface ProjectState {
    /**
     * The build command for this project. If omitted, this value will be automatically detected.
     */
    buildCommand?: pulumi.Input<string>;
    /**
     * The dev command for this project. If omitted, this value will be automatically detected.
     */
    devCommand?: pulumi.Input<string>;
    /**
     * A set of Environment Variables that should be configured for the project.
     */
    environments?: pulumi.Input<pulumi.Input<inputs.ProjectEnvironment>[]>;
    /**
     * The framework that is being used for this project. If omitted, no framework is selected.
     */
    framework?: pulumi.Input<string>;
    /**
     * The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected
     * Git Repository will be automatically deployed. This requires the corresponding Vercel for
     * [Github](https://vercel.com/docs/concepts/git/vercel-for-github),
     * [Gitlab](https://vercel.com/docs/concepts/git/vercel-for-gitlab) or
     * [Bitbucket](https://vercel.com/docs/concepts/git/vercel-for-bitbucket) plugins to be installed.
     */
    gitRepository?: pulumi.Input<inputs.ProjectGitRepository>;
    /**
     * When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build
     * has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a
     * command that exits with code 1 (new Build needed) or code 0.
     */
    ignoreCommand?: pulumi.Input<string>;
    /**
     * The install command for this project. If omitted, this value will be automatically detected.
     */
    installCommand?: pulumi.Input<string>;
    /**
     * The desired name for the project.
     */
    name?: pulumi.Input<string>;
    /**
     * The output directory of the project. If omitted, this value will be automatically detected.
     */
    outputDirectory?: pulumi.Input<string>;
    /**
     * Ensures visitors of your Preview Deployments must enter a password in order to gain access.
     */
    passwordProtection?: pulumi.Input<inputs.ProjectPasswordProtection>;
    /**
     * By default, visitors to the `/_logs` and `/_src` paths of your Production and Preview Deployments must log in with
     * Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project. Setting
     * `public_source` to `true` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly
     * viewed.
     */
    publicSource?: pulumi.Input<boolean>;
    /**
     * The name of a directory or relative path to the source code of your project. If omitted, it will default to the project
     * root.
     */
    rootDirectory?: pulumi.Input<string>;
    /**
     * The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source
     * your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see
     * [Vercel's documentation](https://vercel.com/docs/concepts/edge-network/regions) for a full list of regions.
     */
    serverlessFunctionRegion?: pulumi.Input<string>;
    /**
     * The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the
     * provider.
     */
    teamId?: pulumi.Input<string>;
    /**
     * Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.
     */
    vercelAuthentication?: pulumi.Input<inputs.ProjectVercelAuthentication>;
}

/**
 * The set of arguments for constructing a Project resource.
 */
export interface ProjectArgs {
    /**
     * The build command for this project. If omitted, this value will be automatically detected.
     */
    buildCommand?: pulumi.Input<string>;
    /**
     * The dev command for this project. If omitted, this value will be automatically detected.
     */
    devCommand?: pulumi.Input<string>;
    /**
     * A set of Environment Variables that should be configured for the project.
     */
    environments?: pulumi.Input<pulumi.Input<inputs.ProjectEnvironment>[]>;
    /**
     * The framework that is being used for this project. If omitted, no framework is selected.
     */
    framework?: pulumi.Input<string>;
    /**
     * The Git Repository that will be connected to the project. When this is defined, any pushes to the specified connected
     * Git Repository will be automatically deployed. This requires the corresponding Vercel for
     * [Github](https://vercel.com/docs/concepts/git/vercel-for-github),
     * [Gitlab](https://vercel.com/docs/concepts/git/vercel-for-gitlab) or
     * [Bitbucket](https://vercel.com/docs/concepts/git/vercel-for-bitbucket) plugins to be installed.
     */
    gitRepository?: pulumi.Input<inputs.ProjectGitRepository>;
    /**
     * When a commit is pushed to the Git repository that is connected with your Project, its SHA will determine if a new Build
     * has to be issued. If the SHA was deployed before, no new Build will be issued. You can customize this behavior with a
     * command that exits with code 1 (new Build needed) or code 0.
     */
    ignoreCommand?: pulumi.Input<string>;
    /**
     * The install command for this project. If omitted, this value will be automatically detected.
     */
    installCommand?: pulumi.Input<string>;
    /**
     * The desired name for the project.
     */
    name?: pulumi.Input<string>;
    /**
     * The output directory of the project. If omitted, this value will be automatically detected.
     */
    outputDirectory?: pulumi.Input<string>;
    /**
     * Ensures visitors of your Preview Deployments must enter a password in order to gain access.
     */
    passwordProtection?: pulumi.Input<inputs.ProjectPasswordProtection>;
    /**
     * By default, visitors to the `/_logs` and `/_src` paths of your Production and Preview Deployments must log in with
     * Vercel (requires being a member of your team) to see the Source, Logs and Deployment Status of your project. Setting
     * `public_source` to `true` disables this behaviour, meaning the Source, Logs and Deployment Status can be publicly
     * viewed.
     */
    publicSource?: pulumi.Input<boolean>;
    /**
     * The name of a directory or relative path to the source code of your project. If omitted, it will default to the project
     * root.
     */
    rootDirectory?: pulumi.Input<string>;
    /**
     * The region on Vercel's network to which your Serverless Functions are deployed. It should be close to any data source
     * your Serverless Function might depend on. A new Deployment is required for your changes to take effect. Please see
     * [Vercel's documentation](https://vercel.com/docs/concepts/edge-network/regions) for a full list of regions.
     */
    serverlessFunctionRegion?: pulumi.Input<string>;
    /**
     * The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the
     * provider.
     */
    teamId?: pulumi.Input<string>;
    /**
     * Ensures visitors to your Preview Deployments are logged into Vercel and have a minimum of Viewer access on your team.
     */
    vercelAuthentication?: pulumi.Input<inputs.ProjectVercelAuthentication>;
}
