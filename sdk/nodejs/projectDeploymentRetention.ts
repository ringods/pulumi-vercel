// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class ProjectDeploymentRetention extends pulumi.CustomResource {
    /**
     * Get an existing ProjectDeploymentRetention resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectDeploymentRetentionState, opts?: pulumi.CustomResourceOptions): ProjectDeploymentRetention {
        return new ProjectDeploymentRetention(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vercel:index/projectDeploymentRetention:ProjectDeploymentRetention';

    /**
     * Returns true if the given object is an instance of ProjectDeploymentRetention.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ProjectDeploymentRetention {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ProjectDeploymentRetention.__pulumiType;
    }

    /**
     * The retention period for canceled deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    public readonly expirationCanceled!: pulumi.Output<string>;
    /**
     * The retention period for errored deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    public readonly expirationErrored!: pulumi.Output<string>;
    /**
     * The retention period for preview deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    public readonly expirationPreview!: pulumi.Output<string>;
    /**
     * The retention period for production deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    public readonly expirationProduction!: pulumi.Output<string>;
    /**
     * The ID of the Project for the retention policy
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * The ID of the Vercel team.
     */
    public readonly teamId!: pulumi.Output<string>;

    /**
     * Create a ProjectDeploymentRetention resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProjectDeploymentRetentionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProjectDeploymentRetentionArgs | ProjectDeploymentRetentionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProjectDeploymentRetentionState | undefined;
            resourceInputs["expirationCanceled"] = state ? state.expirationCanceled : undefined;
            resourceInputs["expirationErrored"] = state ? state.expirationErrored : undefined;
            resourceInputs["expirationPreview"] = state ? state.expirationPreview : undefined;
            resourceInputs["expirationProduction"] = state ? state.expirationProduction : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["teamId"] = state ? state.teamId : undefined;
        } else {
            const args = argsOrState as ProjectDeploymentRetentionArgs | undefined;
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            resourceInputs["expirationCanceled"] = args ? args.expirationCanceled : undefined;
            resourceInputs["expirationErrored"] = args ? args.expirationErrored : undefined;
            resourceInputs["expirationPreview"] = args ? args.expirationPreview : undefined;
            resourceInputs["expirationProduction"] = args ? args.expirationProduction : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["teamId"] = args ? args.teamId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ProjectDeploymentRetention.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ProjectDeploymentRetention resources.
 */
export interface ProjectDeploymentRetentionState {
    /**
     * The retention period for canceled deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    expirationCanceled?: pulumi.Input<string>;
    /**
     * The retention period for errored deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    expirationErrored?: pulumi.Input<string>;
    /**
     * The retention period for preview deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    expirationPreview?: pulumi.Input<string>;
    /**
     * The retention period for production deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    expirationProduction?: pulumi.Input<string>;
    /**
     * The ID of the Project for the retention policy
     */
    projectId?: pulumi.Input<string>;
    /**
     * The ID of the Vercel team.
     */
    teamId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ProjectDeploymentRetention resource.
 */
export interface ProjectDeploymentRetentionArgs {
    /**
     * The retention period for canceled deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    expirationCanceled?: pulumi.Input<string>;
    /**
     * The retention period for errored deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    expirationErrored?: pulumi.Input<string>;
    /**
     * The retention period for preview deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    expirationPreview?: pulumi.Input<string>;
    /**
     * The retention period for production deployments. Should be one of '1m', '2m', '3m', '6m', '1y', 'unlimited'.
     */
    expirationProduction?: pulumi.Input<string>;
    /**
     * The ID of the Project for the retention policy
     */
    projectId: pulumi.Input<string>;
    /**
     * The ID of the Vercel team.
     */
    teamId?: pulumi.Input<string>;
}
