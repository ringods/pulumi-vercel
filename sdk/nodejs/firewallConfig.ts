// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class FirewallConfig extends pulumi.CustomResource {
    /**
     * Get an existing FirewallConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallConfigState, opts?: pulumi.CustomResourceOptions): FirewallConfig {
        return new FirewallConfig(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vercel:index/firewallConfig:FirewallConfig';

    /**
     * Returns true if the given object is an instance of FirewallConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FirewallConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FirewallConfig.__pulumiType;
    }

    /**
     * Whether firewall is enabled or not.
     */
    public readonly enabled!: pulumi.Output<boolean>;
    /**
     * IP rules to apply to the project.
     */
    public readonly ipRules!: pulumi.Output<outputs.FirewallConfigIpRules | undefined>;
    /**
     * The managed rulesets that are enabled.
     */
    public readonly managedRulesets!: pulumi.Output<outputs.FirewallConfigManagedRulesets | undefined>;
    /**
     * The ID of the project this configuration belongs to.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Custom rules to apply to the project
     */
    public readonly rules!: pulumi.Output<outputs.FirewallConfigRules | undefined>;
    /**
     * The ID of the team this project belongs to.
     */
    public readonly teamId!: pulumi.Output<string>;

    /**
     * Create a FirewallConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FirewallConfigArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FirewallConfigArgs | FirewallConfigState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as FirewallConfigState | undefined;
            resourceInputs["enabled"] = state ? state.enabled : undefined;
            resourceInputs["ipRules"] = state ? state.ipRules : undefined;
            resourceInputs["managedRulesets"] = state ? state.managedRulesets : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["rules"] = state ? state.rules : undefined;
            resourceInputs["teamId"] = state ? state.teamId : undefined;
        } else {
            const args = argsOrState as FirewallConfigArgs | undefined;
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            resourceInputs["enabled"] = args ? args.enabled : undefined;
            resourceInputs["ipRules"] = args ? args.ipRules : undefined;
            resourceInputs["managedRulesets"] = args ? args.managedRulesets : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["rules"] = args ? args.rules : undefined;
            resourceInputs["teamId"] = args ? args.teamId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(FirewallConfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FirewallConfig resources.
 */
export interface FirewallConfigState {
    /**
     * Whether firewall is enabled or not.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * IP rules to apply to the project.
     */
    ipRules?: pulumi.Input<inputs.FirewallConfigIpRules>;
    /**
     * The managed rulesets that are enabled.
     */
    managedRulesets?: pulumi.Input<inputs.FirewallConfigManagedRulesets>;
    /**
     * The ID of the project this configuration belongs to.
     */
    projectId?: pulumi.Input<string>;
    /**
     * Custom rules to apply to the project
     */
    rules?: pulumi.Input<inputs.FirewallConfigRules>;
    /**
     * The ID of the team this project belongs to.
     */
    teamId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a FirewallConfig resource.
 */
export interface FirewallConfigArgs {
    /**
     * Whether firewall is enabled or not.
     */
    enabled?: pulumi.Input<boolean>;
    /**
     * IP rules to apply to the project.
     */
    ipRules?: pulumi.Input<inputs.FirewallConfigIpRules>;
    /**
     * The managed rulesets that are enabled.
     */
    managedRulesets?: pulumi.Input<inputs.FirewallConfigManagedRulesets>;
    /**
     * The ID of the project this configuration belongs to.
     */
    projectId: pulumi.Input<string>;
    /**
     * Custom rules to apply to the project
     */
    rules?: pulumi.Input<inputs.FirewallConfigRules>;
    /**
     * The ID of the team this project belongs to.
     */
    teamId?: pulumi.Input<string>;
}
