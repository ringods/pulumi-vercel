// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Vercel.Inputs
{

    public sealed class CustomEnvironmentBranchTrackingGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The pattern of the branch name to track.
        /// </summary>
        [Input("pattern", required: true)]
        public Input<string> Pattern { get; set; } = null!;

        /// <summary>
        /// How a branch name should be matched against the pattern. Must be one of 'startsWith', 'endsWith' or 'equals'.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public CustomEnvironmentBranchTrackingGetArgs()
        {
        }
        public static new CustomEnvironmentBranchTrackingGetArgs Empty => new CustomEnvironmentBranchTrackingGetArgs();
    }
}
