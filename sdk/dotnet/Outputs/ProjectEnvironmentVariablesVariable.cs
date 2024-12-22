// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Vercel.Outputs
{

    [OutputType]
    public sealed class ProjectEnvironmentVariablesVariable
    {
        /// <summary>
        /// A comment explaining what the environment variable is for.
        /// </summary>
        public readonly string? Comment;
        /// <summary>
        /// The IDs of Custom Environments that the Environment Variable should be present on. At least one of `target` or `custom_environment_ids` must be set.
        /// </summary>
        public readonly ImmutableArray<string> CustomEnvironmentIds;
        /// <summary>
        /// The git branch of the Environment Variable.
        /// </summary>
        public readonly string? GitBranch;
        /// <summary>
        /// The ID of the Environment Variable.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// Whether the Environment Variable is sensitive or not.
        /// </summary>
        public readonly bool? Sensitive;
        /// <summary>
        /// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`. At least one of `target` or `custom_environment_ids` must be set.
        /// </summary>
        public readonly ImmutableArray<string> Targets;
        /// <summary>
        /// The value of the Environment Variable.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private ProjectEnvironmentVariablesVariable(
            string? comment,

            ImmutableArray<string> customEnvironmentIds,

            string? gitBranch,

            string? id,

            string key,

            bool? sensitive,

            ImmutableArray<string> targets,

            string value)
        {
            Comment = comment;
            CustomEnvironmentIds = customEnvironmentIds;
            GitBranch = gitBranch;
            Id = id;
            Key = key;
            Sensitive = sensitive;
            Targets = targets;
            Value = value;
        }
    }
}
