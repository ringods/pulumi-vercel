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

    public sealed class DeploymentProjectSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The build command for this deployment. If omitted, this value will be taken from the project or automatically detected.
        /// </summary>
        [Input("buildCommand")]
        public Input<string>? BuildCommand { get; set; }

        /// <summary>
        /// The framework that is being used for this deployment. If omitted, no framework is selected.
        /// </summary>
        [Input("framework")]
        public Input<string>? Framework { get; set; }

        /// <summary>
        /// The install command for this deployment. If omitted, this value will be taken from the project or automatically detected.
        /// </summary>
        [Input("installCommand")]
        public Input<string>? InstallCommand { get; set; }

        /// <summary>
        /// The output directory of the deployment. If omitted, this value will be taken from the project or automatically detected.
        /// </summary>
        [Input("outputDirectory")]
        public Input<string>? OutputDirectory { get; set; }

        /// <summary>
        /// The name of a directory or relative path to the source code of your project. When null is used it will default to the project root.
        /// </summary>
        [Input("rootDirectory")]
        public Input<string>? RootDirectory { get; set; }

        public DeploymentProjectSettingsArgs()
        {
        }
        public static new DeploymentProjectSettingsArgs Empty => new DeploymentProjectSettingsArgs();
    }
}
