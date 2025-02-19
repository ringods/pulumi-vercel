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
    public static class GetEdgeConfigSchema
    {
        public static Task<GetEdgeConfigSchemaResult> InvokeAsync(GetEdgeConfigSchemaArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEdgeConfigSchemaResult>("vercel:index/getEdgeConfigSchema:getEdgeConfigSchema", args ?? new GetEdgeConfigSchemaArgs(), options.WithDefaults());

        public static Output<GetEdgeConfigSchemaResult> Invoke(GetEdgeConfigSchemaInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEdgeConfigSchemaResult>("vercel:index/getEdgeConfigSchema:getEdgeConfigSchema", args ?? new GetEdgeConfigSchemaInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEdgeConfigSchemaArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        [Input("teamId")]
        public string? TeamId { get; set; }

        public GetEdgeConfigSchemaArgs()
        {
        }
        public static new GetEdgeConfigSchemaArgs Empty => new GetEdgeConfigSchemaArgs();
    }

    public sealed class GetEdgeConfigSchemaInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        public GetEdgeConfigSchemaInvokeArgs()
        {
        }
        public static new GetEdgeConfigSchemaInvokeArgs Empty => new GetEdgeConfigSchemaInvokeArgs();
    }


    [OutputType]
    public sealed class GetEdgeConfigSchemaResult
    {
        public readonly string Definition;
        public readonly string Id;
        public readonly string TeamId;

        [OutputConstructor]
        private GetEdgeConfigSchemaResult(
            string definition,

            string id,

            string teamId)
        {
            Definition = definition;
            Id = id;
            TeamId = teamId;
        }
    }
}
