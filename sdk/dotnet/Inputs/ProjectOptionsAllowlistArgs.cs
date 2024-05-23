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

    public sealed class ProjectOptionsAllowlistArgs : global::Pulumi.ResourceArgs
    {
        [Input("paths", required: true)]
        private InputList<Inputs.ProjectOptionsAllowlistPathArgs>? _paths;

        /// <summary>
        /// The allowed paths for the OPTIONS Allowlist. Incoming requests will bypass Deployment Protection if they have the method `OPTIONS` and **start with** one of the path values.
        /// </summary>
        public InputList<Inputs.ProjectOptionsAllowlistPathArgs> Paths
        {
            get => _paths ?? (_paths = new InputList<Inputs.ProjectOptionsAllowlistPathArgs>());
            set => _paths = value;
        }

        public ProjectOptionsAllowlistArgs()
        {
        }
        public static new ProjectOptionsAllowlistArgs Empty => new ProjectOptionsAllowlistArgs();
    }
}
