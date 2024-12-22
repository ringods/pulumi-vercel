// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Vercel
{
    [VercelResourceType("vercel:index/customEnvironment:CustomEnvironment")]
    public partial class CustomEnvironment : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The branch tracking configuration for the environment. When enabled, each qualifying merge will generate a deployment.
        /// </summary>
        [Output("branchTracking")]
        public Output<Outputs.CustomEnvironmentBranchTracking> BranchTracking { get; private set; } = null!;

        /// <summary>
        /// A description of what the environment is.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the environment.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the existing Vercel Project.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the
        /// provider.
        /// </summary>
        [Output("teamId")]
        public Output<string> TeamId { get; private set; } = null!;


        /// <summary>
        /// Create a CustomEnvironment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CustomEnvironment(string name, CustomEnvironmentArgs args, CustomResourceOptions? options = null)
            : base("vercel:index/customEnvironment:CustomEnvironment", name, args ?? new CustomEnvironmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CustomEnvironment(string name, Input<string> id, CustomEnvironmentState? state = null, CustomResourceOptions? options = null)
            : base("vercel:index/customEnvironment:CustomEnvironment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CustomEnvironment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CustomEnvironment Get(string name, Input<string> id, CustomEnvironmentState? state = null, CustomResourceOptions? options = null)
        {
            return new CustomEnvironment(name, id, state, options);
        }
    }

    public sealed class CustomEnvironmentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The branch tracking configuration for the environment. When enabled, each qualifying merge will generate a deployment.
        /// </summary>
        [Input("branchTracking")]
        public Input<Inputs.CustomEnvironmentBranchTrackingArgs>? BranchTracking { get; set; }

        /// <summary>
        /// A description of what the environment is.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the environment.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the existing Vercel Project.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        /// <summary>
        /// The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the
        /// provider.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        public CustomEnvironmentArgs()
        {
        }
        public static new CustomEnvironmentArgs Empty => new CustomEnvironmentArgs();
    }

    public sealed class CustomEnvironmentState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The branch tracking configuration for the environment. When enabled, each qualifying merge will generate a deployment.
        /// </summary>
        [Input("branchTracking")]
        public Input<Inputs.CustomEnvironmentBranchTrackingGetArgs>? BranchTracking { get; set; }

        /// <summary>
        /// A description of what the environment is.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the environment.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the existing Vercel Project.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The team ID to add the project to. Required when configuring a team resource if a default team has not been set in the
        /// provider.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        public CustomEnvironmentState()
        {
        }
        public static new CustomEnvironmentState Empty => new CustomEnvironmentState();
    }
}
